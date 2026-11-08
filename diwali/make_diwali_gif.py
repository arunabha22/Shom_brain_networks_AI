"""Turn the lotus pond photo into a dreamlike animated Diwali greeting GIF.

* violet night water, emerald lily pads, glowing lotuses with drifting light motes
* clay diyas floating in the open water: shaded bowls sitting low in the water,
  flickering flames, mirrored reflections, flame streaks and expanding ripples
* fireworks and a full moon that exist only as reflections in the pond
* gold "Happy Diwali" title

    python3 make_diwali_gif.py [input.jpg] [output.gif]
"""
import math
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "lotus_pond_original.jpg")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "happy_diwali.gif")
W, H = 800, 600           # render size
OUT_SIZE = (640, 480)     # gif size
N = 40                    # frames per loop
FRAME_MS = 80
rng = np.random.default_rng(11)
YY, XX = np.mgrid[0:H, 0:W].astype(np.float32)


def blur(a, r):
    im = Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))
    return np.asarray(im.filter(ImageFilter.GaussianBlur(r))).astype(np.float32) / 255


# ---------------------------------------------------------------- base grade
photo = Image.open(SRC).convert("RGB").resize((W, H), Image.LANCZOS)
rgb = np.asarray(photo).astype(np.float32) / 255
lum = rgb @ np.array([0.299, 0.587, 0.114], np.float32)
hsv = np.asarray(photo.convert("HSV")).astype(np.float32) / 255
hue, sat = hsv[..., 0], hsv[..., 1]

PINK = blur((((hue > 0.80) | (hue < 0.04)) & (sat > 0.18) & (lum > 0.30)).astype(np.float32), 1.2)
WATER = blur((lum < 0.16).astype(np.float32), 2.5)      # open dark water
WATER = np.clip((WATER - 0.25) / 0.5, 0, 1)

# lily pads -> deep emerald, water -> violet night, strong contrast
pads = np.stack([lum * 0.30, lum * 0.78, lum * 0.62], -1) * 1.05
pads = pads ** 1.25 * 1.25
water = np.array([0.05, 0.02, 0.13]) + np.stack([lum * 0.35, lum * 0.20, lum * 0.75], -1)
night = pads * (1 - WATER[..., None]) + water * WATER[..., None]

lot = Image.fromarray((rgb * 255).astype(np.uint8)).convert("HSV")
lot = np.asarray(lot).astype(np.float32) / 255
lot[..., 1] = np.clip(lot[..., 1] * 1.7 + 0.15, 0, 1)
lot[..., 2] = np.clip(lot[..., 2] * 1.2, 0, 1)
lot = np.asarray(Image.fromarray((lot * 255).astype(np.uint8), "HSV").convert("RGB")).astype(np.float32) / 255
lot = lot * np.array([1.05, 0.78, 1.02])

base = night * (1 - PINK[..., None]) + lot * PINK[..., None]
vig = np.clip(1.2 - 0.5 * ((XX / W * 2 - 1) ** 2 + ((YY / H - 0.45) * 2) ** 2), 0.4, 1)
BASE = np.clip(base * vig[..., None], 0, 1).astype(np.float32)
LOTUS_GLOW = blur(PINK, 10)[..., None] * np.array([1.0, 0.15, 0.6], np.float32)
REFL_MASK = (0.12 + 0.88 * WATER)[..., None]             # reflections live on the water


def wave(layer, t, amp=3.0):
    """Horizontal ripple distortion of a layer, loops with t in [0,1)."""
    shift = amp * np.sin(2 * np.pi * (YY[:, 0] / 7.0 + 2 * t)) + 0.6 * amp * np.sin(2 * np.pi * (YY[:, 0] / 19.0 - t))
    idx = np.clip((XX - shift[:, None]).astype(np.int32), 0, W - 1)
    return layer[YY.astype(np.int32), idx]


def glow(cx, cy, r, color, power=2.0, aspect=1.0):
    d = np.sqrt(((XX - cx) / aspect) ** 2 + (YY - cy) ** 2) / r
    return (np.clip(1 - d, 0, 1) ** power)[..., None] * np.array(color, np.float32)


# ---------------------------------------------------------------- diya sprite
def render_diya(w, ss=3):
    """Shaded terracotta diya, cut at the waterline. Returns (rgba, wick_xy, waterline_y)."""
    W_, H_ = int(w * 1.45) * ss, int(w * 0.75) * ss
    y, x = np.mgrid[0:H_, 0:W_].astype(np.float32)
    a, b, e = 0.5 * w * ss, 0.45 * w * ss, 0.085 * w * ss
    cx, ry = 0.62 * w * ss, 0.24 * w * ss
    wl = ry + 0.5 * b                                       # waterline
    u, v = (x - cx) / a, (y - ry) / e

    def half_h(uu):  # teardrop top outline, spout pointing +x
        hh = np.sqrt(np.clip(1 - uu ** 2, 0, 1))
        sp = np.sqrt(1 - 0.55 ** 2) * np.clip((1.38 - uu) / (1.38 - 0.55), 0, 1)
        return np.where(uu < 0.55, hh, sp)

    top_outer = (np.abs(v) <= half_h(u)) & (u > -1) & (u < 1.38)
    top_inner = (np.abs(v) <= 0.80 * half_h(u / 0.86)) & (u / 0.86 > -1) & (u / 0.86 < 1.38)
    nx, ny = (x - cx) / a, (y - ry) / b
    body = (nx ** 2 + ny ** 2 <= 1) & (y >= ry)
    nz = np.sqrt(np.clip(1 - nx ** 2 - ny ** 2, 0, 1))

    noise = rng.normal(0, 1, (H_ // 3 + 1, W_ // 3 + 1)).astype(np.float32)
    noise = np.asarray(Image.fromarray(noise).resize((W_, H_), Image.BILINEAR))
    clay = np.array([0.66, 0.29, 0.13], np.float32) * (1 + 0.06 * noise[..., None])

    L = np.array([-0.35, -0.55, 0.75]); L /= np.linalg.norm(L)
    lam = np.clip(nx * L[0] + ny * L[1] + nz * L[2], 0, 1)
    warm = np.clip(1 - ny, 0, 1) ** 2 * 0.45                 # flame light on upper bowl
    col = clay * (0.22 + 0.85 * lam)[..., None] + np.array([0.55, 0.30, 0.08]) * warm[..., None]
    spec = np.clip(nx * -0.3 + ny * -0.5 + nz * 0.8, 0, 1) ** 22 * 0.35
    col += spec[..., None]
    # painted rangoli band
    band = np.abs(ny - 0.30) < 0.045
    dots = (np.abs(ny - 0.30) < 0.075) & (np.sin(nx * 22) > 0.75)
    col = np.where((band | dots)[..., None] & body[..., None],
                   np.array([0.95, 0.80, 0.35]) * (0.4 + 0.7 * lam)[..., None], col)

    rim_col = np.array([0.80, 0.42, 0.20]) * (0.85 + 0.15 * noise[..., None]) + np.array([0.25, 0.12, 0.02])
    oil_d = np.sqrt(((x - (cx + 1.05 * a)) / (0.9 * a)) ** 2 + ((y - ry) / (1.2 * e)) ** 2)
    oil = np.array([0.30, 0.13, 0.02]) + np.array([0.85, 0.55, 0.12]) * np.clip(1 - oil_d, 0, 1)[..., None] ** 1.5
    rgb_ = np.where(body[..., None], col, 0)
    rgb_ = np.where(top_outer[..., None], rim_col, rgb_)
    rgb_ = np.where(top_inner[..., None], oil, rgb_)
    alpha = (body | top_outer).astype(np.float32)
    # sit in the water: hide below waterline, darken the wet edge
    alpha *= (y < wl)
    wet = np.clip(1 - (wl - y) / (0.12 * b), 0, 1)
    rgb_ *= (1 - 0.45 * wet)[..., None]

    rgba = np.dstack([np.clip(rgb_, 0, 1), alpha])
    im = Image.fromarray((rgba * 255).astype(np.uint8), "RGBA").resize((W_ // ss, H_ // ss), Image.LANCZOS)
    out = np.asarray(im).astype(np.float32) / 255
    return out, ((cx + 1.22 * a) / ss, ry / ss), wl / ss


def flame_layer(fx, fy, size, t, seed):
    """Additive soft flame + halo, base at (fx, fy)."""
    flick = 1 + 0.15 * math.sin(2 * math.pi * 3 * t + seed) + 0.07 * math.sin(2 * math.pi * 7 * t + 2 * seed)
    hgt = size * 2.4 * flick
    sway = 0.18 * size * math.sin(2 * math.pi * 2 * t + 1.7 * seed)
    x0, x1 = int(fx - size * 2), int(fx + size * 2) + 1
    y0, y1 = int(fy - hgt - 2), int(fy + size) + 1
    out = np.zeros((H, W, 3), np.float32)
    x0c, x1c, y0c, y1c = max(0, x0), min(W, x1), max(0, y0), min(H, y1)
    if x0c >= x1c or y0c >= y1c:
        return out
    gx, gy = XX[y0c:y1c, x0c:x1c], YY[y0c:y1c, x0c:x1c]
    s = np.clip((fy - gy) / hgt, -0.3, 1)                    # 0 at base, 1 at tip
    width = size * 0.5 * np.where(s < 0.25, np.sqrt(np.clip(s + 0.3, 0, None) / 0.55), (1 - s) / 0.75 * 1.0)
    width = np.maximum(width, 0.01)
    cxs = fx + sway * np.clip(s, 0, 1) ** 1.5
    d = np.abs(gx - cxs) / width
    body = np.exp(-d ** 2 * 1.6) * (s > -0.3) * (s < 1)
    core = np.exp(-d ** 2 * 5) * np.clip(1 - np.abs(s - 0.25) / 0.35, 0, 1)
    c = (body[..., None] * np.array([1.0, 0.45, 0.08]) * 1.3
         + body[..., None] ** 2 * np.array([0.3, 0.45, 0.1])
         + core[..., None] * np.array([1.0, 0.95, 0.75]) * 1.2)
    blue = np.exp(-d ** 2 * 3) * np.clip(1 - np.abs(s + 0.05) / 0.12, 0, 1)
    c += blue[..., None] * np.array([0.1, 0.2, 0.6])
    out[y0c:y1c, x0c:x1c] = c
    out += glow(fx, fy - hgt * 0.4, size * 5, (0.45, 0.22, 0.04), 2.2) * flick
    return out


# ---------------------------------------------------------------- scene
# (x, waterline_y, width) -- all in open water; smaller = farther away
DIYAS = [(205, 118, 42), (420, 110, 40), (575, 100, 36), (55, 142, 50),
         (320, 160, 56), (500, 150, 54), (740, 134, 50), (640, 178, 62)]
diya_sprites = [render_diya(w) for *_, w in DIYAS]

BURSTS = [  # reflected fireworks: cx, cy, start frame, colour, particles, radius
    (380, 85, 0, (1.0, 0.80, 0.25), 70, 95),
    (650, 95, 13, (1.0, 0.25, 0.80), 70, 100),
    (240, 150, 26, (0.30, 0.95, 1.0), 60, 85),
    (740, 60, 7, (1.0, 0.55, 0.15), 50, 70),
    (520, 160, 20, (0.70, 1.0, 0.35), 50, 70),
    (90, 70, 33, (1.0, 0.95, 0.90), 50, 65),
]
LIFE = 20
b_ang = [rng.uniform(0, 2 * np.pi, n) for *_, n, _ in BURSTS]
b_spd = [rng.uniform(0.5, 1.0, n) for *_, n, _ in BURSTS]

MOON = (150, 92, 34)
moon = glow(MOON[0], MOON[1], MOON[2], (1.0, 0.92, 0.70), 0.25) + glow(MOON[0], MOON[1], MOON[2] * 3, (0.35, 0.25, 0.5), 2)

# light motes rising from the lotuses
M = 55
mote_x = rng.uniform(20, W - 20, M)
mote_y0 = rng.uniform(200, 420, M)
mote_rise = rng.uniform(60, 160, M)
mote_ph = rng.uniform(0, 1, M)

# title
font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf", 86)
txt = "Happy Diwali"
bx = ImageDraw.Draw(Image.new("L", (1, 1))).textbbox((0, 0), txt, font=font)
TX, TY = (W - (bx[2] - bx[0])) // 2 - bx[0], 492 - bx[1]
mask = Image.new("L", (W, H), 0)
ImageDraw.Draw(mask).text((TX, TY), txt, font=font, fill=255)
T_MASK = (np.asarray(mask).astype(np.float32) / 255)[..., None]
T_OUT = (np.asarray(mask.filter(ImageFilter.MaxFilter(7))).astype(np.float32) / 255)[..., None]
T_GLOW = (np.asarray(mask.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(16))).astype(np.float32) / 255)[..., None]
tg = np.clip((YY - (TY + bx[1])) / (bx[3] - bx[1]), 0, 1)
T_GOLD = np.stack([np.ones_like(tg), 0.96 - 0.42 * tg, 0.55 - 0.50 * tg], -1)


# ---------------------------------------------------------------- render
frames = []
for f in range(N):
    t = f / N
    img = BASE.copy()

    # --- reflections in the water: moon + fireworks, rippled and masked to open water
    refl = moon.copy()
    fw = Image.new("RGB", (W, H))
    dl = ImageDraw.Draw(fw)
    for (cx, cy, start, col, n, rad), ang, spd in zip(BURSTS, b_ang, b_spd):
        age = (f - start) % N
        if age >= LIFE:
            continue
        p = age / LIFE
        fade = (1 - p) ** 1.3
        if age < 2:
            refl += glow(cx, cy, 70, [c * 0.7 for c in col], 2.5)
        refl += glow(cx, cy, rad * 1.5, [c * 0.12 * fade for c in col], 1.5)
        for trail in range(4):
            pt = max(0.0, p - trail * 0.035)
            reach = rad * (1 - (1 - pt) ** 2.2)
            drop = -30 * pt ** 2          # mirrored: sparks "fall" upward in the reflection
            for aa, ss_ in zip(ang, spd):
                x = cx + math.cos(aa) * reach * ss_
                y = cy + math.sin(aa) * reach * ss_ * 0.8 + drop
                bri = fade * (1 - trail * 0.25)
                r = 2.6 - trail * 0.5
                c = tuple(int(255 * min(1, ch * bri + (0.35 * bri if trail == 0 else 0))) for ch in col)
                dl.ellipse([x - r, y - r, x + r, y + r], fill=c)
    fwa = np.asarray(fw).astype(np.float32) / 255
    refl += fwa + np.asarray(fw.filter(ImageFilter.GaussianBlur(4))).astype(np.float32) / 255 * 2.0
    refl = wave(refl, t, 3.0) * REFL_MASK
    img = img + refl * (1 - 0.4 * img)

    # --- lotus glow + rising motes
    pulse = 0.75 + 0.25 * math.sin(2 * math.pi * t)
    img += LOTUS_GLOW * 0.45 * pulse
    mo = Image.new("RGB", (W, H))
    dm = ImageDraw.Draw(mo)
    for i in range(M):
        ph = (t + mote_ph[i]) % 1
        x = mote_x[i] + 6 * math.sin(2 * math.pi * (ph * 2 + i))
        y = mote_y0[i] - mote_rise[i] * ph
        bri = math.sin(math.pi * ph) ** 1.5
        r = 1.6
        dm.ellipse([x - r, y - r, x + r, y + r], fill=(int(255 * bri), int(190 * bri), int(230 * bri)))
    img += np.asarray(mo).astype(np.float32) / 255 + np.asarray(mo.filter(ImageFilter.GaussianBlur(3))).astype(np.float32) / 255 * 2

    # --- diyas: light pool, reflection, flame streak, ripples, body, flame
    for i, ((x, wl, w), (spr, (wx, wy), swl)) in enumerate(zip(DIYAS, diya_sprites)):
        bob = 0.8 * math.sin(2 * math.pi * (t * 2) + i)
        sh, sw = spr.shape[:2]
        ox, oy = int(round(x - wx)), int(round(wl - swl + bob))     # sprite top-left
        fx, fy = ox + wx, oy + wy                                    # wick position
        flick = 1 + 0.12 * math.sin(2 * math.pi * 3 * t + i * 1.3)
        add = glow(fx, wl, w * 1.9 * flick, (0.34, 0.16, 0.03), 2.0, aspect=2.4)

        # reflected flame streak
        streak_len = w * 2.2
        sx = fx + 1.5 * np.sin(2 * np.pi * (YY / 6.0 + 2 * t))
        sd = np.abs(XX - sx) / (w * 0.10)
        sy = (YY - wl) / streak_len
        band = 0.55 + 0.45 * np.sin(2 * np.pi * (YY / 4.0 + 3 * t + i))
        streak = np.exp(-sd ** 2) * np.clip(1 - sy, 0, 1) * (sy > 0) * band * flick
        add += streak[..., None] * np.array([1.0, 0.55, 0.12]) * 0.9

        # ripple rings
        rip = Image.new("L", (W, H))
        dr = ImageDraw.Draw(rip)
        for k in range(2):
            ph = (t * 2 + k * 0.5 + i * 0.13) % 1
            rx = w * (0.75 + 1.4 * ph)
            ryy = rx * 0.22
            a_ = int(110 * (1 - ph) ** 1.5)
            dr.ellipse([x - rx, wl - ryy, x + rx, wl + ryy], outline=a_, width=1)
        ripa = (np.asarray(rip).astype(np.float32) / 255)[..., None]
        add += ripa * np.array([1.0, 0.65, 0.3]) * 0.35
        img = img + add * (1 - 0.35 * img)

        # mirrored diya reflection
        vis_h = int(round(swl))
        part = spr[:vis_h][::-1].copy()
        part[..., :3] *= 0.45
        part[..., 3] *= np.linspace(0.65, 0.0, part.shape[0])[:, None]
        rx0, ry0 = ox, int(round(wl + bob))
        ph_, pw_ = part.shape[:2]
        ya, yb = max(0, ry0), min(H, ry0 + ph_)
        xa, xb = max(0, rx0), min(W, rx0 + pw_)
        if ya < yb and xa < xb:
            sub = part[ya - ry0:yb - ry0, xa - rx0:xb - rx0]
            shift = (1.5 * np.sin(2 * np.pi * (np.arange(ya, yb) / 5.0 + 2 * t))).astype(int)
            for r_, s_ in enumerate(shift):
                sub[r_] = np.roll(sub[r_], s_, axis=0)
            reg = img[ya:yb, xa:xb]
            reg[:] = reg * (1 - sub[..., 3:]) + sub[..., :3] * sub[..., 3:]

        # diya body
        ya, yb = max(0, oy), min(H, oy + sh)
        xa, xb = max(0, ox), min(W, ox + sw)
        sub = spr[ya - oy:yb - oy, xa - ox:xb - ox]
        reg = img[ya:yb, xa:xb]
        reg[:] = reg * (1 - sub[..., 3:]) + sub[..., :3] * sub[..., 3:]

        img = img + flame_layer(fx, fy + 1, w * 0.16, t, i * 2.1) * (1 - 0.2 * np.clip(img, 0, 1))

    # --- title
    tp = 0.85 + 0.15 * math.sin(2 * math.pi * t * 2)
    img = img * (1 - 0.8 * T_OUT) + np.array([0.22, 0.02, 0.10]) * 0.8 * T_OUT
    img += T_GLOW * np.array([1.0, 0.42, 0.05]) * 0.9 * tp
    shine_x = (t * 1.6 - 0.3) * W
    shine = np.exp(-((XX - shine_x - (YY - 520) * 0.5) / 45) ** 2)[..., None]
    img = img * (1 - T_MASK) + np.clip(T_GOLD + shine * 0.9, 0, 1) * T_MASK

    frames.append(Image.fromarray((np.clip(img, 0, 1) * 255).astype(np.uint8)))

frames = [fr.resize(OUT_SIZE, Image.LANCZOS) for fr in frames]
if os.environ.get("PREVIEW"):
    frames[int(os.environ["PREVIEW"])].save(os.environ.get("PREVIEW_OUT", "preview.png"))
pal = [fr.quantize(colors=192, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG) for fr in frames]
pal[0].save(OUT, save_all=True, append_images=pal[1:], duration=FRAME_MS, loop=0, disposal=1)
print("wrote", OUT)

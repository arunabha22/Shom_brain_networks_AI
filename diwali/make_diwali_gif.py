"""Turn the lotus pond photo into an animated Diwali greeting GIF.

Night colour grade, floating clay diyas and brass pradips on the lily pads,
looping fireworks in the dark reflection area, twinkling sparkles and a
glowing "Happy Diwali" title.

    python3 make_diwali_gif.py [input.jpg] [output.gif]
"""
import math
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = __file__.rsplit("/", 1)[0] if "/" in __file__ else "."
SRC = sys.argv[1] if len(sys.argv) > 1 else f"{HERE}/lotus_pond_original.jpg"
OUT = sys.argv[2] if len(sys.argv) > 2 else f"{HERE}/happy_diwali.gif"
W, H = 800, 600
N = 36           # frames
FRAME_MS = 85
rng = np.random.default_rng(7)

# ---------- base image: night grade with vivid lotuses ----------
base = Image.open(SRC).convert("RGB").resize((W, H), Image.LANCZOS)
hsv = np.asarray(base.convert("HSV")).astype(np.float32) / 255.0
h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
pink = (((h > 0.80) | (h < 0.04)) & (s > 0.18) & (v > 0.35)).astype(np.float32)
pink = np.asarray(Image.fromarray((pink * 255).astype(np.uint8)).filter(
    ImageFilter.GaussianBlur(1.5))).astype(np.float32) / 255.0

rgb = np.asarray(base).astype(np.float32) / 255.0
lum = rgb @ np.array([0.299, 0.587, 0.114], np.float32)
# everything that is not a flower goes to a deep teal/indigo night
night = np.stack([lum * 0.25, lum * 0.55, lum * 0.75], -1)
night = night * 0.85 + rgb * np.array([0.10, 0.22, 0.20]) 
yy = np.linspace(0, 1, H)[:, None]
sky = np.clip(1.0 - yy / 0.42, 0, 1)                   # top area = night sky
night = night * (1 - 0.55 * sky[..., None]) + np.array([0.02, 0.0, 0.08]) * sky[..., None]

hot = np.asarray(Image.fromarray((rgb * 255).astype(np.uint8)).convert("HSV")).astype(np.float32) / 255
hot[..., 1] = np.clip(hot[..., 1] * 1.6 + 0.15, 0, 1)
hot[..., 2] = np.clip(hot[..., 2] * 1.15, 0, 1)
hot = np.asarray(Image.fromarray((hot * 255).astype(np.uint8), "HSV").convert("RGB")).astype(np.float32) / 255
hot = hot * np.array([1.05, 0.80, 1.0])                # push pink toward magenta

graded = night * (1 - pink[..., None]) + hot * pink[..., None]
# vignette
xx = np.linspace(-1, 1, W)[None, :]
vig = np.clip(1.15 - 0.55 * (xx ** 2 + ((yy - 0.55) * 2) ** 2), 0.35, 1)
graded *= vig[..., None]
BASE = np.clip(graded, 0, 1).astype(np.float32)


# ---------- helpers ----------
def radial(cx, cy, r, color, power=2.0):
    """Additive soft glow layer."""
    x0, x1 = max(0, int(cx - r)), min(W, int(cx + r) + 1)
    y0, y1 = max(0, int(cy - r)), min(H, int(cy + r) + 1)
    out = np.zeros((H, W, 3), np.float32)
    if x0 >= x1 or y0 >= y1:
        return out
    gx, gy = np.meshgrid(np.arange(x0, x1), np.arange(y0, y1))
    d = np.sqrt((gx - cx) ** 2 + (gy - cy) ** 2) / r
    a = np.clip(1 - d, 0, 1) ** power
    out[y0:y1, x0:x1] = a[..., None] * np.array(color, np.float32)
    return out


def sprite_paste(canvas, spr, cx, cy):
    """Alpha composite an RGBA float sprite centred at (cx, cy)."""
    sh, sw = spr.shape[:2]
    x0, y0 = int(cx - sw / 2), int(cy - sh / 2)
    xs0, ys0 = max(0, -x0), max(0, -y0)
    xs1, ys1 = min(sw, W - x0), min(sh, H - y0)
    if xs0 >= xs1 or ys0 >= ys1:
        return
    a = spr[ys0:ys1, xs0:xs1, 3:4]
    region = canvas[y0 + ys0:y0 + ys1, x0 + xs0:x0 + xs1]
    region[:] = region * (1 - a) + spr[ys0:ys1, xs0:xs1, :3] * a


def to_float(img):
    return np.asarray(img).astype(np.float32) / 255.0


SS = 4  # supersampling for sprites


def clay_diya(width):
    w, hgt = width * SS, int(width * 0.55) * SS
    im = Image.new("RGBA", (w, hgt), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    # bowl
    d.chord([0, -hgt * 0.9, w, hgt * 0.95], 0, 180, fill=(196, 74, 22, 255))
    d.chord([w * 0.06, -hgt * 0.75, w * 0.94, hgt * 0.80], 0, 180, fill=(232, 112, 30, 255))
    # spout
    d.polygon([(w * 0.70, hgt * 0.02), (w * 0.98, -1), (w * 0.80, hgt * 0.22)], fill=(214, 92, 26, 255))
    # rim + oil
    d.ellipse([0, -hgt * 0.10, w, hgt * 0.16], fill=(150, 48, 14, 255))
    d.ellipse([w * 0.08, -hgt * 0.04, w * 0.92, hgt * 0.11], fill=(255, 196, 70, 255))
    # painted dots and band
    for i in range(7):
        px = w * (0.16 + i * 0.113)
        py = hgt * 0.45 + math.sin(i * 0.9) * hgt * 0.03
        r = w * 0.028
        d.ellipse([px - r, py - r, px + r, py + r], fill=(255, 236, 120, 255))
    d.arc([w * 0.05, -hgt * 0.55, w * 0.95, hgt * 0.68], 20, 160, fill=(255, 220, 90, 255), width=SS * 2)
    im = im.resize((width, int(width * 0.55)), Image.LANCZOS)
    return to_float(im)


def brass_pradip(width):
    w, hgt = width * SS, int(width * 1.5) * SS
    im = Image.new("RGBA", (w, hgt), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    gold, dark, light = (212, 160, 40, 255), (150, 100, 20, 255), (255, 222, 120, 255)
    # base
    d.ellipse([w * 0.12, hgt * 0.86, w * 0.88, hgt * 0.99], fill=dark)
    d.polygon([(w * 0.2, hgt * 0.92), (w * 0.8, hgt * 0.92), (w * 0.58, hgt * 0.78), (w * 0.42, hgt * 0.78)], fill=gold)
    # stem with knobs
    d.rectangle([w * 0.45, hgt * 0.30, w * 0.55, hgt * 0.80], fill=gold)
    d.rectangle([w * 0.47, hgt * 0.30, w * 0.50, hgt * 0.80], fill=light)
    for ky in (0.42, 0.60):
        d.ellipse([w * 0.36, hgt * (ky - 0.03), w * 0.64, hgt * (ky + 0.03)], fill=gold)
        d.ellipse([w * 0.40, hgt * (ky - 0.02), w * 0.52, hgt * (ky + 0.005)], fill=light)
    # cup
    d.chord([0, hgt * 0.05, w, hgt * 0.36], 0, 180, fill=gold)
    d.chord([w * 0.08, hgt * 0.09, w * 0.6, hgt * 0.30], 30, 150, fill=light)
    d.ellipse([0, hgt * 0.16, w, hgt * 0.25], fill=dark)
    d.ellipse([w * 0.08, hgt * 0.18, w * 0.92, hgt * 0.23], fill=(255, 200, 80, 255))
    im = im.resize((width, int(width * 1.5)), Image.LANCZOS)
    return to_float(im)


def flame(size, t, seed):
    """Flickering teardrop flame sprite (RGBA float)."""
    flick = 1 + 0.18 * math.sin(t * 2 * math.pi * 3 + seed) + 0.08 * math.sin(t * 2 * math.pi * 7 + seed * 2)
    sway = 0.12 * math.sin(t * 2 * math.pi * 2 + seed * 1.7)
    w, hgt = int(size * SS), int(size * 2.2 * flick * SS)
    im = Image.new("RGBA", (w * 2, hgt + w), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    cx = w
    for scale, col in ((1.0, (255, 90, 10, 230)), (0.75, (255, 170, 30, 255)),
                       (0.5, (255, 235, 120, 255)), (0.28, (255, 255, 235, 255))):
        r = w * 0.5 * scale
        top = hgt * (1 - scale) + w * 0.1
        bottom = hgt + w * 0.5
        tip = (cx + sway * w * 2 * scale, top)
        d.polygon([tip, (cx - r, bottom - r), (cx + r, bottom - r)], fill=col)
        d.ellipse([cx - r, bottom - 2 * r, cx + r, bottom], fill=col)
    im = im.resize((max(1, im.width // SS), max(1, im.height // SS)), Image.LANCZOS)
    return to_float(im)


# ---------- scene layout ----------
# (x, y_of_base, width, kind) -- placed on lily pads in the lower half
LAMPS = [
    (95, 545, 70, "diya"), (250, 470, 52, "diya"), (400, 560, 78, "diya"),
    (560, 500, 56, "diya"), (720, 560, 72, "diya"), (650, 415, 40, "diya"),
    (40, 455, 44, "pradip"), (765, 440, 44, "pradip"),
]
sprites = []
for x, y, wd, kind in LAMPS:
    spr = clay_diya(wd) if kind == "diya" else brass_pradip(wd)
    sprites.append(spr)

# fireworks: (cx, cy, start_frame, colour, n_particles, radius)
BURSTS = [
    (150, 175, 0, (1.0, 0.80, 0.25), 70, 115),
    (640, 165, 12, (1.0, 0.25, 0.75), 70, 120),
    (400, 215, 24, (0.30, 0.95, 1.0), 60, 95),
    (730, 55, 6, (1.0, 0.55, 0.15), 45, 70),
    (70, 60, 18, (0.70, 1.0, 0.35), 45, 70),
    (280, 150, 30, (1.0, 0.95, 0.9), 50, 75),
]
BURST_LIFE = 18
burst_angles = [rng.uniform(0, 2 * np.pi, n) for *_, n, _ in BURSTS]
burst_speeds = [rng.uniform(0.55, 1.0, n) for *_, n, _ in BURSTS]

SPARKS = rng.uniform([0, 0], [W, H * 0.45], (60, 2))
SPARK_PH = rng.uniform(0, 1, 60)

# ---------- title ----------
font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf", 92)
txt = "Happy Diwali"
tmp = ImageDraw.Draw(Image.new("L", (1, 1)))
bx = tmp.textbbox((0, 0), txt, font=font)
tw, th = bx[2] - bx[0], bx[3] - bx[1]
TX, TY = (W - tw) // 2 - bx[0], 22 - bx[1]
mask = Image.new("L", (W, H), 0)
ImageDraw.Draw(mask).text((TX, TY), txt, font=font, fill=255)
MASK = to_float(mask)
OUTLINE = to_float(mask.filter(ImageFilter.MaxFilter(7)))
GLOW = to_float(mask.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(14)))
gy = np.linspace(0, 1, H)[:, None] * np.ones((1, W))
ty0, ty1 = TY + bx[1], TY + bx[3]
tg = np.clip((gy - ty0) / max(1, ty1 - ty0), 0, 1)
GOLD = np.stack([np.ones_like(tg), 0.95 - 0.40 * tg, 0.55 - 0.50 * tg], -1)  # yellow -> deep orange
XS = np.arange(W)[None, :] * np.ones((H, 1))


# ---------- render ----------
frames = []
for f in range(N):
    t = f / N
    img = BASE.copy()
    add = np.zeros_like(img)

    # fireworks
    for (cx, cy, start, col, n, rad), ang, spd in zip(BURSTS, burst_angles, burst_speeds):
        age = (f - start) % N
        if age >= BURST_LIFE:
            continue
        p = age / BURST_LIFE
        if age < 2:   # bright flash
            add += radial(cx, cy, 60, [c * 0.8 for c in col], 2.5)
        layer = Image.new("RGB", (W, H))
        dl = ImageDraw.Draw(layer)
        fade = (1 - p) ** 1.3
        for trail in range(4):
            pt = max(0.0, p - trail * 0.035)
            reach = rad * (1 - (1 - pt) ** 2.2)
            drop = 40 * pt ** 2
            for a, s_ in zip(ang, spd):
                x = cx + math.cos(a) * reach * s_
                y = cy + math.sin(a) * reach * s_ + drop
                b = fade * (1 - trail * 0.25)
                r = 2.7 - trail * 0.5
                c = tuple(int(255 * min(1, ch * b + (0.35 * b if trail == 0 else 0))) for ch in col)
                dl.ellipse([x - r, y - r, x + r, y + r], fill=c)
        lf = to_float(layer)
        add += lf + to_float(layer.filter(ImageFilter.GaussianBlur(4))) * 2.2
        add += radial(cx, cy, rad * 1.4, [c * 0.10 * fade for c in col], 1.5)

    # sparkles
    sp = Image.new("RGB", (W, H))
    ds = ImageDraw.Draw(sp)
    for (sx, sy), ph in zip(SPARKS, SPARK_PH):
        b = max(0.0, math.sin(2 * math.pi * (t * 2 + ph))) ** 3
        if b < 0.05:
            continue
        L = 2 + 5 * b
        c = (int(255 * b), int(235 * b), int(170 * b))
        ds.line([sx - L, sy, sx + L, sy], fill=c, width=1)
        ds.line([sx, sy - L, sx, sy + L], fill=c, width=1)
    add += to_float(sp) + to_float(sp.filter(ImageFilter.GaussianBlur(2)))

    # lamp warm light on the scene + water reflections (under the sprites)
    for i, (x, y, wd, kind) in enumerate(LAMPS):
        fl = 1 + 0.12 * math.sin(2 * math.pi * (t * 3) + i * 1.3)
        add += radial(x, y - wd * 0.3, wd * 2.2 * fl, (0.50, 0.26, 0.05), 1.8)
        add += radial(x, y + wd * 0.35, wd * 0.9, (0.45, 0.22, 0.03), 2.0)

    img = img + add * (1 - 0.3 * np.clip(img, 0, 1))  # screen-ish additive

    # lamp bodies and flames
    for i, ((x, y, wd, kind), spr) in enumerate(zip(LAMPS, sprites)):
        sh = spr.shape[0]
        sprite_paste(img, spr, x, y - sh / 2)
        if kind == "diya":
            fx, fy, fs = x + wd * 0.40, y - sh * 1.0, wd * 0.20
        else:
            fx, fy, fs = x, y - sh * 0.83, wd * 0.30
        fsp = flame(fs, t, i * 2.1)
        img += radial(fx, fy - fs, fs * 4.5, (0.9, 0.55, 0.12), 2.2)
        sprite_paste(img, fsp, fx, fy - fsp.shape[0] / 2 + fs * 0.25)

    # title: dark outline, glow, gold fill with moving shimmer
    pulse = 0.85 + 0.15 * math.sin(2 * math.pi * t * 2)
    img = img * (1 - 0.75 * OUTLINE[..., None]) + np.array([0.25, 0.02, 0.10]) * 0.75 * OUTLINE[..., None]
    img += GLOW[..., None] * np.array([1.0, 0.45, 0.05]) * 0.9 * pulse
    shine_x = (t * 1.6 - 0.3) * W
    shine = np.exp(-((XS - shine_x - (gy - 70) * 0.5) / 45) ** 2)[..., None]
    fill = np.clip(GOLD + shine * 0.9, 0, 1)
    img = img * (1 - MASK[..., None]) + fill * MASK[..., None]

    frames.append(Image.fromarray((np.clip(img, 0, 1) * 255).astype(np.uint8)))

frames = [fr.resize((640, 480), Image.LANCZOS) for fr in frames]
pal = [fr.quantize(colors=192, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG) for fr in frames]
pal[0].save(OUT, save_all=True, append_images=pal[1:], duration=FRAME_MS, loop=0, optimize=False, disposal=1)

print("wrote", OUT)

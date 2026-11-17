# Arunabha's own 2-page LaTeX CV kept exactly as is; only the References section is replaced with his three
# referees, written in Computer Modern (CMU) so the font matches. Nothing in experience/education is changed.
import os, pymupdf
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "original_resume.pdf")
OUT = os.path.join(HERE, "Arunabha_Majumder_CV_2_page.pdf")
REG = "/usr/share/fonts/truetype/cmu/cmunrm.ttf"   # Computer Modern Roman (same face as SFRM1000)
BOLD = "/usr/share/fonts/truetype/cmu/cmunbx.ttf"  # Computer Modern Bold Extended (same face as SFBX1000)
SIZE = 9.9626
REFS = [
    ("Shaoping Bai, PhD, ", "Professor", "Department of Materials and Production, Aalborg University, Denmark. Email: sbh@mp.aau.dk"),
    ("Lars Rosgaard Jensen, ", "Associate Professor", "Head of Section, Physics, Mechanics and Materials; Head of Labs, Department of Materials and Production, Aalborg University, Denmark"),
    ("Anderson de Souza Castelo Oliveira, ", "Associate Professor", "Department of Materials and Production, Aalborg University, Denmark"),
]

d = pymupdf.open(SRC)
p = d[1]
hits = p.search_for("Available upon request.")
assert len(hits) == 1, hits
r = hits[0]
p.add_redact_annot(pymupdf.Rect(r.x0 - 1, r.y0 - 1, r.x1 + 1, r.y1 + 1), fill=(1, 1, 1))
p.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE)
p.insert_font(fontname="cmr", fontfile=REG)
p.insert_font(fontname="cmbx", fontfile=BOLD)
fr, fb = pymupdf.Font(fontfile=REG), pymupdf.Font(fontfile=BOLD)

x_bul, x_txt, x_max = 43.2, 53.2, 552.0
y = r.y0 + 8.4          # baseline of the old "Available upon request." line
lead = 11.95
for name, title, detail in REFS:
    p.insert_text((x_bul, y), "•", fontname="cmr", fontfile=REG, fontsize=SIZE)
    p.insert_text((x_txt, y), name, fontname="cmbx", fontsize=SIZE)
    p.insert_text((x_txt + fb.text_length(name, SIZE), y), title, fontname="cmr", fontfile=REG, fontsize=SIZE)
    words, line = detail.split(), ""
    for w in words:                      # simple word wrap for the detail line(s)
        test = (line + " " + w).strip()
        if x_txt + fr.text_length(test, SIZE) > x_max:
            y += lead; p.insert_text((x_txt, y), line, fontname="cmr", fontfile=REG, fontsize=SIZE); line = w
        else:
            line = test
    y += lead; p.insert_text((x_txt, y), line, fontname="cmr", fontfile=REG, fontsize=SIZE)
    y += lead + 2

meta = d.metadata
meta.update(title="Arunabha Majumder CV", author="Arunabha Majumder", creator="Arunabha Majumder", producer="Arunabha Majumder")
d.set_metadata(meta)
d.save(OUT, garbage=3, deflate=True)
print("saved", OUT, "last baseline", round(y, 1))

# Step 1b (his requests, 2026-11): "one journal submission" (not two) and a new Professional Profile,
# written in the same Computer Modern font, fully justified, inside the old 4-line profile area.
dd = pymupdf.open(OUT)
pg = dd[0]
fr = pymupdf.Font(fontfile=REG)
LEAD = 11.955
# journal line
jr = pymupdf.Rect(53.0, 519.6, 400.0, 530.6)
pg.add_redact_annot(jr, fill=(1, 1, 1))
# profile lines
PR = pymupdf.Rect(42.5, 161.8, 553.0, 208.8)
pg.add_redact_annot(PR, fill=(1, 1, 1))
pg.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE)
pg.insert_font(fontname="cmr", fontfile=REG)
pg.insert_text((53.16, 528.04), "data pipeline, producing the validation dataset for one journal submission.",
               fontname="cmr", fontfile=REG, fontsize=SIZE)
PROFILE = ("Mechanical and mechatronics R&D engineer who designs, builds and tests robotic mechanisms, actuators "
           "and exoskeletons. Hands-on from hand sketches and SolidWorks CAD to 3D printed prototypes, motor and "
           "sensor integration, control and testing with real users. Designed a hybrid shoulder exoskeleton that "
           "uses over 25% less motor energy (Best Paper Award, ISRM 2026) and a 5-bar robot with stiffness "
           "estimated within 10% error.")
xl, xr, y0 = 43.2, 552.0, 170.38
words = PROFILE.split()
lines, cur = [], []
for w in words:
    test = cur + [w]
    if fr.text_length(" ".join(test), SIZE) > (xr - xl) and cur:
        lines.append(cur); cur = [w]
    else:
        cur = test
lines.append(cur)
assert len(lines) <= 4, len(lines)
for i, ln in enumerate(lines):
    y = y0 + i * LEAD
    if i == len(lines) - 1:
        pg.insert_text((xl, y), " ".join(ln), fontname="cmr", fontfile=REG, fontsize=SIZE)
        continue
    wsum = sum(fr.text_length(w, SIZE) for w in ln)
    gap = (xr - xl - wsum) / (len(ln) - 1)
    x = xl
    for w in ln:
        pg.insert_text((x, y), w, fontname="cmr", fontfile=REG, fontsize=SIZE)
        x += fr.text_length(w, SIZE) + gap
dd.save(OUT + ".tmp", garbage=3, deflate=True); dd.close(); os.replace(OUT + ".tmp", OUT)
print("profile and journal line updated")

# Step 2 (his request, 2026-11): move the 12-participant trial bullet above the 5-bar robot bullets on page 1.
# Swap two vertical bands of the page by redacting them and redrawing them (as vector content) in the new order.
src = pymupdf.open(OUT)
dst = pymupdf.open(OUT)
pg = dst[0]
X0, X1 = 40.0, 556.0
TOP, MID, BOT = 417.6, 494.4, 532.6          # 5-bar + stiffness bullets = [TOP, MID); 12-participant bullet = [MID, BOT)
pg.add_redact_annot(pymupdf.Rect(X0, TOP, X1, BOT), fill=(1, 1, 1))
pg.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE)
h2 = BOT - MID
pg.show_pdf_page(pymupdf.Rect(X0, TOP, X1, TOP + h2), src, 0, clip=pymupdf.Rect(X0, MID, X1, BOT))
pg.show_pdf_page(pymupdf.Rect(X0, TOP + h2, X1, BOT), src, 0, clip=pymupdf.Rect(X0, TOP, X1, MID))
dst.save(OUT + ".tmp", garbage=3, deflate=True)
src.close(); dst.close()
os.replace(OUT + ".tmp", OUT)
print("reordered bullets on page 1")

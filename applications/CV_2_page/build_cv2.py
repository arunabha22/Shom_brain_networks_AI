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
    p.insert_text((x_bul, y), "•", fontname="cmr", fontsize=SIZE)
    p.insert_text((x_txt, y), name, fontname="cmbx", fontsize=SIZE)
    p.insert_text((x_txt + fb.text_length(name, SIZE), y), title, fontname="cmr", fontsize=SIZE)
    words, line = detail.split(), ""
    for w in words:                      # simple word wrap for the detail line(s)
        test = (line + " " + w).strip()
        if x_txt + fr.text_length(test, SIZE) > x_max:
            y += lead; p.insert_text((x_txt, y), line, fontname="cmr", fontsize=SIZE); line = w
        else:
            line = test
    y += lead; p.insert_text((x_txt, y), line, fontname="cmr", fontsize=SIZE)
    y += lead + 2

meta = d.metadata
meta.update(title="Arunabha Majumder CV", author="Arunabha Majumder", creator="Arunabha Majumder", producer="Arunabha Majumder")
d.set_metadata(meta)
d.save(OUT, garbage=3, deflate=True)
print("saved", OUT, "last baseline", round(y, 1))

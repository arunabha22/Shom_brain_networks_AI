import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import NAME, tidy
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

# Designed one-page CV in the style of a template he liked (navy bars, round photo, big name).
# No skill-percentage bars: no made-up numbers. Facts follow CLAUDE.md.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
PHOTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/assets/photo.jpeg"
PATH = OUT + "Arunabha_Majumder_CV_Designed.pdf"
NAVY = HexColor("#25344F"); TXT = HexColor("#222222"); HATCH = HexColor("#BFC5CE")
W, H = A4
LX, LW = 38, 178          # left column
RX, RW = 238, 320         # right column

def style(size=8.8, bold=False, center=False, color=TXT, lead=1.3):
    return ParagraphStyle("s", fontName="Arial-B" if bold else "Arial", fontSize=size, leading=size * lead,
                          textColor=color, alignment=TA_CENTER if center else 0)

def para(c, text, x, y, w, **k):
    p = Paragraph(tidy(text), style(**k)); _, h = p.wrap(w, 1000); p.drawOn(c, x, y - h); return y - h

def bar(c, text, x, y, w):
    c.setFillColor(NAVY); c.rect(x, y - 17, w, 17, stroke=0, fill=1)
    c.setFillColor(white); c.setFont("Arial", 9.5); c.drawCentredString(x + w / 2, y - 12, text.upper())
    return y - 26

def bullets(c, items, x, y, w, size=9):
    for it in items:
        c.setFillColor(TXT); c.circle(x + 8, y - size * 0.62, 1.6, stroke=0, fill=1)
        y = para(c, it, x + 16, y, w - 16, size=size) - 3.5
    return y

def hatch_circle(c, cx, cy, r):
    c.saveState(); p = c.beginPath(); p.circle(cx, cy, r); c.clipPath(p, stroke=0, fill=0)
    c.setStrokeColor(HATCH); c.setLineWidth(0.6)
    for i in range(-int(2 * r), int(2 * r), 4): c.line(cx - r + i, cy - r, cx + r + i, cy + r)
    c.restoreState()

def icon(c, kind, x, y):
    c.setFillColor(NAVY); c.circle(x, y, 9, stroke=0, fill=1)
    c.setFillColor(white); c.setStrokeColor(white); c.setLineWidth(0.9)
    if kind == "phone":
        c.roundRect(x - 2.6, y - 4.5, 5.2, 9, 1.2, stroke=0, fill=1)
        c.setFillColor(NAVY); c.rect(x - 1.6, y - 2.6, 3.2, 5.6, stroke=0, fill=1)
    elif kind == "mail":
        c.rect(x - 4.5, y - 3, 9, 6, stroke=0, fill=1); c.setStrokeColor(NAVY)
        c.line(x - 4.5, y + 3, x, y - 0.5); c.line(x, y - 0.5, x + 4.5, y + 3)
    elif kind == "web":
        c.circle(x, y, 4.5, stroke=1, fill=0); c.line(x - 4.5, y, x + 4.5, y); c.ellipse(x - 2, y - 4.5, x + 2, y + 4.5)
    elif kind == "home":
        p = c.beginPath(); p.moveTo(x - 5, y); p.lineTo(x, y + 4.8); p.lineTo(x + 5, y); p.close(); c.drawPath(p, stroke=0, fill=1)
        c.rect(x - 3.4, y - 4, 6.8, 4.2, stroke=0, fill=1)

c = canvas.Canvas(PATH, pagesize=A4)
c.setAuthor(NAME); c.setCreator(NAME); c.setTitle("Arunabha Majumder CV"); c.setSubject(""); c.setKeywords("")
c._doc.info.producer = NAME

# decoration
c.setFillColor(NAVY); c.rect(0, H - 118, 148, 118, stroke=0, fill=1)
hatch_circle(c, W - 8, H - 10, 55); hatch_circle(c, -4, 22, 40); hatch_circle(c, W - 10, 20, 62)

# round photo
cx, cy, r = 128, H - 128, 72
c.setFillColor(white); c.circle(cx, cy, r + 6, stroke=0, fill=1)
c.saveState(); p = c.beginPath(); p.circle(cx, cy, r); c.clipPath(p, stroke=0, fill=0)
img = ImageReader(PHOTO); iw, ih = img.getSize(); s = 2 * r / min(iw, ih)
c.drawImage(img, cx - iw * s / 2, cy - ih * s / 2 + 18, iw * s, ih * s); c.restoreState()
c.setStrokeColor(NAVY); c.setLineWidth(3); c.circle(cx, cy, r + 1.5, stroke=1, fill=0)

# name
c.setFillColor(NAVY); c.setFont("Arial-B", 40)
c.drawString(228, H - 82, "ARUNABHA"); c.drawString(262, H - 126, "MAJUMDER")
c.setFillColor(TXT); c.setFont("Arial", 13); c.drawString(300, H - 150, "Mechanical | Mechatronics Engineer")

# left column
y = H - 228
c.setFillColor(TXT); c.setFont("Arial", 15); c.drawCentredString(LX + LW / 2, y, "About Me"); y -= 10
y = para(c, "I design, build and test robotic hardware and exoskeletons, from the first hand sketch to a tested "
            "prototype. PhD researcher at Aalborg University.", LX + 4, y, LW - 8, size=9, center=True) - 14
for kind, t in [("phone", "+45 71 62 24 00"), ("mail", "somrkmv1997@gmail.com"), ("mail", "97arunabhasit027@gmail.com"),
                ("web", "arunabha22.github.io/arunabha-majumder"), ("home", "Aalborg, Denmark")]:
    icon(c, kind, LX + 10, y - 3); c.setFillColor(TXT); c.setFont("Arial", 8.2 if kind == "web" else 8.8)
    c.drawString(LX + 26, y - 6, t); y -= 25
y -= 4
y = bar(c, "Language", LX, y, LW)
y = bullets(c, ["English (C1)", "Bengali (native)", "Hindi (spoken)"], LX + 6, y, LW - 6) - 6
y = bar(c, "Expertise", LX, y, LW)
y = bullets(c, ["Mechanical design and prototyping", "Stiffness analysis in SolidWorks", "Genetic algorithm optimisation",
                "Sensor integration, test rigs", "Motion capture and EMG testing", "Hand sketching, illustration"],
            LX + 6, y, LW - 6) - 6
y = bar(c, "Software", LX, y, LW)
y = bullets(c, ["SolidWorks (CSWA)", "MATLAB/Simulink, LabVIEW", "Arduino, Python (basic)", "Qualisys",
                "Bambu Lab, Ultimaker Cura", "Adobe Illustrator, Photoshop", "Procreate, LaTeX"], LX + 6, y, LW - 6)

# right column
y = H - 214
y = bar(c, "Experience", RX, y, RW)
for org, place, yrs, desc in [
    ("Aalborg University", "PhD Researcher, Shoulder Exoskeleton", "2023 - Present",
     "Designed a hybrid exoskeleton (spring + 6 Nm motor) that uses over 25% less energy, Best Paper Award. "
     "Integrated motor, encoder and force sensors, built test rigs, and tested with 12 people. "
     "Estimated force on a 5-bar robot within 10% RMS error. Implemented an Arduino trigger to sync the robot "
     "with Qualisys. Taught courses and supervised students."),
    ("CSIR-CMERI, India", "MTech Researcher, Pneumatic Muscles", "2020 - 2022",
     "Fabricated pneumatic muscles. Designed the outer PID loop of a neural network-based controller in "
     "MATLAB/Simulink and implemented it in LabVIEW to drive the muscle (0.3 - 0.78% error)."),
    ("Siddaganga Institute of Technology", "Bachelor's Project, Rehab Exoskeleton", "2018 - 2019",
     "Designed and built an upper-limb exoskeleton for a paralysed arm: CAD, machining, assembly and testing.")]:
    y = para(c, "<b>%s</b><br/><b>%s</b><br/><b>%s</b>" % (org, place, yrs), RX, y, RW, size=9, lead=1.28) - 2
    y = para(c, desc, RX, y, RW, size=8.8) - 10
y -= 2
y = bar(c, "Education", RX, y, RW)
for uni, deg in [("Aalborg University, Denmark", "PhD, Mechatronics and Robotics | 2023 - present"),
                 ("CSIR-CMERI (AcSIR), India", "MTech, Mechatronics | 2020 - 2022"),
                 ("Siddaganga Institute of Technology, India", "BTech, Mechanical Engineering | 2015 - 2019"),
                 ("Bangiya Sangeet Parishad, India", "Diploma in Fine Arts (Painting)")]:
    y = para(c, "<b>%s</b><br/>%s" % (uni, deg), RX, y, RW, size=8.8) - 6
y -= 4
y = bar(c, "Awards and Publications", RX, y, RW)
y = bullets(c, ["Best Paper Award, IFToMM ISRM 2026 (Springer)", "IEEE CONECCT 2022 paper",
            "Best Major Project Award and TATA Technologies grant, 2019"], RX, y, RW, size=8.8) - 8
y = bar(c, "References", RX, y, RW)
para(c, "Available upon request.", RX, y, RW, size=8.8)
c.showPage(); c.save()

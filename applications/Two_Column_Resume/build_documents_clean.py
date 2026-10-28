import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import NAME, tidy, esc
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, FrameBreak, HRFlowable, Image

# Clean, low-text one-page two-column CV (feedback: too much text) built from his own resume, corrected to CLAUDE.md facts.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
PHOTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/assets/photo.jpeg"
PATH = OUT + "Arunabha_Majumder_CV_1page_clean.pdf"
ACC = HexColor("#1F4E79"); GREY = HexColor("#404040")
W, H = A4; M = 1.2 * cm; GAP = 0.6 * cm; HEAD_H = 3.3 * cm
LW = (W - 2 * M - GAP) * 0.35; RW = (W - 2 * M - GAP) - LW

def st(size=8.9, bold=False, color=GREY, after=1.5, lead=1.22, left=0, first=0):
    return ParagraphStyle("s", fontName="Arial-B" if bold else "Arial", fontSize=size, leading=size * lead,
                          textColor=color, spaceAfter=after, leftIndent=left, firstLineIndent=first)

def P(t, **k): return Paragraph(tidy(t), st(**k))
def sec(t): return [Spacer(0, 4), P(t.upper(), size=9.6, bold=True, color=ACC, after=0),
                    HRFlowable(width="100%", thickness=0.7, color=ACC, spaceBefore=1, spaceAfter=3)]
def bl(t, size=8.6): return Paragraph(tidy("&bull;&nbsp;" + t), st(size=size, left=8, first=-8, after=3))
def role(title, org, dates):
    return [P("<b>%s</b>" % title, size=8.9, color=HexColor("#000000"), after=0),
            P("%s &nbsp;|&nbsp; <i>%s</i>" % (org, dates), size=8.2, after=1.5)]

head = [P(NAME, size=21, bold=True, color=ACC, after=1, lead=1.1),
        P("Mechanical | Mechatronics Engineer", size=11, bold=True, color=HexColor("#000000"), after=3),
        P("Aalborg, Denmark &nbsp;|&nbsp; +45 71 62 24 00", size=8.6, after=0),
        P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=8.6, after=0),
        P("Portfolio: arunabha22.github.io/arunabha-majumder &nbsp;|&nbsp; LinkedIn: arunabha-majumder-681264107", size=8.6, after=0)]

left = sec("Education") + [
    P("<b>PhD, Mechatronics and Robotics</b>", after=0), P("Aalborg University | 2023 - present", after=0),
    P("Thesis expected March", size=8.2, after=0), P("Study abroad: NUS Singapore, 2025", size=8.2, after=4),
    P("<b>MTech, Mechatronics</b>", after=0), P("CSIR-CMERI, India | 2020 - 2022", after=4),
    P("<b>BTech, Mechanical Engineering</b>", after=0), P("SIT (VTU), India | 2015 - 2019", after=4),
    P("<b>Diploma in Fine Arts</b>", after=0), P("Bangiya Sangeet Parishad, India", after=0),
] + sec("Skills") + [
    P("SolidWorks (CSWA) | 3D printing"), P("Stiffness analysis in SolidWorks"), P("Genetic algorithm optimisation"),
    P("MATLAB/Simulink | LabVIEW | Arduino"), P("Sensor integration | Test rigs"), P("Qualisys motion capture and EMG"),
    P("Hand sketching | Adobe Illustrator"),
] + sec("Awards") + [
    P("Best Paper Award, IFToMM ISRM 2026"), P("Best Major Project Award, 2019"), P("TATA Technologies Innovation Grant"),
] + sec("Publications") + [
    P("Hybrid actuated shoulder exoskeleton, ISRM 2026 (Springer)"), P("Neural network-based control of a pneumatic muscle, IEEE CONECCT 2022"),
] + sec("Languages") + [P("English (C1) | Bengali | Hindi")] + sec("References") + [P("Available upon request")]

right = sec("Profile") + [
    P("Mechanical and mechatronics engineer. I design, build and test robotic hardware and exoskeletons, "
      "from the first sketch to a tested prototype.", size=9.2, after=1)
] + sec("Experience") + role("Research Engineer, Shoulder Exoskeleton (PhD)", "Aalborg University, Denmark", "2023 - Present") + [
    bl("Designed a hybrid exoskeleton (spring + 6 Nm motor) that uses over 25% less energy. Best Paper Award.", 9),
    bl("SolidWorks design and genetic algorithm optimisation; stiffness tested on a physical test setup.", 9),
    bl("Integrated the motor, encoder and force sensors; built test rigs.", 9),
    bl("Designed and modelled a novel 5-bar parallel robot with VSM; estimated its stiffness with less than 10% error and quantified human arm impedance.", 9),
    bl("Collected EMG and motion data from 12 people; implemented an Arduino trigger to sync robot and Qualisys.", 9),
    bl("Taught university courses and supervised Bachelor's students.", 9),
    Spacer(0, 5),
] + role("MTech Researcher, Pneumatic Muscles", "CSIR-CMERI, India", "2020 - 2022") + [
    bl("Fabricated and assembled pneumatic muscles and collected test data.", 9),
    bl("Designed the outer PID loop of a neural network-based controller in MATLAB/Simulink and implemented "
       "it in LabVIEW to drive the muscle (0.3 - 0.78% error).", 9),
    Spacer(0, 5),
] + role("Bachelor's Project, Rehabilitation Exoskeleton", "Siddaganga Institute of Technology, India", "2018 - 2019") + [
    bl("Designed and built an upper-limb exoskeleton for a paralysed arm: CAD, machining, assembly and testing.", 9),
]

doc = BaseDocTemplate(PATH, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=M,
                      title="Arunabha Majumder CV", author=NAME, creator=NAME, producer=NAME, subject="", keywords="")
top = H - M - HEAD_H
frames = [Frame(M, top, W - 2 * M - 2.6 * cm, HEAD_H, id="head", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0),
          Frame(M, M, LW, top - M - 0.2 * cm, id="left", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0),
          Frame(M + LW + GAP, M, RW, top - M - 0.2 * cm, id="right", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)]

def deco(c, d):
    c.saveState()
    c.drawImage(PHOTO, W - M - 2.35 * cm, H - M - 2.95 * cm, width=2.35 * cm, height=2.95 * cm, preserveAspectRatio=True, mask="auto")
    c.setStrokeColor(ACC); c.setLineWidth(1.2); c.line(M, top - 0.1 * cm, W - M, top - 0.1 * cm)
    c.setStrokeColor(HexColor("#C8D3DF")); c.setLineWidth(0.6)
    x = M + LW + GAP / 2; c.line(x, M, x, top - 0.3 * cm)
    c.restoreState()

doc.addPageTemplates([PageTemplate(id="p", frames=frames, onPage=deco)])
doc.build(head + [FrameBreak()] + left + [FrameBreak()] + right)

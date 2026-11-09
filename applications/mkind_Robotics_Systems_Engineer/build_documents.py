import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import NAME, tidy
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, SimpleDocTemplate, Frame, PageTemplate, Paragraph, Spacer,
                                FrameBreak, HRFlowable)

# mkind (Munich) - Robotics Systems Engineer: robot work cells, data collection setups, deployment, CE.
# Ad REQUIRES fluent German: he has none (said honestly in the letter). No CE / commissioning / PLC claims.
# Short two-column CV (same layout as Two_Column_Resume/build_documents_clean.py). Files named "AM mkind ...".
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
PHOTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/assets/photo.jpeg"
ACC = HexColor("#1F4E79"); GREY = HexColor("#404040"); BLACK = HexColor("#000000")
W, H = A4; M = 1.2 * cm; GAP = 0.6 * cm; HEAD_H = 3.3 * cm
LW = (W - 2 * M - GAP) * 0.35; RW = (W - 2 * M - GAP) - LW

def st(size=8.9, bold=False, color=GREY, after=1.5, lead=1.22, left=0, first=0):
    return ParagraphStyle("s", fontName="Arial-B" if bold else "Arial", fontSize=size, leading=size * lead,
                          textColor=color, spaceAfter=after, leftIndent=left, firstLineIndent=first)

def P(t, **k): return Paragraph(tidy(t), st(**k))
def sec(t): return [Spacer(0, 4), P(t.upper(), size=9.6, bold=True, color=ACC, after=0),
                    HRFlowable(width="100%", thickness=0.7, color=ACC, spaceBefore=1, spaceAfter=3)]
def bl(t): return Paragraph(tidy("&bull;&nbsp;" + t), st(size=9, left=8, first=-8, after=3))
def role(title, org, dates):
    return [P("<b>%s</b>" % title, size=9.2, color=BLACK, after=0),
            P("%s &nbsp;|&nbsp; <i>%s</i>" % (org, dates), size=8.2, after=1.5)]

def cv():
    path = OUT + "AM mkind CV.pdf"
    head = [P(NAME, size=21, bold=True, color=ACC, after=1, lead=1.1),
            P("Mechatronics Engineer", size=11, bold=True, color=BLACK, after=3),
            P("Aalborg, Denmark &nbsp;|&nbsp; +45 71 62 24 00", size=8.6, after=0),
            P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=8.6, after=0),
            P("Portfolio: arunabha22.github.io/arunabha-majumder &nbsp;|&nbsp; LinkedIn: arunabha-majumder-681264107",
              size=8.6, after=0)]
    left = sec("Education") + [
        P("<b>PhD, Mechatronics and Robotics</b>", after=0), P("Aalborg University | 2023 - present", after=0),
        P("Thesis expected to be finished in March", size=8.2, after=0),
        P("Study abroad: NUS Singapore, 2025", size=8.2, after=4),
        P("<b>MTech, Mechatronics</b>", after=0), P("CSIR-CMERI, India | 2020 - 2022", after=4),
        P("<b>BTech, Mechanical Engineering</b>", after=0), P("SIT (VTU), India | 2015 - 2019", after=4),
        P("<b>Senior Diploma in Fine Arts (Painting)</b>", after=0),
        P("Bangiya Sangeet Parishad | 2008, Distinction", after=0),
    ] + sec("Skills") + [
        P("SolidWorks (CSWA) | 3D printing"), P("Fusion 360 (basic, last used 2019)"),
        P("Motors, encoders, force/torque sensors"), P("Arduino | LabVIEW | MATLAB/Simulink"),
        P("PID control | Python (basic)"), P("Qualisys motion capture and EMG"),
        P("Hand sketching and painting"), P("Illustrator | Photoshop | Procreate"),
    ] + sec("Awards") + [
        P("Best Paper Award, IFToMM ISRM 2026"), P("Best Major Project Award, 2019"),
        P("TATA Technologies Prayatna grant"),
    ] + sec("Languages") + [P("English (C1) | Bengali | Hindi")] + sec("References") + [
        P("<b>Shaoping Bai</b>, Professor", after=0), P("Aalborg University | sbh@mp.aau.dk", size=8.2, after=3),
        P("<b>Lars Rosgaard Jensen</b>, Associate Professor", after=0),
        P("Head of Section and Head of Labs, Aalborg University", size=8.2, after=3),
        P("<b>Anderson de Souza Castelo Oliveira</b>, Associate Professor", after=0),
        P("Materials and Production, Aalborg University", size=8.2)]
    right = sec("Profile") + [
        P("I build physical robot systems and get them working: mechanics, motors, sensors, wiring up the data "
          "side and the control loop. I like small teams where I can touch every part of the hardware.",
          size=9.2, after=1)
    ] + sec("Experience") + role("PhD Researcher, Robotics", "Aalborg University, Denmark", "2023 - Present") + [
        bl("Designed a hybrid shoulder exoskeleton (spring mechanism + 6 Nm motor) that uses over 25% "
           "less motor energy. Best Paper Award, ISRM 2026."),
        bl("Integrated the motor, encoder and force/torque sensors and measured stiffness on a physical setup."),
        bl("When a clutch kept breaking, swapped it for a simple bolt-locking clutch that was easy to make."),
        bl("Designed and modelled a novel 5-bar planar parallel robot with VSM; estimated its stiffness with less "
           "than 10% error and quantified human arm impedance."),
        bl("Ran data collection: EMG from 12 people and arm motion from 6 with Qualisys; implemented an Arduino "
           "trigger to sync robot motion with the recordings."),
        bl("Taught university courses and supervised Bachelor's students."),
        Spacer(0, 5),
    ] + role("MTech Researcher, Soft Exosuit", "CSIR-CMERI, India", "2020 - 2022") + [
        bl("Fabricated and assembled pneumatic muscles; designed the outer PID loop of a neural network-based "
           "controller in MATLAB/Simulink and implemented it in LabVIEW to drive the muscle."),
        Spacer(0, 5),
    ] + role("Bachelor's Projects", "Siddaganga Institute of Technology, India", "2017 - 2019") + [
        bl("Built an arm exoskeleton and exo glove for a paralysed arm: CAD, machining, assembly, testing."),
        bl("Built a Go-Kart and an Efficycle hybrid vehicle with student teams."),
    ]
    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=M,
                          title="AM mkind CV", author=NAME, creator=NAME, producer=NAME, subject="", keywords="")
    top = H - M - HEAD_H
    frames = [Frame(M, top, W - 2 * M - 2.6 * cm, HEAD_H, id="head", leftPadding=0, rightPadding=0, topPadding=0,
                    bottomPadding=0),
              Frame(M, M, LW, top - M - 0.2 * cm, id="left", leftPadding=0, rightPadding=0, topPadding=0,
                    bottomPadding=0),
              Frame(M + LW + GAP, M, RW, top - M - 0.2 * cm, id="right", leftPadding=0, rightPadding=0,
                    topPadding=0, bottomPadding=0)]
    def deco(c, d):
        c.saveState()
        c.drawImage(PHOTO, W - M - 2.35 * cm, H - M - 2.95 * cm, width=2.35 * cm, height=2.95 * cm,
                    preserveAspectRatio=True, mask="auto")
        c.setStrokeColor(ACC); c.setLineWidth(1.2); c.line(M, top - 0.1 * cm, W - M, top - 0.1 * cm)
        c.setStrokeColor(HexColor("#C8D3DF")); c.setLineWidth(0.6)
        x = M + LW + GAP / 2; c.line(x, M, x, top - 0.3 * cm)
        c.restoreState()
    doc.addPageTemplates([PageTemplate(id="p", frames=frames, onPage=deco)])
    doc.build(head + [FrameBreak()] + left + [FrameBreak()] + right)
    return path

PARAS = [
    "I'd like to apply for the Robotics Systems Engineer role. You say you welcome junior people who want to grow "
    "into more ownership, and that is exactly where I am.",
    "Most of my PhD at Aalborg University was spent building physical things and making them work together. I "
    "designed a shoulder exoskeleton with a spring mechanism and a 6 Nm motor, 3D printed the first parts, had the "
    "final ones manufactured, and integrated the motor, encoder and force/torque sensors myself. It uses over 25% less "
    "motor energy and won the Best Paper Award at ISRM 2026. Not everything worked the first time. My first clutch "
    "kept breaking and was hard to make, so I replaced it with a simple bolt-locking one. I learned to keep things "
    "simple for the person who has to build and use it, which sounds close to how you think about your cells.",
    "I have also set up data collection with real people. I recorded EMG from 12 participants and arm motion from 6 "
    "with Qualisys, and implemented an Arduino trigger so the robot's motion and the recordings stayed in sync. "
    "In my Master's I designed the outer PID loop of a pneumatic muscle controller and ran it in LabVIEW. As a "
    "student I built an arm exoskeleton, an exo glove, a Go-Kart and a hybrid Efficycle. Outside engineering I "
    "paint and do graphic design (Senior Diploma in Fine Arts; Illustrator, Photoshop, Procreate), which helps when "
    "I need to explain a design to someone quickly.",
    "I should be upfront: I don't speak German, and I haven't done CE certification or customer-site "
    "commissioning yet. I know German is on your list, so I understand if that rules me out. If not, I'm ready to "
    "move to Munich, and I can start as soon as possible once the visa is sorted.",
    "Thanks for reading.",
]

def letter():
    path = OUT + "AM mkind Cover Letter.pdf"
    head = [P(NAME, size=18, bold=True, color=ACC, after=1, lead=1.1),
            P("+45 71 62 24 00 &nbsp;|&nbsp; Aalborg, Denmark", size=9, after=0),
            P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=9, after=0),
            P("Portfolio: arunabha22.github.io/arunabha-majumder", size=9, after=12),
            P("mkind, Munich", size=10, after=4),
            P("<b>Robotics Systems Engineer</b>", size=10.5, color=BLACK, after=10),
            P("Hi mkind team,", size=10.5, color=BLACK, after=6)]
    body = [P(t, size=10.2, color=BLACK, after=7, lead=1.32) for t in PARAS] + [
        P("Best,", size=10.2, color=BLACK, after=2), P(NAME, size=10.2, color=BLACK)]
    SimpleDocTemplate(path, pagesize=A4, leftMargin=2.1 * cm, rightMargin=2.1 * cm, topMargin=1.8 * cm,
                      bottomMargin=1.6 * cm, title="AM mkind Cover Letter", author=NAME, creator=NAME,
                      producer=NAME, subject="", keywords="").build(head + body)
    return path

if __name__ == "__main__":
    print(cv()); print(letter())

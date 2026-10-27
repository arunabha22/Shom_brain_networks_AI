import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import NAME, tidy, esc
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, FrameBreak, HRFlowable, Image

# One-page, two-column general CV built from his own resume, corrected to CLAUDE.md facts.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
PHOTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/assets/photo.jpeg"
PATH = OUT + "Arunabha_Majumder_CV_1page.pdf"
ACC = HexColor("#1F4E79"); GREY = HexColor("#404040")
W, H = A4; M = 1.2 * cm; GAP = 0.6 * cm; HEAD_H = 3.3 * cm
LW = (W - 2 * M - GAP) * 0.35; RW = (W - 2 * M - GAP) - LW

def st(size=8.6, bold=False, color=GREY, after=1.5, lead=1.22, left=0, first=0):
    return ParagraphStyle("s", fontName="Arial-B" if bold else "Arial", fontSize=size, leading=size * lead,
                          textColor=color, spaceAfter=after, leftIndent=left, firstLineIndent=first)

def P(t, **k): return Paragraph(tidy(t), st(**k))
def sec(t): return [Spacer(0, 4), P(t.upper(), size=9.6, bold=True, color=ACC, after=0),
                    HRFlowable(width="100%", thickness=0.7, color=ACC, spaceBefore=1, spaceAfter=3)]
def bl(t, size=8.6): return Paragraph(tidy("&bull;&nbsp;" + t), st(size=size, left=8, first=-8, after=1.6))
def role(title, org, dates):
    return [P("<b>%s</b>" % title, size=8.9, color=HexColor("#000000"), after=0),
            P("%s &nbsp;|&nbsp; <i>%s</i>" % (org, dates), size=8.2, after=1.5)]

head = [P(NAME, size=21, bold=True, color=ACC, after=1, lead=1.1),
        P("Mechanical | Mechatronics Engineer", size=11, bold=True, color=HexColor("#000000"), after=3),
        P("Aalborg, Denmark &nbsp;|&nbsp; +45 71 62 24 00", size=8.6, after=0),
        P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=8.6, after=0),
        P("Portfolio: arunabha22.github.io/arunabha-majumder &nbsp;|&nbsp; LinkedIn: arunabha-majumder-681264107", size=8.6, after=0)]

left = sec("Education") + [
    P("<b>PhD, Mechatronics and Robotics</b>", after=0), P("Aalborg University, Denmark", after=0),
    P("<i>2023 - Present (thesis expected March)</i>", after=1),
    P("Study abroad: National University of Singapore (NUS), Sep - Nov 2025", size=8.2, after=3),
    P("<b>MTech, Mechatronics</b>", after=0), P("AcSIR - CSIR-CMERI, Durgapur, India", after=0), P("<i>2020 - 2022</i>", after=3),
    P("<b>BTech, Mechanical Engineering</b>", after=0), P("Siddaganga Institute of Technology (VTU), India", after=0),
    P("<i>2015 - 2019</i>", after=3),
    P("<b>Diploma in Fine Arts (Painting)</b>", after=0), P("Bangiya Sangeet Parishad, India", after=0),
] + sec("Skills") + [
    P("<b>Design:</b> mechanical product development, actuators and robotic mechanisms, Design for Assembly"),
    P("<b>Analysis:</b> stiffness and kinematic modelling, stiffness analysis in SolidWorks, design optimisation with a genetic algorithm"),
    P("<b>Testing:</b> prototype building, sensor integration, custom test rigs, test data processing"),
    P("<b>Visuals:</b> hand sketching of concepts, technical illustrations for papers, posters and demos"),
] + sec("Tools") + [
    P("<b>CAD:</b> SolidWorks (CSWA), 3D printing (Bambu Lab, Ultimaker Cura)"),
    P("<b>Software:</b> MATLAB/Simulink, Arduino, LaTeX, Python and LabVIEW (basic)"),
    P("<b>Lab:</b> Qualisys motion capture and data acquisition, Forsentec force/torque sensors, pneumatics"),
    P("<b>Graphics:</b> Adobe Illustrator, Photoshop, Procreate"),
] + sec("Awards") + [
    bl("Best Research Paper Award, 9th IFToMM ISRM (2026)"),
    bl("Certified SolidWorks Associate (CSWA)"),
    bl("Best Major Project Award (2019)"),
    bl("TATA Technologies Innovation Grant, INR 100,000 (2019)"),
] + sec("Languages") + [P("English (C1), Bengali (native), Hindi (spoken)")] + sec("Interests") + [
    P("Painting and illustration; built a Go-Kart (2017) and an Efficycle hybrid vehicle (2018) with student teams"),
] + sec("References") + [P("Available upon request.")]

right = sec("Profile") + [
    P("Mechanical and mechatronics engineer who takes robotic hardware from a hand sketch to CAD, prototypes and "
      "testing with real people. I design actuators and exoskeleton mechanisms, integrate motors and sensors, and "
      "check designs against measurements. I explain ideas clearly with sketches, reports and talks.", size=8.8, after=1)
] + sec("Experience") + role("Research Engineer, Shoulder Exoskeleton (PhD project VIEXO)", "Aalborg University, Denmark", "2023 - Present") + [
    bl("Designed a hybrid shoulder exoskeleton where a parallel spring carries most of the arm load and a 6 Nm motor "
       "adds the rest; cut energy use by more than 25% (Best Paper Award, IFToMM ISRM 2026)."),
    bl("Took the design from hand sketches to SolidWorks models and drawings, checked parts with stiffness analysis in "
       "SolidWorks, optimised the design with a genetic algorithm, and 3D printed and rebuilt parts after each test."),
    bl("Integrated the motor, encoder and force sensors into the frame and built custom test rigs."),
    bl("Worked in a team of 3 on an Assist-as-Needed controller (my part: equations such as the Fourier fit, and "
       "defining the GUI behaviour); muscle effort dropped by more than 15%."),
    bl("Collected data from 12 participants (EMG with the Qualisys data acquisition system, and motion capture)."),
    bl("Estimated tip force on a 5-bar parallel robot from its variable-stiffness actuators (within 10% RMS error vs "
       "a force sensor), removing the need for an extra sensor; mapped actuator stiffness to workspace stiffness."),
    bl("Built an Arduino-based trigger to sync robot motion with Qualisys cameras for arm impedance tests (6 participants)."),
    bl("Taught university courses and supervised Bachelor's students (2023 - 2025)."),
    Spacer(0, 3),
] + role("MTech Researcher, Pneumatic Artificial Muscles", "CSIR-CMERI (National Laboratory), Durgapur, India", "2020 - 2022") + [
    bl("Fabricated and assembled pneumatic muscles to an existing lab design and collected test data on the lab's setup."),
    bl("Used the data to design the outer PID loop of a gain-scheduled controller in MATLAB/Simulink "
       "(0.3 - 0.78% position error, IEEE CONECCT 2022)."),
    Spacer(0, 3),
] + role("Bachelor's Capstone, Upper-Limb Rehabilitation Exoskeleton", "Siddaganga Institute of Technology, India", "2018 - 2019") + [
    bl("Led CAD design, machining, assembly and user testing; Best Major Project Award and TATA Technologies grant."),
] + sec("Publications") + [
    bl("Majumder, A., Wagner, J.W., Zhu, Y., Oliveira, A.S., Bai, S. \"A Hybrid Actuated Shoulder Exoskeleton for "
       "Energy-Efficient Upper Arm Support.\" ISRM 2026, Springer. <b>Best Research Paper Award.</b>"),
    bl("Majumder, A., Sarkar, D., Chakraborty, S., Singh, A., Roy, S.S., Arora, A. \"Neural Network-Based Gain "
       "Scheduled Position Control of a Pneumatic Artificial Muscle.\" IEEE CONECCT 2022."),
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

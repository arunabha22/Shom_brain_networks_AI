import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import NAME, tidy
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, SimpleDocTemplate, Frame, PageTemplate, Paragraph, Spacer,
                                FrameBreak, HRFlowable)

# mkind (Munich) - Robotics Systems Engineer. His rules (2026-11): title "Research Assistant, Aalborg University";
# NO clutch story; outer PID loop has integral anti-windup + error nonlinearisation; 6 participants = 5-bar robot;
# German = "willing to learn" only, no gap talk; GATE + Study Abroad heading + portfolio; letter ends with
# innovative ideas. Files named "AM mkind ...".
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
PHOTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/assets/photo.jpeg"
ACC = HexColor("#1F4E79"); ACC2 = HexColor("#2E75B6"); GREY = HexColor("#3A3A3A"); BLACK = HexColor("#000000")
PANEL = HexColor("#EEF3F8")
W, H = A4; M = 1.2 * cm; GAP = 0.7 * cm; HEAD_H = 3.5 * cm
LW = (W - 2 * M - GAP) * 0.34; RW = (W - 2 * M - GAP) - LW
PAD = 0.25 * cm

def st(size=9, bold=False, color=GREY, after=1.5, lead=1.25, left=0, first=0, italic=False):
    font = "Arial-B" if bold else "Arial"
    return ParagraphStyle("s", fontName=font, fontSize=size, leading=size * lead, textColor=color,
                          spaceAfter=after, leftIndent=left, firstLineIndent=first)

def P(t, **k): return Paragraph(tidy(t), st(**k))
def sec(t, first=False):
    return [Spacer(0, 0 if first else 6), P(t.upper(), size=10, bold=True, color=ACC, after=0),
            HRFlowable(width="100%", thickness=1.1, color=ACC2, spaceBefore=1.5, spaceAfter=4)]
def bl(t): return Paragraph(tidy("&bull;&nbsp;" + t), st(size=9.2, left=9, first=-9, after=3.2, lead=1.27))
def role(title, org, dates):
    return [P("<b>%s</b>" % title, size=9.6, color=BLACK, after=0),
            P("%s &nbsp;|&nbsp; <i>%s</i>" % (org, dates), size=8.6, color=ACC2, after=2.5)]
def item(a, b, gap=4): return [P("<b>%s</b>" % a, size=9, color=BLACK, after=0), P(b, size=8.5, after=gap)]

def cv():
    path = OUT + "AM mkind CV.pdf"
    head = [P(NAME, size=23, bold=True, color=ACC, after=2, lead=1.1),
            P("Mechatronics Engineer", size=11.5, bold=True, color=BLACK, after=4),
            P("Aalborg, Denmark &nbsp;|&nbsp; +45 71 62 24 00", size=8.8, after=0.5),
            P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=8.8, after=0.5),
            P("Portfolio: arunabha22.github.io/arunabha-majumder", size=8.8, after=0.5),
            P("LinkedIn: linkedin.com/in/arunabha-majumder-681264107", size=8.8, after=0)]
    left = sec("Education", first=True) + \
        item("PhD, Mechatronics and Robotics", "Aalborg University, Denmark<br/>2023 - present, thesis expected to "
             "be finished in March") + \
        item("MTech, Mechatronics", "AcSIR - CSIR-CMERI, India<br/>2020 - 2022") + \
        item("BTech, Mechanical Engineering", "Siddaganga Institute of Technology, India<br/>2015 - 2019") + \
        item("Senior Diploma in Fine Arts (Painting)", "Bangiya Sangeet Parishad<br/>2008, First Division with "
             "Distinction", 0) + \
        sec("Study Abroad") + item("National University of Singapore", "Study abroad stay during my PhD<br/>Sep - Nov 2025",
                                   0) + \
        sec("Skills") + [
            P("<b>CAD:</b> SolidWorks (CSWA), Fusion 360 (basic, last used 2019), technical drawings", size=8.7,
              after=2.5),
            P("<b>Prototyping:</b> 3D printing, hands-on assembly", size=8.7, after=2.5),
            P("<b>Hardware:</b> motors, encoders, force/torque sensors, Arduino", size=8.7, after=2.5),
            P("<b>Control and data:</b> MATLAB/Simulink, LabVIEW, Python (basic), Qualisys motion capture and EMG",
              size=8.7, after=2.5),
            P("<b>Art and design:</b> hand sketching, painting, Adobe Illustrator, Photoshop, Procreate", size=8.7,
              after=0),
        ] + sec("Achievements") + [
            P("Best Paper Award, IFToMM ISRM 2026", size=8.7, after=2), P("Best Major Project Award, 2019", size=8.7,
                                                                           after=2),
            P("TATA Technologies Prayatna grant", size=8.7, after=2), P("GATE qualified", size=8.7, after=0),
        ] + sec("Languages") + [P("English (C1), Bengali (native), Hindi, German (willing to learn)", size=8.7,
                                  after=0)] + sec("References") + [
            P("<b>Prof. Shaoping Bai</b><br/>Aalborg University, sbh@mp.aau.dk", size=8.3, after=2.5),
            P("<b>Assoc. Prof. Lars Rosgaard Jensen</b><br/>Head of Section and Head of Labs, AAU", size=8.3,
              after=2.5),
            P("<b>Assoc. Prof. Anderson de Souza Castelo Oliveira</b><br/>Materials and Production, AAU", size=8.3,
              after=0)]

    right = sec("Profile", first=True) + [
        P("I am a mechatronics engineer who likes building real robot hardware and getting all of it to work "
          "together: the mechanics, the motors and sensors, the control loop and the data side. Over the last 6 "
          "years I have designed exoskeletons and robots, put them together, integrated the electronics, and run "
          "experiments with real people. I like small teams where I can work across the whole hardware stack, learn "
          "from what goes wrong in the lab, and keep making the system simpler for the person who uses it.",
          size=9.3, after=1, lead=1.32)
    ] + sec("Experience") + role("Research Assistant", "Aalborg University, Denmark", "2023 - Present") + [
        bl("Designed a hybrid shoulder exoskeleton: a variable stiffness mechanism (spring pretensioned by a worm "
           "gear) working in parallel with a 6 Nm motor. It uses over 25% less motor energy (Best Paper Award, "
           "IFToMM ISRM 2026)."),
        bl("Optimised the design with a genetic algorithm, modelled it in SolidWorks, 3D printed the first parts "
           "and had the final parts manufactured."),
        bl("Integrated the motor, encoder and force/torque sensors and measured its stiffness on a physical setup."),
        bl("Designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms (VSM); "
           "estimated its stiffness with less than 10% error and quantified human arm impedance."),
        bl("Arm impedance study with the 5-bar robot (6 participants): Qualisys cameras tracked the arm, and I "
           "implemented an Arduino-based trigger to sync the robot's motion with the recording."),
        bl("Collected EMG data from 12 participants with the Qualisys data acquisition system."),
        bl("Taught university courses and supervised Bachelor's students (2023 - 2025)."),
        Spacer(0, 4),
    ] + role("MTech Researcher, Soft Exosuit", "CSIR-CMERI, India", "2020 - 2022") + [
        bl("Fabricated and assembled pneumatic artificial muscles for a soft exosuit. Designed the outer PID loop, "
           "with integral anti-windup and error nonlinearisation, of a neural network-based gain-scheduled "
           "controller in MATLAB/Simulink and implemented it in LabVIEW to drive the muscle (0.3 - 0.78% error)."),
        Spacer(0, 4),
    ] + role("Bachelor's Projects", "Siddaganga Institute of Technology, India", "2017 - 2019") + [
        bl("Built an arm exoskeleton and exo glove for a paralysed arm: CAD, machining, assembly and testing."),
        bl("Built a Go-Kart (2017) and an Efficycle hybrid vehicle (2018) with student teams."),
    ] + sec("Publications") + [
        bl("Hybrid actuated shoulder exoskeleton, IFToMM ISRM 2026 (Springer), Best Paper Award."),
        bl("Neural network-based control of a pneumatic artificial muscle, IEEE CONECCT 2022."),
    ] + sec("Portfolio") + [
        P("Videos and results from my work: "
          "<link href='https://arunabha22.github.io/arunabha-majumder/' color='#2E75B6'>"
          "arunabha22.github.io/arunabha-majumder</link>", size=9.2, after=0),
    ]

    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=M,
                          title="AM mkind CV", author=NAME, creator=NAME, producer=NAME, subject="", keywords="")
    top = H - M - HEAD_H
    body_h = top - M - 0.35 * cm
    frames = [Frame(M, top, W - 2 * M - 2.8 * cm, HEAD_H, id="head", leftPadding=0, rightPadding=0,
                    topPadding=0, bottomPadding=0),
              Frame(M, M, LW, body_h, id="left", leftPadding=PAD, rightPadding=PAD, topPadding=PAD,
                    bottomPadding=PAD),
              Frame(M + LW + GAP, M, RW, body_h, id="right", leftPadding=0, rightPadding=0, topPadding=PAD,
                    bottomPadding=0)]
    def deco(c, d):
        c.saveState()
        c.setFillColor(ACC); c.rect(0, H - 0.35 * cm, W, 0.35 * cm, stroke=0, fill=1)
        c.setFillColor(PANEL); c.rect(M, M, LW, body_h, stroke=0, fill=1)
        c.setFillColor(ACC2); c.rect(M, M + body_h - 0.08 * cm, LW, 0.08 * cm, stroke=0, fill=1)
        c.drawImage(PHOTO, W - M - 2.5 * cm, H - M - 3.15 * cm, width=2.5 * cm, height=3.15 * cm,
                    preserveAspectRatio=True, mask="auto")
        c.setStrokeColor(ACC); c.setLineWidth(1.4); c.line(M, top - 0.12 * cm, W - M, top - 0.12 * cm)
        c.setFillColor(ACC); c.rect(0, 0, W, 0.2 * cm, stroke=0, fill=1)
        c.restoreState()
    doc.addPageTemplates([PageTemplate(id="p", frames=frames, onPage=deco)])
    doc.build(head + [FrameBreak()] + left + [FrameBreak()] + right)
    return path

PARAS = [
    "I'd like to apply for the Robotics Systems Engineer role. I like that you want people who build things with "
    "their hands and take on more ownership over time, because that is how I have worked so far.",
    "As a research assistant at Aalborg University I designed a hybrid shoulder exoskeleton: a variable stiffness "
    "mechanism, with a worm gear pretensioning the spring, working in parallel with a 6 Nm motor. I optimised it "
    "with a genetic algorithm, modelled it in SolidWorks, 3D printed the first parts and had the final ones "
    "manufactured. I integrated the motor, encoder and force/torque sensors and measured its stiffness on a physical "
    "setup. It uses over 25% less motor energy and won the Best Paper Award at ISRM 2026.",
    "I have also built data collection setups with real people, which sounds close to what you do in your lab. I "
    "designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms and used it to "
    "quantify human arm impedance with 6 participants. Qualisys cameras tracked the arm, and I implemented an "
    "Arduino-based trigger so the robot's motion and the recording stayed in sync. I also collected EMG data from "
    "12 participants with the Qualisys system.",
    "In my Master's at CSIR-CMERI I fabricated pneumatic artificial muscles for a soft exosuit and designed the outer "
    "PID loop of a neural network-based gain-scheduled controller, with integral anti-windup and error "
    "nonlinearisation, in MATLAB/Simulink and ran it in LabVIEW. As a student I built an arm exoskeleton, an exo "
    "glove, a Go-Kart and a hybrid Efficycle. I also paint and do graphic design (Senior Diploma in Fine Arts; "
    "Illustrator, Photoshop, Procreate), which helps me sketch and explain ideas quickly.",
    "I'm ready to move to Munich and I'm willing to learn German. I would love to bring new and innovative ideas "
    "to your robot cells, and to keep improving them from what we learn in the lab and at customer sites. My "
    "portfolio is at arunabha22.github.io/arunabha-majumder. Thank you for reading.",
]

def letter():
    path = OUT + "AM mkind Cover Letter.pdf"
    head = [P(NAME, size=18, bold=True, color=ACC, after=1, lead=1.1),
            P("+45 71 62 24 00 &nbsp;|&nbsp; Aalborg, Denmark", size=9, after=0),
            P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=9, after=0),
            P("Portfolio: arunabha22.github.io/arunabha-majumder", size=9, after=4),
            HRFlowable(width="100%", thickness=1.1, color=ACC2, spaceBefore=2, spaceAfter=10),
            P("mkind, Munich", size=10, after=3),
            P("<b>Robotics Systems Engineer</b>", size=10.5, color=BLACK, after=10),
            P("Hi mkind team,", size=10.5, color=BLACK, after=6)]
    body = [P(t, size=10.1, color=BLACK, after=7, lead=1.32) for t in PARAS] + [
        P("Best,", size=10.1, color=BLACK, after=2), P(NAME, size=10.1, color=BLACK)]
    def deco(c, d):
        c.saveState(); c.setFillColor(ACC); c.rect(0, H - 0.35 * cm, W, 0.35 * cm, stroke=0, fill=1)
        c.rect(0, 0, W, 0.2 * cm, stroke=0, fill=1); c.restoreState()
    SimpleDocTemplate(path, pagesize=A4, leftMargin=2.1 * cm, rightMargin=2.1 * cm, topMargin=1.8 * cm,
                      bottomMargin=1.5 * cm, title="AM mkind Cover Letter", author=NAME, creator=NAME,
                      producer=NAME, subject="", keywords="").build(head + body, onFirstPage=deco)
    return path

if __name__ == "__main__":
    print(cv()); print(letter())

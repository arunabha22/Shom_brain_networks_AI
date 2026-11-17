import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import NAME, tidy
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, SimpleDocTemplate, Frame, PageTemplate, Paragraph, Spacer,
                                FrameBreak, HRFlowable)

# Laerdal Medical (Stavanger, Norway) - Cybernetics & Robotics Engineer (req3238), patient simulators.
# Contact Fredrik Saevland. Deadline 7 Dec. Not claimed: pumps, hydraulics, flow measurement, C/C++, embedded firmware,
# source control, industry experience, FEA. Norway relocation not confirmed yet, so no relocation line. Letter has no gap paragraph (his rule). Letter has no gap paragraph (his rule). His rules (2026-11): title "Research Assistant, Aalborg University";
# NO clutch story; outer PID loop has integral anti-windup + error nonlinearisation; 6 participants = 5-bar robot;
# German = "willing to learn" only, no gap talk; GATE + Study Abroad heading + portfolio; letter ends with
# innovative ideas. Files named "AM Mechatronics Robotics ...".
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
PHOTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/assets/photo_blue_bg_crop.jpg"
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
    path = OUT + "AM Laerdal CV.pdf"
    head = [P(NAME, size=23, bold=True, color=ACC, after=2, lead=1.1),
            P("Mechatronics and Robotics Engineer", size=11.5, bold=True, color=BLACK, after=4),
            P("Aalborg, Denmark &nbsp;|&nbsp; +45 71 62 24 00", size=8.8, after=0.5),
            P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=8.8, after=0.5),
            P("Portfolio: arunabha22.github.io/arunabha-majumder", size=8.8, after=0.5),
            P("LinkedIn: linkedin.com/in/arunabha-majumder-681264107", size=8.8, after=0)]
    left = sec("Education", first=True) + \
        item("PhD, Mechatronics and Robotics", "Aalborg University | 2023 - present<br/>Thesis expected March") + \
        item("MTech, Mechatronics", "AcSIR - CSIR-CMERI, India<br/>2020 - 2022") + \
        item("BTech, Mechanical Engineering", "Siddaganga Institute of Technology, India<br/>2015 - 2019") + \
        item("Senior Diploma in Fine Arts (Painting)", "Bangiya Sangeet Parishad<br/>2008, First Division with "
             "Distinction", 0) + \
        sec("Study Abroad") + item("National University of Singapore", "Sep - Nov 2025 (during my PhD)",
                                   0) + \
        sec("Skills") + [
            P("<b>CAD and prototyping:</b> SolidWorks (CSWA), drawings, 3D printing, machining (Bachelor's), Fusion 360 "
              "(basic, last used 2019)", size=8.7,
              after=2.5),
            P("<b>Mechanics:</b> mechanisms, torque and force calculations, Jacobian-based force estimation, "
              "springs, GA optimisation", size=8.7, after=2.5),
            P("<b>Mechatronics:</b> pneumatic muscles, pressure valves, motors, encoders, force/torque sensors, "
              "Arduino, PID control (anti-windup), MATLAB/Simulink, LabVIEW, Python (basic), Qualisys", size=8.7,
              after=2.5),
            P("<b>Art and design:</b> hand sketching, painting, Adobe Illustrator, Photoshop, Procreate", size=8.7,
              after=0),
        ] + sec("Achievements") + [
            P("Best Paper Award, IFToMM ISRM 2026", size=8.7, after=2), P("Best Major Project Award, 2019", size=8.7,
                                                                           after=2),
            P("TATA Technologies Prayatna grant", size=8.7, after=2), P("GATE qualified", size=8.7, after=0),
        ] + sec("Languages") + [P("English (C1), Bengali (native), Hindi", size=8.7,
                                  after=0)] + sec("References") + [
            P("<b>Prof. Shaoping Bai</b><br/>Aalborg University, sbh@mp.aau.dk", size=8.3, after=2.5),
            P("<b>Assoc. Prof. Lars Rosgaard Jensen</b><br/>Head of Section and Head of Labs, AAU", size=8.3,
              after=2.5),
            P("<b>Assoc. Prof. Anderson de Souza Castelo Oliveira</b><br/>Materials and Production, AAU", size=8.3,
              after=0)]

    right = sec("Profile", first=True) + [
        P("I am a mechatronics and robotics engineer who builds physical systems that move like, or with, the human "
          "body. I have worked with pneumatic muscles and pressure valves, motors, encoders and force sensors, and I "
          "like the whole loop: an idea on paper, SolidWorks CAD, a 3D printed prototype, wiring and control, then "
          "testing it on a real setup and with real people. I work closely with electronics and software engineers.",
          size=9.3, after=1, lead=1.32)
    ] + sec("Experience") + role("Research Assistant", "Aalborg University, Denmark", "2023 - Present") + [
        bl("Designed a hybrid shoulder exoskeleton: a variable stiffness mechanism (spring pretensioned by a worm "
           "gear) working in parallel with a 6 Nm motor; together they give the torque needed to lift the arm. It uses "
           "over 25% less motor energy (Best Paper Award, IFToMM ISRM 2026)."),
        bl("Optimised the mechanism with a genetic algorithm (diameter, spring stiffness, pretension force), made the "
           "CAD and drawings in SolidWorks, 3D printed the first parts and had the final parts manufactured."),
        bl("Integrated the motor, encoder and force/torque sensors and measured its stiffness on a physical setup."),
        bl("Designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms (VSM); "
           "estimated its stiffness with less than 10% error and quantified human arm impedance. Force estimation "
           "used the variable stiffness actuators and the robot's Jacobian."),
        bl("Arm impedance study with the 5-bar robot (6 participants): Qualisys cameras recorded arm position data, and I "
           "implemented an Arduino-based trigger to sync the robot's motion with the recording."),
        bl("Taught university courses and supervised Bachelor's students (2023 - 2025)."),
        Spacer(0, 4),
    ] + role("MTech Researcher, Soft Exosuit", "CSIR-CMERI, India", "2020 - 2022") + [
        bl("Fabricated and assembled silicone pneumatic artificial muscles for a soft exosuit (team of 4) and "
           "worked with pressure valves on the lab's test setup. Designed the outer PID loop, "
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
                          title="AM Laerdal CV", author=NAME, creator=NAME, producer=NAME, subject="", keywords="")
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
    "I'd like to apply for the Cybernetics & Robotics Engineer role. A patient simulator that breathes, blinks and "
    "moves is really a humanoid robot, and its mix of mechanics, pneumatics, sensors and control is very close to "
    "what I have worked on for the last six years. Saving lives through better "
    "training is also a goal I can easily get behind.",
    "In my Master's at CSIR-CMERI I worked in a team of 4 electronics and mechanical engineers on a soft exosuit. I "
    "fabricated silicone pneumatic artificial muscles, worked with pressure valves on the lab's test setup and "
    "designed the outer PID loop, with integral anti-windup and error nonlinearisation, of a neural network-based "
    "gain-scheduled controller in MATLAB/Simulink. I implemented it in LabVIEW to drive the muscle with 0.3 to 0.78% "
    "position error (IEEE CONECCT 2022). Air-driven actuators are not always easy to control, and I learned a lot "
    "from getting that one to behave.",
    "As a research assistant at Aalborg University I designed a hybrid shoulder exoskeleton, where a spring "
    "mechanism and a 6 Nm motor share the load. I optimised it with a genetic algorithm, made the CAD in "
    "SolidWorks, 3D printed the first parts, had the final ones manufactured and integrated the motor, encoder and "
    "force/torque sensors. It uses over 25% less motor energy and won the Best Paper Award at ISRM 2026. I also "
    "designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms (VSM), estimated "
    "its stiffness with less than 10% error and quantified human arm impedance. In the exoskeleton study I recorded "
    "EMG from 12 participants with Qualisys, so I know how much testing with real people teaches you.",
    "I also hold a Senior Diploma in Fine Arts (Painting) and do graphic design in Illustrator, Photoshop and "
    "Procreate. I sketch every idea by hand first, and I like making technical drawings and visuals that help a "
    "team understand a design quickly. I have also taught university courses and supervised Bachelor's students, "
    "which made me better at clear documentation.",
    "I would love to bring new and innovative ideas to your simulators and keep learning from a team that works "
    "across mechanics, firmware and electronics. My portfolio, with videos and results from my work, is at "
    "arunabha22.github.io/arunabha-majumder. Thank you for reading.",
]

def letter():
    path = OUT + "AM Laerdal Cover Letter.pdf"
    head = [P(NAME, size=18, bold=True, color=ACC, after=1, lead=1.1),
            P("+45 71 62 24 00 &nbsp;|&nbsp; Aalborg, Denmark", size=9, after=0),
            P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=9, after=0),
            P("Portfolio: arunabha22.github.io/arunabha-majumder", size=9, after=4),
            HRFlowable(width="100%", thickness=1.1, color=ACC2, spaceBefore=2, spaceAfter=10),
            P("Laerdal Medical, Stavanger (req3238)", size=10, after=3),
            P("<b>Cybernetics &amp; Robotics Engineer</b>", size=10.5, color=BLACK, after=10),
            P("Dear Fredrik,", size=10.5, color=BLACK, after=6)]
    body = [P(t, size=10.1, color=BLACK, after=7, lead=1.32) for t in PARAS] + [
        P("Best,", size=10.1, color=BLACK, after=2), P(NAME, size=10.1, color=BLACK)]
    def deco(c, d):
        c.saveState(); c.setFillColor(ACC); c.rect(0, H - 0.35 * cm, W, 0.35 * cm, stroke=0, fill=1)
        c.rect(0, 0, W, 0.2 * cm, stroke=0, fill=1); c.restoreState()
    SimpleDocTemplate(path, pagesize=A4, leftMargin=2.1 * cm, rightMargin=2.1 * cm, topMargin=1.8 * cm,
                      bottomMargin=1.5 * cm, title="AM Laerdal Cover Letter", author=NAME, creator=NAME,
                      producer=NAME, subject="", keywords="").build(head + body, onFirstPage=deco)
    return path

def shrink(p):
    import pymupdf
    d = pymupdf.open(p); d.rewrite_images(dpi_threshold=200, dpi_target=150, quality=80)
    d.save(p + ".tmp", garbage=4, deflate=True, clean=True); d.close(); os.replace(p + ".tmp", p)

if __name__ == "__main__":
    for p in (cv(), letter()):
        shrink(p); print(p, os.path.getsize(p))

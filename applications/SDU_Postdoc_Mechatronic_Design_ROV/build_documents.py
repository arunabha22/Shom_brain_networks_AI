import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import NAME, tidy
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (NextPageTemplate, BaseDocTemplate, SimpleDocTemplate, Frame, PageTemplate, Paragraph, Spacer,
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
    path = OUT + "AM SDU CV.pdf"
    head = [P(NAME, size=23, bold=True, color=ACC, after=2, lead=1.1),
            P("Mechatronics and Robotics Engineer", size=11.5, bold=True, color=BLACK, after=4),
            P("Aalborg, Denmark &nbsp;|&nbsp; +45 71 62 24 00", size=8.8, after=0.5),
            P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=8.8, after=0.5),
            P("Portfolio: <link href='https://arunabha22.github.io/arunabha-majumder/' color='#2E75B6'>"
              "<u>arunabha22.github.io/arunabha-majumder</u></link>", size=8.8, after=0.5),
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
        ] + sec("Languages") + [P("English (C1), Bengali (native), Hindi, Danish (willing to learn)", size=8.7,
                                  after=0)]

    right = [NextPageTemplate("p2")] + sec("Profile", first=True) + [
        P("Mechatronics and robotics engineer who can design, build, integrate and test electromechanical systems: "
          "actuation mechanisms and transmissions, SolidWorks CAD, 3D printed and manufactured prototypes, sensor and "
          "actuator integration, data acquisition and experimental validation. I want to keep doing research that ends "
          "in working hardware, tested outside the lab.", size=9.3, after=1, lead=1.32)
    ] + sec("Core Engineering Competencies") + [
        bl("Mechanical and mechatronic design: actuation, transmissions (worm gear), springs, structural parts"),
        bl("CAD and engineering modelling: SolidWorks (CSWA), stiffness modelling, genetic algorithm optimisation"),
        bl("Integration of sensors, actuators and control hardware: motors, encoders, force/torque sensors, Arduino"),
        bl("Rapid prototyping: additive manufacturing, machining (Bachelor's), assembly, experimental development"),
        bl("Experimental testing, instrumentation and data acquisition: Qualisys, EMG, system characterisation"),
        bl("Programming and control: MATLAB/Simulink, LabVIEW, Python (basic)"),
    ] + sec("Experience") + role("Research Assistant", "Aalborg University, Denmark", "2023 - Present") + [
        bl("Designed a hybrid shoulder exoskeleton: a variable stiffness mechanism (spring pretensioned by a worm "
           "gear transmission) working in parallel with a 6 Nm motor; together they give the torque needed to lift "
           "the arm. It uses over 25% less motor energy (Best Paper Award, IFToMM ISRM 2026)."),
        bl("Optimised the mechanism with a genetic algorithm (diameter, spring stiffness, pretension force), made the "
           "CAD and drawings in SolidWorks, 3D printed the first parts for testing and had the final parts "
           "manufactured."),
        bl("Integrated the motor, encoder and force/torque sensors, characterised the stiffness on a physical test "
           "setup, and collected EMG data from 12 participants with the Qualisys system in the exoskeleton study."),
        bl("Designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms (VSM); "
           "estimated its stiffness with less than 10% error and quantified human arm impedance. Force estimation "
           "used the variable stiffness actuators and the robot's Jacobian."),
        bl("Arm impedance study with the 5-bar robot (6 participants): Qualisys cameras recorded arm position data, "
           "and I implemented an Arduino-based trigger to sync the robot's motion with the recording."),
        Spacer(0, 4),
    ] + role("MTech Researcher, Soft Exosuit", "CSIR-CMERI, India", "2020 - 2022") + [
        bl("Fabricated and assembled silicone pneumatic artificial muscles for a soft exosuit in a team of 4 "
           "electronics and mechanical engineers, and worked with pressure valves on the lab's test setup."),
        bl("Designed the outer PID loop, with integral anti-windup and error nonlinearisation, of a neural "
           "network-based gain-scheduled controller in MATLAB/Simulink and implemented it in LabVIEW to drive the "
           "pneumatic muscle (0.3 - 0.78% error, IEEE CONECCT 2022)."),
        bl("Collected the experimental data used to train the neural network for gain scheduling."),
        Spacer(0, 4),
    ] + role("Bachelor's Projects", "Siddaganga Institute of Technology, India", "2017 - 2019") + [
        bl("Designed and built an upper-limb rehabilitation exoskeleton and an exo glove for a paralysed arm, with "
           "servo motors and Arduino-based control: CAD, assembly and testing (TATA Technologies Prayatna "
           "grant; Best Major Project Award)."),
        bl("Built a Go-Kart (2017) and an Efficycle hybrid vehicle (2018) with student teams, and small hexapod "
           "robots (2017)."),
    ] + sec("Publications") + [
        bl("Hybrid actuated shoulder exoskeleton, IFToMM ISRM 2026 (Springer), Best Paper Award."),
        bl("Neural network-based control of a pneumatic artificial muscle, IEEE CONECCT 2022."),
    ] + sec("Awards and Grants") + [
        bl("Best Paper Award, IFToMM ISRM 2026, for the hybrid actuated shoulder exoskeleton."),
        bl("TATA Technologies Prayatna Innovation Fund grant (INR 100,000) for my Bachelor's exoskeleton project."),
        bl("Best Major Project Award, Department of Mechanical Engineering, Siddaganga Institute of Technology, 2019."),
        bl("GATE qualified (national engineering exam in India)."),
    ] + sec("Research Interests") + [
        bl("Actuation mechanisms and transmissions for robots that have to work reliably outside the lab."),
        bl("Design optimisation and stiffness modelling of mechanisms, checked against physical tests."),
        bl("Integrating sensors, actuators and data acquisition into compact, testable prototypes."),
    ] + sec("References") + [
        P("<b>Shaoping Bai, PhD, Professor</b>, Department of Materials and Production, Aalborg University. "
          "sbh@mp.aau.dk", size=9, after=3),
        P("<b>Lars Rosgaard Jensen, Associate Professor</b>, Head of Section (Physics, Mechanics and Materials), "
          "Head of Labs, Department of Materials and Production, Aalborg University", size=9, after=3),
        P("<b>Anderson de Souza Castelo Oliveira, Associate Professor</b>, Department of Materials and Production, "
          "Aalborg University", size=9, after=0),
    ]

    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=M,
                          title="AM SDU CV", author=NAME, creator=NAME, producer=NAME, subject="", keywords="")
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
    def deco2(c, d):
        c.saveState(); c.setFillColor(ACC); c.rect(0, H - 0.35 * cm, W, 0.35 * cm, stroke=0, fill=1)
        c.rect(0, 0, W, 0.2 * cm, stroke=0, fill=1); c.restoreState()
    f2 = [Frame(M, M, W - 2 * M, H - 2 * M - 0.3 * cm, id="p2main", leftPadding=0, rightPadding=0,
                topPadding=0, bottomPadding=0)]
    doc.addPageTemplates([PageTemplate(id="p", frames=frames, onPage=deco),
                          PageTemplate(id="p2", frames=f2, onPage=deco2)])
    doc.build(head + [FrameBreak()] + left + [FrameBreak()] + right)
    return path

TITLE = ("Mechatronics engineer with 6 years of research experience designing, building and testing actuated "
         "systems, from CAD to validated prototypes")
PARAS = [
    "I am a mechatronics and robotics engineer doing my PhD at Aalborg University, where I design, "
    "build and test actuated systems. I feel qualified for this postdoc because the work you describe is what I have "
    "done in my research. I designed a hybrid shoulder exoskeleton with a spring mechanism, a worm gear transmission "
    "and a 6 Nm motor, optimised it with a genetic algorithm, modelled it in SolidWorks, 3D printed and then "
    "manufactured the parts, integrated the motor, encoder and force/torque sensors and characterised its stiffness "
    "on a physical test setup. It uses over 25% less motor energy and won the Best Paper Award at ISRM 2026. I also "
    "designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms (VSM), estimated "
    "its stiffness with less than 10% error and quantified human arm impedance, with Qualisys data acquisition "
    "synced to the robot.",
    "What made me apply is the chance to take this way of working into a harder environment. Under water, every "
    "actuator, transmission and enclosure has to keep working under pressure and in the field, and I like problems "
    "where the hardware has to prove itself outside the lab. I have moved between fields before: in my Master's I "
    "fabricated silicone pneumatic muscles and designed the outer PID loop (with anti-windup and error "
    "nonlinearisation) of their controller, and in my PhD I "
    "moved to full mechanical design. The mix of design, modelling, prototyping and experiments at CIM in "
    "Sønderborg is the kind of place where I want to grow as a researcher. I also hold a Senior Diploma in Fine "
    "Arts and do graphic design in Illustrator, Photoshop and Procreate, which helps me sketch concepts and make "
    "clear figures for papers and posters.",
    "I would be excited to bring my mechatronic design experience, my hands-on way of building and testing "
    "prototypes, and new ideas to the ROV research team at CIM.",
    "I am in the final stage of my PhD. My research is done and my thesis is expected to be finished in March 2027, "
    "and I would be glad to agree on a start date that fits the project.",
    "Thank you for your time. I look forward to hearing from you.",
]

def letter():
    path = OUT + "AM SDU Cover Letter.pdf"
    head = [P(NAME, size=22, bold=True, color=ACC, after=3, lead=1.1),
            P(TITLE, size=11.5, bold=True, color=ACC2, after=4, lead=1.25),
            HRFlowable(width="100%", thickness=1.1, color=ACC2, spaceBefore=2, spaceAfter=12),
            P("<b>Application for Postdoc in Mechatronic Design for Remotely Operated Vehicles</b>", size=11.5, color=BLACK, after=8),
            P("Dear Hiring Committee,", size=10.5, color=BLACK, after=7)]
    body = [P(t, size=10.3, color=BLACK, after=8, lead=1.36) for t in PARAS] + [
        Spacer(0, 4), P("Best regards,", size=10.3, color=BLACK, after=2),
        P("<b>%s</b>" % NAME, size=10.5, color=BLACK, after=2),
        P("+45 71 62 24 00 &nbsp;|&nbsp; somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com &nbsp;|&nbsp; "
          "arunabha22.github.io/arunabha-majumder", size=8.6, after=0)]
    def deco(c, d):
        c.saveState(); c.setFillColor(ACC); c.rect(0, H - 0.35 * cm, W, 0.35 * cm, stroke=0, fill=1)
        c.rect(0, 0, W, 0.2 * cm, stroke=0, fill=1); c.restoreState()
    SimpleDocTemplate(path, pagesize=A4, leftMargin=2.1 * cm, rightMargin=2.1 * cm, topMargin=1.8 * cm,
                      bottomMargin=1.5 * cm, title="AM SDU Cover Letter", author=NAME, creator=NAME,
                      producer=NAME, subject="", keywords="").build(head + body, onFirstPage=deco)
    return path

def shrink(p):
    import pymupdf
    d = pymupdf.open(p); d.rewrite_images(dpi_threshold=200, dpi_target=150, quality=80)
    d.save(p + ".tmp", garbage=4, deflate=True, clean=True); d.close(); os.replace(p + ".tmp", p)

if __name__ == "__main__":
    for p in (cv(), letter()):
        shrink(p); print(p, os.path.getsize(p))

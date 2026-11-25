import os, sys, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)) + "/"
APPS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("t", os.path.join(APPS, "Sample_New_Format", "build_sample.py"))
t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
from reportlab.platypus import (BaseDocTemplate, SimpleDocTemplate, Frame, PageTemplate, FrameBreak, NextPageTemplate,
                                Spacer, HRFlowable)
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
P, sec, bl, role, item, NAME = t.P, t.sec, t.bl, t.role, t.item, t.NAME
ACC, ACC2, PANEL, BLACK, W, H, M, GAP, HEAD_H, LW, RW, PAD = (t.ACC, t.ACC2, t.PANEL, t.BLACK, t.W, t.H, t.M, t.GAP,
                                                             t.HEAD_H, t.LW, t.RW, t.PAD)
PHOTO = t.PHOTO

# MetoMotion NL (Ridder Group) - Mechanical R&D Engineer, Robotics & AGV (greenhouse harvesting robot), NL.
# Daily list 2026-11-25 #2 (62%); he marked it -> drafted with defaults: R&D -> 2 pages two-column, approved
# headline, no Dutch line, relocate to NL, letter to the named contact Boy de Nijs. No contact email -> no draft.

def cv():
    path = HERE + "AM Ridder CV.pdf"
    head = [P(NAME, size=23, bold=True, color=ACC, after=2, lead=1.1),
            P("Mechatronics and Robotics Engineer", size=11.5, bold=True, color=BLACK, after=4),
            P("Aalborg, Denmark &nbsp;|&nbsp; +45 71 62 24 00", size=8.8, after=0.5),
            P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=8.8, after=0.5),
            P("Portfolio: <link href='https://arunabha22.github.io/arunabha-majumder/' color='#2E75B6'>"
              "<u>arunabha22.github.io/arunabha-majumder</u></link>", size=8.8, after=0.5),
            P("LinkedIn: linkedin.com/in/arunabha-majumder-681264107", size=8.8, after=0)]

    left1 = sec("Education", first=True) + \
        item("PhD, Mechatronics and Robotics", "Aalborg University | 2023 - present<br/>Thesis expected March") + \
        item("MTech, Mechatronics", "AcSIR - CSIR-CMERI, India<br/>2020 - 2022") + \
        item("BTech, Mechanical Engineering", "Siddaganga Institute of Technology, India<br/>2015 - 2019") + \
        item("Senior Diploma in Fine Arts (Painting)", "Bangiya Sangeet Parishad<br/>2008, First Division with "
             "Distinction", 0) + \
        sec("Study Abroad") + item("National University of Singapore", "Sep - Nov 2025 (during my PhD)", 0) + \
        sec("Skills") + [
            P("<b>CAD and analysis:</b> SolidWorks (CSWA), drawings, BOMs, SolidWorks Simulation, GA optimisation, "
              "MATLAB/Simulink, Fusion 360 (basic, last used 2019)", size=8.7, after=2.5),
            P("<b>Prototyping and manufacturing:</b> 3D printing (Ultimaker Cura, Bambu Lab), CNC-machined aluminium "
              "parts, silicone casting, lathe and welding (Bachelor's)", size=8.7, after=2.5),
            P("<b>Motors, actuators and sensing:</b> motors, Maxon ESCON drivers (basic), encoders, FSRs, load cells, "
              "torque sensors, pneumatic muscles, pressure valves, Qualisys", size=8.7, after=2.5),
            P("<b>Software:</b> LabVIEW, Arduino (C/C++, basic), Python (basic), PID control", size=8.7, after=2.5),
            P("<b>Art and design:</b> hand sketching, painting, Adobe Illustrator, Photoshop, Procreate", size=8.7,
              after=0)]

    right1 = sec("Profile", first=True) + [
        P("Mechanical engineer who designs robot mechanisms and assemblies in SolidWorks, builds the prototypes and "
          "tests them until they work. My robots had to carry real loads and work with real people, not only in the "
          "lab. I want to build robots that take over hard physical work.", size=9.3, after=1, lead=1.32)
    ] + sec("Core Engineering Competencies") + [
        bl("Mechanical design of robotic subsystems: mechanisms, joints, actuators and assemblies"),
        bl("SolidWorks (CSWA) 3D CAD, detailed drawings and BOMs"),
        bl("Prototyping and testing: 3D printed parts, CNC-machined aluminium parts, physical tests"),
        bl("Engineering analysis to guide design: GA optimisation, models matched to test data"),
        bl("Manufacturing know-how: machining (via supplier), 3D printing, sheet metal (go-kart)"),
    ] + sec("Experience") + role("Research Assistant", "Aalborg University, Denmark", "2023 - Present") + [
        bl("Designed a hybrid shoulder exoskeleton: a variable stiffness mechanism (spring pretensioned by a worm gear) "
           "working in parallel with a 6 Nm motor. It uses over 25% less motor energy (Best Paper Award, IFToMM ISRM "
           "2026)."),
        bl("Added FSRs, a Forsentek load cell and torque sensors, connected them with the motor, Maxon ESCON driver "
           "and encoder through Arduino, built a test setup for the sensors, compared options before choosing parts, "
           "and measured the stiffness on a physical test setup."),
        bl("Optimised the mechanism with a genetic algorithm, made the CAD, drawings and BOMs in SolidWorks, 3D "
           "printed the first parts, and worked with an external manufacturer to have the final aluminium parts CNC "
           "machined."),
        bl("Designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms (VSM); "
           "estimated its stiffness with less than 10% error and quantified human arm impedance."),
        bl("Collected EMG data from 12 participants in the exoskeleton study, and position data from 6 participants "
           "in the arm impedance study with the 5-bar robot (Qualisys, Arduino-based trigger for sync)."),
        Spacer(0, 3),
    ] + role("MTech Researcher, Soft Exosuit", "CSIR-CMERI, India", "2020 - 2022") + [
        bl("Fabricated silicone pneumatic artificial muscles by casting in a team of 4 electronics and mechanical "
           "engineers, and worked with pressure valves, reading and controlling pressure through LabVIEW."),
        bl("Designed the outer PID loop, with integral anti-windup and error nonlinearisation, of a neural "
           "network-based gain-scheduled controller in MATLAB/Simulink and implemented it in LabVIEW to drive the "
           "pneumatic muscle (0.3 - 0.78% error, IEEE CONECCT 2022)."),
    ]

    left2 = sec("Achievements", first=True) + [
        P("Best Paper Award, IFToMM ISRM 2026", size=8.7, after=2), P("Best Major Project Award, 2019", size=8.7,
                                                                       after=2),
        P("TATA Technologies Prayatna grant (INR 100,000)", size=8.7, after=2), P("GATE qualified", size=8.7,
                                                                                   after=0),
    ] + sec("Languages") + [
        P("English (C1, IELTS 7.0)", size=8.7, after=1), P("Bengali (native)", size=8.7, after=1),
        P("Hindi", size=8.7, after=0),
    ] + sec("References") + [
        P("<b>Shaoping Bai, PhD</b><br/>Professor, Department of Materials and Production, Aalborg University<br/>"
          "sbh@mp.aau.dk", size=8.3, after=4),
        P("<b>Lars Rosgaard Jensen</b><br/>Associate Professor, Head of Section (Physics, Mechanics and Materials), "
          "Head of Labs, Department of Materials and Production, Aalborg University", size=8.3, after=4),
        P("<b>Anderson de Souza Castelo Oliveira</b><br/>Associate Professor, Department of Materials and "
          "Production, Aalborg University", size=8.3, after=0),
    ]

    right2 = sec("Experience (continued)", first=True) + \
        role("Bachelor's Capstone and Side Projects", "Siddaganga Institute of Technology, India", "2017 - 2019") + [
        bl("Capstone: designed and built an upper-limb rehabilitation exoskeleton and an exo glove for a paralysed arm, "
           "with servo motors and Arduino-based control. I did the CAD, wiring and connectors, assembly and "
           "testing (TATA Technologies Prayatna grant; Best Major Project Award)."),
        bl("Side projects during my BTech: designed the Efficycle hybrid trike (2018) and built a Go-Kart (2017) with "
           "student teams, with sheet metal parts and a frame strength check in SolidWorks Simulation; small hexapod "
           "robots (2017)."),
    ] + sec("Publications") + [
        bl("Hybrid actuated shoulder exoskeleton, IFToMM ISRM 2026 (Springer), Best Paper Award."),
        bl("Neural network-based control of a pneumatic artificial muscle, IEEE CONECCT 2022."),
    ] + sec("Awards and Grants") + [
        bl("Best Paper Award, IFToMM ISRM 2026, for the hybrid actuated shoulder exoskeleton."),
        bl("TATA Technologies Prayatna Innovation Fund grant for my Bachelor's exoskeleton project."),
        bl("Best Major Project Award, Department of Mechanical Engineering, 2019."),
    ] + sec("What I Bring to an R&amp;D Team") + [
        bl("Hands-on from first sketch to a tested prototype, and comfortable switching between technologies."),
        bl("New ideas I would like to explore: origami-based and Bowden cable exoskeletons, and cable and pressure "
           "mechanisms for the hand."),
        bl("Clear sketches and visuals, helped by my fine arts and graphic design background."),
    ]

    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=M,
                          title="Arunabha Majumder CV", author=NAME, creator=NAME, producer=NAME, subject="",
                          keywords="")
    top = H - M - HEAD_H
    body_h = top - M - 0.35 * cm
    body2_h = H - 2 * M - 0.35 * cm
    f1 = [Frame(M, top, W - 2 * M - 2.8 * cm, HEAD_H, id="head", leftPadding=0, rightPadding=0, topPadding=0,
                bottomPadding=0),
          Frame(M, M, LW, body_h, id="left", leftPadding=PAD, rightPadding=PAD, topPadding=PAD, bottomPadding=PAD),
          Frame(M + LW + GAP, M, RW, body_h, id="right", leftPadding=0, rightPadding=0, topPadding=PAD,
                bottomPadding=0)]
    f2 = [Frame(M, M, LW, body2_h, id="left2", leftPadding=PAD, rightPadding=PAD, topPadding=PAD, bottomPadding=PAD),
          Frame(M + LW + GAP, M, RW, body2_h, id="right2", leftPadding=0, rightPadding=0, topPadding=PAD,
                bottomPadding=0)]

    def band(c):
        c.setFillColor(ACC); c.rect(0, H - 0.35 * cm, W, 0.35 * cm, stroke=0, fill=1)
        c.rect(0, 0, W, 0.2 * cm, stroke=0, fill=1)

    def deco1(c, d):
        c.saveState(); band(c)
        c.setFillColor(PANEL); c.rect(M, M, LW, body_h, stroke=0, fill=1)
        c.setFillColor(ACC2); c.rect(M, M + body_h - 0.08 * cm, LW, 0.08 * cm, stroke=0, fill=1)
        c.drawImage(PHOTO, W - M - 2.5 * cm, H - M - 3.15 * cm, width=2.5 * cm, height=3.15 * cm,
                    preserveAspectRatio=True, mask="auto")
        c.setStrokeColor(ACC); c.setLineWidth(1.4); c.line(M, top - 0.12 * cm, W - M, top - 0.12 * cm)
        c.restoreState()

    def deco2(c, d):
        c.saveState(); band(c)
        c.setFillColor(PANEL); c.rect(M, M, LW, body2_h, stroke=0, fill=1)
        c.setFillColor(ACC2); c.rect(M, M + body2_h - 0.08 * cm, LW, 0.08 * cm, stroke=0, fill=1)
        c.setFont("Helvetica", 8); c.setFillColor(ACC)
        c.drawRightString(W - M, M - 0.55 * cm + 0.35 * cm, "Arunabha Majumder  |  page 2")
        c.restoreState()

    doc.addPageTemplates([PageTemplate(id="p1", frames=f1, onPage=deco1),
                          PageTemplate(id="p2", frames=f2, onPage=deco2)])
    doc.build(head + [FrameBreak()] + left1 + [FrameBreak()] + right1 + [NextPageTemplate("p2"), FrameBreak()]
              + left2 + [FrameBreak()] + right2)
    return path

TITLE = ("Mechanical engineer with 6 years of experience designing robot mechanisms and testing them in the real "
         "world")
PARAS = [
    "I am a mechanical engineer doing my PhD at Aalborg University, and I feel qualified for this role because "
    "designing robot mechanisms in SolidWorks, building them and testing them is what my research has been about. I "
    "designed a hybrid shoulder exoskeleton where a spring mechanism, pretensioned by a worm gear, works in parallel "
    "with a motor. I optimised it with a genetic algorithm, 3D printed the first parts and worked with an external "
    "manufacturer to have the final aluminium parts CNC machined, then tested it on a physical setup and with people. "
    "It uses over 25% less motor energy and won the Best Paper Award at ISRM 2026. I also designed and modelled a novel "
    "5-bar planar parallel robot with variable stiffness mechanisms (VSM), estimated its stiffness with less than 10% "
    "error, and quantified human arm impedance.",
    "What made me apply is the Ridder Harvesting Robot. A robot that harvests in a greenhouse has to deal with real "
    "plants, humidity and long working days, so every mechanism has to hold up outside a clean lab. I like that kind "
    "of problem, because the design only counts when it works in the field. My own robots also had to work with real "
    "people and real loads, and I learned a lot from fixing what broke in tests. I also hold a Senior Diploma in Fine "
    "Arts and do graphic design in Illustrator, Photoshop and Procreate, which helps me sketch ideas and explain them "
    "clearly to the team.",
    "I would be excited to bring my mechanism design experience, my habit of testing early, and new ideas to your "
    "Labour and Robotics team.",
    "I am in the final stage of my PhD. My research is done, and I am available to move into an industrial "
    "engineering role while I finish my thesis. I am happy to relocate to the Netherlands.",
    "Thank you for your time. I look forward to hearing from you.",
]

def letter():
    path = HERE + "AM Ridder Cover Letter.pdf"
    head = [P(NAME, size=22, bold=True, color=ACC, after=3, lead=1.1),
            P(TITLE, size=11.5, bold=True, color=ACC2, after=4, lead=1.25),
            HRFlowable(width="100%", thickness=1.1, color=ACC2, spaceBefore=2, spaceAfter=12),
            P("<b>Application for Mechanical R&amp;D Engineer, Robotics and AGV</b>", size=11.5, color=BLACK, after=8),
            P("Dear Boy de Nijs,", size=10.5, color=BLACK, after=7)]
    body = [P(x, size=10.3, color=BLACK, after=8, lead=1.36) for x in PARAS] + [
        Spacer(0, 4), P("Best regards,", size=10.3, color=BLACK, after=2),
        P("<b>%s</b>" % NAME, size=10.5, color=BLACK, after=2),
        P("+45 71 62 24 00 &nbsp;|&nbsp; somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com &nbsp;|&nbsp; "
          "arunabha22.github.io/arunabha-majumder", size=8.6, after=0)]
    def deco(c, d):
        c.saveState(); c.setFillColor(ACC); c.rect(0, H - 0.35 * cm, W, 0.35 * cm, stroke=0, fill=1)
        c.rect(0, 0, W, 0.2 * cm, stroke=0, fill=1); c.restoreState()
    SimpleDocTemplate(path, pagesize=A4, leftMargin=2.1 * cm, rightMargin=2.1 * cm, topMargin=1.8 * cm,
                      bottomMargin=1.5 * cm, title="Arunabha Majumder Cover Letter", author=NAME, creator=NAME,
                      producer=NAME, subject="", keywords="").build(head + body, onFirstPage=deco)
    return path

if __name__ == "__main__":
    for p in (cv(), letter()):
        t.shrink(p) if hasattr(t, "shrink") else None
        print(p)

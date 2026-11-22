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

# Danfoss Drives (Graasten, DK) - Development Engineer, Req 52689, mid-senior (5+ yrs industry, NX, Danish valued).
# His answers 2026-11-22: Danish willing to learn; SolidWorks + Fusion 360 only; sheet metal (go-kart, sometimes);
# silicone casting of pneumatic muscles in the group (not his design); exo aluminium parts CNC machined by a manufacturer
# he talked with + 3D printing; BTech 3D printing supplier; BTech wiring/connectors; basic ESCON motor driver wiring.
# 2 pages, two-column on BOTH pages (he disliked the plain page 2). Letter to the named hiring manager.

def cv():
    path = HERE + "AM Danfoss CV.pdf"
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
            P("<b>CAD:</b> SolidWorks (CSWA), detailed drawings, BOMs, SolidWorks Simulation, Fusion 360 (basic, last "
              "used 2019)", size=8.7, after=2.5),
            P("<b>Manufacturing:</b> CNC-machined aluminium parts (via manufacturer), 3D printing (Ultimaker Cura, "
              "Bambu Lab), sheet metal (go-kart), silicone casting, lathe, welding", size=8.7, after=2.5),
            P("<b>Electromechanics:</b> motors, Maxon ESCON drivers (basic), encoders, force/torque sensors, wiring and "
              "connectors, soldering, Arduino (C/C++, basic)", size=8.7, after=2.5),
            P("<b>Analysis and control:</b> MATLAB/Simulink, LabVIEW, Python (basic), GA optimisation, PID control",
              size=8.7, after=2.5),
            P("<b>Art and design:</b> hand sketching, painting, Adobe Illustrator, Photoshop, Procreate", size=8.7,
              after=0)]

    right1 = sec("Profile", first=True) + [
        P("Mechanical engineer who can design, develop and test electromechanical products, turn customer and "
          "production needs into practical designs that balance quality, cost and manufacturability, and validate "
          "and document the results with manufacturers and suppliers. I want my designs to save energy and work "
          "reliably once they leave the factory.", size=9.3, after=1, lead=1.32)
    ] + sec("Core Engineering Competencies") + [
        bl("Design, development and testing of electromechanical products: motors, drivers, encoders, sensors"),
        bl("Design for manufacture: CNC-machined aluminium parts and 3D printed parts, drawings and BOMs"),
        bl("Working with manufacturers and suppliers to get parts made, checked and changed"),
        bl("Validation and documentation of designs, test results and engineering decisions"),
        bl("Materials and processes: aluminium, 3D printing, sheet metal, silicone casting"),
        bl("Energy efficiency: hybrid actuation design that uses over 25% less motor energy"),
    ] + sec("Experience") + role("Research Assistant", "Aalborg University, Denmark", "2023 - Present") + [
        bl("Designed a hybrid shoulder exoskeleton: a variable stiffness mechanism (spring pretensioned by a worm gear) "
           "working in parallel with a 6 Nm motor. It uses over 25% less motor energy (Best Paper Award, IFToMM ISRM "
           "2026)."),
        bl("Optimised the mechanism with a genetic algorithm, made the CAD, drawings and BOMs in SolidWorks, 3D "
           "printed the first parts and worked with an external manufacturer to have the final aluminium parts CNC "
           "machined."),
        bl("Integrated the motor with a Maxon ESCON driver, the encoder and force/torque sensors, measured the "
           "stiffness on a physical test setup and documented the test results."),
        bl("Designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms (VSM); "
           "estimated its stiffness with less than 10% error and quantified human arm impedance."),
        bl("Collected EMG data from 12 participants in the exoskeleton study, and position data from 6 participants "
           "in the arm impedance study with the 5-bar robot (Qualisys, Arduino-based trigger for sync)."),
        Spacer(0, 3),
    ] + role("MTech Researcher, Soft Exosuit", "CSIR-CMERI, India", "2020 - 2022") + [
        bl("Fabricated silicone pneumatic artificial muscles by casting in a team of 4 electronics and mechanical "
           "engineers, and worked with pressure valves on the lab's test setup."),
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
        P("Hindi", size=8.7, after=1), P("Danish (willing to learn)", size=8.7, after=0),
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
           "with servo motors and Arduino-based control. I did the CAD, wiring and connectors, lathe machining, "
           "welding, assembly and testing, and worked with an external 3D printing business for parts (TATA "
           "Technologies Prayatna grant; Best Major Project Award)."),
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
    ] + sec("What I Bring to a Product Team") + [
        bl("Hands-on from first sketch to manufactured part, and comfortable on the workshop floor."),
        bl("Clear drawings and visuals, helped by my fine arts and graphic design background."),
        bl("Used to explaining design decisions to people from different fields and changing designs based on tests."),
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

TITLE = ("Mechanical engineer with 6 years of experience designing, building and testing electromechanical products, "
         "from CAD to manufactured parts")
PARAS = [
    "I am a mechanical engineer doing my PhD at Aalborg University, and I feel qualified for this role because "
    "designing, testing and documenting electromechanical products together with the people who make them is what "
    "I have done in my research. I designed a hybrid shoulder exoskeleton in SolidWorks, made the drawings and BOMs, "
    "3D printed the first parts and then worked with an external manufacturer to have the final aluminium parts CNC "
    "machined. I integrated the motor with its ESCON driver, the encoder and force/torque sensors, tested the design "
    "on a physical setup and documented the results. It uses over 25% less motor energy and won the Best Paper Award "
    "at ISRM 2026. I have also worked with sheet metal parts on a go-kart, cast silicone pneumatic muscles in a lab "
    "team, and done the wiring and connectors on my Bachelor's exoskeleton.",
    "What made me apply is that your team owns products that are already running in production, and that the work "
    "is about energy efficiency and electrification. Saving energy was a key goal in my own design work, and I would "
    "like to see my engineering decisions make a difference in products that leave a factory every day. I enjoy the "
    "practical side of solving problems with production, suppliers and colleagues from other fields. I also hold a "
    "Senior Diploma in Fine Arts and do graphic design in Illustrator, Photoshop and Procreate, which helps me make "
    "clear drawings and explain design changes simply.",
    "I would be excited to bring my mechanical design experience, my hands-on way of building and testing, and new "
    "ideas to your Product Engineering team in Gråsten.",
    "I am in the final stage of my PhD. My research is done, I already live in Denmark, and I am available to move "
    "into an industrial engineering role while I finish my thesis.",
    "Thank you for your time. I look forward to hearing from you.",
]

def letter():
    path = HERE + "AM Danfoss Cover Letter.pdf"
    head = [P(NAME, size=22, bold=True, color=ACC, after=3, lead=1.1),
            P(TITLE, size=11.5, bold=True, color=ACC2, after=4, lead=1.25),
            HRFlowable(width="100%", thickness=1.1, color=ACC2, spaceBefore=2, spaceAfter=12),
            P("<b>Application for Development Engineer (Req ID 52689)</b>", size=11.5, color=BLACK, after=8),
            P("Dear Naveen Deepak Selvarajan,", size=10.5, color=BLACK, after=7)]
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
    print(cv()); print(letter())

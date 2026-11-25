import os, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)) + "/"
APPS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); return m
t = load("t", os.path.join(APPS, "Sample_New_Format", "build_sample.py"))
one = load("one", os.path.join(APPS, "JBT_Marel_Mechanical_Design_Engineer_Helsingborg", "build_documents.py"))
from reportlab.platypus import (BaseDocTemplate, SimpleDocTemplate, Frame, PageTemplate, FrameBreak, Spacer,
                                HRFlowable, Table, TableStyle, Image)
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
P, sec, bl, role, item, NAME = t.P, t.sec, t.bl, t.role, t.item, t.NAME
ACC, ACC2, PANEL, BLACK, W, H, M, GAP, HEAD_H, LW, RW, PAD = (t.ACC, t.ACC2, t.PANEL, t.BLACK, t.W, t.H, t.M, t.GAP,
                                                             t.HEAD_H, t.LW, t.RW, t.PAD)

# GENERAL CV, 1 page (NEW_CV_1page.pdf), rebuilt 2026-11-25 with the latest facts and rules. Job title shown as
# "PhD Fellow, R&D Engineering" (official AAU title PhD Fellow; R&D only as work descriptor). Headline from his
# portfolio. No company name, no Danish/German/Dutch line (general). Confirm with him what happened after 28 Feb 2026.
HEADLINE = "Mechanical and Robotics R&amp;D Engineer"
PROFILE = ("Mechanical and mechatronics engineer who designs, builds and tests robotic mechanisms, actuators and "
           "exoskeletons: from hand sketches and SolidWorks CAD to 3D printed prototypes, motor and sensor integration "
           "and tests with real people. I want to build robots and devices that work well with people.")
COMP = ["Mechanism and actuator design: springs, worm gears, motors, variable stiffness",
        "3D CAD, drawings and BOMs in SolidWorks (CSWA); 3D printed and CNC-machined parts",
        "Motor and sensor integration: ESCON drivers, encoders, FSRs, load cells, torque sensors",
        "Design optimisation and testing: genetic algorithm, models matched to test data",
        "Testing with people: EMG and motion capture (Qualisys)"]
PHD = ["Designed a hybrid shoulder exoskeleton in SolidWorks: a spring mechanism pretensioned by a worm gear, "
       "working in parallel with a 6 Nm motor. It uses over 25% less motor energy (Best Paper Award, IFToMM ISRM 2026).",
       "Made the 3D models, assemblies, detailed drawings and BOM, 3D printed the first parts, and worked with an "
       "external manufacturer who CNC machined and assembled the final aluminium parts.",
       "Optimised the mechanism with a genetic algorithm and designed an adjustable arm cuff that slides and locks "
       "to fit different arm sizes.",
       "Integrated the motor, encoder, FSRs, load cell and torque sensors; tested the stiffness on a physical test "
       "setup, matched my model to the test data and improved the design.",
       "Designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms (VSM); estimated "
       "its stiffness with less than 10% error and quantified human arm impedance."]
MTECH = ("Fabricated silicone pneumatic muscles in a team of 4. Designed the "
         "outer PID loop, with integral anti-windup and error nonlinearisation, of a neural network-based "
         "gain-scheduled controller in MATLAB/Simulink and implemented it in LabVIEW to drive the pneumatic muscle "
         "(0.3 - 0.78% error, IEEE CONECCT 2022).")
BTECH = ("Capstone: designed and built an upper-limb rehabilitation exoskeleton and exo glove for a paralysed arm with "
         "servo motors and Arduino control (CAD, wiring and connectors, assembly, testing; TATA Prayatna grant, Best "
         "Major Project Award). Side projects: Efficycle trike design and a Go-Kart with sheet metal parts and a frame "
         "strength analysis in SolidWorks Simulation.")

def cv_two():
    path = HERE + "NEW_CV_1page.pdf"
    head = [P(NAME, size=23, bold=True, color=ACC, after=2, lead=1.1),
            P(HEADLINE, size=11.5, bold=True, color=BLACK, after=4),
            P("Aalborg, Denmark (open to relocation) &nbsp;|&nbsp; +45 71 62 24 00", size=8.8, after=0.5),
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
        sec("Study Abroad") + item("National University of Singapore", "Sep - Nov 2025 (during my PhD)", 0) + \
        sec("Skills") + [
            P("<b>CAD:</b> SolidWorks (CSWA), drawings, BOMs, SolidWorks Simulation, Fusion 360 (basic, last used "
              "2019)", size=8.5, after=2),
            P("<b>Manufacturing:</b> CNC-machined aluminium parts, 3D printing (Ultimaker Cura, Bambu Lab), sheet "
              "metal, silicone casting, lathe, welding", size=8.5, after=2),
            P("<b>Mechatronics:</b> motors, encoders, FSRs, load cells, torque sensors, Arduino (C/C++, basic), "
              "MATLAB/Simulink, LabVIEW", size=8.5, after=2),
            P("<b>Art and design:</b> hand sketching, painting, Adobe Illustrator, Photoshop, Procreate", size=8.5,
              after=0)] + \
        sec("Achievements") + [P("Best Paper Award, IFToMM ISRM 2026<br/>Best Major Project Award, 2019<br/>"
                                 "TATA Technologies Prayatna grant<br/>GATE qualified", size=8.5, after=0)] + \
        sec("Languages") + [P("English (C1, IELTS 7.0), Bengali (native), Hindi", size=8.5, after=0)] + \
        sec("References") + [
            P("<b>Prof. Shaoping Bai</b><br/>Aalborg University, sbh@mp.aau.dk", size=8.2, after=2),
            P("<b>Assoc. Prof. Lars Rosgaard Jensen</b><br/>Head of Section and Head of Labs, AAU", size=8.2,
              after=2),
            P("<b>Assoc. Prof. Anderson de Souza Castelo Oliveira</b><br/>Materials and Production, AAU", size=8.2,
              after=0)]
    right = sec("Profile", first=True) + [P(PROFILE, size=9.1, after=1, lead=1.3)] + \
        sec("Core Engineering Competencies") + [bl(x) for x in COMP] + \
        sec("Experience") + role("PhD Fellow, R&amp;D Engineering", "Aalborg University, Denmark", "2023 - 2026") + \
        [bl(x) for x in PHD] + \
        role("MTech Researcher, Soft Exosuit", "CSIR-CMERI, India", "2020 - 2022") + [bl(MTECH)] + \
        role("Bachelor's Projects", "Siddaganga Institute of Technology, India", "2017 - 2019") + [bl(BTECH)] + \
        sec("Publications") + [bl("Hybrid actuated shoulder exoskeleton, IFToMM ISRM 2026 (Best Paper); neural "
                                  "network-based control of a pneumatic muscle, IEEE CONECCT 2022.")]
    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=M,
                          title="Arunabha Majumder CV", author=NAME, creator=NAME, producer=NAME, subject="",
                          keywords="")
    top = H - M - HEAD_H; body_h = top - M - 0.35 * cm
    frames = [Frame(M, top, W - 2 * M - 2.8 * cm, HEAD_H, id="head", leftPadding=0, rightPadding=0, topPadding=0,
                    bottomPadding=0),
              Frame(M, M, LW, body_h, id="left", leftPadding=PAD, rightPadding=PAD, topPadding=PAD, bottomPadding=PAD),
              Frame(M + LW + GAP, M, RW, body_h, id="right", leftPadding=0, rightPadding=0, topPadding=PAD,
                    bottomPadding=0)]
    def deco(c, d):
        c.saveState()
        c.setFillColor(ACC); c.rect(0, H - 0.35 * cm, W, 0.35 * cm, stroke=0, fill=1)
        c.setFillColor(PANEL); c.rect(M, M, LW, body_h, stroke=0, fill=1)
        c.setFillColor(ACC2); c.rect(M, M + body_h - 0.08 * cm, LW, 0.08 * cm, stroke=0, fill=1)
        c.drawImage(t.PHOTO, W - M - 2.5 * cm, H - M - 3.15 * cm, width=2.5 * cm, height=3.15 * cm,
                    preserveAspectRatio=True, mask="auto")
        c.setStrokeColor(ACC); c.setLineWidth(1.4); c.line(M, top - 0.12 * cm, W - M, top - 0.12 * cm)
        c.setFillColor(ACC); c.rect(0, 0, W, 0.2 * cm, stroke=0, fill=1)
        c.restoreState()
    doc.addPageTemplates([PageTemplate(id="p", frames=frames, onPage=deco)])
    doc.build(head + [FrameBreak()] + left + [FrameBreak()] + right)
    return path

def cv_one():
    path = HERE + "AM ASSA ABLOY CV single column.pdf"
    s, b, r, ln, Pp = one.sec, one.bl, one.role, one.line, one.P
    left = [Pp(NAME, size=21, bold=True, color=ACC, after=2, lead=1.1),
            Pp(HEADLINE, size=11, bold=True, color=BLACK, after=3),
            Pp("Aalborg, Denmark (open to relocation) &nbsp;|&nbsp; +45 71 62 24 00", size=8.7, after=0.5),
            Pp("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=8.7, after=0.5),
            Pp("Portfolio: <link href='https://arunabha22.github.io/arunabha-majumder/' color='#2E75B6'>"
               "<u>arunabha22.github.io/arunabha-majumder</u></link>", size=8.7, after=0.5),
            Pp("LinkedIn: linkedin.com/in/arunabha-majumder-681264107", size=8.7, after=0)]
    head = Table([[left, Image(t.PHOTO, width=2.2 * cm, height=2.75 * cm)]],
                 colWidths=[W - 2 * 1.3 * cm - 2.4 * cm, 2.4 * cm])
    head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("ALIGN", (1, 0), (1, 0), "RIGHT"),
                              ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                              ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    body = [head, HRFlowable(width="100%", thickness=1.3, color=ACC, spaceBefore=4, spaceAfter=4)]
    body += s("Profile", first=True) + [Pp(PROFILE, size=8.8, after=1, lead=1.22)]
    body += s("Core Engineering Competencies") + [b(x) for x in COMP]
    body += s("Experience") + r("Research Assistant", "Aalborg University, Denmark", "2023 - Present") + \
        [b(x) for x in PHD] + r("MTech Researcher, Soft Exosuit", "CSIR-CMERI, India", "2020 - 2022") + [b(MTECH)] + \
        r("Bachelor's Projects", "Siddaganga Institute of Technology, India", "2017 - 2019") + [b(BTECH)]
    body += s("Education") + [
        ln("<b>PhD, Mechatronics and Robotics</b>, Aalborg University, Denmark | 2023 - Present (thesis expected March)"),
        ln("<b>MTech, Mechatronics</b>, AcSIR - CSIR-CMERI, India | 2020 - 2022"),
        ln("<b>BTech, Mechanical Engineering</b>, Siddaganga Institute of Technology, India | 2015 - 2019"),
        ln("<b>Senior Diploma in Fine Arts (Painting)</b>, Bangiya Sangeet Parishad | 2008, First Division with "
           "Distinction")]
    body += s("Study Abroad") + [ln("National University of Singapore, independent research | 2025 (Sep - Nov)")]
    body += s("Skills") + [
        ln("<b>CAD:</b> SolidWorks (CSWA), detailed drawings, BOMs, SolidWorks Simulation, Fusion 360 (basic, last "
           "used 2019)"),
        ln("<b>Manufacturing:</b> CNC-machined aluminium parts, 3D printing (Ultimaker Cura, Bambu Lab), sheet "
           "metal, silicone casting, lathe, welding"),
        ln("<b>Mechatronics:</b> motors, encoders, FSRs, load cells, torque sensors, Arduino (C/C++, basic), "
           "MATLAB/Simulink, LabVIEW"),
        ln("<b>Art and design:</b> hand sketching, painting, Adobe Illustrator, Photoshop, Procreate")]
    body += s("Achievements and Publications") + [
        ln("Best Paper Award, IFToMM ISRM 2026 (hybrid actuated shoulder exoskeleton) | IEEE CONECCT 2022 "
           "(neural network-based control of a pneumatic artificial muscle)"),
        ln("Best Major Project Award, 2019 | TATA Technologies Prayatna grant (INR 100,000) | GATE qualified")]
    body += s("Languages") + [ln("English (C1, IELTS 7.0) | Bengali (native) | Hindi")]
    body += s("References") + [
        ln("Shaoping Bai, PhD, Professor, Dept. of Materials and Production, Aalborg University, sbh@mp.aau.dk"),
        ln("Lars Rosgaard Jensen, Associate Professor, Head of Section and Head of Labs, Dept. of Materials and "
           "Production, Aalborg University"),
        ln("Anderson de Souza Castelo Oliveira, Associate Professor, Dept. of Materials and Production, Aalborg "
           "University", after=0)]
    SimpleDocTemplate(path, pagesize=A4, leftMargin=1.3 * cm, rightMargin=1.3 * cm, topMargin=0.9 * cm,
                      bottomMargin=0.8 * cm, title="Arunabha Majumder CV", author=NAME, creator=NAME, producer=NAME,
                      subject="", keywords="").build(body)
    return path

TITLE = ("Mechanical engineer with 6 years of experience designing mechanisms and taking them from 3D model to "
         "tested prototype")
PARAS = [
    "I am a mechanical engineer doing my PhD at Aalborg University, and I feel qualified for this role because "
    "designing mechanisms, making the 3D models and drawings, and then building and testing the prototype is what I "
    "have done in my research. I designed a hybrid shoulder exoskeleton in SolidWorks where a spring mechanism, "
    "pretensioned by a worm gear, works in parallel with a motor. I optimised it with a genetic algorithm, made the "
    "drawings and BOM, 3D printed the first parts and worked with an external manufacturer who CNC machined the "
    "final aluminium parts. Then I tested it on a physical setup, compared the results with my model and improved "
    "the design. It uses over 25% less motor energy and won the Best Paper Award at ISRM 2026.",
    "What made me apply is that a lock is a small mechanism that has to work every single time, for many years. I "
    "like that kind of precise mechanical problem, where the small details decide the quality. I also like that "
    "the role covers the whole path from a new idea to prototype, testing and production, working with "
    "manufacturing, quality and test colleagues along the way. I also hold a Senior Diploma in Fine Arts and do "
    "graphic design in Illustrator, Photoshop and Procreate, which helps me sketch ideas and make clear drawings.",
    "I would be excited to bring my mechanism design experience, my habit of testing and improving, and new ideas to "
    "your R&amp;D team in Rychnov.",
    "I am in the final stage of my PhD. My research is done, and I am available to move into an industrial "
    "engineering role while I finish my thesis. I am happy to relocate to Rychnov.",
    "Thank you for your time. I look forward to hearing from you.",
]

def letter():
    path = HERE + "AM ASSA ABLOY Cover Letter.pdf"
    head = [P(NAME, size=22, bold=True, color=ACC, after=3, lead=1.1),
            P(TITLE, size=11.5, bold=True, color=ACC2, after=4, lead=1.25),
            HRFlowable(width="100%", thickness=1.1, color=ACC2, spaceBefore=2, spaceAfter=12),
            P("<b>Application for Mechanical Design Engineer, Locking Products</b>", size=11.5, color=BLACK, after=8),
            P("Dear Hiring Team,", size=10.5, color=BLACK, after=7)]
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
    for p in (cv_two(),):
        t.shrink(p); print(p, os.path.getsize(p) // 1024, "KB")

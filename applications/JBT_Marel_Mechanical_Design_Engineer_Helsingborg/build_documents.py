import os, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)) + "/"
APPS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("t", os.path.join(APPS, "Sample_New_Format", "build_sample.py"))
t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
from reportlab.platypus import SimpleDocTemplate, Spacer, HRFlowable, Table, TableStyle, Image
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
P, NAME, ACC, ACC2, BLACK, W, H = t.P, t.NAME, t.ACC, t.ACC2, t.BLACK, t.W, t.H
from reportlab.platypus import Paragraph
from doc_helpers import tidy

# JBT Marel (Helsingborg, SE) - Mechanical Design Engineer, Req 22204 (Workday portal). Industry role: 2+ yrs
# industrial machinery, Creo/Windchill strongly preferred, Swedish an advantage -> scored 42.
# His answers 2026-11-24: SINGLE-COLUMN CV (Workday ATS), willing to relocate to Helsingborg.
# Not claimed: Creo, Windchill, industrial/food machinery, automation, customer projects, leading design.
# No Swedish line (not confirmed). Headline kept (no OK to change). 1 page. Supplier contact in ONE line only.

def sec(x, first=False):
    return [Spacer(0, 0 if first else 3), P(x.upper(), size=9.4, bold=True, color=ACC, after=0),
            HRFlowable(width="100%", thickness=1, color=ACC2, spaceBefore=1, spaceAfter=2)]
def bl(x): return Paragraph(tidy("&bull;&nbsp;" + x), t.st(size=8.6, left=9, first=-9, after=1.2, lead=1.18))
def role(title, org, dates):
    return [P("<b>%s</b>, %s &nbsp;|&nbsp; <i>%s</i>" % (title, org, dates), size=9.2, color=BLACK, after=1.5)]
def line(x, after=1): return P(x, size=8.6, after=after, lead=1.18)

def cv():
    path = HERE + "AM JBT Marel CV.pdf"
    left = [P(NAME, size=21, bold=True, color=ACC, after=2, lead=1.1),
            P("Mechatronics and Robotics Engineer", size=11, bold=True, color=BLACK, after=3),
            P("Aalborg, Denmark (willing to relocate) &nbsp;|&nbsp; +45 71 62 24 00", size=8.7, after=0.5),
            P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=8.7, after=0.5),
            P("Portfolio: <link href='https://arunabha22.github.io/arunabha-majumder/' color='#2E75B6'>"
              "<u>arunabha22.github.io/arunabha-majumder</u></link>", size=8.7, after=0.5),
            P("LinkedIn: linkedin.com/in/arunabha-majumder-681264107", size=8.7, after=0)]
    head = Table([[left, Image(t.PHOTO, width=2.2 * cm, height=2.75 * cm)]], colWidths=[W - 2 * 1.3 * cm - 2.4 * cm, 2.4 * cm])
    head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("ALIGN", (1, 0), (1, 0), "RIGHT"),
                              ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                              ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    body = [head, HRFlowable(width="100%", thickness=1.3, color=ACC, spaceBefore=4, spaceAfter=4)]
    body += sec("Profile", first=True) + [P(
        "Mechanical engineer who designs in 3D CAD, makes the drawings and BOMs to get parts built, and tests the "
        "result on real hardware. I take ownership of a design from first sketch to tested prototype, troubleshoot "
        "what fails and improve it. I want to see my designs become working machines on the shop floor.",
        size=8.8, after=1, lead=1.22)]
    body += sec("Core Engineering Competencies") + [
        bl("Mechanical design in 3D CAD (SolidWorks, CSWA): parts, assemblies, detailed drawings and BOMs"),
        bl("Design for production: CNC-machined aluminium parts, 3D printed parts, sheet metal parts (go-kart)"),
        bl("Testing and troubleshooting: physical tests, matching models to test data, product improvements"),
        bl("Structured, analytical design: torque and stiffness calculations, genetic algorithm optimisation"),
        bl("Hands-on: assembly, 3D printing, lathe and welding (Bachelor's), wiring and soldering (basic)")]
    body += sec("Experience") + role("Research Assistant", "Aalborg University, Denmark", "2023 - Present") + [
        bl("Designed a hybrid shoulder exoskeleton in SolidWorks: a variable stiffness mechanism (spring pretensioned "
           "by a worm gear) working in parallel with a 6 Nm motor. It uses over 25% less motor energy (Best Paper "
           "Award, IFToMM ISRM 2026)."),
        bl("Made the detailed drawings and BOM, 3D printed the first parts, and worked with an external manufacturer "
           "who CNC machined and assembled the final aluminium parts."),
        bl("Optimised the mechanism with a genetic algorithm (spring stiffness, pretension force, mechanism diameter) "
           "and designed an adjustable arm cuff that slides and locks to fit different arm sizes."),
        bl("Integrated the motor, Maxon ESCON driver, encoder, FSRs, load cell and torque sensors; tested the stiffness "
           "on a physical test setup, matched my model to the test data and improved the design."),
        bl("Designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms (VSM); "
           "estimated its stiffness with less than 10% error and quantified human arm impedance."),
        ] + role("MTech Researcher, Soft Exosuit", "CSIR-CMERI, India", "2020 - 2022") + [
        bl("Fabricated silicone pneumatic artificial muscles by casting in a team of 4, and worked with pressure valves."),
        bl("Designed the outer PID loop, with integral anti-windup and error nonlinearisation, of a neural "
           "network-based gain-scheduled controller in MATLAB/Simulink and implemented it in LabVIEW to drive the "
           "pneumatic muscle (0.3 - 0.78% error, IEEE CONECCT 2022)."),
        ] + role("Bachelor's Capstone and Side Projects", "Siddaganga Institute of Technology, India",
                             "2017 - 2019") + [
        bl("Capstone: designed and built an upper-limb rehabilitation exoskeleton and an exo glove for a paralysed arm "
           "with servo motors and Arduino control; CAD, wiring and connectors, assembly and testing (TATA "
           "Technologies Prayatna grant; Best Major Project Award)."),
        bl("Side projects during my BTech: designed the Efficycle hybrid trike (2018) and built a Go-Kart (2017) with "
           "student teams, with sheet metal parts and a frame strength analysis in SolidWorks Simulation.")]
    body += sec("Education") + [
        line("<b>PhD, Mechatronics and Robotics</b>, Aalborg University, Denmark | 2023 - Present (thesis expected March)"),
        line("<b>MTech, Mechatronics</b>, AcSIR - CSIR-CMERI, India | 2020 - 2022"),
        line("<b>BTech, Mechanical Engineering</b>, Siddaganga Institute of Technology, India | 2015 - 2019"),
        line("<b>Senior Diploma in Fine Arts (Painting)</b>, Bangiya Sangeet Parishad | 2008, First Division with "
             "Distinction")]
    body += sec("Study Abroad") + [line("National University of Singapore, independent research | 2025 (Sep - Nov)")]
    body += sec("Skills") + [
        line("<b>CAD:</b> SolidWorks (CSWA), detailed drawings, BOMs, SolidWorks Simulation, Fusion 360 (basic, last "
             "used 2019)"),
        line("<b>Manufacturing:</b> CNC-machined aluminium parts, 3D printing (Ultimaker Cura, Bambu Lab), sheet "
             "metal, silicone casting, lathe, welding"),
        line("<b>Electromechanics and analysis:</b> motors, drivers, encoders, sensors, Arduino (C/C++, basic), "
             "MATLAB/Simulink, LabVIEW, Python (basic)"),
        line("<b>Art and design:</b> hand sketching, painting, Adobe Illustrator, Photoshop, Procreate")]
    body += sec("Achievements and Publications") + [
        line("Best Paper Award, IFToMM ISRM 2026 (hybrid actuated shoulder exoskeleton) | IEEE CONECCT 2022 "
             "(neural network-based control of a pneumatic artificial muscle)"),
        line("Best Major Project Award, 2019 | TATA Technologies Prayatna grant (INR 100,000) | GATE qualified")]
    body += sec("Languages") + [line("English (C1, IELTS 7.0) | Bengali (native) | Hindi")]
    body += sec("References") + [
        line("Shaoping Bai, PhD, Professor, Dept. of Materials and Production, Aalborg University, sbh@mp.aau.dk"),
        line("Lars Rosgaard Jensen, Associate Professor, Head of Section and Head of Labs, Dept. of Materials and "
             "Production, Aalborg University"),
        line("Anderson de Souza Castelo Oliveira, Associate Professor, Dept. of Materials and Production, Aalborg "
             "University", after=0)]
    SimpleDocTemplate(path, pagesize=A4, leftMargin=1.3 * cm, rightMargin=1.3 * cm, topMargin=0.9 * cm,
                      bottomMargin=0.8 * cm, title="Arunabha Majumder CV", author=NAME, creator=NAME, producer=NAME,
                      subject="", keywords="").build(body)
    return path

TITLE = ("Mechanical engineer with 6 years of experience designing parts in 3D CAD and seeing them built and "
         "tested")
PARAS = [
    "I am a mechanical engineer doing my PhD at Aalborg University, and I feel qualified for this role because my "
    "designs have always ended up as real hardware that I then tested myself. I designed a hybrid shoulder "
    "exoskeleton in SolidWorks, made the drawings and BOM, 3D printed the first parts and worked with an external "
    "manufacturer who CNC machined the final aluminium parts. Then I tested it on a physical setup, compared the "
    "results with my model and improved what did not work. It uses over 25% less motor energy and won the Best Paper "
    "Award at ISRM 2026. In my Bachelor's I worked with sheet metal parts on a go-kart, checked the frame with a "
    "strength analysis in SolidWorks Simulation, and used a lathe and did some welding.",
    "What made me apply is that in Helsingborg design, assembly and testing happen under one roof. I like being "
    "close to the people who build and test what I draw, because that is where most problems show up and get "
    "solved. Food processing machines also have to run every day for the customer, and I would like my work to "
    "make that kind of difference. I also hold a Senior Diploma in Fine Arts and do graphic design in Illustrator, "
    "Photoshop and Procreate, which helps me sketch ideas and make clear drawings for colleagues.",
    "I would be excited to bring my hands-on design experience, my habit of testing and improving, and new ideas to "
    "your engineering team in Helsingborg.",
    "I am in the final stage of my PhD. My research is done, and I am available to move into an industrial "
    "engineering role while I finish my thesis. I am happy to relocate to Helsingborg.",
    "Thank you for your time. I look forward to hearing from you.",
]

def letter():
    path = HERE + "AM JBT Marel Cover Letter.pdf"
    head = [P(NAME, size=22, bold=True, color=ACC, after=3, lead=1.1),
            P(TITLE, size=11.5, bold=True, color=ACC2, after=4, lead=1.25),
            HRFlowable(width="100%", thickness=1.1, color=ACC2, spaceBefore=2, spaceAfter=12),
            P("<b>Application for Mechanical Design Engineer (Req 22204)</b>", size=11.5, color=BLACK, after=8),
            P("Dear Hiring Team,", size=10.5, color=BLACK, after=7)]
    body = [P(x, size=10.3, color=BLACK, after=8, lead=1.36) for x in PARAS] + [
        Spacer(0, 4), P("Best regards,", size=10.3, color=BLACK, after=2),
        P("<b>%s</b>" % NAME, size=10.5, color=BLACK, after=2),
        P("+45 71 62 24 00 &nbsp;|&nbsp; somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com &nbsp;|&nbsp; "
          "arunabha22.github.io/arunabha-majumder", size=8.6, after=0)]
    SimpleDocTemplate(path, pagesize=A4, leftMargin=2.1 * cm, rightMargin=2.1 * cm, topMargin=1.8 * cm,
                      bottomMargin=1.5 * cm, title="Arunabha Majumder Cover Letter", author=NAME, creator=NAME,
                      producer=NAME, subject="", keywords="").build(head + body)
    return path

if __name__ == "__main__":
    for p in (cv(), letter()):
        t.shrink(p); print(p, os.path.getsize(p) // 1024, "KB")

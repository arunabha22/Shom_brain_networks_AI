import os, sys, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)) + "/"
APPS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, APPS)
spec = importlib.util.spec_from_file_location("base", os.path.join(APPS, "Adaptyv_Mechanical_Mechatronics_Engineer", "build_v2.py"))
b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
P, sec, bl, role, NAME = b.P, b.sec, b.bl, b.role, b.NAME

# REVEL (Prague) - Industrial Design CAD Engineer. Ad wants substantial professional Fusion 360: he knows it a little, last used 2019 (basic only)
# (never claim it; stated honestly in the letter). 3+ years professional: PhD research + teaching, no industry.
# Not Denmark, so no Danish. Fine arts + graphic design always kept (his rule).

def cv():
    head = [P(NAME, size=20, bold=True, color=b.BLUE, after=1, lead=1.1),
            P("Mechanical Design Engineer", size=11, bold=True, after=3),
            P("Aalborg, Denmark &nbsp;|&nbsp; +45 71 62 24 00", size=9, after=0),
            P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=9, after=0),
            P("Portfolio: arunabha22.github.io/arunabha-majumder", size=9, after=0),
            P("LinkedIn: linkedin.com/in/arunabha-majumder-681264107", size=9, after=4)]
    body = sec("Profile") + [P(
        "Mechanical design engineer with a fine arts background. I turn concepts and sketches into parametric CAD "
        "parts and assemblies (SolidWorks), 3D print them, assemble them and fit test them on real hardware. Most of "
        "my work is wearable robotics: I designed a shoulder exoskeleton that sits on the human body, with a motor, "
        "encoder and sensors built into it.")]
    body += sec("Experience") + role("PhD Researcher, Robotics (project VIEXO)", "Aalborg University, Denmark",
                                    "2023 - Present") + [
        bl("Designed a hybrid shoulder exoskeleton from concept to prototype: a variable stiffness mechanism with a "
           "worm gear for pretension, working in parallel with a 6 Nm motor. It uses more than 25% less motor energy "
           "(Best Paper Award, IFToMM ISRM 2026)."),
        bl("Built the full parametric CAD assembly and technical drawings in SolidWorks: parts, mounting points, "
           "fasteners and clearances around the moving joints; optimised the mechanism with a genetic algorithm."),
        bl("3D printed parts for fit and function testing, refined them over several iterations, then had the final "
           "parts manufactured."),
        bl("Integrated the motor, encoder and torque/force sensors into the structure; "
           "measured the stiffness on a physical test setup."),
        bl("Design for manufacture and assembly: replaced a clutch part that kept breaking and was hard to make with "
           "a simple bolt-locking clutch (8 locking angles) that was easy to make, fit and replace."),
        bl("Designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms (VSM); "
           "estimated its stiffness with less than 10% error and quantified human arm impedance."),
        bl("Taught university courses and supervised Bachelor's students (2023 - 2025)."),
    ] + role("MTech Researcher, Soft Exosuit (Pneumatic Muscles)", "CSIR-CMERI, India", "2020 - 2022") + [
        bl("Fabricated and assembled pneumatic artificial muscles for a soft exosuit; designed the outer PID loop of a "
           "neural network-based controller in MATLAB/Simulink and implemented it in LabVIEW (IEEE CONECCT 2022)."),
    ] + role("Bachelor's Capstone and Student Teams", "Siddaganga Institute of Technology, India", "2017 - 2019") + [
        bl("Designed and built an arm exoskeleton and exo glove: CAD, machining, assembly and testing (TATA "
           "Technologies Prayatna Innovation Fund grant; Best Major Project Award)."),
        bl("Built a Go-Kart (2017) and an Efficycle hybrid vehicle (2018) with student teams."),
    ]
    body += sec("Skills") + [
        P("<b>CAD:</b> SolidWorks (CSWA): parametric parts and assemblies, technical drawings, tolerances, "
          "fasteners, clearances, organised assembly files; Fusion 360 (basic, last used 2019)"),
        P("<b>Prototyping:</b> 3D printing (Bambu Lab, Ultimaker Cura), design for 3D printing, fit testing, "
          "machining and hands-on assembly, DFM and DFA"),
        P("<b>Integration:</b> motors, encoders, torque/force sensors, Arduino, MATLAB/Simulink"),
        P("<b>Art and graphic design:</b> hand sketching of concepts, painting, technical illustration and visuals "
          "for papers, posters and demos; Adobe Illustrator, Photoshop, Procreate"),
    ]
    body += sec("Education") + [
        P("<b>PhD, Mechatronics and Robotics</b>, Aalborg University, Denmark | 2023 - present (research complete)"),
        P("<b>MTech, Mechatronics</b>, AcSIR - CSIR-CMERI, India | 2020 - 2022"),
        P("<b>BTech, Mechanical Engineering</b>, Siddaganga Institute of Technology, India | 2015 - 2019"),
        P("<b>Senior Diploma in Fine Arts (Painting)</b>, Bangiya Sangeet Parishad | 2008, First Division with "
          "Distinction"),
    ]
    body += sec("Languages and References") + [
        P("English (C1), Bengali (native), Hindi (spoken)"),
        P("<b>References:</b> Prof. Shaoping Bai (sbh@mp.aau.dk); Assoc. Prof. Lars Rosgaard Jensen; Assoc. Prof. "
          "Anderson de Souza Castelo Oliveira; all Department of Materials and Production, Aalborg University"),
    ]
    path = HERE + "Arunabha_Majumder_REVEL_CV.pdf"
    def deco(c, d):
        c.drawImage(b.PHOTO, b.W - b.M - 2.3 * cm, b.H - b.M - 2.9 * cm, width=2.3 * cm, height=2.9 * cm,
                    preserveAspectRatio=True, mask="auto")
    SimpleDocTemplate(path, pagesize=A4, leftMargin=b.M, rightMargin=b.M, topMargin=b.M, bottomMargin=1.2 * cm,
                      title="Arunabha Majumder CV", author=NAME, creator=NAME, producer=NAME,
                      subject="", keywords="").build(head + body, onFirstPage=deco)
    return path

def letter():
    head = [P(NAME, size=18, bold=True, color=b.BLUE, after=1, lead=1.1),
            P("+45 71 62 24 00 &nbsp;|&nbsp; Aalborg, Denmark", size=9, after=0),
            P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=9, after=0),
            P("Portfolio: arunabha22.github.io/arunabha-majumder", size=9, after=10),
            P("REVEL, Design team, Prague", size=10, after=6),
            P("<b>Application: Industrial Design CAD Engineer</b>", size=10.5, after=8),
            P("Dear REVEL Design Team,", size=10.5, after=6)]
    paras = [
        "I am applying for the Industrial Design CAD Engineer role. I like work where the look of a product and the "
        "way it is built have to agree, and your Neural Gambit wearable is close to what I have spent my PhD on at "
        "Aalborg University: hardware that sits on a human body.",
        "My main project was a hybrid shoulder exoskeleton. I took it from sketches to a full parametric CAD assembly "
        "in SolidWorks: the mechanism, the mounting points, the fasteners and the clearances around the moving joints. "
        "I integrated a 6 Nm motor, an encoder and torque/force sensors into it. I 3D printed the parts, assembled them, checked the fit on the real prototype "
        "and refined the CAD before the final parts were manufactured. It uses more than 25% less "
        "motor energy and won the Best Paper Award at IFToMM ISRM 2026.",
        "One lesson stayed with me. My first clutch kept breaking and was hard to make in our workshop, so I replaced "
        "it with a simple bolt-locking clutch that still locks at 8 angles and is easy to fit and replace. Since then "
        "I think about assembly and maintenance from the first sketch.",
        "I also have a Senior Diploma in Fine Arts (Painting), and I do graphic design and illustration in Adobe "
        "Illustrator, Photoshop and Procreate. I sketch concepts by hand before I open CAD, which helps me talk with "
        "product designers and keep their design intent when I build the parts underneath the surfaces.",
        "To be honest about the gaps: my main parametric CAD is SolidWorks. I used Fusion 360 a little, last in 2019, "
        "and never professionally. My 3+ years are in research and teaching, not in a company. The way of working "
        "is the same, and I can get back up to speed in Fusion quickly. My portfolio has videos and results from my work. My research is finished, "
        "so I can start soon, and I am happy to move to Prague. Thank you for reading.",
    ]
    body = [P(t, size=10, after=6, lead=1.28) for t in paras] + [P("Kind regards,", size=10, after=2),
                                                                 P(NAME, size=10)]
    path = HERE + "Arunabha_Majumder_REVEL_Cover_Letter.pdf"
    SimpleDocTemplate(path, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=1.8 * cm,
                      bottomMargin=1.5 * cm, title="Arunabha Majumder Cover Letter", author=NAME, creator=NAME,
                      producer=NAME, subject="", keywords="").build(head + body)
    return path

if __name__ == "__main__":
    print(cv()); print(letter())

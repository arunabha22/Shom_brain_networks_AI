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

# NEURA Robotics - Senior Mechanical Engineer, MiPA (cognitive mobile robots). Ad asks 10+ years (big gap, stated
# honestly in the letter). Germany: no Danish. Not claimed: housings, sheet metal/casting/moulding production, PDM/PLM,
# parts lists in industry, Creo/NX, project management.

def cv():
    head = [P(NAME, size=20, bold=True, color=b.BLUE, after=1, lead=1.1),
            P("Mechanical Engineer, Robotics", size=11, bold=True, after=3),
            P("Aalborg, Denmark &nbsp;|&nbsp; +45 71 62 24 00", size=9, after=0),
            P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=9, after=0),
            P("Portfolio: arunabha22.github.io/arunabha-majumder", size=9, after=0),
            P("LinkedIn: linkedin.com/in/arunabha-majumder-681264107", size=9, after=4)]
    body = sec("Profile") + [P(
        "Mechanical engineer in robotics who designs mechanical systems, mechanisms and electromechanical subsystems "
        "for robots that work safely with people. I take products from concept and CAD (SolidWorks) to prototypes, "
        "integration, validation and testing, with stiffness testing, design optimisation and Design for "
        "Manufacturing (DFM) and Design for Assembly (DFA) in mind.")]
    body += sec("Experience") + role("PhD Researcher, Robotics (project VIEXO)", "Aalborg University, Denmark",
                                    "2023 - Present") + [
        bl("Designed a hybrid shoulder exoskeleton: a variable stiffness mechanism with a worm gear for pretension, "
           "working in parallel with a 6 Nm motor. It uses more than 25% less motor energy (Best Paper Award, "
           "IFToMM ISRM 2026)."),
        bl("Created CAD models and technical drawings in SolidWorks; optimised the mechanism with a genetic algorithm "
           "(diameter, spring stiffness, pretension force); 3D printed prototypes, then had parts manufactured."),
        bl("Integrated the motor, encoder and torque/force sensors into the structure and measured its stiffness on "
           "a physical test setup (validation and testing)."),
        bl("Designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms (VSM); "
           "estimated its stiffness with less than 10% error and quantified human arm impedance."),
        bl("DFM in practice: replaced a clutch part that kept breaking and was hard to make with a simple "
           "bolt-locking clutch (8 locking angles) that was easy to manufacture and reliable."),
        bl("Worked closely with control engineering and software colleagues (team of 3 on an Assist-as-Needed "
           "controller); implemented an Arduino-based trigger to sync a robot with Qualisys motion capture."),
        bl("Taught university courses and supervised Bachelor's students (2023 - 2025)."),
    ] + role("MTech Researcher, Soft Exosuit (Pneumatic Muscles)", "CSIR-CMERI, India", "2020 - 2022") + [
        bl("Fabricated and assembled pneumatic artificial muscles for a soft exosuit; designed the outer PID loop of a "
           "neural network-based controller in MATLAB/Simulink and implemented it in LabVIEW (0.3 - 0.78% error, "
           "IEEE CONECCT 2022)."),
    ] + role("Bachelor's Capstone and Student Teams", "Siddaganga Institute of Technology, India", "2017 - 2019") + [
        bl("Designed and built an arm exoskeleton and exo glove: CAD, machining, assembly and testing (TATA "
           "Technologies Prayatna Innovation Fund grant; Best Major Project Award)."),
        bl("Built a Go-Kart (2017) and an Efficycle hybrid vehicle (2018) with student teams."),
    ]
    body += sec("Skills") + [
        P("<b>Mechanical design:</b> mechanisms, machine elements (worm gears, springs, clutches), structural "
          "components, electromechanical subsystems, materials selection"),
        P("<b>CAD and documentation:</b> SolidWorks (CSWA), CAD models, technical drawings, tolerances, stiffness "
          "analysis in SolidWorks"),
        P("<b>Manufacturing:</b> DFM, DFA, 3D printing (Bambu Lab, Ultimaker Cura), machining and assembly"),
        P("<b>Mechatronics and testing:</b> motors, encoders, torque/force sensors, Arduino, MATLAB/Simulink, LabVIEW, "
          "Python (basic), Qualisys, prototype validation"),
        P("<b>Communication:</b> hand sketching and technical illustration (Senior Diploma in Fine Arts)"),
    ]
    body += sec("Education") + [
        P("<b>PhD, Mechatronics and Robotics</b>, Aalborg University, Denmark | 2023 - present (research complete)"),
        P("<b>MTech, Mechatronics</b>, AcSIR - CSIR-CMERI, India | 2020 - 2022"),
        P("<b>BTech, Mechanical Engineering</b>, Siddaganga Institute of Technology, India | 2015 - 2019"),
        P("<b>Senior Diploma in Fine Arts (Painting)</b>, Bangiya Sangeet Parishad | 2008, Distinction"),
    ]
    body += sec("Languages and References") + [
        P("English (C1), Bengali (native), Hindi (spoken)"),
        P("<b>References:</b> Prof. Shaoping Bai (sbh@mp.aau.dk); Assoc. Prof. Lars Rosgaard Jensen; Assoc. Prof. "
          "Anderson de Souza Castelo Oliveira; all Department of Materials and Production, Aalborg University"),
    ]
    path = HERE + "Arunabha_Majumder_NEURA_CV.pdf"
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
            P("NEURA Robotics, MiPA Robotics team", size=10, after=6),
            P("<b>Application: Senior Mechanical Engineer, MiPA</b>", size=10.5, after=8),
            P("Dear NEURA Robotics Hiring Team,", size=10.5, after=6)]
    paras = [
        "I am applying for the Senior Mechanical Engineer role in the MiPA Robotics team. Robots that work safely "
        "and close to people are what I have built in my PhD at Aalborg University, so MiPA is a team I would really "
        "like to join.",
        "My main project was a hybrid shoulder exoskeleton. I designed the mechanism myself: a variable stiffness "
        "mechanism, pretensioned by a worm gear, working in parallel with a 6 Nm motor. I optimised its diameter, "
        "spring stiffness and pretension with a genetic algorithm, made the CAD models and drawings in SolidWorks, "
        "3D printed prototypes and then had the parts manufactured. I integrated the motor, encoder and torque/force "
        "sensors and measured the stiffness on a physical test setup. It uses more than 25% less motor energy and "
        "won the Best Paper Award at IFToMM ISRM 2026. When a clutch part kept breaking and was hard to make, I "
        "replaced it with a simple bolt-locking clutch, a small lesson in Design for Manufacturing that stayed with me.",
        "I also designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms, "
        "estimated its stiffness with less than 10% error and quantified human arm impedance. Across these projects I "
        "worked closely with control engineering and software colleagues, which is how I like to work.",
        "I want to be honest: I do not have 10 years in industry, and I have not yet run series production, PDM/PLM "
        "systems or injection moulding projects. If this senior role is a step too far, I would be glad to be "
        "considered for a mechanical engineer position in the MiPA team. My research is finished, so I can start "
        "soon, and I am ready to move to Germany. Thank you for considering my application.",
    ]
    body = [P(t, size=10.2, after=7, lead=1.3) for t in paras] + [P("Kind regards,", size=10.2, after=2),
                                                                   P(NAME, size=10.2)]
    path = HERE + "Arunabha_Majumder_NEURA_Cover_Letter.pdf"
    SimpleDocTemplate(path, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=1.8 * cm,
                      bottomMargin=1.6 * cm, title="Arunabha Majumder Cover Letter", author=NAME, creator=NAME,
                      producer=NAME, subject="", keywords="").build(head + body)
    return path

if __name__ == "__main__":
    print(cv()); print(letter())

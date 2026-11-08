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

# REVEL (Prague) - Mechanical design of the Neural Gambit (NG) sleeve and clip-on hub (wearable). Not claimed:
# SLS, soft-goods sewing/textiles, material selection for flexible parts, medical/sports wearable products in industry.
# Fusion 360 basic (last used 2019). Not Denmark, so no Danish. Fine arts + graphic design always kept.

def cv():
    head = [P(NAME, size=20, bold=True, color=b.BLUE, after=1, lead=1.1),
            P("Wearable Mechanical Engineer", size=11, bold=True, after=3),
            P("Aalborg, Denmark &nbsp;|&nbsp; +45 71 62 24 00", size=9, after=0),
            P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=9, after=0),
            P("Portfolio: arunabha22.github.io/arunabha-majumder", size=9, after=0),
            P("LinkedIn: linkedin.com/in/arunabha-majumder-681264107", size=9, after=4)]
    body = sec("Profile") + [P(
        "Mechanical engineer who designs hardware worn on the human arm. Since 2018 I have worked on an arm "
        "exoskeleton and exo glove, pneumatic muscles for a soft exosuit and a shoulder exoskeleton. I take wearable "
        "parts from sketches and SolidWorks CAD to 3D printed prototypes, test them on real people and iterate.")]
    body += sec("Experience") + role("PhD Researcher, Robotics (project VIEXO)", "Aalborg University, Denmark",
                                    "2023 - Present") + [
        bl("Designed a hybrid shoulder exoskeleton worn on the arm and shoulder: a variable stiffness mechanism with a "
           "worm gear for pretension, working in parallel with a 6 Nm motor. It uses more than 25% less motor energy, "
           "which means longer battery life (Best Paper Award, IFToMM ISRM 2026)."),
        bl("Built the CAD assembly and drawings in SolidWorks, optimised the mechanism with a genetic algorithm, 3D "
           "printed parts for fit testing, refined them and then had the final parts manufactured."),
        bl("Integrated the motor, encoder and torque/force sensors; measured the stiffness on a physical test setup."),
        bl("Collected data from 12 participants for a biomechanics study, recording EMG with the Qualisys system."),
        bl("Design for manufacture: replaced a clutch that kept breaking and was hard to make with a simple "
           "bolt-locking clutch (8 locking angles) that was easy to make, fit and replace."),
        bl("Designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms (VSM); "
           "estimated its stiffness with less than 10% error and quantified human arm impedance (6 participants, "
           "Qualisys motion capture)."),
        bl("Taught university courses and supervised Bachelor's students (2023 - 2025)."),
    ] + role("MTech Researcher, Soft Exosuit (Pneumatic Muscles)", "CSIR-CMERI, India", "2020 - 2022") + [
        bl("Fabricated and assembled pneumatic artificial muscles for a soft exosuit; designed the outer PID loop of a "
           "neural network-based controller in MATLAB/Simulink and implemented it in LabVIEW (IEEE CONECCT 2022)."),
    ] + role("Bachelor's Capstone and Student Teams", "Siddaganga Institute of Technology, India", "2017 - 2019") + [
        bl("Designed and built an arm exoskeleton and an exo glove for a paralysed arm: CAD, machining, assembly and "
           "testing (TATA Technologies Prayatna Innovation Fund grant; Best Major Project Award)."),
        bl("Built a Go-Kart (2017) and an Efficycle hybrid vehicle (2018) with student teams."),
    ]
    body += sec("Skills") + [
        P("<b>CAD:</b> SolidWorks (CSWA): parametric parts and assemblies, technical drawings, tolerances, "
          "fasteners, clearances, organised assembly files; Fusion 360 (basic, last used 2019)"),
        P("<b>Wearables and prototyping:</b> arm exoskeletons, exo glove, soft exosuit (pneumatic muscles), testing "
          "with participants, 3D printing (Bambu Lab, Ultimaker Cura), hands-on assembly, DFM and DFA"),
        P("<b>Human testing:</b> Qualisys motion capture and EMG data collection, torque/force sensors"),
        P("<b>Integration:</b> motors, encoders, Arduino, MATLAB/Simulink, LabVIEW"),
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
    path = HERE + "Arunabha_Majumder_REVEL_NG_Sleeve_CV.pdf"
    def deco(c, d):
        c.drawImage(b.PHOTO, b.W - b.M - 2.3 * cm, b.H - b.M - 2.9 * cm, width=2.3 * cm, height=2.9 * cm,
                    preserveAspectRatio=True, mask="auto")
    SimpleDocTemplate(path, pagesize=A4, leftMargin=b.M, rightMargin=b.M, topMargin=b.M, bottomMargin=1.2 * cm,
                      title="Arunabha Majumder CV", author=NAME, creator=NAME, producer=NAME,
                      subject="", keywords="").build(head + body, onFirstPage=deco)
    return path

if __name__ == "__main__":
    print(cv())

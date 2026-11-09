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

# Clira Health (Paris, medtech startup) - Mechanical Engineer, Founding Team: blood collection device + disposable.
# Apply by email (hiring@clirahealth.com): why Clira + what you built. Not claimed: sealing, fluidics/microfluidics,
# medical device QMS (ISO 13485), injection moulding, supplier management, building test rigs (Master's rig was the
# lab's). No PhD video. France: relocation confirmed, no French but willing to learn. Fine arts + graphic design kept.

def cv():
    head = [P(NAME, size=20, bold=True, color=b.BLUE, after=1, lead=1.1),
            P("Mechanical Engineer", size=11, bold=True, after=3),
            P("Aalborg, Denmark &nbsp;|&nbsp; +45 71 62 24 00", size=9, after=0),
            P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=9, after=0),
            P("Portfolio: arunabha22.github.io/arunabha-majumder", size=9, after=0),
            P("LinkedIn: linkedin.com/in/arunabha-majumder-681264107", size=9, after=4)]
    body = sec("Profile") + [P(
        "Mechanical engineer who builds and tests mechanisms for medical and assistive devices. I design from first "
        "principles, prototype fast with 3D printing, test on physical setups and on people, and change the design "
        "when it fails. My last device, a shoulder exoskeleton, won the Best Paper Award at IFToMM ISRM 2026.")]
    body += sec("Experience") + role("PhD Researcher, Robotics (project VIEXO)", "Aalborg University, Denmark",
                                    "2023 - Present") + [
        bl("Designed a hybrid shoulder exoskeleton from first principles: a variable stiffness mechanism with a worm "
           "gear for spring pretension, working in parallel with a 6 Nm motor. It uses more than 25% less motor "
           "energy, which means longer battery life."),
        bl("Optimised the mechanism with a genetic algorithm (diameter, spring stiffness, pretension force), built the "
           "CAD and drawings in SolidWorks, 3D printed prototypes and then had the final parts manufactured."),
        bl("Integrated the motor (actuation), encoder and torque/force sensors; measured the stiffness on a physical "
           "test setup to characterise performance."),
        bl("Failure and manufacturability: the first clutch kept breaking and was hard to make, so I replaced it with "
           "a simple bolt-locking clutch (8 locking angles) that was easy to make and reliable."),
        bl("Designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms (VSM); "
           "estimated its stiffness with less than 10% error and quantified human arm impedance (6 participants)."),
        bl("Collected EMG data from 12 participants with the Qualisys system; implemented an Arduino-based trigger to "
           "sync robot motion with Qualisys recordings."),
        bl("Taught university courses and supervised Bachelor's students (2023 - 2025)."),
    ] + role("MTech Researcher, Soft Exosuit (Pneumatic Muscles)", "CSIR-CMERI, India", "2020 - 2022") + [
        bl("Fabricated and assembled pneumatic artificial muscles for a soft exosuit; designed the outer PID loop of a "
           "neural network-based controller in MATLAB/Simulink and implemented it in LabVIEW to drive the pneumatic "
           "muscle (0.3 - 0.78% error, IEEE CONECCT 2022)."),
    ] + role("Bachelor's Capstone and Student Teams", "Siddaganga Institute of Technology, India", "2017 - 2019") + [
        bl("Designed and built an arm exoskeleton and exo glove for a paralysed arm: CAD, machining, assembly and "
           "testing (TATA Technologies Prayatna Innovation Fund grant; Best Major Project Award)."),
        bl("Built a Go-Kart (2017) and an Efficycle hybrid vehicle (2018) with student teams."),
    ]
    body += sec("Skills") + [
        P("<b>Mechanical design:</b> mechanisms from first principles, machine elements (worm gears, springs, "
          "clutches), tolerances, actuation (electric motors, pneumatic muscles), DFM and DFA"),
        P("<b>CAD and prototyping:</b> SolidWorks (CSWA), technical drawings, 3D printing (Bambu Lab, Ultimaker "
          "Cura), machining and hands-on assembly; Fusion 360 (basic, last used 2019)"),
        P("<b>Testing:</b> torque/force sensors, encoders, Qualisys motion capture and EMG, Arduino, MATLAB/Simulink, "
          "LabVIEW, Python (basic)"),
        P("<b>Art and graphic design:</b> hand sketching of concepts, painting, technical illustration; Adobe "
          "Illustrator, Photoshop, Procreate"),
    ]
    body += sec("Education") + [
        P("<b>PhD, Mechatronics and Robotics</b>, Aalborg University, Denmark | 2023 - present (research complete)"),
        P("<b>MTech, Mechatronics</b>, AcSIR - CSIR-CMERI, India | 2020 - 2022"),
        P("<b>BTech, Mechanical Engineering</b>, Siddaganga Institute of Technology, India | 2015 - 2019"),
        P("<b>Senior Diploma in Fine Arts (Painting)</b>, Bangiya Sangeet Parishad | 2008, First Division with "
          "Distinction"),
    ]
    body += sec("Languages and References") + [
        P("English (C1), Bengali (native), Hindi (spoken), French (willing to learn)"),
        P("<b>References:</b> Prof. Shaoping Bai (sbh@mp.aau.dk); Assoc. Prof. Lars Rosgaard Jensen; Assoc. Prof. "
          "Anderson de Souza Castelo Oliveira; all Department of Materials and Production, Aalborg University"),
    ]
    path = HERE + "Arunabha_Majumder_Clira_Health_CV.pdf"
    def deco(c, d):
        c.drawImage(b.PHOTO, b.W - b.M - 2.3 * cm, b.H - b.M - 2.9 * cm, width=2.3 * cm, height=2.9 * cm,
                    preserveAspectRatio=True, mask="auto")
    SimpleDocTemplate(path, pagesize=A4, leftMargin=b.M, rightMargin=b.M, topMargin=b.M, bottomMargin=1.2 * cm,
                      title="Arunabha Majumder CV", author=NAME, creator=NAME, producer=NAME,
                      subject="", keywords="").build(head + body, onFirstPage=deco)
    return path

PARAS = [
    "I am looking for a mechanical or mechatronics engineering role at Clira Health, starting with the Mechanical "
    "Engineer position on your founding team. Making mechanical and mechatronic devices is what I enjoy most, and a "
    "device that lets patients do their blood tests at home is the kind of hard, useful problem I want to own.",
    "What I have built: in my PhD at Aalborg University I designed a hybrid shoulder exoskeleton from first "
    "principles. It has a variable stiffness mechanism, with a worm gear that pretensions the spring, working in "
    "parallel with a 6 Nm motor. I optimised it with a genetic algorithm, modelled it in SolidWorks, 3D printed "
    "prototypes, had the final parts manufactured and measured its stiffness on a physical test setup. It uses more "
    "than 25% less motor energy and won the Best Paper Award at IFToMM ISRM 2026. I also designed and modelled a "
    "novel 5-bar planar parallel robot with variable stiffness mechanisms (VSM), estimated its stiffness with less "
    "than 10% error and quantified human arm impedance.",
    "A failed experiment: my first clutch kept breaking and was hard to make with our workshop's tools. I stopped "
    "defending it and switched to a simple bolt-locking clutch that still locks at 8 angles. It taught me to design "
    "for manufacturing from day one, which matters even more for a disposable.",
    "Before that I fabricated pneumatic artificial muscles for a soft exosuit and designed the outer PID loop of "
    "their controller (IEEE CONECCT 2022), and as a student I built an arm exoskeleton, an exo glove, a Go-Kart and "
    "a hybrid Efficycle. I also hold a Senior Diploma in Fine Arts, do graphic design in Illustrator, Photoshop "
    "and Procreate, and sketch every idea by hand before CAD.",
    "To be honest about gaps: I have not yet designed fluidic seals or worked under ISO 13485, and I do not speak "
    "French yet, but I am willing to learn. My research is finished, so I can start as soon as possible (with time "
    "for a visa and moving), and I am ready to move to Paris. My portfolio has videos and results from my work.",
]

def letter():
    head = [P(NAME, size=18, bold=True, color=b.BLUE, after=1, lead=1.1),
            P("+45 71 62 24 00 &nbsp;|&nbsp; Aalborg, Denmark", size=9, after=0),
            P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=9, after=0),
            P("Portfolio: arunabha22.github.io/arunabha-majumder", size=9, after=10),
            P("Clira Health, Paris", size=10, after=6),
            P("<b>Application: Mechanical Engineer, Founding Team</b>", size=10.5, after=8),
            P("Dear Clira Health team,", size=10.5, after=6)]
    body = [P(t, size=10, after=6, lead=1.28) for t in PARAS] + [P("Kind regards,", size=10, after=2),
                                                                 P(NAME, size=10)]
    path = HERE + "Arunabha_Majumder_Clira_Health_Cover_Letter.pdf"
    SimpleDocTemplate(path, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=1.8 * cm,
                      bottomMargin=1.5 * cm, title="Arunabha Majumder Cover Letter", author=NAME, creator=NAME,
                      producer=NAME, subject="", keywords="").build(head + body)
    return path

if __name__ == "__main__":
    print(cv()); print(letter())

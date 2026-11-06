import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import NAME, tidy
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

# Adaptyv Bio (Lausanne) - Mechanical / Mechatronics Engineer (Early Career), Hardware. Second attempt after a
# screening rejection. Single-column, ATS-safe, 1 page, photo top right. Uses the ad's exact keywords only where
# true for him. Not claimed: enclosures, fixtures, PCB design, C/C++, vacuum, CNC/lathe in the PhD, Fusion/Onshape.
HERE = os.path.dirname(os.path.abspath(__file__)) + "/"
PHOTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/assets/photo.jpeg"
W, H = A4; M = 1.5 * cm
BLUE = HexColor("#1F4E79"); TXT = HexColor("#222222")

def st(size=9.3, bold=False, after=1.6, left=0, first=0, color=TXT, lead=1.22):
    return ParagraphStyle("s", fontName="Arial-B" if bold else "Arial", fontSize=size, leading=size * lead,
                          textColor=color, spaceAfter=after, leftIndent=left, firstLineIndent=first)
def P(t, **k): return Paragraph(tidy(t), st(**k))
def sec(t): return [Spacer(0, 3), P(t.upper(), size=10, bold=True, color=BLUE, after=0),
                    HRFlowable(width="100%", thickness=0.7, color=BLUE, spaceBefore=1, spaceAfter=3)]
def bl(t): return Paragraph(tidy("&bull;&nbsp;" + t), st(left=9, first=-9, after=1.8))
def role(title, org, dates): return [P("<b>%s</b>" % title, after=0, size=9.6),
                                     P("%s &nbsp;|&nbsp; <i>%s</i>" % (org, dates), size=8.8, after=1.5)]

def build_cv():
    head = [P(NAME, size=20, bold=True, color=BLUE, after=1, lead=1.1),
            P("Mechanical / Mechatronics Engineer", size=11, bold=True, after=3),
            P("Aalborg, Denmark &nbsp;|&nbsp; +45 71 62 24 00", size=9, after=0),
            P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=9, after=0),
            P("Portfolio: arunabha22.github.io/arunabha-majumder", size=9, after=0),
            P("LinkedIn: linkedin.com/in/arunabha-majumder-681264107", size=9, after=4)]
    body = sec("Profile") + [P(
        "Hands-on mechanical and mechatronics engineer who enjoys building things. I design, prototype and build "
        "robotic hardware, from concept and CAD (SolidWorks) through 3D printing, fabrication, mechanical assembly, "
        "testing and troubleshooting. I integrate sensors, actuators, motors and Arduino-based control electronics, "
        "and I built a Go-Kart and a hybrid vehicle in student competition teams.")]
    body += sec("Experience") + role("PhD Researcher, Robotics Hardware (project VIEXO)", "Aalborg University, Denmark",
                                    "2023 - Present") + [
        bl("Designed, prototyped and built a shoulder exoskeleton: custom mechanical components in SolidWorks, "
           "3D printed, assembled and rebuilt over many iterations. It cut energy use by more than 25% (Best Paper "
           "Award, IFToMM ISRM 2026)."),
        bl("Integrated a motor, encoder and force sensors with the mechanical frame, and measured the stiffness it "
           "provides on a physical test setup."),
        bl("Designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms; estimated "
           "its stiffness with less than 10% error and quantified human arm impedance."),
        bl("Implemented an Arduino-based trigger system to synchronise robot motion with Qualisys motion capture; "
           "collected EMG and motion data (data acquisition) from 12 participants."),
        bl("Troubleshooting and root cause: a clutch part kept breaking and was hard to make, so I redesigned it "
           "as a simple bolt-locking clutch that was easier to fabricate and reliable."),
        bl("Optimised the design with a genetic algorithm; taught courses and supervised Bachelor's students."),
    ] + role("MTech Researcher, Pneumatic Artificial Muscles", "CSIR-CMERI, India", "2020 - 2022") + [
        bl("Fabricated and assembled pneumatic artificial muscles (pneumatics, valves, pressure sensors, DAQ) and "
           "collected test data on the lab's setup."),
        bl("Designed the outer PID loop of a neural network-based gain-scheduled controller in MATLAB/Simulink and "
           "implemented it in LabVIEW to drive the pneumatic muscle (0.3 - 0.78% error, IEEE CONECCT 2022)."),
    ] + role("Bachelor's Capstone and Student Teams", "Siddaganga Institute of Technology, India", "2017 - 2019") + [
        bl("Designed and built an upper-limb rehabilitation exoskeleton: CAD, machining, mechanical assembly and "
           "testing (Best Major Project Award, TATA Technologies grant)."),
        bl("Student competition teams: built a Go-Kart (2017) and an Efficycle hybrid vehicle (2018) in the "
           "workshop with hand and power tools."),
    ]
    body += sec("Skills") + [
        P("<b>CAD and design:</b> SolidWorks (CSWA), mechanical design, materials and tolerances, design for assembly"),
        P("<b>Prototyping and fabrication:</b> 3D printing (Bambu Lab, Ultimaker Cura), basic machining, mechanical "
          "assembly, hand and power tools"),
        P("<b>Mechatronics:</b> sensor integration, actuators, motors, encoders, force sensors, Arduino, control "
          "systems (PID), pneumatics, data acquisition, testing and troubleshooting"),
        P("<b>Software:</b> MATLAB/Simulink, LabVIEW, Python (basic) &nbsp;|&nbsp; <b>Drawing:</b> hand sketching, "
          "technical illustration"),
    ]
    body += sec("Education") + [
        P("<b>PhD, Mechatronics and Robotics</b>, Aalborg University, Denmark | 2023 - present (research complete)"),
        P("<b>MTech (MSc), Mechatronics</b>, AcSIR - CSIR-CMERI, India | 2020 - 2022"),
        P("<b>BTech (BSc), Mechanical Engineering</b>, Siddaganga Institute of Technology, India | 2015 - 2019"),
        P("<b>Senior Diploma in Fine Arts (Painting)</b>, Bangiya Sangeet Parishad | 2008, Distinction"),
    ]
    body += sec("Languages and References") + [
        P("English (C1), Bengali (native), Hindi (spoken)"),
        P("<b>References:</b> Prof. Shaoping Bai (sbh@mp.aau.dk); Assoc. Prof. Lars Rosgaard Jensen; Assoc. Prof. "
          "Anderson de Souza Castelo Oliveira; all Department of Materials and Production, Aalborg University"),
    ]
    path = HERE + "Arunabha_Majumder_Adaptyv_CV.pdf"
    def deco(c, d):
        c.drawImage(PHOTO, W - M - 2.3 * cm, H - M - 2.9 * cm, width=2.3 * cm, height=2.9 * cm,
                    preserveAspectRatio=True, mask="auto")
    SimpleDocTemplate(path, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=1.2 * cm,
                      title="Arunabha Majumder CV", author=NAME, creator=NAME, producer=NAME,
                      subject="", keywords="").build(head + body, onFirstPage=deco)
    return path

def build_letter():
    head = [P(NAME, size=18, bold=True, color=BLUE, after=1, lead=1.1),
            P("+45 71 62 24 00 &nbsp;|&nbsp; Aalborg, Denmark", size=9, after=0),
            P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=9, after=0),
            P("Portfolio: arunabha22.github.io/arunabha-majumder", size=9, after=10),
            P("Adaptyv Bio, Lausanne", size=10, after=6),
            P("<b>Application: Mechanical / Mechatronics Engineer (Early Career), Hardware</b>", size=10.5, after=8),
            P("Dear Adaptyv Hiring Team,", size=10.5, after=6)]
    paras = [
        "I am applying again for the Mechanical / Mechatronics Engineer role, as your email kindly invited. I think my "
        "first application did not show clearly enough how hands-on my work is, so I want to fix that here. I enjoy "
        "building things and turning ideas into working systems, and helping AI agents run real lab experiments is a "
        "problem I would love to work on.",
        "In my PhD at Aalborg University I designed, prototyped and built robotic hardware from concept to testing. "
        "For a shoulder exoskeleton, I made custom mechanical components in SolidWorks, 3D printed them, did the "
        "mechanical assembly, and integrated a motor, encoder and force sensors. When one clutch part kept breaking, "
        "I found the root cause and redesigned it into a simpler part that was easy to fabricate and reliable. The "
        "exoskeleton cut energy use by more than 25% and won the Best Paper Award at IFToMM ISRM 2026. I also "
        "implemented an Arduino-based trigger system to synchronise a robot with a Qualisys motion capture system, "
        "so I know what it takes to make separate instruments work together in one workflow.",
        "Before that, I worked with pneumatics, valves, pressure sensors and data acquisition on pneumatic artificial "
        "muscles, and implemented a controller in LabVIEW. In my Bachelor's I did machining and mechanical assembly, "
        "and built a Go-Kart and a hybrid vehicle with student teams, so I am comfortable in a workshop with hand "
        "and power tools.",
        "My research work is complete, so I can start soon, and I am ready to relocate to Lausanne. I have not built "
        "lab automation yet, but I learn quickly and I like working closely with software and biology people to make "
        "hardware run reliably with minimal human help. Thank you for taking a second look.",
    ]
    body = [P(t, size=10.2, after=7, lead=1.3) for t in paras] + [P("Kind regards,", size=10.2, after=2),
                                                                   P(NAME, size=10.2)]
    path = HERE + "Arunabha_Majumder_Adaptyv_Cover_Letter.pdf"
    SimpleDocTemplate(path, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=1.8 * cm,
                      bottomMargin=1.6 * cm, title="Arunabha Majumder Cover Letter", author=NAME, creator=NAME,
                      producer=NAME, subject="", keywords="").build(head + body)
    return path

if __name__ == "__main__":
    print(build_cv()); print(build_letter())

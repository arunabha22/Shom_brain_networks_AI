import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *
import pymupdf
from docx.shared import Cm as DCm

# Interstellar Lab Paris - Senior Mechanical Design Engineer. Short headline so it never reaches the photo.
# No Onshape / CATIA / mechanical analysis / space claims. Photo always on the CV (CLAUDE.md).
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
PHOTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/assets/photo.jpeg"
BASE = "Arunabha_Majumder_Interstellar_Lab"

def head(doc, after=6):
    para(doc, NAME, bold=True, size=18, after=0)
    para(doc, "Mechanical Design Engineer", bold=True, size=11, after=2)
    para(doc, "+45 71 62 24 00  |  Aalborg, Denmark", size=9.5, after=0)
    para(doc, "somrkmv1997@gmail.com  |  97arunabhasit027@gmail.com", size=9.5, after=0)
    para(doc, "Portfolio: arunabha22.github.io/arunabha-majumder", size=9.5, after=0)
    para(doc, "LinkedIn: linkedin.com/in/arunabha-majumder-681264107", size=9.5, after=after)

d = new_doc()
head(d)
heading(d, "Profile")
para(d, "Mechanical design engineer who takes systems from concept and hand sketches to SolidWorks assemblies, "
        "2D drawings, working prototypes and tests. For 3 years I have led the mechanical design of a motor-assisted "
        "shoulder exoskeleton, working closely with control, electronics and software colleagues and doing the "
        "integration myself in the lab. PhD in Mechatronics and Robotics at Aalborg University (thesis expected "
        "March), and a Diploma in Fine Arts, so I explain ideas clearly with sketches.")
heading(d, "Core Skills")
bullet(d, "SolidWorks (CSWA): parts, assemblies, 2D technical drawings, Design for Assembly", "CAD: ")
bullet(d, "3D printing (Bambu Lab, Ultimaker Cura), iterative prototypes, custom test rigs, troubleshooting", "Prototyping: ")
bullet(d, "Motor, encoder and force sensor integration; Arduino; MATLAB/Simulink", "Integration: ")
bullet(d, "Qualisys motion capture and data acquisition, Forsentec force/torque sensors, user trials", "Testing: ")
bullet(d, "Hand sketching of concepts, technical illustrations (Adobe Illustrator, Photoshop, Procreate)", "Sketching and visuals: ")
heading(d, "Professional Experience")
role(d, "Research Engineer, Shoulder Exoskeleton (PhD project VIEXO)", "2023 - Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Came up with and designed a hybrid shoulder exoskeleton where a spring carries most of the arm load and a "
          "small 6 Nm motor adds the rest; it cut energy use by more than 25% (Best Paper Award, IFToMM ISRM 2026).")
bullet(d, "Owned the mechanical design from hand sketches to SolidWorks models and drawings, then 3D printed and "
          "rebuilt parts many times to improve fit, strength and ease of assembly.")
bullet(d, "Integrated the motor, encoder and force sensors into the frame and worked with control and software "
          "colleagues to get it running as one system; built custom test rigs.")
bullet(d, "Collected data from 12 participants (EMG with the Qualisys data acquisition system and motion capture).")
bullet(d, "Worked in a team of 3 on an Assist-as-Needed controller (my part: equations such as the Fourier fit, and "
          "defining how the GUI should behave); muscle effort dropped by more than 15%.")
bullet(d, "Estimated tip force on a 5-bar parallel robot from its variable-stiffness actuators (within 10% RMS error "
          "vs a force sensor), so no extra sensor was needed; built an Arduino-based trigger to sync robot motion "
          "with Qualisys cameras for arm impedance tests (6 participants).")
bullet(d, "Taught university courses and supervised Bachelor's students (2023 - 2025).")
role(d, "MTech Researcher, Pneumatic Artificial Muscles (Master's thesis)", "2020 - 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
bullet(d, "Fabricated and assembled pneumatic muscles to an existing lab design, collected test data on the lab's "
          "setup and used it to design the outer PID loop of a gain-scheduled controller "
          "(0.3-0.78% position error, IEEE CONECCT 2022).")
role(d, "Bachelor's Capstone, Upper-Limb Rehabilitation Exoskeleton", "2018 - 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Led CAD design, machining, assembly and testing; Best Major Project Award and an INR 100,000 TATA "
          "Technologies Innovation Grant.")
bullet(d, "Student teams: built a Go-Kart (2017) and an Efficycle hybrid vehicle (2018).")
heading(d, "Education")
role(d, "PhD, Mechatronics and Robotics (defence expected in 2027)", "2023 - Present",
     "Aalborg University, Department of Materials and Production, Denmark")
para(d, "Study abroad, National University of Singapore (NUS), Sep - Nov 2025", after=2)
role(d, "MTech, Mechatronics", "2020 - 2022", "AcSIR - CSIR-CMERI, Durgapur, India")
role(d, "BTech, Mechanical Engineering", "2015 - 2019", "Siddaganga Institute of Technology (VTU), India")
role(d, "Diploma in Fine Arts (Painting)", "", "Bangiya Sangeet Parishad, India")
heading(d, "Awards and Publications")
bullet(d, "Best Research Paper Award, 9th IFToMM ISRM (2026); Certified SolidWorks Associate (CSWA); Best Major "
          "Project Award and TATA Technologies Innovation Grant (2019)")
bullet(d, "Majumder, A., et al. \"A Hybrid Actuated Shoulder Exoskeleton for Energy-Efficient Upper Arm Support.\" "
          "ISRM 2026, Springer. Also IEEE CONECCT 2022.")
heading(d, "Languages")
para(d, "English (C1), Bengali (native), Hindi (spoken)")
heading(d, "References")
para(d, "Available upon request.")
d.paragraphs[0].runs[0].add_picture(PHOTO, width=DCm(2.2))
d.save(OUT + BASE + "_CV.docx")
to_pdf(d, OUT + BASE + "_CV.pdf")
p = pymupdf.open(OUT + BASE + "_CV.pdf")
p[0].insert_image(pymupdf.Rect(470, 40, 541, 128), filename=PHOTO, keep_proportion=True)
meta = p.metadata; meta.update(author=NAME, creator=NAME, producer=NAME); p.set_metadata(meta)
p.save(OUT + "tmp.pdf", garbage=3, deflate=True); p.close(); os.replace(OUT + "tmp.pdf", OUT + BASE + "_CV.pdf")

c = new_doc(); c.sections[0].top_margin = Cm(1.8)
head(c, after=8)
para(c, "October 26, 2026", after=6)
para(c, "Interstellar Lab, Paris", after=6)
para(c, "Application: Senior Mechanical Design Engineer", bold=True, after=6)
para(c, "Dear Interstellar Lab team,", after=6)
for t in [
 "I am applying for the Senior Mechanical Design Engineer role. I am a mechanical engineer doing my PhD in "
 "Mechatronics and Robotics at Aalborg University, with my thesis expected to be finished in March. Your BioPods "
 "caught my eye because they are the kind of product I like most: a closed system where mechanics, electronics and "
 "software all have to work together, and where small design choices decide if it works reliably or not.",
 "For the last 3 years I have owned the mechanical design of a hybrid shoulder exoskeleton. I came up with the idea "
 "of a spring carrying most of the arm load so a small 6 Nm motor is enough, and took it from hand sketches to "
 "SolidWorks assemblies and drawings. I 3D printed and rebuilt the parts many times, keeping track of each revision, "
 "and integrated the motor, encoder and force sensors with the control and software people. It cut energy use by "
 "more than 25% and won the Best Paper Award at IFToMM ISRM 2026.",
 "I am happiest in the lab with the hardware in front of me. I built custom test rigs, an Arduino-based trigger to "
 "sync a 5-bar robot with Qualisys motion capture, and collected data from 12 participants to check the design on "
 "real people. In my Bachelor's capstone I did the CAD, machining and assembly of a rehab exoskeleton myself.",
 "I want to be honest that I do not have 6 years in industry, and I have not used Onshape yet, though moving from "
 "SolidWorks should be quick. I have not worked on plant growth or space hardware either. What I bring is full "
 "ownership of a design from sketch to tested prototype, and the habit of explaining ideas clearly. I have a "
 "Diploma in Fine Arts, so a quick sketch in a design review comes naturally to me.",
 "Thank you for considering my application. My portfolio is at arunabha22.github.io/arunabha-majumder.",
]:
    para(c, t, after=6)
para(c, "Kind regards,", after=2); para(c, NAME)
c.save(OUT + BASE + "_Cover_Letter.docx"); to_pdf(c, OUT + BASE + "_Cover_Letter.pdf", top=1.8)

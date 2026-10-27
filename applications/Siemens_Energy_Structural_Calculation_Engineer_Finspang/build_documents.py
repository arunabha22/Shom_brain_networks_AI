import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *
import pymupdf
from docx.shared import Cm as DCm

# Siemens Energy Finspang - Structural Calculation Engineer (id 287947). NO FEM/FEA/Abaqus/Ansys claims (CLAUDE.md). Photo always on the CV (CLAUDE.md).
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
PHOTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/assets/photo.jpeg"
BASE = "Arunabha_Majumder_Siemens_Energy"

def head(doc, after=6):
    para(doc, NAME, bold=True, size=18, after=0)
    para(doc, "Mechanical Engineer", bold=True, size=11, after=2)
    para(doc, "+45 71 62 24 00  |  Aalborg, Denmark", size=9.5, after=0)
    para(doc, "somrkmv1997@gmail.com  |  97arunabhasit027@gmail.com", size=9.5, after=0)
    para(doc, "Portfolio: arunabha22.github.io/arunabha-majumder", size=9.5, after=0)
    para(doc, "LinkedIn: linkedin.com/in/arunabha-majumder-681264107", size=9.5, after=after)

d = new_doc()
head(d)
heading(d, "Profile")
para(d, "Mechanical engineer with a strong base in modelling, calculations and test validation. In my PhD I "
        "worked on stiffness modelling and Jacobian-based force estimation for a parallel robot, checked against "
        "force sensor measurements, and designed load-carrying parts for a shoulder exoskeleton. I use MATLAB "
        "daily for calculations and data processing, and I write clear technical reports and papers. PhD in "
        "Mechatronics and Robotics at Aalborg University (thesis expected March).")
heading(d, "Core Skills")
bullet(d, "Stiffness modelling, kinematics and Jacobian-based force estimation, validated against sensor data", "Modelling and calculation: ")
bullet(d, "MATLAB/Simulink (daily use), Python (basic), LaTeX", "Scripting and tools: ")
bullet(d, "Test rigs, force/torque sensors, Qualisys motion capture and data acquisition, test data processing", "Testing and validation: ")
bullet(d, "SolidWorks (CSWA): parts, assemblies, technical drawings; design of load-carrying parts", "CAD: ")
bullet(d, "Technical reports, conference papers and presentations; sketches and visuals for papers and demos", "Reporting: ")
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
para(d, "English (C1), Bengali (native), Hindi (spoken), Danish (willing to learn)")
heading(d, "References")
para(d, "Available upon request.")
d.paragraphs[0].runs[0].add_picture(PHOTO, width=DCm(2.2))
d.save(OUT + BASE + "_CV.docx")
to_pdf(d, OUT + BASE + "_CV.pdf")
p = pymupdf.open(OUT + BASE + "_CV.pdf")
p[0].insert_image(pymupdf.Rect(470, 40, 541, 128), filename=PHOTO, keep_proportion=True)
meta = p.metadata; meta.update(author=NAME, creator=NAME, producer=NAME); p.set_metadata(meta)
p.save(OUT + "tmp.pdf", garbage=3, deflate=True); p.close(); os.replace(OUT + "tmp.pdf", OUT + BASE + "_CV.pdf")


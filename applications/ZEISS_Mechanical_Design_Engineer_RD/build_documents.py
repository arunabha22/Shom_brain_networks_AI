import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# ZEISS - Mechanical Design Engineer, R&D (scientific instrumentation). CV + 1-page letter. Follows CLAUDE.md facts.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  |  "

def head(doc, after=6):
    para(doc, NAME, bold=True, size=18, after=0)
    para(doc, "Mechanical Design Engineer | SolidWorks, Electromechanical Assemblies, Prototyping and Testing",
         bold=True, size=11, after=2)
    para(doc, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]),
         size=9.5, after=0)
    para(doc, SEP.join(["Portfolio: arunabha22.github.io/arunabha-majumder",
                        "LinkedIn: linkedin.com/in/arunabha-majumder-681264107"]), size=9.5, after=after)

d = new_doc()
head(d)
heading(d, "Summary")
para(d, "Mechanical design engineer with a PhD in progress in Mechatronics and Robotics at Aalborg University, "
        "plus an MTech in Mechatronics and a BTech in Mechanical Engineering. I design electromechanical "
        "assemblies in SolidWorks, build and test the prototypes and test rigs myself, and find and fix what goes "
        "wrong. Best Research Paper Award, IFToMM ISRM 2026. Certified SolidWorks Associate.")

heading(d, "Experience")
role(d, "PhD Researcher, Mechatronics and Robotics (project VIEXO)", "2023 - Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
bullet(d, "Designed a hybrid shoulder exoskeleton in SolidWorks, where a spring carries most of the load and a small "
          "6 Nm motor adds the rest; it cut energy use by more than 25% (Best Paper Award, IFToMM ISRM 2026).")
bullet(d, "Took the assembly from hand sketches to 3D CAD models and drawings, then built and rebuilt prototypes with "
          "3D printing, improving weak parts after each test round.")
bullet(d, "Integrated the motor, encoder and force sensors into the mechanical frame and built my own test rigs; "
          "found and fixed faults in mounting, wiring, sensors and data logging.")
bullet(d, "Validated a force estimate on a 5-bar parallel robot (variable-stiffness actuators, robot Jacobian) against "
          "a reference force sensor, within 10% RMS error.")
bullet(d, "Worked in a team of 3 on an Assist-as-Needed controller (my part: equations such as the Fourier fit, and "
          "GUI behaviour); collected data from 12 participants; presented at international conferences and taught "
          "and supervised students (2023 - 2025).")

role(d, "MTech Researcher, Pneumatic Artificial Muscles (Master's thesis)", "2020 - 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
bullet(d, "Fabricated and assembled pneumatic artificial muscles to an existing lab design and ran experiments on the "
          "lab's setup with valves, pressure sensors and DAQ.")
bullet(d, "Collected the data, fed it into the lab's existing neural network and used its output to design the outer "
          "PID loop of a gain-scheduled controller (0.3-0.78% error, IEEE CONECCT 2022).")

role(d, "Bachelor's Capstone, Upper-Limb Rehabilitation Exoskeleton", "2018 - 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Designed, machined, assembled and user-tested the device. Best Major Project Award and an INR 100,000 "
          "TATA Technologies grant.")

heading(d, "Skills")
bullet(d, "SolidWorks (CSWA): parts, assemblies and technical drawings", "CAD: ")
bullet(d, "Electromechanical integration: motors, encoders, force/torque and pressure sensors, DAQ", "Systems: ")
bullet(d, "3D printing, test rigs; machining and assembly (Bachelor's)", "Prototyping: ")
bullet(d, "MATLAB/Simulink, Python, LabVIEW (basic)", "Analysis and software: ")
bullet(d, "Diploma in Fine Arts; concept sketches, technical illustrations, clear figures for reports and talks",
       "Drawing and communication: ")
bullet(d, "English (C1, fluent), Bengali (native), Hindi (conversational)", "Languages: ")

heading(d, "Education")
role(d, "PhD, Mechatronics and Robotics (defence expected in 2027)", "2023 - Present", "Aalborg University, Denmark")
role(d, "MTech, Mechatronics", "2020 - 2022", "AcSIR - CSIR-CMERI, India")
role(d, "BTech, Mechanical Engineering", "2015 - 2019", "Siddaganga Institute of Technology (VTU), India")

heading(d, "Awards and Publications")
bullet(d, "Best Research Paper Award, IFToMM ISRM 2026; Certified SolidWorks Associate (CSWA)")
bullet(d, "Majumder, A., et al. \"A Hybrid Actuated Shoulder Exoskeleton for Energy-Efficient Upper Arm Support.\" "
          "ISRM 2026, Springer.")
bullet(d, "Majumder, A., et al. \"Neural Network-Based Gain Scheduled Position Control of a Pneumatic Artificial "
          "Muscle.\" IEEE CONECCT, 2022.")
heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "ZEISS_CV_Arunabha_Majumder.docx")
to_pdf(d, OUT + "ZEISS_CV_Arunabha_Majumder.pdf")

c = new_doc()
c.sections[0].top_margin = Cm(1.8)
head(c, after=8)
para(c, "October 23, 2026", after=6)
para(c, "ZEISS Recruiting Team (Kate Benyon, Lara Haslam, Suya Rolph)", after=6)
para(c, "Application: Mechanical Design Engineer, R&D", bold=True, after=6)
para(c, "Dear ZEISS Recruiting Team,", after=6)
body = [
 "I am applying for the Mechanical Design Engineer position in your R&D team. I am finishing my PhD in Mechatronics "
 "and Robotics at Aalborg University, and I hold an MTech in Mechatronics and a BTech in Mechanical Engineering. My "
 "PhD ends in March.",

 "Most of my work has been designing electromechanical assemblies in SolidWorks and then building and testing them "
 "myself. For my PhD I designed a shoulder exoskeleton where a spring carries most of the load and a small motor "
 "adds the rest. I made the models and drawings, rebuilt the prototypes many times, integrated the motor, encoder "
 "and force sensors, and built the test rigs. When something failed, I worked out why and changed the design. The "
 "result cut energy use by more than 25% and won the Best Paper Award at IFToMM ISRM 2026. On a separate robot, I "
 "validated a force estimate against a reference sensor to within 10%.",

 "I also enjoy explaining technical work clearly. I have presented at international conferences, taught and "
 "supervised students, and I hold a Diploma in Fine Arts, which helps when a design needs a clear sketch or figure.",

 "I have not yet released a product into production, and I would like to build up tolerance stack-ups, thermal "
 "analysis, BOM management and DFM in an industrial setting. ZEISS, with its precision instruments, is where I "
 "would most like to learn them.",

 "Thank you for considering my application. I would be glad to discuss how I can contribute.",
]
for t in body:
    para(c, t, after=6)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "ZEISS_Cover_Letter_Arunabha_Majumder.docx")
to_pdf(c, OUT + "ZEISS_Cover_Letter_Arunabha_Majumder.pdf", top=1.8)

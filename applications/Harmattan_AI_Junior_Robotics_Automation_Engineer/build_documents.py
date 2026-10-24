import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Harmattan AI (Orly) - Junior Robotics Automation Engineer. CV + 1-page letter. Follows CLAUDE.md facts:
# no PLC/TIA, no French, no industrial-robot programming claimed.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  |  "

def head(doc, after=6):
    para(doc, NAME, bold=True, size=18, after=0)
    para(doc, "Robotics and Mechatronics Engineer | Hands-on Integration, Sensors and Actuators, Testing", bold=True,
         size=11, after=2)
    para(doc, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark (open to relocating to Paris area)"]), size=9.5, after=0)
    para(doc, SEP.join(["somrkmv1997@gmail.com", "97arunabhasit027@gmail.com",
                        "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=after)

d = new_doc()
head(d)
heading(d, "Summary")
para(d, "Robotics and mechatronics engineer who works best with hands on the hardware. During my PhD at Aalborg "
        "University I integrated motors, encoders and force sensors into robotic devices, built and debugged my own "
        "test rigs, and found root causes when things failed. I write clear technical notes and specifications, "
        "and I learn new tools quickly.")
heading(d, "Experience")
role(d, "PhD Researcher, Mechatronics and Robotics (project VIEXO)", "2023 - Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
bullet(d, "Integrated the motor, encoder and force sensors into a shoulder exoskeleton and built the test rigs "
          "around it; found and fixed faults in mounting, wiring, sensors and data logging.")
bullet(d, "Designed the hybrid spring and 6 Nm motor actuator in SolidWorks and iterated it with 3D printing; it cut "
          "energy use by more than 25% (Best Paper Award, IFToMM ISRM 2026).")
bullet(d, "Validated a force estimate on a 5-bar parallel robot against a reference force sensor, within 10% RMS "
          "error.")
bullet(d, "Worked in a team of 3 on an Assist-as-Needed controller (my part: equations such as the Fourier fit, and "
          "GUI behaviour); collected data from 12 participants with attention to safety at every session.")
bullet(d, "Taught and supervised Bachelor's students (2023 - 2025).")
role(d, "MTech Researcher, Pneumatic Artificial Muscles (Master's thesis)", "2020 - 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
bullet(d, "Fabricated and assembled pneumatic muscles to an existing lab design, ran experiments on the lab's setup "
          "with valves, pressure sensors and DAQ, and used the data to design the outer PID loop of a "
          "gain-scheduled controller (0.3-0.78% error, IEEE CONECCT 2022).")
role(d, "Student Builds, Siddaganga Institute of Technology", "2017 - 2019", "Tumakuru, India")
bullet(d, "Designed, machined, assembled and tested a rehabilitation exoskeleton (Best Major Project Award, "
          "TATA Technologies grant); built a Go-Kart and an Efficycle hybrid vehicle.")
heading(d, "Skills")
bullet(d, "Motors, encoders, force/torque and pressure sensors, pneumatic valves, DAQ, Arduino", "Sensors and actuators: ")
bullet(d, "SolidWorks (CSWA), 3D printing, test rigs; machining and assembly (Bachelor's)", "Mechanical: ")
bullet(d, "MATLAB/Simulink, Python, LabVIEW (basic)", "Software: ")
bullet(d, "Diploma in Fine Arts; clear sketches and figures for specifications and reports", "Drawing: ")
bullet(d, "English (C1, fluent), Bengali (native), Hindi (conversational)", "Languages: ")
heading(d, "Education")
role(d, "PhD, Mechatronics and Robotics (defence expected in 2027)", "2023 - Present", "Aalborg University, Denmark")
para(d, "Study abroad, National University of Singapore (NUS), Sep - Nov 2025", after=2)
role(d, "MTech, Mechatronics", "2020 - 2022", "AcSIR - CSIR-CMERI, India")
role(d, "BTech, Mechanical Engineering", "2015 - 2019", "Siddaganga Institute of Technology (VTU), India")
heading(d, "Awards and Publications")
bullet(d, "Best Research Paper Award, IFToMM ISRM 2026; Certified SolidWorks Associate (CSWA)")
bullet(d, "Majumder, A., et al. ISRM 2026 (Springer), hybrid actuated shoulder exoskeleton; IEEE CONECCT 2022.")
heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Harmattan_CV_Arunabha_Majumder.docx"); to_pdf(d, OUT + "Harmattan_CV_Arunabha_Majumder.pdf")

c = new_doc(); c.sections[0].top_margin = Cm(1.8)
head(c, after=8)
para(c, "October 24, 2026", after=6)
para(c, "Harmattan AI, Automation and Industrialisation team, Orly", after=6)
para(c, "Application: Junior Robotics Automation Engineer", bold=True, after=6)
para(c, "Dear Harmattan AI team,", after=6)
for t in [
 "I am applying for the Junior Robotics Automation Engineer position in Orly. I am finishing my PhD in Mechatronics "
 "and Robotics at Aalborg University, with an MTech in Mechatronics and a BTech in Mechanical Engineering. My PhD "
 "ends in March.",
 "Most of my work has been hands-on: integrating motors, encoders and force sensors into robotic devices, building "
 "test rigs, and tracking down faults until a setup runs reliably. For my PhD I built a shoulder exoskeleton that "
 "cut energy use by more than 25% and won the Best Paper Award at IFToMM ISRM 2026, and I validated a force "
 "estimate on a 5-bar robot against a reference sensor to within 10%. Testing with 12 people taught me to plan "
 "carefully and take safety seriously.",
 "I want to be clear about my gaps. I have not yet programmed PLCs or Siemens TIA Portal, worked with industrial "
 "robots such as UR or FANUC, or managed integrators, and I do not speak French yet. These are what I would work "
 "hardest to learn alongside your senior engineer. What I bring is a practical, hands-on approach, root-cause "
 "thinking and clear technical writing.",
 "Thank you for considering my application.",
]:
    para(c, t, after=6)
para(c, "Kind regards,", after=2); para(c, NAME)
c.save(OUT + "Harmattan_Cover_Letter_Arunabha_Majumder.docx"); to_pdf(c, OUT + "Harmattan_Cover_Letter_Arunabha_Majumder.pdf", top=1.8)

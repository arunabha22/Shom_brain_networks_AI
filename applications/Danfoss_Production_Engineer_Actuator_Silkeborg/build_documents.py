import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Danfoss Silkeborg - Production Engineer, Actuator Production (radiator thermostats). CV + 1-page cover letter.
# Follows CLAUDE.md facts: both emails, drawing skills, no FEA/Fusion/PLC/force control, machining = Bachelor's,
# Master's = fabricated existing muscle design + outer PID loop, AAN controller = team of 3, study = data collection.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  |  "

def head(doc, after=6):
    para(doc, NAME, bold=True, size=18, after=0)
    para(doc, "Mechanical / Production Engineer | Troubleshooting, Validation, Equipment and Test Rigs", bold=True,
         size=11, after=2)
    para(doc, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]),
         size=9.5, after=0)
    para(doc, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                        "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=after)

# ---------------- CV ----------------
d = new_doc()
head(d)
heading(d, "Summary")
para(d, "Mechanical engineer who likes being close to the hardware and fixing things until they work every time. "
        "During my PhD at Aalborg University I built and maintained test rigs, integrated motors and sensors, found "
        "and fixed faults, and documented setups so others could repeat them. I hold an MTech in Mechatronics and a "
        "BTech in Mechanical Engineering, with workshop experience in machining and assembly from my Bachelor's. I "
        "want to bring this hands-on, structured way of working into production.")

heading(d, "Key Results")
bullet(d, " less energy from a shoulder exoskeleton actuator I designed and built (Best Paper Award, 2026)", ">25%")
bullet(d, " force estimate on a 5-bar robot, validated against a reference force sensor", "<10% error")
bullet(d, " participants in experiments where I collected the data with EMG and motion capture", "12")

heading(d, "Experience")
role(d, "PhD Researcher, Mechatronics and Robotics (project VIEXO)", "2023 - Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
bullet(d, "Built and maintained test rigs for a shoulder exoskeleton and kept them running through repeated test "
          "sessions, finding and fixing faults in mounting, wiring, sensors and data logging.")
bullet(d, "Integrated the motor, encoder and force sensors into the mechanical frame myself, and iterated parts in "
          "SolidWorks and 3D printing until they held up in testing. The design cut energy use by more than 25% "
          "(Best Paper Award, IFToMM ISRM 2026).")
bullet(d, "Validated a force estimate on a 5-bar parallel robot (variable-stiffness actuators, robot Jacobian) "
          "against a reference force sensor, within 10% RMS error.")
bullet(d, "Worked in a team of 3 on an Assist-as-Needed controller: I helped with the equations, such as the Fourier "
          "fit, and defined how the GUI should behave. User muscle effort dropped by more than 15%.")
bullet(d, "Collected data from 12 participants across 3 modes and 2 load conditions, kept clear records of each "
          "setup, and taught and supervised Bachelor's students (2023 - 2025).")

role(d, "MTech Researcher, Pneumatic Artificial Muscles (Master's thesis)", "2020 - 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
bullet(d, "Fabricated and assembled pneumatic artificial muscles to an existing lab design and ran experiments on the "
          "lab's setup with valves, pressure sensors and DAQ.")
bullet(d, "Collected the experimental data, fed it into the lab's existing neural network and used its output to "
          "design the outer PID loop of a gain-scheduled controller, reaching 0.3-0.78% position error "
          "(IEEE CONECCT 2022).")

role(d, "Bachelor's Capstone, Upper-Limb Rehabilitation Exoskeleton", "2018 - 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Designed, machined, assembled and tested it in the college workshop. Best Major Project Award and an "
          "INR 100,000 TATA Technologies grant. Also built a Go-Kart (2017) and an Efficycle hybrid vehicle (2018).")

heading(d, "Skills")
bullet(d, "Troubleshooting hardware, test rigs, validation against reference sensors, documentation",
       "Production-relevant: ")
bullet(d, "SolidWorks (CSWA), 3D printing; machining and assembly (Bachelor's)", "CAD and workshop: ")
bullet(d, "Motors, encoders, force/torque and pressure sensors, pneumatic valves, DAQ, Arduino", "Equipment: ")
bullet(d, "MATLAB/Simulink, Python, LabVIEW (basic)", "Software: ")
bullet(d, "Diploma in Fine Arts; hand sketches, technical illustrations and clear figures for work instructions "
          "and reports", "Drawing: ")
bullet(d, "English (C1, fluent), Bengali (native), Hindi (conversational)", "Languages: ")

heading(d, "Education")
role(d, "PhD, Mechatronics and Robotics (defence expected in 2027)", "2023 - Present", "Aalborg University, Denmark")
role(d, "MTech, Mechatronics", "2020 - 2022", "AcSIR - CSIR-CMERI, Durgapur, India")
role(d, "BTech, Mechanical Engineering", "2015 - 2019", "Siddaganga Institute of Technology (VTU), India")

heading(d, "Awards and Publications")
bullet(d, "Best Research Paper Award, IFToMM ISRM 2026; Certified SolidWorks Associate (CSWA)")
bullet(d, "Majumder, A., et al. \"A Hybrid Actuated Shoulder Exoskeleton for Energy-Efficient Upper Arm Support.\" "
          "ISRM 2026, Springer.")
bullet(d, "Majumder, A., et al. \"Neural Network-Based Gain Scheduled Position Control of a Pneumatic Artificial "
          "Muscle.\" IEEE CONECCT, 2022.")
heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Danfoss_CV_Arunabha_Majumder.docx")
to_pdf(d, OUT + "Danfoss_CV_Arunabha_Majumder.pdf")

# ---------------- COVER LETTER ----------------
c = new_doc()
c.sections[0].top_margin = Cm(1.8)
head(c, after=8)
para(c, "October 21, 2026", after=6)
para(c, "Danfoss A/S, Actuator Production, Silkeborg", after=0)
para(c, "Attn: Gerd Veierskov, Talent Acquisition Partner", after=6)
para(c, "Application: Production Engineer, Actuator Production", bold=True, after=6)
para(c, "Dear Gerd Veierskov and the Actuator Production team,", after=6)
body = [
 "I am applying for the Production Engineer position in Actuator Production in Silkeborg. I am finishing my PhD in "
 "Mechatronics and Robotics at Aalborg University, and I hold an MTech in Mechatronics and a BTech in Mechanical "
 "Engineering. My PhD ends in March, and I would like my next step to be close to real production, where "
 "improvements show up in quality and uptime.",

 "Much of my PhD was spent keeping hardware running. I built and maintained test rigs for a shoulder exoskeleton, "
 "integrated the motor, encoder and force sensors myself, and tracked down faults in mounting, wiring, sensors and "
 "logging until the setup gave repeatable results. I validated a force estimate on a 5-bar robot against a reference "
 "sensor within 10% error, and I kept clear records so others could repeat the tests. In my Master's I worked with "
 "pneumatic valves and pressure sensors, and in my Bachelor's I machined and assembled a rehabilitation exoskeleton "
 "in the workshop.",

 "I have not yet worked in a production line, with PLC systems, or with APQP and PFMEA, and I would like to learn "
 "these with your team. What I bring is a practical, step-by-step way of solving "
 "problems, good documentation habits, and experience explaining technical issues to colleagues and students.",

 "Thank you for considering my application. I would be glad to visit Silkeborg and talk about the role.",
]
for t in body:
    para(c, t, after=6)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Danfoss_Cover_Letter_Arunabha_Majumder.docx")
to_pdf(c, OUT + "Danfoss_Cover_Letter_Arunabha_Majumder.pdf", top=1.8)

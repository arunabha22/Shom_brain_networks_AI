import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Aarhus University MPE - Lab Engineer in Mechanical Engineering (ID 170084). CV + 1-page cover letter.
# Facts only: PhD = SolidWorks + 3D printing; machining = Bachelor's; study = data collection; no flow/accel/temp claimed.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  |  "

def head(doc, after=6):
    para(doc, NAME, bold=True, size=18, after=0)
    para(doc, "Lab Engineer | Experimental Setups, Sensors, Calibration and Data Acquisition", bold=True,
         size=11, after=2)
    para(doc, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com",
                        "97arunabhasit027@gmail.com"]), size=9.5, after=0)
    para(doc, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                        "Portfolio: arunabha22.github.io/arunabha-majumder", "Project: www.viexo.aau.dk"]),
         size=9.5, after=after)

# ---------------- CV ----------------
d = new_doc()
head(d)

heading(d, "Summary")
para(d, "I build experimental setups and keep them running. For the past three years at Aalborg University I have "
        "designed test rigs, fitted force, pressure and motion sensors to them, calibrated them against reference "
        "sensors and collected data from 12 human participants with EMG and motion capture. Before that I built a "
        "pneumatic test bench from scratch in a national lab in India. I enjoy the practical side of research and "
        "helping students and colleagues get reliable data out of their experiments.")

heading(d, "Key Results")
bullet(d, " force error after calibrating a sensorless force estimate against a reference force sensor", "<10%")
bullet(d, " participants measured with EMG, motion capture and force data across 3 modes and 2 loads", "12")
bullet(d, " position error on a pneumatic test bench I built, with a controller in MATLAB/Simulink", "0.3-0.78%")

heading(d, "Experience")
role(d, "PhD Researcher, Experimental Robotics Lab (project VIEXO)", "2023 - Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
bullet(d, "Got force estimates within 10% RMS of a reference force sensor by calibrating a 5-bar parallel robot "
          "with variable-stiffness actuators against a force sensor, and then used the setup to measure human arm "
          "impedance in the gait lab.")
bullet(d, "Collected a full dataset from 12 participants across 3 assistance modes and 2 loads by preparing the "
          "protocol and running the sessions with EMG, Qualisys motion capture and force/torque sensors, with "
          "attention to participant safety and ethics approval.")
bullet(d, "Built and maintained custom test rigs for a shoulder exoskeleton, fitting the motor, encoder, force "
          "sensors and DAQ, and fixing faults in wiring, mounting and logging so the rig gave repeatable results.")
bullet(d, "Cut energy use by more than 25% (Best Paper Award, IFToMM ISRM 2026) with a spring plus 6 Nm motor "
          "actuator that I designed in SolidWorks, 3D printed and tested on those rigs.")
bullet(d, "Taught university students and supervised Bachelor's students in the lab (2023 - 2025), from setting "
          "up equipment to helping them make sense of their measurements.")

role(d, "MTech Researcher, Pneumatic Actuator Test Bench (Master's thesis)", "2020 - 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Built a test bench from the ground up with proportional valves, pressure sensors and DAQ, made the "
          "pneumatic muscles by hand and measured their load-displacement behaviour.")
bullet(d, "Brought position error down to 0.3-0.78%, better than a standard PID, with a neural-network "
          "gain-scheduled controller in MATLAB/Simulink running on the bench (IEEE CONECCT 2022).")

role(d, "Bachelor's Capstone, Upper-Limb Rehabilitation Exoskeleton", "2018 - 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Designed, machined, assembled and tested it with users in the college workshop. Best Major Project "
          "Award and an INR 100,000 TATA Technologies grant.")

heading(d, "Skills")
bullet(d, "Force/torque sensors (Forsentec), pressure sensors, encoders, EMG, Qualisys motion capture",
       "Sensors and measurement: ")
bullet(d, "DAQ hardware, calibration against reference sensors, test rigs and fixtures, Arduino",
       "Data acquisition and setups: ")
bullet(d, "MATLAB/Simulink, Python, LabVIEW (basic) for logging, control and data analysis", "Software: ")
bullet(d, "SolidWorks (CSWA) for fixtures and parts, 3D printing (Bambu Lab, Ultimaker Cura); machining and "
          "assembly (Bachelor's)", "Design and workshop: ")
bullet(d, "Diploma in Fine Arts; hand sketches, technical illustrations and clear figures for lab guides, "
          "reports and teaching", "Drawing and documentation: ")
bullet(d, "English (C1, fluent), Bengali (native), Hindi (conversational)", "Languages: ")

heading(d, "Education")
role(d, "PhD, Mechatronics and Robotics (defence expected in 2027)", "2023 - Present",
     "Aalborg University, Department of Materials and Production, Denmark")
role(d, "MTech (MSc level), Mechatronics", "2020 - 2022", "AcSIR - CSIR-CMERI, Durgapur, India")
role(d, "BTech, Mechanical Engineering", "2015 - 2019", "Siddaganga Institute of Technology (VTU), India")

heading(d, "Awards and Publications")
bullet(d, "Best Research Paper Award, IFToMM ISRM 2026; Certified SolidWorks Associate (CSWA)")
bullet(d, "Majumder, A., et al. \"A Hybrid Actuated Shoulder Exoskeleton for Energy-Efficient Upper Arm Support.\" "
          "ISRM 2026, Springer.")
bullet(d, "Majumder, A., et al. \"Neural Network-Based Gain Scheduled Position Control of a Pneumatic Artificial "
          "Muscle.\" IEEE CONECCT, 2022.")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_CV_Aarhus_Lab_Engineer.docx")
to_pdf(d, OUT + "Arunabha_Majumder_CV_Aarhus_Lab_Engineer.pdf")

# ---------------- COVER LETTER ----------------
c = new_doc()
c.sections[0].top_margin = Cm(1.6)
head(c, after=8)
para(c, "October 12, 2026", after=6)
para(c, "Department of Mechanical and Production Engineering, Workshop and Laboratories", after=0)
para(c, "Aarhus University, Katrinebjergvej 89C, 8200 Aarhus N", after=6)
para(c, "Application: Lab Engineer in Mechanical Engineering (ID 170084)", bold=True, after=6)
para(c, "Dear Peter Lykke and the hiring committee,", after=6)
body = [
 "I am applying for the Lab Engineer position in your workshop and laboratory unit. I hold an MTech in Mechatronics "
 "and a BTech in Mechanical Engineering, and I am finishing my PhD at Aalborg University, where most of my days are "
 "spent in the lab. Reading the ad, I recognised my own work: building setups, fitting sensors, calibrating them and "
 "helping other people get good data.",

 "On a 5-bar parallel robot I calibrated a force estimate from variable-stiffness actuators against a reference "
 "force sensor and got it within 10% RMS error. We then used that setup to measure human arm impedance in the gait "
 "lab. For my exoskeleton project I built and maintained the test rigs, with a motor, encoder, force sensors and "
 "DAQ, and I collected data from 12 participants using EMG, Qualisys motion capture and force/torque sensors. That "
 "work meant writing protocols, keeping recordings in order and thinking about participant safety at every session.",

 "Before Aalborg I spent two years at CSIR-CMERI, a national research lab in India. There I built a pneumatic test "
 "bench from scratch with proportional valves, pressure sensors and DAQ, and used it to test a controller in "
 "MATLAB/Simulink. My tools are MATLAB, Python, LabVIEW at a basic level and Arduino, and I design fixtures in "
 "SolidWorks and print or machine them as needed.",

 "I also like the teaching side of a lab. I have taught university students and supervised Bachelor's students "
 "since 2023, often helping them set up equipment and understand strange readings. I hold a Diploma in Fine Arts, "
 "and I use it to make clear sketches and figures for lab guides and reports, which helps when a student needs to "
 "rebuild a setup alone.",

 "I have less hands-on experience with acceleration, temperature and flow sensors than with force and pressure, "
 "and I would be glad to learn them from your team. I expect to defend my PhD in 2027 and would like to discuss "
 "a start date that works for the department.",

 "Thank you for considering my application. I would be happy to visit Katrinebjergvej and talk about the role.",
]
for t in body:
    para(c, t, after=6)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Cover_Letter_Aarhus_Lab_Engineer.docx")
to_pdf(c, OUT + "Arunabha_Majumder_Cover_Letter_Aarhus_Lab_Engineer.pdf", top=1.6)

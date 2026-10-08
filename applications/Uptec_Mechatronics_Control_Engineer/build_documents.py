import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Uptec (NL) – Mechatronics Engineer (Control Systems) CV. Corrected facts:
# PhD = SolidWorks + 3D printing (no Fusion 360 / FEM); machining and assembly = Bachelor's capstone.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  •  "

d = new_doc()
para(d, NAME, bold=True, size=18, after=0)
para(d, "Mechatronics Engineer — Control Systems, Motion, System Modelling & Integration (MATLAB/Simulink)",
     bold=True, size=11, after=2)
para(d, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]),
     size=9.5, after=0)
para(d, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                  "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=6)

heading(d, "Summary")
para(d, "Mechatronics engineer focused on control systems. Designs control strategies, models system dynamics and "
        "kinematics, and integrates sensors and actuators into prototypes tested at system level. Achieved 0.3–0.78% "
        "tracking error on a non-linear pneumatic actuator and a 25% energy reduction through a new actuation "
        "architecture. MATLAB/Simulink, Python.")

heading(d, "Key Results")
bullet(d, " tracking error with a neural-network gain-scheduled PID controller", "0.3–0.78%")
bullet(d, " energy reduction from a new actuation system concept (Best Paper Award, 2026)", ">25%")
bullet(d, " RMS error from a kinematic (Jacobian) force-estimation model", "<10%")

heading(d, "Experience")
role(d, "Research Engineer – Mechatronic Systems & Control (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Reduced user muscle effort by more than 15%, measured with EMG, by developing and implementing a control "
          "strategy (Assist-as-Needed hybrid control) on a mechatronic system, then testing and tuning it at system "
          "level.")
bullet(d, "Cut energy consumption by more than 25% (Best Paper Award, IFToMM ISRM 2026) by translating functional "
          "requirements into a system concept: a hybrid actuation architecture with a parallel spring and a 6 Nm motor.")
bullet(d, "Achieved below 10% RMS error in end-effector force estimation, validated against a force sensor, by "
          "modelling the kinematics of a 5-bar planar parallel robot (Jacobian) and its variable-stiffness actuators.")
bullet(d, "Selected and integrated sensors and actuators (motor, encoder, force sensors, DAQ, embedded control) into "
          "prototypes designed in SolidWorks and built through 3D printing.")
bullet(d, "Solved system and integration problems by analysing measurement data from custom test rigs, working "
          "closely with electronics, control and biomechanics specialists; mentored Bachelor's students (2023 – 2025).")

role(d, "MTech Researcher – Control of Non-Linear Pneumatic Actuators (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Reduced position-tracking error to 0.3–0.78%, outperforming classical PID under varying load, by designing "
          "a neural-network-based gain-scheduled PID controller in MATLAB/Simulink for a highly non-linear actuator.")
bullet(d, "Built an empirical dynamic model from measurement data by fabricating pneumatic muscles and a test rig "
          "(valves, pressure sensors, DAQ) and characterising their load–displacement behaviour.")

role(d, "Bachelor's Capstone – Upper-Limb Rehabilitation Exoskeleton", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Led CAD design, machining, hands-on assembly and user testing; Best Major Project Award and INR 100,000 "
          "TATA Technologies Innovation Grant.")

heading(d, "Skills")
bullet(d, "PID, gain scheduling, neural-network-based control, Assist-as-Needed control, motion control",
       "Control engineering: ")
bullet(d, "System dynamics, kinematics, Jacobian-based estimation, empirical modelling from test data",
       "Modelling & analysis: ")
bullet(d, "MATLAB/Simulink, Python, LabVIEW (basic), Arduino", "Tools: ")
bullet(d, "Motors, encoders, force and pressure sensors, pneumatic valves, DAQ, embedded control",
       "Sensors & actuators: ")
bullet(d, "SolidWorks (CSWA), 3D printing, test rigs", "Prototyping: ")
bullet(d, "English (C1, fluent), Bengali (Native), Hindi (Conversational)", "Languages: ")

heading(d, "Education")
role(d, "Ph.D. Candidate, Mechatronics & Robotics", "2023 – Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
role(d, "M.Tech, Mechatronics", "2020 – 2022",
     "AcSIR – CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
role(d, "B.Tech, Mechanical Engineering", "2015 – 2019",
     "Siddaganga Institute of Technology, Visvesvaraya Technological University (VTU), Tumakuru, India")

heading(d, "Awards & Publications")
bullet(d, "Best Research Paper Award, IFToMM ISRM 2026; Certified SolidWorks Associate (CSWA)")
bullet(d, "Majumder, A., et al. \"Neural Network-Based Gain Scheduled Position Control of a Pneumatic Artificial "
          "Muscle.\" IEEE CONECCT, 2022.")
bullet(d, "Majumder, A., et al. \"A Hybrid Actuated Shoulder Exoskeleton for Energy-Efficient Upper Arm Support.\" "
          "ISRM 2026, Springer.")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_CV_Uptec.docx")
to_pdf(d, OUT + "Arunabha_Majumder_CV_Uptec.pdf")

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Iono (Austria) – Mechanical Engineer, robotic joints/actuators/exoskeletons. Corrected facts:
# PhD = SolidWorks + 3D printing (no Fusion 360 / FEM claimed); machining and assembly = Bachelor's capstone.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  •  "

d = new_doc()
para(d, NAME, bold=True, size=18, after=0)
para(d, "Mechanical Design Engineer — Robotic Joints, Actuators & Exoskeletons | Mechatronic Integration",
     bold=True, size=11, after=2)
para(d, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark (open to relocate to Austria)", "somrkmv1997@gmail.com",
                  "97arunabhasit027@gmail.com"]), size=9.5, after=0)
para(d, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                  "Portfolio: arunabha22.github.io/arunabha-majumder", "Project: www.viexo.aau.dk"]),
     size=9.5, after=6)

heading(d, "Summary")
para(d, "Mechanical design engineer who builds exoskeletons and robotic actuators from CAD to tested hardware. "
        "Designs mechanical assemblies for robotic joints, linkages and actuator transmissions in SolidWorks (CSWA), "
        "integrates motors, encoders and sensors, and prototypes rapidly through 3D printing. Designed a hybrid-actuated "
        "shoulder exoskeleton that cut energy consumption by more than 25% (Best Paper Award, 2026). Programs "
        "hardware tests in Python and MATLAB.")

heading(d, "Key Results")
bullet(d, " energy reduction from a new spring-plus-motor actuator design for a shoulder exoskeleton", ">25%")
bullet(d, " lower user muscle effort with the motor and sensors integrated and controlled", ">15%")
bullet(d, " RMS force-estimation error on a 5-bar linkage robot with variable-stiffness actuators", "<10%")

heading(d, "Experience")
role(d, "Research Engineer – Exoskeleton & Robotic Actuator Design (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Cut energy consumption by more than 25% (Best Paper Award, IFToMM ISRM 2026) by designing the mechanical "
          "assembly of a shoulder exoskeleton joint with a new robotic actuation concept: a parallel spring working "
          "with a 6 Nm motor.")
bullet(d, "Reduced user muscle effort by more than 15%, measured with EMG in tests with 12 participants, by integrating "
          "the motor, encoder and force sensors with the mechanical structure and implementing the control in "
          "software.")
bullet(d, "Achieved below 10% RMS error in end-effector force estimation, validated against a force sensor, by working "
          "with the linkage kinematics (Jacobian) of a 5-bar planar parallel robot driven by variable-stiffness "
          "actuators.")
bullet(d, "Shortened design iterations by rapidly prototyping lightweight joint and actuator parts in SolidWorks and "
          "3D printing, and testing each version on custom test rigs.")
bullet(d, "Delivered the integrated system by working across mechanical, electronics, control and biomechanics "
          "teams; supervised Bachelor's students (2023 – 2025).")

role(d, "MTech Researcher – Pneumatic Robotic Actuators (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Reduced position-tracking error to 0.3–0.78%, outperforming classical PID, by designing a neural-network "
          "gain-scheduled controller in MATLAB/Simulink for a pneumatic artificial muscle actuator.")
bullet(d, "Built the actuator and its test rig from raw materials (valves, pressure sensors, DAQ) and characterised "
          "its load–displacement behaviour.")

role(d, "Bachelor's Capstone – Upper-Limb Rehabilitation Exoskeleton", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Led CAD design, machining, hands-on assembly and user testing; Best Major Project Award and INR 100,000 "
          "TATA Technologies Innovation Grant.")
bullet(d, "Designed, fabricated and assembled a Go-Kart (2017) and a human-electric hybrid vehicle for Efficycle (2018).")

heading(d, "Skills")
bullet(d, "SolidWorks (CSWA), mechanical assemblies, robotic joints, linkages, actuator transmissions",
       "Mechanical design & CAD: ")
bullet(d, "Motors, encoders, force/torque sensors, pressure sensors, pneumatic valves, DAQ, Arduino",
       "Mechatronic integration: ")
bullet(d, "3D printing (Bambu Lab, Ultimaker Cura), test rigs; machining and assembly (Bachelor's)",
       "Prototyping: ")
bullet(d, "Python, MATLAB/Simulink, LabVIEW (basic) for hardware testing and data analysis",
       "Programming & testing: ")
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
bullet(d, "Majumder, A., et al. \"A Hybrid Actuated Shoulder Exoskeleton for Energy-Efficient Upper Arm Support.\" "
          "ISRM 2026, Springer.")
bullet(d, "Majumder, A., et al. \"Neural Network-Based Gain Scheduled Position Control of a Pneumatic Artificial "
          "Muscle.\" IEEE CONECCT, 2022.")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_CV_Iono.docx")
to_pdf(d, OUT + "Arunabha_Majumder_CV_Iono.pdf")

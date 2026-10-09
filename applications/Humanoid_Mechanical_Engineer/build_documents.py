import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Humanoid (Vancouver) - Mechanical Engineer, humanoid robots. Corrected facts only:
# PhD = SolidWorks + 3D printing (no Fusion 360 / FEA / GD&T claimed); machining + assembly = Bachelor's.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  |  "

d = new_doc()
para(d, NAME, bold=True, size=18, after=0)
para(d, "Mechanical Engineer | Robot Joints, Actuators and Linkages | Prototyping and Testing", bold=True,
     size=11, after=2)
para(d, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark (open to relocating to Vancouver)",
                  "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]), size=9.5, after=0)
para(d, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                  "Portfolio: arunabha22.github.io/arunabha-majumder", "Project: www.viexo.aau.dk"]),
     size=9.5, after=6)

heading(d, "Summary")
para(d, "I design robot joints and actuators and then build and test them myself. For my PhD I designed a "
        "shoulder exoskeleton that works next to the human arm, using a spring and a small 6 Nm motor that share "
        "the load. It cut energy use by more than 25% and won a Best Paper Award in 2026. I work in SolidWorks "
        "(CSWA), prototype with 3D printing, and sit with the electronics and software people until the whole "
        "thing runs.")

heading(d, "Key Results")
bullet(d, " less energy from a new spring and motor actuator for a shoulder joint", ">25%")
bullet(d, " less muscle effort for the user, tested on 12 people", ">15%")
bullet(d, " force error on a 5-bar linkage robot, checked against a force sensor", "<10%")

heading(d, "Experience")
role(d, "Research Engineer, Exoskeleton Joints and Actuators (PhD project VIEXO)", "2023 - Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Cut energy use by more than 25% (Best Paper Award, IFToMM ISRM 2026) by designing the joint, frame "
          "and actuator of a shoulder exoskeleton in SolidWorks, where a parallel spring carries part of the load "
          "and a 6 Nm motor handles the rest.")
bullet(d, "Got force estimates within 10% RMS of a reference force sensor by working out the linkage kinematics "
          "(Jacobian) of a 5-bar planar parallel robot driven by variable-stiffness actuators.")
bullet(d, "Went through several versions of each part in weeks rather than months by 3D printing them, fitting "
          "them on the rig and fixing what broke or flexed too much.")
bullet(d, "Lowered user muscle effort by more than 15%, measured with EMG on 12 participants, after fitting the "
          "motor, encoder and force sensors into the frame and getting the control running with the electronics "
          "and software side.")
bullet(d, "Built my own test rigs to check torque, motion and durability of each version, and kept the drawings, "
          "parts lists and test notes so others could rebuild the setup. Supervised Bachelor's students "
          "(2023 - 2025).")

role(d, "MTech Researcher, Pneumatic Actuators (Master's thesis)", "2020 - 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
bullet(d, "Brought position error down to 0.3-0.78%, better than a standard PID, with a neural-network "
          "gain-scheduled controller in MATLAB/Simulink for a pneumatic artificial muscle.")
bullet(d, "Made the muscles by hand and built the test bench around them (valves, pressure sensors, DAQ) to map "
          "load against stroke.")

role(d, "Bachelor's Capstone, Upper-Limb Rehabilitation Exoskeleton", "2018 - 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Designed it in CAD, machined the parts, assembled it and tested it with users. Best Major Project "
          "Award and an INR 100,000 TATA Technologies grant.")
bullet(d, "Also designed, machined and put together a Go-Kart (2017) and a human-electric hybrid vehicle for "
          "Efficycle (2018).")

heading(d, "Skills")
bullet(d, "SolidWorks (CSWA), parts, assemblies and drawings, joints, linkages, actuator layouts",
       "Mechanical design: ")
bullet(d, "Statics, dynamics, kinematics and Jacobians, choosing parts for strength and weight",
       "Engineering basics: ")
bullet(d, "3D printing (Bambu Lab, Ultimaker Cura); CNC and manual machining and assembly (Bachelor's)",
       "Building: ")
bullet(d, "Motors, encoders, force/torque sensors, pressure sensors, DAQ, Arduino; Python, MATLAB/Simulink",
       "Integration and test: ")
bullet(d, "English (C1, fluent), Bengali (native), Hindi (conversational)", "Languages: ")

heading(d, "Education")
role(d, "PhD, Mechatronics and Robotics (in progress)", "2023 - Present",
     "Aalborg University, Department of Materials and Production, Denmark")
role(d, "MTech, Mechatronics", "2020 - 2022", "AcSIR - CSIR-CMERI, Durgapur, India")
role(d, "BTech, Mechanical Engineering", "2015 - 2019",
     "Siddaganga Institute of Technology (VTU), Tumakuru, India")

heading(d, "Awards and Publications")
bullet(d, "Best Research Paper Award, IFToMM ISRM 2026; Certified SolidWorks Associate (CSWA)")
bullet(d, "Majumder, A., et al. \"A Hybrid Actuated Shoulder Exoskeleton for Energy-Efficient Upper Arm Support.\" "
          "ISRM 2026, Springer.")
bullet(d, "Majumder, A., et al. \"Neural Network-Based Gain Scheduled Position Control of a Pneumatic Artificial "
          "Muscle.\" IEEE CONECCT, 2022.")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_CV_Humanoid.docx")
to_pdf(d, OUT + "Arunabha_Majumder_CV_Humanoid.pdf")

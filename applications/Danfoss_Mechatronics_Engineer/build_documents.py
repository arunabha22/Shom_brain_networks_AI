import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Danfoss Mechatronics Engineer CV: energy efficiency, prototyping and lab verification up front.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  •  "

d = new_doc()
para(d, NAME, bold=True, size=18, after=0)
para(d, "Mechatronics Engineer — Product Development, Prototyping & Laboratory Verification", bold=True,
     size=11, after=2)
para(d, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]),
     size=9.5, after=0)
para(d, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                  "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=6)

heading(d, "Summary")
para(d, "Mechatronics engineer who develops energy-efficient electromechanical products from concept to validated "
        "prototype. Designed a mechatronic actuation subsystem that improved energy efficiency by more than 25% "
        "(Best Paper Award, 2026), with hands-on experience in 3D CAD, prototyping, laboratory testing and "
        "verification.")

heading(d, "Key Results")
bullet(d, " energy-efficiency gain from a new mechatronic subsystem", ">25%")
bullet(d, " RMS error on a verified sensing method", "<10%")
bullet(d, " delivered end to end", "Concept → prototype → lab validation")

heading(d, "Experience")
role(d, "Research Engineer – Mechatronic Product Development (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Improved energy efficiency by more than 25%, measured in laboratory testing of an actuated shoulder "
          "exoskeleton, by developing a new mechatronic subsystem: a hybrid actuation concept that pairs a parallel "
          "spring with a 6 Nm motor (Best Paper Award, IFToMM ISRM 2026).")
bullet(d, "Turned design targets into a working functional model, from product concept to detailed design, by "
          "creating the 3D CAD design and assemblies in SolidWorks, using FEA for strength, stiffness and weight, and "
          "planning, building and evaluating prototypes made from machined and 3D-printed parts.")
bullet(d, "Achieved force estimation accurate to below 10% RMS error, verified against a force sensor, by developing a "
          "sensorless method for a 5-bar planar parallel robot using variable-stiffness actuators and the robot "
          "Jacobian, as part of product verification and performance evaluation.")
bullet(d, "Reduced user muscle effort by more than 15%, measured with EMG, by integrating the motor, encoder, force "
          "sensors and DAQ with an Assist-as-Needed controller in the embedded control system.")
bullet(d, "Delivered a complete laboratory test dataset from a 12-participant study across 3 operating modes and 2 "
          "load conditions by running the data collection within a multidisciplinary project team (mechanical, "
          "electronics, control, biomechanics).")
bullet(d, "Documented results in peer-reviewed publications; mentored and supervised Bachelor's (B.Tech) students "
          "(2023 – 2025).")

role(d, "MTech Researcher – Pneumatic Actuator Systems (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Reduced position-tracking error to 0.3–0.78%, outperforming classical PID under varying load, by designing "
          "a neural-network-based controller for a non-linear pneumatic actuator.")
bullet(d, "Characterised actuator performance through lab testing by fabricating pneumatic artificial muscles in-house "
          "and building a test rig with valves, pressure sensors and DAQ.")

heading(d, "Skills")
bullet(d, "SolidWorks (CSWA), Fusion 360; quickly transferable to PTC Creo", "3D CAD: ")
bullet(d, "Functional models, test rigs, verification, performance evaluation, DAQ", "Prototyping & lab testing: ")
bullet(d, "Motors, encoders, sensors, pneumatics, embedded control, MATLAB/Simulink, Python", "Mechatronics: ")
bullet(d, "FEA, kinematics, control design", "Analysis: ")
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
bullet(d, "Two peer-reviewed publications: ISRM 2026 (Springer) and IEEE CONECCT 2022")

heading(d, "Hands-On Projects")
bullet(d, "Rehabilitation exoskeleton (Best Major Project Award and TATA Technologies Innovation Grant, 2019), "
          "Go-Kart (2017), Efficycle human-electric hybrid vehicle (2018)")

heading(d, "References")
para(d, "Available upon request.")

d.save(OUT + "Arunabha_Majumder_CV_Danfoss.docx")
to_pdf(d, OUT + "Arunabha_Majumder_CV_Danfoss.pdf")

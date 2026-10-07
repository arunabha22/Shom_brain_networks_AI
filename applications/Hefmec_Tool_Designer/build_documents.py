import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Hefmec Tool Designer CV: design, strength calculation and hands-on building up front.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  •  "

d = new_doc()
para(d, NAME, bold=True, size=18, after=0)
para(d, "Mechanical Designer — 3D Design, Strength Calculation (FEA), Drawings & Prototyping", bold=True,
     size=11, after=2)
para(d, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]),
     size=9.5, after=0)
para(d, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                  "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=6)

heading(d, "Summary")
para(d, "Mechanical designer with 3+ years of hands-on 3D design, strength calculation (FEA) and prototype building. "
        "Takes projects from concept and detail design to workshop drawings, manufacture and testing, and has built "
        "machines outside work since student years, including a Go-Kart from the ground up.")

heading(d, "Key Results")
bullet(d, " designed, drew, built and tested a load-carrying actuated device (Best Paper Award, 2026)",
       "Concept to working hardware:")
bullet(d, " energy reduction through a better technical solution", ">25%")
bullet(d, " error on a validated measurement method", "<10%")

heading(d, "Experience")
role(d, "Research Engineer – Mechanical Design & Actuator Development (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Delivered a working prototype from concept to tested hardware by taking ownership of the design project: "
          "concept design, 3D modelling and detail design in SolidWorks, workshop drawings for machined and "
          "3D-printed parts, and hands-on assembly and testing.")
bullet(d, "Verified the structural safety and weight of load-carrying parts before manufacture by using strength "
          "calculation with FEA for stiffness, strength and weight under expected load cases, then iterated the design "
          "for manufacturability.")
bullet(d, "Cut energy consumption by more than 25% in prototype testing (Best Paper Award, IFToMM ISRM 2026) by "
          "defining the technical solution for a hybrid actuation system: a parallel spring working with a 6 Nm motor.")
bullet(d, "Achieved force estimation accurate to below 10% RMS error, validated against a force sensor, by developing "
          "a sensorless method for a 5-bar planar parallel robot using variable-stiffness actuators and the robot "
          "Jacobian; applied it to measure human arm impedance in the gait lab.")
bullet(d, "Reduced user muscle effort by more than 15%, measured with EMG, by implementing an Assist-as-Needed "
          "controller on the prototype; ran data collection for a 12-participant study in a multidisciplinary team.")
bullet(d, "Mentored and supervised Bachelor's (B.Tech) students on engineering projects (2023 – 2025).")

role(d, "MTech Researcher – Pneumatic Actuator Systems (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Built an empirical actuator model from test data by fabricating pneumatic artificial muscles in-house from "
          "raw materials and setting up a test rig with valves, pressure sensors and DAQ.")
bullet(d, "Reduced position-tracking error to 0.3–0.78%, outperforming classical PID under varying load, by designing "
          "a neural-network-based controller.")

heading(d, "Hands-On Engineering")
bullet(d, "Designed, fabricated and assembled a custom Go-Kart from the ground up.", "Go-Kart (2017): ")
bullet(d, "Built a human-electric hybrid vehicle in a multidisciplinary team for the Efficycle competition.",
       "Efficycle (2018): ")
bullet(d, "Led CAD design, fabrication and user testing of an upper-limb rehabilitation exoskeleton; Best Major "
          "Project Award and INR 100,000 TATA Technologies Innovation Grant.", "Rehabilitation device (2018–2019): ")
bullet(d, "Fabricated actuators from raw materials; machining, 3D printing and assembly for every prototype.",
       "Workshop: ")

heading(d, "Skills")
bullet(d, "Stiffness, strength, load cases, weight optimisation", "Strength calculation & FEA: ")
bullet(d, "SolidWorks (CSWA), Fusion 360, detail design, workshop drawings, assemblies, DFA",
       "3D design & drawings: ")
bullet(d, "Machining, 3D printing, assembly, test rigs, DAQ", "Manufacturing & prototyping: ")
bullet(d, "MATLAB/Simulink, Python, LabVIEW (basic), Arduino", "Software: ")
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

heading(d, "References")
para(d, "Available upon request.")

d.save(OUT + "Arunabha_Majumder_CV_Hefmec.docx")
to_pdf(d, OUT + "Arunabha_Majumder_CV_Hefmec.pdf")

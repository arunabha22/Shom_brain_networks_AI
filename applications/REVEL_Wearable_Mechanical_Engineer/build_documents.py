import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# REVEL (Prague) – Mechanical Engineer, NG sleeve & hub (wearable). Corrected facts:
# PhD = SolidWorks + 3D printing (no Fusion 360 / FEM); machining and assembly = Bachelor's capstone.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  •  "

d = new_doc()
para(d, NAME, bold=True, size=18, after=0)
para(d, "Mechanical Engineer — Arm-Worn Wearables, Prototyping & Fit Testing (SolidWorks)", bold=True, size=11,
     after=2)
para(d, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]),
     size=9.5, after=0)
para(d, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                  "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=6)

heading(d, "Summary")
para(d, "Mechanical engineer for arm-worn devices. Designed and built two upper-limb wearables, prototyped them through "
        "3D printing and tested them on real arms with participants. Also built soft pneumatic actuators by hand. "
        "SolidWorks (CSWA), Best Paper Award 2026.")

heading(d, "Key Results")
bullet(d, " upper-limb wearables designed, built and tested on people", "2")
bullet(d, " energy reduction from the wearable's actuation and mounting architecture", ">25%")
bullet(d, " lower wearer muscle effort, measured with EMG", ">15%")

heading(d, "Experience")
role(d, "Research Engineer – Wearable Arm & Shoulder Devices (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Designed and prototyped a body-worn shoulder and upper-arm device in SolidWorks, iterating through "
          "3D-printed prototypes and testing on real arms with 12 participants.")
bullet(d, "Cut energy use by more than 25% (Best Paper Award, IFToMM ISRM 2026) through the wearable's actuation and "
          "mounting architecture: a parallel spring working with a 6 Nm motor.")
bullet(d, "Integrated sensors and electronics into the wearable (motor, encoder, force sensors, DAQ, cabling), working "
          "across mechanical, electronics and control.")
bullet(d, "Measured human arm impedance with a force-estimation method on a 5-bar planar parallel robot, validated "
          "against a force sensor to below 10% RMS error.")
bullet(d, "Reduced wearer muscle effort by more than 15%, measured with EMG, through Assist-as-Needed control; "
          "mentored Bachelor's (B.Tech) students (2023 – 2025).")

role(d, "MTech Researcher – Soft Pneumatic Actuators (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Built soft pneumatic artificial muscles from raw materials and their test rig (valves, pressure sensors, "
          "DAQ); reduced tracking error to 0.3–0.78% with a neural-network-based controller.")

role(d, "Bachelor's Capstone – Upper-Limb Rehabilitation Exoskeleton (Medical Wearable)", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Won the Best Major Project Award and an INR 100,000 TATA Technologies Innovation Grant by leading CAD "
          "design, machining, hands-on assembly and user testing.")

heading(d, "Skills")
bullet(d, "Arm and shoulder exoskeletons, body-worn mechanisms, testing with participants", "Wearables: ")
bullet(d, "SolidWorks (CSWA), 3D printing (FDM), rapid iteration; machining and assembly (Bachelor's)",
       "CAD & prototyping: ")
bullet(d, "Soft pneumatic artificial muscles, motors, encoders, force sensors, DAQ", "Actuators & sensors: ")
bullet(d, "MATLAB/Simulink, Python, Arduino", "Software: ")
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
d.save(OUT + "Arunabha_Majumder_CV_REVEL.docx")
to_pdf(d, OUT + "Arunabha_Majumder_CV_REVEL.pdf")

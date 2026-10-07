import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# mimic robotics – Senior Mechanical Engineer (Wearable Devices) CV. Uses corrected facts:
# PhD = SolidWorks + 3D printing (no Fusion 360 / FEM); machining and assembly = Bachelor's capstone.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  •  "

d = new_doc()
para(d, NAME, bold=True, size=18, after=0)
para(d, "Mechanical Engineer — Wearable Devices, Exoskeletons, Sensor Integration & Rapid Prototyping", bold=True,
     size=11, after=2)
para(d, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]),
     size=9.5, after=0)
para(d, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                  "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=6)

heading(d, "Summary")
para(d, "Mechanical engineer for body-worn devices. Designed and built two exoskeletons, from mechanical "
        "architecture and sensor integration to rapid 3D-printed iterations and testing with human participants. "
        "Force-sensing method validated to below 10% error; wearable design that cut energy use by more than 25% "
        "(Best Paper Award, 2026).")

heading(d, "Key Results")
bullet(d, " energy reduction from the wearable's actuation architecture", ">25%")
bullet(d, " lower wearer muscle effort, tested with human participants", ">15%")
bullet(d, " RMS error on force sensing, validated against a force sensor", "<10%")

heading(d, "Experience")
role(d, "Research Engineer – Wearable Robotics & Mechanical Architecture (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Cut energy consumption by more than 25% (Best Paper Award, IFToMM ISRM 2026) by owning the mechanical "
          "architecture of a wearable shoulder exoskeleton: choosing a hybrid actuation concept that pairs a parallel "
          "spring with a 6 Nm motor, balancing performance, component packaging and weight on the body.")
bullet(d, "Took the wearable from early prototype to tested system by designing it in SolidWorks and iterating "
          "rapidly through 3D-printed prototypes based on hands-on testing.")
bullet(d, "Integrated sensors and embedded components (motor, encoder, force sensors, DAQ and embedded control, with "
          "cabling) into one working device, working across mechanical, electronics and control.")
bullet(d, "Achieved below 10% RMS error in force sensing, validated against a force sensor, by developing a "
          "force-estimation method on a 5-bar planar parallel robot using variable-stiffness actuators and the robot "
          "Jacobian; applied it to measure human arm impedance in the gait lab.")
bullet(d, "Reduced wearer muscle effort by more than 15%, measured with EMG, by implementing an Assist-as-Needed "
          "controller tested with human participants; conducted data collection with 12 participants across 3 modes "
          "and 2 load conditions.")
bullet(d, "Mentored and supervised Bachelor's (B.Tech) students (2023 – 2025).")

role(d, "MTech Researcher – Soft Pneumatic Actuators (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Reduced position-tracking error to 0.3–0.78% with a neural-network-based controller for soft pneumatic "
          "artificial muscles, which I fabricated from raw materials along with their test rig (valves, pressure "
          "sensors, DAQ).")

role(d, "Bachelor's Capstone – Upper-Limb Rehabilitation Exoskeleton (Wearable Device)", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Won the Best Major Project Award and an INR 100,000 TATA Technologies Innovation Grant by leading CAD "
          "design, machining, hands-on assembly and user testing of a wearable rehabilitation device.")

heading(d, "Skills")
bullet(d, "Exoskeletons, body-worn mechanisms, physical human-robot interaction, testing with participants",
       "Wearables: ")
bullet(d, "Force sensors, encoders, motors, DAQ, embedded control, cabling, EMG, Qualisys motion capture",
       "Sensor & electronics integration: ")
bullet(d, "SolidWorks (CSWA), 3D printing, rapid iteration; machining and assembly (Bachelor's)",
       "CAD & prototyping: ")
bullet(d, "Kinematics, force estimation, Assist-as-Needed control, MATLAB/Simulink, Python", "Analysis & control: ")
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
d.save(OUT + "Arunabha_Majumder_CV_mimic.docx")
to_pdf(d, OUT + "Arunabha_Majumder_CV_mimic.pdf")

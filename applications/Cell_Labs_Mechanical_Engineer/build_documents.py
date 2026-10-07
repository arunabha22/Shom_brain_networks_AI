import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Cell Labs (humanoid robots, Berlin) Mechanical Engineer CV and project note.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  •  "
TITLE = "Mechanical Engineer — Robotic Actuators, Joint Kinematics, Prototyping & Test Rigs"

def head(doc, after=6):
    para(doc, NAME, bold=True, size=18, after=0)
    para(doc, TITLE, bold=True, size=11, after=2)
    para(doc, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com",
                        "97arunabhasit027@gmail.com"]), size=9.5, after=0)
    para(doc, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                        "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=after)

# ---------------- CV ----------------
d = new_doc()
head(d)

heading(d, "Summary")
para(d, "Mechanical engineer who designs robotic actuators, joints and kinematic mechanisms and builds them into "
        "working hardware. Designed a robotic shoulder actuation system that cut energy use by more than 25% (Best "
        "Paper Award, 2026), modelled parallel-robot kinematics to below 10% force-estimation error, and builds own "
        "prototypes and test rigs. Works fast: first prototype early, then iterate.")

heading(d, "Key Results")
bullet(d, " energy reduction from a new actuator and transmission concept", ">25%")
bullet(d, " RMS error from Jacobian-based force estimation on a 5-bar parallel robot", "<10%")
bullet(d, " robotic joints and actuators designed, built and tested in-house", "CAD → prototype → test rig:")

heading(d, "Experience")
role(d, "Research Engineer – Robotic Actuators & Mechanical Design (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Cut energy consumption by more than 25% (Best Paper Award, IFToMM ISRM 2026) by designing the actuator and "
          "transmission concept for a robotic shoulder joint: a parallel spring working with a 6 Nm motor, sized so "
          "torque and load requirements were met across the assistance cycle.")
bullet(d, "Took a robotic joint from CAD to working hardware, iterating quickly from a first prototype, by designing "
          "mechanical components and assemblies in SolidWorks and Fusion 360 and making parts through additive "
          "manufacturing and machining.")
bullet(d, "Improved strength-to-weight before manufacture by running stress analysis (FEA) for stiffness, strength and "
          "weight optimisation of load-carrying parts.")
bullet(d, "Achieved below 10% RMS error in end-effector force estimation on a 5-bar planar parallel robot, verified "
          "against a force sensor, by modelling its kinematics (Jacobian) and variable-stiffness actuators.")
bullet(d, "Integrated electronics into the mechanical assembly (motor, encoder, force sensors, DAQ and embedded "
          "control), then built test rigs and tracked down problems on the bench through repeated test campaigns, "
          "including tests under 2 load conditions.")
bullet(d, "Kept several projects moving at once (two robots, testing, a 12-participant data collection, and mentoring "
          "Bachelor's students in 2023 – 2025) with full design documentation: 3D models, drawings and part "
          "specifications.")

role(d, "MTech Researcher – Pneumatic Actuators (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Characterised actuator load–displacement behaviour by building pneumatic artificial muscles in-house from "
          "raw materials and an actuator test rig with valves, pressure sensors and DAQ.")
bullet(d, "Reduced position-tracking error to 0.3–0.78% with a neural-network-based controller, outperforming "
          "classical PID under varying load.")

heading(d, "Things I Built")
bullet(d, "Hybrid-actuated robotic shoulder joint: actuator concept, CAD, FEA, fabrication, electronics, test rigs.",
       "Exoskeleton joint (2023–present): ")
bullet(d, "Kinematic model and force estimation from variable-stiffness actuators, tested in the gait lab.",
       "5-bar parallel robot (PhD): ")
bullet(d, "Concept, CAD, fabrication and user testing; Best Major Project Award and TATA Technologies Innovation "
          "Grant.", "Rehabilitation exoskeleton (2018–2019): ")
bullet(d, "Designed, fabricated and assembled from the ground up.", "Go-Kart (2017): ")

heading(d, "Skills")
bullet(d, "Actuator selection and sizing (motors, encoders), joint kinematics, transmissions, parallel mechanisms",
       "Robotics mechanics: ")
bullet(d, "SolidWorks (CSWA), Autodesk Fusion 360, assemblies, drawings, part specifications", "CAD: ")
bullet(d, "FEA stress analysis, weight optimisation, additive manufacturing, machined parts, DFA",
       "Analysis & manufacturing: ")
bullet(d, "Test rigs, load testing, bench troubleshooting, sensor and DAQ integration, embedded control",
       "Prototyping & testing: ")
bullet(d, "MATLAB/Simulink, Python, Arduino, LabVIEW (basic)", "Software: ")
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
d.save(OUT + "Arunabha_Majumder_CV_Cell_Labs.docx")
to_pdf(d, OUT + "Arunabha_Majumder_CV_Cell_Labs.pdf")

# ---------------- PROJECT NOTE ----------------
p = new_doc()
head(p, after=8)
heading(p, "Project Note: Hybrid-Actuated Robotic Shoulder Joint")
para(p, "What I built", bold=True, after=2)
para(p, "A robotic shoulder joint for an exoskeleton (PhD project VIEXO, Aalborg University) that supports the arm "
        "against gravity. I designed the actuation concept, the mechanical structure and assemblies, made the parts, "
        "integrated the electronics and built the test rigs. Project page: www.viexo.aau.dk", after=8)
para(p, "Challenge 1: Torque demand vs. motor size and weight", bold=True, after=2)
para(p, "Carrying the full gravity torque with a motor alone would need a large, heavy and power-hungry actuator. "
        "I combined a parallel spring that carries the quasi-static gravity load with a small 6 Nm motor that only "
        "supplies what the spring cannot. This kept the joint light and cut energy consumption by more than 25% "
        "(Best Paper Award, IFToMM ISRM 2026).", after=8)
para(p, "Challenge 2: Strength and stiffness without adding weight", bold=True, after=2)
para(p, "Load-carrying parts had to stay stiff and strong while remaining light. I used FEA to iterate the geometry "
        "for stiffness, strength and weight before manufacture, and chose between machined and 3D-printed parts "
        "depending on the part, so I could get a first prototype built quickly and improve from there.",
     after=8)
para(p, "Challenge 3: Getting reliable force information", bold=True, after=2)
para(p, "On a related 5-bar planar parallel robot, I estimated the end-effector force from the variable-stiffness "
        "actuators through the robot's Jacobian and validated it against a force sensor to below 10% RMS error. "
        "I then used it to measure human arm impedance in the gait lab.", after=8)
para(p, "Challenge 4: Making the prototype work on the bench", bold=True, after=2)
para(p, "I integrated the motor, encoder, force sensors, DAQ and embedded control, built custom test rigs, and "
        "tracked down mechanical, electrical and control issues through repeated test campaigns until the system "
        "ran reliably in tests with participants.", after=8)
para(p, "More projects and photos: arunabha22.github.io/arunabha-majumder")
p.save(OUT + "Arunabha_Majumder_Project_Note_Cell_Labs.docx")
to_pdf(p, OUT + "Arunabha_Majumder_Project_Note_Cell_Labs.pdf", top=2.0)

# ---------------- COVER LETTER ----------------
c = new_doc()
c.sections[0].top_margin = Cm(2.0)
head(c, after=8)
para(c, "October 7, 2026", after=8)
para(c, "Hiring Team", after=0)
para(c, "Cell Labs", after=0)
para(c, "Berlin, Germany", after=8)
para(c, "Application: Mechanical Engineer – Humanoid Systems", bold=True, after=8)
para(c, "Dear Cell Labs Team,", after=8)
body = [
 "I am applying for the Mechanical Engineer position. I am a mechanical and mechatronics engineer finishing my PhD "
 "at Aalborg University, and what I enjoy most is exactly what you describe: designing robotic joints and "
 "actuators, getting a first prototype built quickly, and improving it on the bench until it works.",

 "In my PhD, I designed and built a robotic shoulder joint for an exoskeleton. Instead of a large motor carrying "
 "the full gravity torque, I combined a parallel spring with a small 6 Nm motor, sized so the torque and load "
 "requirements were met across the motion. I designed the components and assemblies in SolidWorks and Fusion 360, "
 "used FEA for stress analysis and weight optimisation, made the parts through 3D printing and machining, and "
 "integrated the motor, encoder, force sensors, DAQ and embedded control. The design cut energy consumption by more "
 "than 25% and won the Best Paper Award at IFToMM ISRM 2026.",

 "I understand how kinematics and actuators come together in a working robot. On a 5-bar planar parallel robot, I "
 "modelled the kinematics and estimated the end-effector force from variable-stiffness actuators through the "
 "robot's Jacobian, validated against a force sensor to below 10% RMS error. I build my own test rigs, track down "
 "mechanical, electrical and control problems on the bench, and I have built machines since my student years, "
 "including a Go-Kart from the ground up.",

 "My hardware so far has been prototypes rather than products in series production, and I have not yet worked with "
 "injection moulding, sheet metal or supplier ramp-up, or used Onshape. These are exactly the skills I want to "
 "build, and a team that takes humanoid robots from CAD to production under one roof is the right place to do it. "
 "I am open to relocating to Berlin.",

 "I would welcome the opportunity to show you my work in a technical deep-dive. My portfolio is linked above, and "
 "references are available upon request.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Cover_Letter_Cell_Labs.docx")
to_pdf(c, OUT + "Arunabha_Majumder_Cover_Letter_Cell_Labs.pdf", top=2.0)

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
TAG = "Levitate_Mechanical_RD_Engineer"
TITLE = "Mechanical R&D Engineer | Mechanisms & Wearable Robotics | Prototyping | Test Rigs & Validation"

# ---------------- RESUME ----------------
d = new_doc()
header(d, TITLE)

heading(d, "Professional Summary")
para(d, "Mechanical R&D Engineer with a B.Tech in Mechanical Engineering, an M.Tech in Mechatronics and a PhD in "
        "progress in Denmark, developing wearable load-carrying mechanisms that people use on their bodies. Takes "
        "mechanical concepts from whiteboard idea to tested hardware: mechanism development, SolidWorks CAD, FEA "
        "and structural analysis, rapid prototyping from machined and 3D-printed parts, custom test rigs, "
        "functional testing and validation with human users. Curious about how mechanisms work and why they fail, "
        "with hands-on engineering projects ranging from a self-built Go-Kart to hand-made pneumatic "
        "muscles. Best Paper Award, IFToMM ISRM 2026; Certified SolidWorks Associate (CSWA).")

heading(d, "Core Skills")
bullet(d, "Mechanism development, moving assemblies, compliant and variable-stiffness actuation, new mechanical "
          "concepts, load-bearing wearable structures", "Mechanisms & Concepts: ")
bullet(d, "SolidWorks (CSWA certified), Fusion 360, Finite Element Analysis (FEA), analytical stiffness and "
          "kinematic modelling, structural behaviour", "Mechanical Design & Analysis: ")
bullet(d, "Rapid prototyping, proof-of-concept builds, machined parts, additive manufacturing / 3D printing, "
          "hands-on fabrication and assembly, Design for Assembly (DFA)", "Prototyping & Manufacturing: ")
bullet(d, "Test fixture and test rig design, functional testing, verification and validation, user testing, "
          "experimental data analysis", "Testing & Verification: ")
bullet(d, "Analytical problem solving, model-to-hardware validation, design iteration from test results",
       "Problem Solving: ")
bullet(d, "Motor, encoder, force-sensor and DAQ integration, pneumatic actuators, embedded control, Python, "
          "MATLAB/Simulink", "Mechatronics & Tools: ")

heading(d, "Professional Experience")
role(d, "Research Engineer – Mechanisms & Wearable Robotics R&D (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Developed a hybrid-actuated shoulder exoskeleton from concept to tested hardware: mechanism concept, "
          "SolidWorks CAD, FEA iterations for stiffness, strength and weight, fabrication, assembly and testing.")
bullet(d, "Developed a hybrid actuation principle that pairs a parallel spring with a 6 Nm motor to carry "
          "quasi-static gravity load; cut energy consumption by more than 25% (Best Paper Award, IFToMM ISRM 2026).")
bullet(d, "Built rapid prototypes hands-on from machined and additively manufactured parts, and integrated motor, "
          "encoder, force sensors and DAQ.")
bullet(d, "Designed custom automated test rigs and validated analytical stiffness models of variable-stiffness "
          "actuators against experimental hardware to below 10% RMS error, de-risking mechanisms before "
          "fabrication.")
bullet(d, "Removed the external force/torque sensor from a 5-bar parallel robot by deriving force from the "
          "actuator's torque–deflection characteristic, reducing cost, mass and integration complexity.")
bullet(d, "Validated the device with users in a 12-participant study across 3 assistance modes and 2 load "
          "conditions (EMG, motion capture), reducing muscle effort by more than 15%.")
bullet(d, "Taught university students and supervised Bachelor's (B.Tech) students (2023 – 2025).")

role(d, "M.Tech Researcher – Pneumatic Actuator Systems (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
bullet(d, "Fabricated pneumatic artificial muscle actuators in-house from raw materials and built the test setup "
          "with valves, pressure sensors and DAQ to characterise load–displacement behaviour.")
bullet(d, "Derived an empirical actuator model from test data and designed a neural-network-based controller, "
          "reducing position-tracking error to 0.3–0.78% under varying load.")

role(d, "Mechanical Engineering Capstone – Upper-Limb Rehabilitation Exoskeleton", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Led CAD design, fabrication and user testing of a rehabilitation exoskeleton end to end; won the Best "
          "Major Project Award and an INR 100,000 TATA Technologies Innovation Grant.")

heading(d, "Hands-On Engineering Projects")
bullet(d, "Designed, fabricated and built a custom Go-Kart from the ground up.", "Go-Kart (2017): ")
bullet(d, "Worked in a multidisciplinary team to design and build a human-electric hybrid vehicle for the "
          "Efficycle competition.", "Efficycle (2018): ")
bullet(d, "Diploma in Fine Arts (Painting); freehand sketching for concepts and technical illustration.",
       "Sketching: ")

heading(d, "Education")
role(d, "Ph.D. Candidate, Mechatronics & Robotics", "2023 – Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
role(d, "M.Tech, Mechatronics", "2020 – 2022",
     "AcSIR – CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
role(d, "B.Tech, Mechanical Engineering", "2015 – 2019",
     "Siddaganga Institute of Technology, Visvesvaraya Technological University (VTU), Tumakuru, India")

heading(d, "Certifications & Awards")
bullet(d, "Best Research Paper Award, 9th IFToMM International Symposium on Robotics and Mechatronics (2026)")
bullet(d, "Certified SolidWorks Associate (CSWA) – Mechanical Design")
bullet(d, "Best Major Project Award (2019); TATA Technologies Innovation Award – INR 100,000 Grant (2019)")

heading(d, "Publications")
bullet(d, "Majumder, A., Wagner, J.W., Zhu, Y., Oliveira, A.S., and Bai, S. \"A Hybrid Actuated Shoulder Exoskeleton "
          "for Energy-Efficient Upper Arm Support.\" Robotics and Mechatronics: ISRM 2026, MMS, vol. 213, Springer.")
bullet(d, "Majumder, A., Sarkar, D., Chakraborty, S., Singh, A., Roy, S.S., and Arora, A. \"Neural Network-Based Gain "
          "Scheduled Position Control of a Pneumatic Artificial Muscle.\" IEEE CONECCT, 2022.")

heading(d, "Technical Tools")
bullet(d, "SolidWorks, Fusion 360, FEA, Bambu Lab and Ultimaker Cura (3D printing)", "CAD & Manufacturing: ")
bullet(d, "Python, MATLAB/Simulink, LabVIEW (basic), Arduino", "Software & Modelling: ")
bullet(d, "Qualisys Motion Capture, Forsentec Force/Torque Sensors, Pneumatic Control, Custom Rig Fabrication",
       "Testing & Instrumentation: ")

heading(d, "Languages")
para(d, "English (C1, fluent) | Bengali (Native) | Hindi (Conversational)")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_Resume_%s.docx" % TAG)
to_pdf(d, OUT + "Arunabha_Majumder_Resume_%s.pdf" % TAG)

# ---------------- COVER LETTER ----------------
c = new_doc()
c.sections[0].top_margin = Cm(2.0)
header(c, TITLE)
para(c, "September 29, 2026", after=8)
para(c, "Head of Innovation and R&D Lead", after=0)
para(c, "Levitate", after=0)
para(c, "Copenhagen, Denmark", after=8)
para(c, "Application: Mechanical R&D Engineer", bold=True, after=8)
para(c, "Dear Hiring Team,", after=8)
body = [
 "I am applying for the Mechanical R&D Engineer position. I hold a B.Tech in Mechanical Engineering and an M.Tech "
 "in Mechatronics, and I am finishing my PhD at Aalborg University, where I develop wearable mechanisms that carry "
 "load on the human body. Building devices that people wear and move with, and that have to be light, strong and "
 "predictable, is the work I enjoy most.",

 "In my PhD, I developed a hybrid-actuated shoulder exoskeleton from a whiteboard idea to tested hardware. Instead "
 "of relying on a large motor, I paired a parallel spring with a small 6 Nm motor so the spring carries the "
 "gravity load. I designed the mechanism in SolidWorks, iterated on FEA for stiffness, strength and weight, built "
 "the prototypes hands-on from machined and 3D-printed parts, and tested them. The design cut energy consumption "
 "by more than 25% and won the Best Paper Award at IFToMM ISRM 2026.",

 "Testing and understanding failures is central to how I work. I build custom test rigs, and I validated my "
 "stiffness models of variable-stiffness actuators against hardware to within 10% RMS error before committing to "
 "fabrication. I also validated the device with users in a 12-participant study. On a 5-bar "
 "parallel robot, I questioned whether a force/torque sensor was needed at all and replaced it with force "
 "estimation from the actuator itself.",

 "My curiosity has always gone beyond my main work. I designed and built a Go-Kart from the ground up, helped build a "
 "human-electric hybrid vehicle for the Efficycle competition, and during my Master's I made pneumatic "
 "artificial muscles from raw materials to understand how they behave under load.",

 "So far my testing has been functional and validation testing rather than fatigue and durability testing to ISO "
 "standards, and I have not yet taken a product through industrialisation and launch. Those are exactly the "
 "steps I want to master next, and Levitate's products are where I would most like to learn them.",

 "I would welcome the opportunity to take on your practical engineering interview and development case. "
 "References are available upon request.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Cover_Letter_%s.docx" % TAG)
to_pdf(c, OUT + "Arunabha_Majumder_Cover_Letter_%s.pdf" % TAG, top=2.0)

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
TAG = "CUBIC_Mechanical_Designer"
TITLE = "Mechanical Designer | 3D CAD & Technical Drawings | New Product Development | Prototyping"

# ---------------- RESUME ----------------
d = new_doc()
header(d, TITLE)

heading(d, "Professional Summary")
para(d, "Mechanical Designer with a B.Tech in Mechanical Engineering, an M.Tech in Mechatronics and about three "
        "years of hands-on new product development in Denmark. Turns concepts and requirements into practical "
        "electromechanical designs: 3D CAD models and technical drawings in SolidWorks, FEA-driven iterations for "
        "stiffness, strength and weight, and prototypes built, assembled, tested and verified hands-on. Brings a "
        "structured approach with attention to detail, keeps cost and manufacturability in mind, and collaborates "
        "closely with engineers across disciplines. Certified SolidWorks Associate (CSWA), fluent in English (C1), "
        "based in Aalborg.")

heading(d, "Core Skills")
bullet(d, "SolidWorks (CSWA certified), Fusion 360, 3D CAD modelling, assemblies, creating and interpreting "
          "technical drawings, Finite Element Analysis (FEA)", "3D CAD & Drawings: ")
bullet(d, "New Product Development (NPD), concept to tested prototype, Design for Assembly (DFA), design for "
          "manufacturability, cost and part-count reduction", "Mechanical Design: ")
bullet(d, "Machined parts, additive manufacturing / 3D printing, prototype fabrication and assembly",
       "Manufacturing: ")
bullet(d, "Prototype development, testing, product verification, custom test rigs, experimental validation",
       "Prototyping & Verification: ")
bullet(d, "Electromechanical products: motor, encoder, force-sensor and DAQ integration, actuator design",
       "Electromechanical Systems: ")
bullet(d, "Structured design documentation (3D models, drawings), cross-functional collaboration, ownership, English (C1)",
       "Ways of Working: ")

heading(d, "Professional Experience")
role(d, "Research Engineer – Mechanical Design & Product Development (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Took a wearable electromechanical product from concept and requirements to tested hardware, owning "
          "the SolidWorks 3D CAD models, assemblies and technical drawings throughout development.")
bullet(d, "Iterated designs on FEA results for stiffness, strength and weight before fabrication, and validated "
          "analytical stiffness models against physical tests to below 10% RMS error.")
bullet(d, "Built prototypes hands-on from machined and additively manufactured parts, assembled them, and "
          "integrated motor, encoder, force sensors and DAQ.")
bullet(d, "Planned and ran testing and verification with custom automated test rigs, including a 12-participant "
          "study across 3 assistance modes and 2 load conditions.")
bullet(d, "Reduced system cost, mass and part count of a 5-bar parallel robot by removing the external "
          "force/torque sensor, using a force-estimation method derived from the actuator itself.")
bullet(d, "Cut energy consumption by more than 25% with a hybrid actuation design combining a parallel spring and "
          "a 6 Nm motor; awarded Best Paper, IFToMM ISRM 2026.")
bullet(d, "Taught university students and supervised Bachelor's (B.Tech) students (2023 – 2025).")

role(d, "M.Tech Researcher – Actuator Systems (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
bullet(d, "Fabricated pneumatic artificial muscle actuators in-house and integrated valves, pressure sensors and DAQ "
          "to characterise load–displacement behaviour and derive an empirical actuator model.")
bullet(d, "Reduced dynamic position-tracking error to 0.3–0.78% with a neural-network-based gain-scheduled PID "
          "controller for a non-linear pneumatic actuator.")

role(d, "Mechanical Engineering Capstone – Upper-Limb Rehabilitation Exoskeleton", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Led CAD design, fabrication and user testing of a rehabilitation exoskeleton; won the Best Major Project "
          "Award and an INR 100,000 TATA Technologies Innovation Grant.")

heading(d, "Education")
role(d, "Ph.D. Candidate, Mechatronics & Robotics", "2023 – Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
role(d, "M.Tech, Mechatronics", "2020 – 2022",
     "AcSIR – CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
role(d, "B.Tech, Mechanical Engineering", "2015 – 2019",
     "Siddaganga Institute of Technology, Visvesvaraya Technological University (VTU), Tumakuru, India")

heading(d, "Engineering Projects")
bullet(d, "Led end-to-end design and fabrication of a custom Go-Kart built from the ground up.", "Go-Kart (2017): ")
bullet(d, "Worked in a multidisciplinary team to engineer a human-electric hybrid vehicle for the Efficycle "
          "competition.", "Efficycle (2018): ")

heading(d, "Certifications & Awards")
bullet(d, "Certified SolidWorks Associate (CSWA) – Mechanical Design")
bullet(d, "Best Research Paper Award, 9th IFToMM International Symposium on Robotics and Mechatronics (2026)")
bullet(d, "Best Major Project Award, Department of Mechanical Engineering (2019)")
bullet(d, "TATA Technologies Innovation Award – INR 100,000 Grant (2019)")

heading(d, "Publications")
bullet(d, "Majumder, A., Wagner, J.W., Zhu, Y., Oliveira, A.S., and Bai, S. \"A Hybrid Actuated Shoulder Exoskeleton "
          "for Energy-Efficient Upper Arm Support.\" Robotics and Mechatronics: ISRM 2026, MMS, vol. 213, Springer.")
bullet(d, "Majumder, A., Sarkar, D., Chakraborty, S., Singh, A., Roy, S.S., and Arora, A. \"Neural Network-Based Gain "
          "Scheduled Position Control of a Pneumatic Artificial Muscle.\" IEEE CONECCT, 2022.")

heading(d, "Technical Tools")
bullet(d, "SolidWorks, Fusion 360, FEA, Bambu Lab and Ultimaker Cura (3D printing)", "CAD & Manufacturing: ")
bullet(d, "MATLAB/Simulink, Python, LabVIEW (basic), Arduino", "Software: ")
bullet(d, "Qualisys Motion Capture, Forsentec Force/Torque Sensors, Custom Rig Fabrication", "Testing: ")

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
para(c, "Hiring Team, R&D", after=0)
para(c, "CUBIC-Modulsystem A/S, a Rockwell Automation company", after=0)
para(c, "Brønderslev, Denmark", after=8)
para(c, "Application: Mechanical Designer – R&D", bold=True, after=8)
para(c, "Dear Hiring Team,", after=8)
body = [
 "I am applying for the Mechanical Designer position in CUBIC's R&D team in Brønderslev. I hold a B.Tech in "
 "Mechanical Engineering and an M.Tech in Mechatronics, and I am finishing my PhD at Aalborg University. For the "
 "past three years I have turned concepts and requirements into practical electromechanical designs in Denmark, "
 "and I am motivated by seeing designs become real products.",

 "In my PhD, I took a wearable electromechanical product from concept to tested hardware. I owned the SolidWorks "
 "3D models, assemblies and technical drawings, iterated the design on FEA results for stiffness, strength and "
 "weight, and built the prototypes hands-on from machined and additively manufactured parts. I then planned and "
 "ran testing and verification on custom test rigs. The design cut energy consumption by more than 25% and won "
 "the Best Paper Award at IFToMM ISRM 2026.",

 "I work in a structured way and keep manufacturability and cost in mind. On a 5-bar parallel robot, I removed an "
 "external force/torque sensor by estimating force from the actuator itself, which reduced cost, mass and part "
 "count. I validate my models against physical tests before committing to fabrication, and I produce the drawings "
 "used to build and assemble each part.",

 "My projects combine mechanical design, electronics and control, so I am used to working closely with engineers "
 "from other disciplines. I have worked in Denmark and India with English as my working language, and I am a "
 "Certified SolidWorks Associate. I am based in Aalborg, close to Brønderslev.",

 "My CAD experience is in SolidWorks and Fusion 360 rather than Creo, and my hands-on manufacturing so far is "
 "mainly with machined and additively manufactured parts. Creo, sheet metal and the Engineering Change process "
 "are where I want to grow next, and CUBIC's switchboard systems are the right place to do it.",

 "I would welcome the opportunity to discuss how I can contribute to your team. References are available upon "
 "request.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Cover_Letter_%s.docx" % TAG)
to_pdf(c, OUT + "Arunabha_Majumder_Cover_Letter_%s.pdf" % TAG, top=2.0)

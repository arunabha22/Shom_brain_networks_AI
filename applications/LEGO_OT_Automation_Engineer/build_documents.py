import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
TITLE = "Automation & Robotics Engineer | Proof-of-Concept | Prototyping & Testing | Sensors & Control"

# Short, project-led layout: brief bullets, keyword skills, selected projects.
d = new_doc()
header(d, TITLE, links=True)

heading(d, "Summary")
para(d, "Automation and robotics engineer (MTech Mechatronics, BTech Mechanical Engineering, PhD in progress) who "
        "takes ideas from concept and feasibility to working prototypes and tested hardware. Hands-on with "
        "robotic mechanisms, actuators, sensors, pneumatics and control systems. Clear communicator across "
        "technical and non-technical audiences in international teams in Denmark and India.")

heading(d, "Skills")
bullet(d, "Robotics, actuators, pneumatics, sensors, motors, encoders, DAQ, embedded control (Arduino), LabVIEW",
       "Automation & Robotics: ")
bullet(d, "Concept creation, feasibility studies, proof-of-concept, prototyping, testing, validation",
       "Innovation: ")
bullet(d, "PID and model-based control, kinematics, Jacobian-based force estimation, MATLAB/Simulink, Python",
       "Control & Software: ")
bullet(d, "SolidWorks (CSWA), Autodesk Fusion 360, FEA, 3D printing, machining, assembly, custom test rigs",
       "Design & Build: ")
bullet(d, "Stakeholder collaboration, technical communication, teaching, English (C1)", "Communication: ")

heading(d, "Experience")
role(d, "Research Engineer – Robotics & Automation (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Took a hybrid-actuated shoulder exoskeleton from concept to tested prototype; cut energy use by more "
          "than 25% (Best Paper Award, IFToMM ISRM 2026).")
bullet(d, "Evaluated a sensing approach on a 5-bar planar parallel robot: end-effector force estimated from "
          "variable-stiffness actuators via the Jacobian, validated against a force sensor to below 10% RMS error.")
bullet(d, "Integrated motor, encoder, force sensors, DAQ and embedded control; built custom automated test rigs.")
bullet(d, "Designed and tested an Assist-as-Needed controller, reducing user muscle effort by more than 15%.")
bullet(d, "Taught university students and supervised Bachelor's (B.Tech) students (2023 – 2025).")

role(d, "MTech Researcher – Pneumatic Actuator Systems", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
bullet(d, "Built pneumatic artificial muscles and a pneumatic test set-up (valves, pressure sensors, DAQ).")
bullet(d, "Developed a neural-network gain-scheduled PID controller: tracking error 0.3–0.78%.")

heading(d, "Selected Projects")
bullet(d, "Concept, CAD, fabrication and user testing; Best Major Project Award and INR 100,000 TATA "
          "Technologies Innovation Grant.", "Rehabilitation Exoskeleton (2018–2019): ")
bullet(d, "Multidisciplinary team build of a human-electric hybrid vehicle.", "Efficycle (2018): ")
bullet(d, "Designed, fabricated and assembled from the ground up.", "Go-Kart (2017): ")

heading(d, "Education")
bullet(d, " | Aalborg University, Denmark | 2023 – Present", "PhD Candidate, Mechatronics and Robotics")
bullet(d, " | AcSIR – CSIR-CMERI, India | 2020 – 2022", "MTech, Mechatronics")
bullet(d, " | Siddaganga Institute of Technology (VTU), India | 2015 – 2019", "BTech, Mechanical Engineering")

heading(d, "Publications & Awards")
bullet(d, "Majumder, A., et al. \"A Hybrid Actuated Shoulder Exoskeleton for Energy-Efficient Upper Arm Support.\" "
          "ISRM 2026, Springer. Best Research Paper Award.")
bullet(d, "Majumder, A., et al. \"Neural Network-Based Gain Scheduled Position Control of a Pneumatic Artificial "
          "Muscle.\" IEEE CONECCT, 2022.")
bullet(d, "Certified SolidWorks Associate (CSWA)")

heading(d, "Languages & References")
para(d, "English (C1, fluent) | Bengali (Native) | Hindi (Conversational)")
para(d, "References available upon request.")
d.save(OUT + "Arunabha_Majumder_LEGO_Resume.docx")
to_pdf(d, OUT + "Arunabha_Majumder_LEGO_Resume.pdf")

# ---------------- COVER LETTER ----------------
c = new_doc()
c.sections[0].top_margin = Cm(2.0)
header(c, TITLE, links=True)
para(c, "September 30, 2026", after=8)
para(c, "Operational Technology Innovation", after=0)
para(c, "The LEGO Group", after=0)
para(c, "Billund, Denmark", after=8)
para(c, "Application: OT Automation Engineer (Req. 0000038614)", bold=True, after=8)
para(c, "Dear Hiring Team,", after=8)
body = [
 "I am applying for the OT Automation Engineer role in Operational Technology Innovation. I am an automation and "
 "robotics engineer with an MTech in Mechatronics, finishing my PhD at Aalborg University, and what I enjoy most "
 "is exactly what this role describes: taking an idea through feasibility and proof-of-concept to a prototype "
 "that works.",

 "In my PhD, I took a hybrid-actuated shoulder exoskeleton from concept to tested hardware, combining a parallel "
 "spring with a small motor. I designed and built the prototype, integrated the motor, encoder, force sensors, DAQ "
 "and embedded control, and built custom test rigs. The concept cut energy use by more than 25% and won the Best "
 "Paper Award at IFToMM ISRM 2026.",

 "I like comparing technical options on evidence. On a 5-bar planar parallel robot, I estimated the end-effector "
 "force from variable-stiffness actuators through the robot's Jacobian and validated it against a force sensor to "
 "within 10% RMS error. During my Master's at CSIR-CMERI, I built pneumatic actuators and a pneumatic test set-up, "
 "and developed a controller that reduced tracking error to below 0.8%.",

 "I communicate well with different audiences. I have taught and supervised Bachelor's students, published "
 "peer-reviewed work, and worked in international teams in India and Denmark in English.",

 "My automation experience so far is in research labs rather than factory environments, and I have not yet "
 "programmed industrial PLCs. My controls background in embedded control, LabVIEW and pneumatics gives me a solid "
 "base, and I am ready to build PLC skills quickly in a team that is shaping LEGO's future factories.",

 "I would welcome the opportunity to discuss how I can contribute. References are available upon request.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_LEGO_Cover_Letter.docx")
to_pdf(c, OUT + "Arunabha_Majumder_LEGO_Cover_Letter.pdf", top=2.0)


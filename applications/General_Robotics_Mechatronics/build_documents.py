import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# General robotics/mechatronics version (e.g. for the Odense Robotics talent platform).
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
TITLE = "Mechatronics & Robotics Engineer | Mechanical Design | Actuators & Control | Prototyping"

# ---------------- RESUME ----------------
d = new_doc()
header(d, TITLE, links=True)

heading(d, "Professional Summary")
para(d, "Mechatronics and robotics engineer with a BTech in Mechanical Engineering, an MTech in Mechatronics and a "
        "PhD in progress at Aalborg University, with more than five years of hands-on R&D in robotic and "
        "electromechanical systems. Takes ideas from concept to tested hardware: mechanical design in SolidWorks, "
        "FEA, rapid prototyping, actuator and sensor integration, control implementation, and structured testing "
        "and validation. Designed a hybrid-actuated shoulder exoskeleton that cut energy consumption by more than "
        "25% (Best Paper Award, IFToMM ISRM 2026). Collaborative, structured and fluent in English (C1), with "
        "experience in international teams in Denmark and India.")

heading(d, "Core Skills")
bullet(d, "Mechanical design, mechanisms, actuator design, 3D CAD, technical drawings, FEA, Design for Assembly (DFA)",
       "Mechanical Design: ")
bullet(d, "Robotic systems, parallel robots, compliant and variable-stiffness actuation, exoskeletons, "
          "kinematics and Jacobian-based force estimation", "Robotics: ")
bullet(d, "Motors, encoders, force/torque sensors, pressure sensors, DAQ, embedded control (Arduino), pneumatics",
       "Mechatronics & Integration: ")
bullet(d, "PID, neural-network gain scheduling, Assist-as-Needed control, MATLAB/Simulink, Python",
       "Control & Modelling: ")
bullet(d, "Rapid prototyping, machining, 3D printing, assembly, custom test rigs, test planning, data analysis",
       "Prototyping & Testing: ")
bullet(d, "Cross-disciplinary collaboration, technical writing, teaching and supervision", "Collaboration: ")

heading(d, "Professional Experience")
role(d, "Research Engineer – Robotics & Actuator Development (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Designed a hybrid-actuated shoulder exoskeleton combining a parallel spring with a 6 Nm motor to offload "
          "gravity torque, cutting energy consumption by more than 25% (Best Paper Award, IFToMM ISRM 2026).")
bullet(d, "Built the full prototype from concept to tested hardware: SolidWorks CAD and FEA, machined and 3D-printed "
          "parts, assembly, motor, encoder, force-sensor and DAQ integration, embedded control and custom automated "
          "test rigs.")
bullet(d, "Developed end-effector force estimation for a 5-bar planar parallel robot using variable-stiffness "
          "actuators (VSA) and the robot Jacobian, validated against a force sensor to below 10% RMS error.")
bullet(d, "Implemented an Assist-as-Needed hybrid controller on the prototype, reducing user muscle effort by more "
          "than 15% in tests with human participants.")
bullet(d, "Planned and ran a 12-participant validation study across 3 assistance modes and 2 load conditions, "
          "including statistical power justification, EMG and motion-capture instrumentation, ethics protocol and "
          "data analysis.")
bullet(d, "Taught university students and supervised Bachelor's (B.Tech) students (2023 – 2025).")

role(d, "MTech Researcher – Pneumatic Actuator Systems (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Reduced position-tracking error to 0.3–0.78% with a neural-network-based gain-scheduled PID controller "
          "for a non-linear pneumatic actuator, outperforming classical PID under varying load.")
bullet(d, "Fabricated pneumatic artificial muscles in-house from raw materials and built the test set-up with valves, "
          "pressure sensors and DAQ to characterise load–displacement behaviour and derive an empirical model.")

role(d, "Mechanical Engineering Capstone – Upper-Limb Rehabilitation Exoskeleton", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Led CAD design, fabrication and user testing end to end; won the Best Major Project Award and an "
          "INR 100,000 TATA Technologies Innovation Grant.")

heading(d, "Education")
role(d, "PhD Candidate, Mechatronics and Robotics", "2023 – Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
role(d, "MTech, Mechatronics", "2020 – 2022",
     "AcSIR – CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
role(d, "BTech, Mechanical Engineering", "2015 – 2019",
     "Siddaganga Institute of Technology, Visvesvaraya Technological University (VTU), Tumakuru, India")

heading(d, "Publications")
bullet(d, "Majumder, A., Wagner, J.W., Zhu, Y., Oliveira, A.S., and Bai, S. \"A Hybrid Actuated Shoulder Exoskeleton "
          "for Energy-Efficient Upper Arm Support.\" Robotics and Mechatronics: ISRM 2026, MMS, vol. 213, Springer.")
bullet(d, "Majumder, A., Sarkar, D., Chakraborty, S., Singh, A., Roy, S.S., and Arora, A. \"Neural Network-Based Gain "
          "Scheduled Position Control of a Pneumatic Artificial Muscle.\" IEEE CONECCT, 2022.")

heading(d, "Certifications & Awards")
bullet(d, "Best Research Paper Award, 9th IFToMM International Symposium on Robotics and Mechatronics (2026)")
bullet(d, "Certified SolidWorks Associate (CSWA) – Mechanical Design")
bullet(d, "Best Major Project Award, Department of Mechanical Engineering (2019)")
bullet(d, "TATA Technologies Innovation Award – INR 100,000 Grant (2019)")

heading(d, "Hands-On Projects")
bullet(d, "Led end-to-end design and fabrication of a custom Go-Kart.", "Go-Kart (2017): ")
bullet(d, "Worked in a multidisciplinary team to build a human-electric hybrid vehicle for the Efficycle "
          "competition.", "Efficycle (2018): ")

heading(d, "Technical Tools")
bullet(d, "SolidWorks, Autodesk Fusion 360, FEA, Bambu Lab and Ultimaker Cura (3D printing)", "CAD & Manufacturing: ")
bullet(d, "MATLAB/Simulink, Python, LabVIEW (basic), Arduino, LaTeX", "Software & Control: ")
bullet(d, "Qualisys Motion Capture, Forsentec Force/Torque Sensors, EMG, Pneumatic Control, Custom Rig Fabrication",
       "Instrumentation & Testing: ")
bullet(d, "Adobe Illustrator, Adobe Photoshop; Diploma in Fine Arts (Painting), Bangiya Sangeet Parishad",
       "Visual Communication: ")

heading(d, "Languages")
para(d, "English (C1, fluent) | Bengali (Native) | Hindi (Conversational)")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_Resume.docx")
to_pdf(d, OUT + "Arunabha_Majumder_Resume.pdf")

# ---------------- COVER LETTER ----------------
c = new_doc()
c.sections[0].top_margin = Cm(2.0)
header(c, TITLE, links=True)
para(c, "October 1, 2026", after=8)
para(c, "Application: Mechatronics & Robotics Engineer", bold=True, after=8)
para(c, "Dear Hiring Manager,", after=8)
body = [
 "I am a mechatronics and robotics engineer with a BTech in Mechanical Engineering and an MTech in Mechatronics, "
 "and I am finishing my PhD in Mechatronics and Robotics at Aalborg University. For more than five years I have "
 "worked hands-on with robotic and electromechanical systems, taking ideas from concept to tested hardware, and I "
 "am now looking to bring that experience to a robotics or mechatronics company in Denmark.",

 "In my PhD, I designed a hybrid-actuated shoulder exoskeleton that combines a parallel spring with a small 6 Nm "
 "motor. I created the mechanical design in SolidWorks, used FEA to iterate for stiffness, strength and weight, "
 "built the prototype from machined and 3D-printed parts, and integrated the motor, encoder, force sensors, DAQ and "
 "embedded control. The design cut energy consumption by more than 25% and won the Best Paper Award at IFToMM ISRM "
 "2026. I also implemented an Assist-as-Needed controller that reduced user muscle effort by more than 15%.",

 "I enjoy working where mechanics, sensing and control meet. On a 5-bar planar parallel robot, I estimated the "
 "end-effector force from variable-stiffness actuators through the robot's Jacobian, and validated the estimate "
 "against a force sensor to within 10% RMS error. During my Master's at CSIR-CMERI, I fabricated pneumatic "
 "artificial muscles and developed a neural-network-based controller that reduced tracking error to below 0.8%.",

 "I work in a structured way, from test planning to data analysis, and I communicate clearly with colleagues from "
 "different disciplines. I have planned and run a 12-participant validation study, taught and supervised "
 "Bachelor's students, and published peer-reviewed work. I am a Certified SolidWorks Associate and fluent in "
 "English.",

 "I would welcome the opportunity to discuss how I can contribute to your team. My portfolio and project website "
 "are linked above, and references are available upon request.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Cover_Letter.docx")
to_pdf(c, OUT + "Arunabha_Majumder_Cover_Letter.pdf", top=2.0)

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
TAG = "Anton_Robotics_Founding_Engineer"
TITLE = "Mechatronics & Robotics Engineer | Robotic Hardware | Pneumatics | Sensor Integration | Prototyping"

d = new_doc()
header(d, TITLE)

heading(d, "Professional Summary")
para(d, "Hands-on Mechatronics and Robotics Engineer with a B.Tech in Mechanical Engineering, an M.Tech in "
        "Mechatronics and a PhD in progress at Aalborg University. Designs, builds and tests robotic hardware end "
        "to end: CAD, 3D printing and machined parts, assembly, integration of sensors, actuators, pneumatics and "
        "control systems, and rapid iteration through physical testing. Took robotic systems from concept to "
        "working hardware, including a hybrid-actuated exoskeleton (Best Paper Award, IFToMM ISRM 2026) and "
        "in-house pneumatic actuators, and developed sensorless force estimation for a 5-bar parallel robot. Independent, pragmatic and solution-oriented, with a "
        "builder's mindset; fluent in English (C1).")

heading(d, "Core Skills")
bullet(d, "Robotic hardware, robotic mechanisms, parallel robots, actuator design, wearable robotics",
       "Robotics & Automation: ")
bullet(d, "Pneumatic actuators, valves, pressure sensors, pneumatic control", "Pneumatics: ")
bullet(d, "Motors, encoders, force/torque sensors, DAQ, embedded control, hardware-software co-design, control "
          "systems (PID, neural-network-based gain scheduling)", "Sensor & Control Integration: ")
bullet(d, "SolidWorks (CSWA certified), Fusion 360, 3D modelling, technical drawings, FEA, Design for Assembly (DFA)",
       "CAD & Design: ")
bullet(d, "3D printing (Bambu Lab, Ultimaker Cura), machined parts, hands-on fabrication, assembly in lab and "
          "workshop", "Manufacturing & Prototyping: ")
bullet(d, "Rapid prototyping, custom test rigs, physical testing, troubleshooting, data analysis (Python, MATLAB)",
       "Testing & Iteration: ")

heading(d, "Professional Experience")
role(d, "Research Engineer – Robotics & Actuator Development (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Designed, built and tested robotic hardware end to end: SolidWorks CAD and FEA, 3D-printed and machined "
          "parts, assembly, motor/encoder/force-sensor and DAQ integration, embedded control and custom automated "
          "test rigs.")
bullet(d, "Cut energy consumption of a shoulder exoskeleton by more than 25% by designing a hybrid actuation system "
          "that combines a parallel spring with a 6 Nm motor; awarded Best Paper, IFToMM ISRM 2026.")
bullet(d, "Removed the need for an external force/torque sensor in a 5-bar parallel robot by deriving a sensorless "
          "force-estimation method from the actuator torque–deflection characteristic, reducing cost, mass and "
          "integration complexity.")
bullet(d, "Deployed an Assist-as-Needed hybrid controller on functional prototype hardware, reducing user muscle "
          "effort by more than 15% in tests with human subjects.")
bullet(d, "Validated analytical stiffness models against physical hardware to below 10% RMS error, iterating "
          "designs through rapid prototyping and physical testing.")
bullet(d, "Ran a 12-participant hardware test campaign across 3 assistance modes and 2 load conditions, including "
          "instrumentation (EMG, camera-based motion capture) and the end-to-end data pipeline.")
bullet(d, "Taught university students and supervised Bachelor's (B.Tech) students (2023 – 2025).")

role(d, "M.Tech Researcher – Pneumatic Actuator Systems (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
bullet(d, "Fabricated pneumatic artificial muscle actuators in-house from raw materials and built the pneumatic "
          "test setup with valves, pressure sensors and DAQ.")
bullet(d, "Reduced position-tracking error to 0.3–0.78% by designing and implementing a neural-network-based "
          "gain-scheduled PID controller for a non-linear pneumatic actuator, outperforming classical PID under "
          "varying load.")

role(d, "Mechanical Engineering Capstone – Upper-Limb Rehabilitation Exoskeleton", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Led CAD design, fabrication and user testing of a robotic rehabilitation exoskeleton; won the Best Major "
          "Project Award and an INR 100,000 TATA Technologies Innovation Grant.")

heading(d, "Hands-On Build Projects")
bullet(d, "Led end-to-end design, fabrication and build of a custom Go-Kart from the ground up.", "Go-Kart (2017): ")
bullet(d, "Worked in a multidisciplinary team to design and build a human-electric hybrid vehicle for the "
          "Efficycle competition.", "Efficycle (2018): ")

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
bullet(d, "Python, MATLAB/Simulink, LabVIEW (basic), Arduino", "Software & Control: ")
bullet(d, "Qualisys Motion Capture, Forsentec Force/Torque Sensors, Pneumatic Control, Custom Rig Fabrication",
       "Instrumentation & Testing: ")

heading(d, "Languages")
para(d, "English (C1, fluent) | Bengali (Native) | Hindi (Conversational)")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_Resume_%s.docx" % TAG)
to_pdf(d, OUT + "Arunabha_Majumder_Resume_%s.pdf" % TAG)

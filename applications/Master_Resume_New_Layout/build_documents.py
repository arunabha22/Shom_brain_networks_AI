import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Master resume in the user's preferred layout, with all agreed factual corrections.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  •  "

d = new_doc()
para(d, NAME, bold=True, size=18, after=0)
para(d, "Mechanical & Robotics R&D Engineer — Actuator Development, Controls & Hardware Systems", bold=True,
     size=11, after=2)
para(d, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]),
     size=9.5, after=0)
para(d, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                  "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=6)

heading(d, "Professional Summary")
para(d, "Mechatronics and Mechanical R&D Engineer with practical experience in product development, designing, "
        "prototyping and testing dynamic electromechanical systems, variable-stiffness actuators and robotic "
        "mechanisms. Proven ability to bridge CAD modelling, kinematic analysis, control implementation and sensor "
        "integration into functional hardware solutions.")

heading(d, "Work Experience")
role(d, "Research Engineer — Robotics & Actuator Development (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Cut shoulder exoskeleton energy consumption by more than 25% by designing a hybrid actuation architecture "
          "that coordinates a parallel spring with a 6 Nm motor, offloading quasi-static gravity torque across the "
          "assistance cycle; won the Best Paper Award, IFToMM ISRM 2026.")
bullet(d, "Reduced user anterior deltoid muscle effort by more than 15% by deploying an Assist-as-Needed (AAN) hybrid "
          "controller on functional prototype hardware, tested with human participants.")
bullet(d, "Developed a sensorless end-effector force-estimation method for a 5-bar planar parallel robot using "
          "variable-stiffness actuators (VSA) and the robot Jacobian, validated against a force sensor to below 10% "
          "RMS error, and used it to measure human arm impedance in the gait lab.")
bullet(d, "Conducted data collection for a 12-participant study across 3 assistance modes and 2 load conditions, "
          "using EMG and motion-capture instrumentation.")
bullet(d, "Built the full prototype stack from concept to tested hardware: SolidWorks CAD and FEA, mechanical "
          "fabrication, motor, encoder, force-sensor and DAQ integration, embedded control and custom automated test "
          "rigs.")
bullet(d, "Taught university students and supervised Bachelor's (B.Tech) students (2023 – 2025).")

role(d, "M.Tech Researcher — Actuator Systems (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI — National Laboratory, Govt. of India), "
     "Durgapur, India")
bullet(d, "Reduced dynamic position-tracking error to 0.3–0.78% by designing and implementing a neural-network-based "
          "gain-scheduled PID controller for a highly non-linear pneumatic actuator, outperforming the classical PID "
          "baseline under varying axial load.")
bullet(d, "Fabricated pneumatic artificial muscle actuators in-house from raw materials and built the test set-up "
          "with valves, pressure sensors and DAQ to characterise load–displacement behaviour and derive an empirical "
          "actuator model.")

heading(d, "Education")
role(d, "Ph.D. Candidate, Mechatronics & Robotics", "2023 – Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
role(d, "M.Tech, Mechatronics", "2020 – 2022",
     "AcSIR – CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
role(d, "B.Tech, Mechanical Engineering", "2015 – 2019",
     "Siddaganga Institute of Technology, Visvesvaraya Technological University (VTU), Tumakuru, India")

heading(d, "Skills & Interests")
bullet(d, "Mechanical Product Development, Actuator & Robotic Mechanisms, CAD, FEA, Design for Assembly (DFA), "
          "3D Printing", "Design & Modelling: ")
bullet(d, "Compliant Actuation, Kinematics, Jacobian-Based Force Estimation, Control Systems, Automation, Pneumatic "
          "Control", "Robotics & Controls: ")
bullet(d, "Prototype Fabrication, Sensor Integration, Custom Test-Rig Development, Data Collection, Qualisys Motion "
          "Capture, EMG, Forsentec Force/Torque Sensors", "Testing & Hardware: ")
bullet(d, "SolidWorks, Fusion 360, Ultimaker Cura, MATLAB/Simulink, Python, LabVIEW (basic), Arduino, LaTeX, Adobe "
          "Illustrator, Adobe Photoshop, Procreate (basic)", "Software & Programming: ")
bullet(d, "English (CEFR: C1), Bengali (Native), Hindi (oral proficiency)", "Languages: ")
bullet(d, "Engineering Design & Prototyping, Visual Arts & Illustration", "Interests: ")

heading(d, "Projects")
role(d, "Rehabilitation Robotics (Bachelor's Capstone)", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Delivered an award-winning upper-limb rehabilitation exoskeleton that secured the Best Major Project Award "
          "and an INR 100,000 TATA Technologies Innovation Grant, leading CAD design, fabrication and user testing end "
          "to end. Video: youtube.com/watch?v=q5Ystz9NCpQ")
role(d, "Engineering Design & Prototyping (Extracurricular)", "2017 – 2018", "Siddaganga Institute of Technology")
bullet(d, "Led end-to-end development of a custom-fabricated Go-Kart from the ground up (2017).")
bullet(d, "Collaborated in a multidisciplinary team to engineer an eco-friendly human-electric hybrid vehicle for the "
          "Efficycle competition (2018).")

heading(d, "Certifications")
bullet(d, "Certified SolidWorks Associate (CSWA) — Mechanical Design")

heading(d, "Achievements")
bullet(d, "Best Research Paper Award, 9th IFToMM International Symposium on Robotics and Mechatronics — awarded for "
          "hybrid-actuated exoskeleton design (2026)")
bullet(d, "Best Major Project Award, Department of Mechanical Engineering (2019)")
bullet(d, "TATA Technologies Innovation Award — INR 100,000 Grant (2019)")

heading(d, "Publications")
bullet(d, "Majumder, A., Wagner, J.W., Zhu, Y., Oliveira, A.S., and Bai, S. \"A Hybrid Actuated Shoulder Exoskeleton "
          "for Energy-Efficient Upper Arm Support.\" Robotics and Mechatronics: ISRM 2026, MMS, vol. 213, Springer, "
          "2026.")
bullet(d, "Majumder, A., Sarkar, D., Chakraborty, S., Singh, A., Roy, S.S., and Arora, A. \"Neural Network-Based Gain "
          "Scheduled Position Control of a Pneumatic Artificial Muscle.\" IEEE CONECCT, 2022.")

heading(d, "Visual Arts & Illustration")
bullet(d, "Professionally trained visual artist holding a Diploma in Fine Arts (Painting) from Bangiya Sangeet "
          "Parishad.")
bullet(d, "Use sketching, painting and graphic design skills to create illustrations and technical visuals.")

heading(d, "References")
para(d, "Available upon request.")

d.save(OUT + "Arunabha_Majumder_Resume.docx")
to_pdf(d, OUT + "Arunabha_Majumder_Resume.pdf")

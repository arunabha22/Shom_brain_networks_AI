import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Optimised master CV: XYZ bullets, key results up front, focused skills, academic extras condensed.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  •  "

d = new_doc()
para(d, NAME, bold=True, size=18, after=0)
para(d, "Mechanical Design & Robotics R&D Engineer — Actuators, Controls & Hardware Systems", bold=True,
     size=11, after=2)
para(d, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]),
     size=9.5, after=0)
para(d, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                  "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=6)

heading(d, "Summary")
para(d, "Mechanical design engineer who takes electromechanical systems from concept to tested hardware. Designed "
        "an actuated exoskeleton that cut energy use by more than 25% (Best Paper Award, 2026) and developed a "
        "force-estimation method accurate to below 10% error. Hands-on with SolidWorks, FEA, prototyping, sensors "
        "and control.")

heading(d, "Key Results")
bullet(d, " energy reduction from a hybrid actuation design (Best Paper Award, IFToMM ISRM 2026)", ">25%")
bullet(d, " RMS error on sensorless force estimation, validated against a force sensor", "<10%")
bullet(d, " tracking error on a pneumatic actuator with a neural-network-based controller", "0.3–0.78%")

heading(d, "Experience")
role(d, "Research Engineer – Mechanical Design & Actuator Development (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Cut energy consumption by more than 25% in prototype testing of an actuated shoulder exoskeleton by taking "
          "technical ownership of the concept, mechanical architecture and design decisions for a hybrid actuation "
          "system that pairs a parallel spring with a 6 Nm motor (Best Paper Award, IFToMM ISRM 2026).")
bullet(d, "Delivered a working prototype from concept to tested hardware by designing the structure and assemblies in "
          "SolidWorks, using structural FEA to balance strength, stiffness and weight, choosing between machined and "
          "3D-printed parts for manufacturability, and integrating the motor, encoder, force sensors and DAQ.")
bullet(d, "Achieved force estimation accurate to below 10% RMS error, validated against a force sensor, by developing "
          "a sensorless method for a 5-bar planar parallel robot using variable-stiffness actuators and the robot "
          "Jacobian; applied the method to measure human arm impedance in the gait lab.")
bullet(d, "Reduced user muscle effort by more than 15%, measured with EMG in tests with participants, by implementing "
          "an Assist-as-Needed controller on the prototype.")
bullet(d, "Collected a full EMG and motion-capture dataset from a 12-participant study across 3 assistance modes and "
          "2 load conditions, by running the data collection within a multidisciplinary team spanning mechanical, "
          "electronics, control and biomechanics.")
bullet(d, "Mentored and supervised Bachelor's (B.Tech) students on engineering projects (2023 – 2025) by guiding their "
          "design work, and taught university students.")

role(d, "MTech Researcher – Pneumatic Actuator Systems (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Reduced position-tracking error to 0.3–0.78%, outperforming classical PID under varying load, by designing "
          "a neural-network-based gain-scheduled PID controller for a non-linear pneumatic actuator.")
bullet(d, "Built an empirical actuator model from test data by fabricating pneumatic artificial muscles in-house and "
          "setting up a test rig with valves, pressure sensors and DAQ.")

heading(d, "Education")
role(d, "Ph.D. Candidate, Mechatronics & Robotics", "2023 – Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
role(d, "M.Tech, Mechatronics", "2020 – 2022",
     "AcSIR – CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
role(d, "B.Tech, Mechanical Engineering", "2015 – 2019",
     "Siddaganga Institute of Technology, Visvesvaraya Technological University (VTU), Tumakuru, India")

heading(d, "Awards & Certification")
bullet(d, "Best Research Paper Award, 9th IFToMM International Symposium on Robotics and Mechatronics (2026)")
bullet(d, "Certified SolidWorks Associate (CSWA) – Mechanical Design")
bullet(d, "TATA Technologies Innovation Grant – INR 100,000 (2019); Best Major Project Award (2019)")

heading(d, "Skills")
bullet(d, "SolidWorks (CSWA), Fusion 360, structural FEA, assemblies, technical drawings, DFA, manufacturability",
       "Mechanical Design: ")
bullet(d, "Machining, 3D printing, assembly, test rigs, DAQ, data collection", "Prototyping & Testing: ")
bullet(d, "Motors, encoders, force sensors, pneumatics, embedded control, MATLAB/Simulink, Python",
       "Mechatronics & Control: ")
bullet(d, "Qualisys motion capture, EMG, Forsentec force/torque sensors, LabVIEW (basic), Arduino",
       "Instrumentation: ")

heading(d, "Publications")
bullet(d, "Majumder, A., et al. \"A Hybrid Actuated Shoulder Exoskeleton for Energy-Efficient Upper Arm Support.\" "
          "ISRM 2026, Springer.")
bullet(d, "Majumder, A., et al. \"Neural Network-Based Gain Scheduled Position Control of a Pneumatic Artificial "
          "Muscle.\" IEEE CONECCT, 2022.")

heading(d, "Additional")
bullet(d, "Rehabilitation exoskeleton (Best Major Project Award, 2019; video: youtube.com/watch?v=q5Ystz9NCpQ), "
          "Go-Kart (2017), Efficycle human-electric hybrid vehicle (2018)", "Hands-on builds: ")
bullet(d, "Diploma in Fine Arts (Painting), Bangiya Sangeet Parishad; used for technical sketching and illustration",
       "Visual skills: ")
bullet(d, "English (C1, fluent), Bengali (Native), Hindi (Conversational)", "Languages: ")

heading(d, "References")
para(d, "Available upon request.")

d.save(OUT + "Arunabha_Majumder_CV.docx")
to_pdf(d, OUT + "Arunabha_Majumder_CV.pdf")

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
TAG = "Eaton_Mechanical_Design_Engineer"

# ---------------- RESUME ----------------
d = new_doc()
header(d, "Mechanical Design Engineer | 3D CAD | Prototyping | Electromechanical Systems")

heading(d, "Professional Summary")
para(d, "Mechanical Design Engineer with a B.Tech in Mechanical Engineering, an M.Tech in Mechatronics and about "
        "three years of hands-on R&D design experience at Aalborg University. Designs, documents, prototypes and "
        "tests electromechanical products in 3D CAD (SolidWorks, Fusion 360), using FEA to iterate on stiffness, "
        "strength and weight before fabrication. Builds prototypes hands-on from machined and additively "
        "manufactured parts, integrates motors, sensors and DAQ, and analyses test data to solve design issues. "
        "Certified SolidWorks Associate (CSWA), fluent in English (C1) and experienced in R&D project teams in "
        "Denmark and India.")

heading(d, "Core Skills")
bullet(d, "SolidWorks (CSWA certified), Fusion 360, 3D modelling, engineering drawings, Finite Element Analysis "
          "(FEA), MATLAB/Simulink", "3D CAD & Simulation: ")
bullet(d, "Mechanical Design, R&D Product Development, Design for Assembly (DFA), System Cost and Part-Count "
          "Reduction, Machined Parts, Additive Manufacturing / 3D Printing", "Mechanical Design: ")
bullet(d, "Specifying and building prototypes hands-on, Assembly, Custom Test Rigs, Experimental Validation, "
          "Root-Cause Analysis of Test Results", "Prototyping & Testing: ")
bullet(d, "Motor, Encoder, Force-Sensor and DAQ Integration, Embedded Control, Pneumatic Systems, Actuator Design",
       "Electromechanical Systems: ")
bullet(d, "English (C1, fluent written and spoken), technical writing (peer-reviewed publications), R&D project "
          "teamwork", "Communication: ")

heading(d, "Professional Experience")
role(d, "Research Engineer – Mechanical Design & Actuator Development (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Designed, documented and built a wearable electromechanical device from concept to tested hardware: "
          "SolidWorks 3D models and drawings, FEA-driven design iterations, machined and 3D-printed parts, "
          "hands-on assembly and custom automated test rigs.")
bullet(d, "Integrated motor, encoder, force sensors and DAQ with embedded control into the functional prototype.")
bullet(d, "Cut energy consumption by more than 25% by designing a hybrid actuation architecture that combines a "
          "parallel spring with a 6 Nm motor to offload gravity torque; awarded Best Paper, IFToMM ISRM 2026.")
bullet(d, "Reduced system cost, mass and integration complexity of a 5-bar parallel robot by removing the external "
          "force/torque sensor, using a sensorless force-estimation method derived from the actuator "
          "torque–deflection characteristic.")
bullet(d, "Validated analytical stiffness models against physical tests to below 10% RMS error, de-risking the "
          "mechanism before fabrication.")
bullet(d, "Planned and ran a 12-participant validation study across 3 assistance modes and 2 load conditions, "
          "including instrumentation (EMG, motion capture), ethics protocol and data analysis; results support "
          "two journal submissions.")

role(d, "M.Tech Researcher – Actuator Systems (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
bullet(d, "Fabricated pneumatic artificial muscle actuators in-house and integrated valves, pressure sensors and DAQ "
          "to characterise load–displacement behaviour and derive an empirical actuator model.")
bullet(d, "Reduced dynamic position-tracking error to 0.3–0.78% with a neural-network-based gain-scheduled PID "
          "controller for a non-linear pneumatic actuator, outperforming the classical PID baseline under varying "
          "axial load.")

role(d, "Mechanical Engineering Capstone – Upper-Limb Rehabilitation Exoskeleton", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Led CAD design, fabrication and user testing of an upper-limb rehabilitation exoskeleton; won the Best "
          "Major Project Award and an INR 100,000 TATA Technologies Innovation Grant.")

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
          "for Energy-Efficient Upper Arm Support.\" Robotics and Mechatronics: ISRM 2026, MMS, vol. 213, Springer. "
          "(Best Research Paper Award)")
bullet(d, "Majumder, A., Sarkar, D., Chakraborty, S., Singh, A., Roy, S.S., and Arora, A. \"Neural Network-Based Gain "
          "Scheduled Position Control of a Pneumatic Artificial Muscle.\" IEEE CONECCT, 2022.")

heading(d, "Technical Tools")
bullet(d, "SolidWorks, Fusion 360, FEA, Bambu Lab and Ultimaker Cura (3D printing)", "CAD & Manufacturing: ")
bullet(d, "MATLAB/Simulink, Python, LabVIEW (basic), Arduino, LaTeX", "Software & Programming: ")
bullet(d, "Qualisys Motion Capture, Forsentec Force/Torque Sensors, Pneumatic Control, Custom Rig Fabrication",
       "Instrumentation & Testing: ")

heading(d, "Languages")
para(d, "English (C1, fluent) | Bengali (Native) | Hindi (Conversational)")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_Resume_%s.docx" % TAG)
to_pdf(d, OUT + "Arunabha_Majumder_Resume_%s.pdf" % TAG)

# ---------------- COVER LETTER ----------------
c = new_doc()
c.sections[0].top_margin = Cm(2.0)
header(c, "Mechanical Design Engineer | 3D CAD | Prototyping | Electromechanical Systems")
para(c, "September 27, 2026", after=8)
para(c, "Hiring Team, R&D Mechanical Design", after=0)
para(c, "Eaton", after=8)
para(c, "Application: Mechanical Design Engineer – UPS Systems", bold=True, after=8)
para(c, "Dear Hiring Team,", after=8)
body = [
 "I am applying for the Mechanical Design Engineer position working on UPS systems and accessories. I hold a "
 "B.Tech in Mechanical Engineering and an M.Tech in Mechatronics, and I am finishing my PhD in Mechatronics and "
 "Robotics at Aalborg University. For the past three years I have designed, documented, built and tested "
 "electromechanical products in R&D, and I want to bring that experience to power management products at Eaton.",

 "In my PhD, I designed a hybrid-actuated wearable device from concept to tested hardware. I created the "
 "SolidWorks 3D models and drawings, iterated the design on FEA results for stiffness, strength and weight, and "
 "built the prototypes hands-on from machined and additively manufactured parts. I integrated the motor, encoder, "
 "force sensors and DAQ, and built custom test rigs to validate the design. The hybrid actuation cut energy "
 "consumption by more than 25% and won the Best Paper Award at IFToMM ISRM 2026.",

 "I enjoy analysing and solving product issues, and I keep cost in mind while doing it. On a 5-bar parallel robot, "
 "I removed an external force/torque sensor by estimating force from the actuator itself, which reduced system "
 "cost, mass and integration complexity. I also validated my analytical stiffness models against physical tests "
 "to within 10% RMS error before committing to fabrication.",

 "I work well in R&D project teams. My projects combine mechanical design, electronics, controls and human "
 "testing, and I have worked in research environments in both India and Denmark with English as my working "
 "language. I am a Certified SolidWorks Associate and have published my work in peer-reviewed venues.",

 "My hands-on manufacturing experience so far is mainly with machined and additively manufactured parts. Sheet "
 "metal, die-cast and injection-moulded design, together with DFSS tools, is where I want to grow next, and "
 "Eaton's UPS R&D team is the right place to do it.",

 "I would welcome the opportunity to discuss how I can contribute to your team. References are available upon "
 "request.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Cover_Letter_%s.docx" % TAG)
to_pdf(c, OUT + "Arunabha_Majumder_Cover_Letter_%s.pdf" % TAG, top=2.0)

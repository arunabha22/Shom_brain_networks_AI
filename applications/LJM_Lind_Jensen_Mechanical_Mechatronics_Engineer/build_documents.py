import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
TAG = "LJM_Mechanical_Mechatronics_Engineer"
TITLE = "Mechanical / Mechatronics Engineer | Machine Design | FEA | Prototyping & Testing | Control Integration"

# ---------------- RESUME ----------------
d = new_doc()
header(d, TITLE, links=True)

heading(d, "Professional Summary")
para(d, "Mechanical and Mechatronics Engineer with a master's degree (MTech) in Mechatronics, a BTech in Mechanical "
        "Engineering and a PhD in progress at Aalborg University, with about three years of hands-on product "
        "development in Denmark. Develops and evaluates machine concepts and operating principles, and turns "
        "technical requirements into working hardware: 3D models, assemblies and production drawings in "
        "SolidWorks, component-level FEA for strength, stiffness and weight, prototype builds, and systematically "
        "planned, analysed and documented tests. Understands the interaction between mechanics, sensors, control "
        "and software, having specified and implemented the control principles for self-built prototypes. Certified "
        "SolidWorks Associate (CSWA); Best Paper Award, IFToMM ISRM 2026.")

heading(d, "Core Skills")
bullet(d, "Machine concepts and operating principles, mechanism and actuator design, 3D models, assemblies, "
          "production drawings, SolidWorks (CSWA certified), Fusion 360", "Machine Design & 3D CAD: ")
bullet(d, "Specifying and performing component-level Finite Element Analysis (FEA), analytical stiffness and "
          "kinematic modelling, optimising designs for strength, stiffness, weight and assembly (DFA)",
       "FEA & Design Optimisation: ")
bullet(d, "Building prototypes, designing test rigs, planning, conducting, analysing and documenting tests, "
          "verification against models", "Prototyping & Testing: ")
bullet(d, "Control principles and sequences, motor, encoder and force-sensor integration, DAQ, embedded control, "
          "pneumatics, PID and model-based control, MATLAB/Simulink, Python", "Mechanics, Automation & Software: ")
bullet(d, "Translating requirements into designs, systematic documentation, project planning, multidisciplinary "
          "collaboration, English (C1)", "Ways of Working: ")

heading(d, "Professional Experience")
role(d, "Research Engineer – Mechanical & Mechatronic Product Development (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Developed and evaluated a new operating principle for a shoulder exoskeleton: a hybrid actuation concept "
          "that pairs a parallel spring with a 6 Nm motor, cutting energy consumption by more than 25% (Best Paper "
          "Award, IFToMM ISRM 2026).")
bullet(d, "Created 3D models, assemblies and production drawings in SolidWorks, and performed component-level FEA to "
          "optimise for strength, stiffness and weight before manufacture.")
bullet(d, "Built prototypes hands-on from machined and additively manufactured parts and integrated motor, encoder, "
          "force sensors, DAQ and embedded control.")
bullet(d, "Specified and implemented control principles, including an Assist-as-Needed hybrid controller that "
          "reduced user muscle effort by more than 15% in tests.")
bullet(d, "Planned, conducted, analysed and documented a 12-participant test campaign across 3 operating modes and "
          "2 load conditions, including test protocol, instrumentation and data pipeline; results support two "
          "journal submissions.")
bullet(d, "Developed end-effector force estimation for a 5-bar planar parallel robot using variable-stiffness "
          "actuators (VSA) and the robot Jacobian, validated against a force sensor to below 10% RMS error.")
bullet(d, "Taught university students and supervised Bachelor's (B.Tech) students (2023 – 2025).")

role(d, "MTech Researcher – Pneumatic Actuator Systems (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Fabricated pneumatic artificial muscle actuators in-house and built the test set-up with valves, "
          "pressure sensors and DAQ to characterise load–displacement behaviour and derive an empirical model.")
bullet(d, "Designed and implemented a neural-network-based gain-scheduled PID controller that reduced position-"
          "tracking error to 0.3–0.78% under varying load, outperforming classical PID.")

role(d, "Mechanical Engineering Capstone – Upper-Limb Rehabilitation Exoskeleton", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Led CAD design, fabrication and user testing end to end; won the Best Major Project Award and an INR "
          "100,000 TATA Technologies Innovation Grant.")

heading(d, "Education")
role(d, "Ph.D. Candidate, Mechatronics & Robotics", "2023 – Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
role(d, "MTech (Master's), Mechatronics", "2020 – 2022",
     "AcSIR – CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
role(d, "BTech, Mechanical Engineering", "2015 – 2019",
     "Siddaganga Institute of Technology, Visvesvaraya Technological University (VTU), Tumakuru, India")

heading(d, "Certifications & Awards")
bullet(d, "Certified SolidWorks Associate (CSWA) – Mechanical Design")
bullet(d, "Best Research Paper Award, 9th IFToMM International Symposium on Robotics and Mechatronics (2026)")
bullet(d, "TATA Technologies Innovation Award – INR 100,000 Grant (2019); Best Major Project Award (2019)")

heading(d, "Engineering Projects")
bullet(d, "Designed, fabricated and assembled a custom Go-Kart from the ground up.", "Go-Kart (2017): ")
bullet(d, "Designed and built a human-electric hybrid vehicle in a multidisciplinary team for the Efficycle "
          "competition.", "Efficycle (2018): ")

heading(d, "Publications")
bullet(d, "Majumder, A., et al. \"A Hybrid Actuated Shoulder Exoskeleton for Energy-Efficient Upper Arm Support.\" "
          "ISRM 2026, MMS, vol. 213, Springer.")
bullet(d, "Majumder, A., et al. \"Neural Network-Based Gain Scheduled Position Control of a Pneumatic Artificial "
          "Muscle.\" IEEE CONECCT, 2022.")

heading(d, "Technical Tools")
bullet(d, "SolidWorks, Fusion 360, FEA, Bambu Lab and Ultimaker Cura (3D printing)", "CAD & Manufacturing: ")
bullet(d, "MATLAB/Simulink, Python, LabVIEW (basic), Arduino", "Software & Control: ")
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
header(c, TITLE, links=True)
para(c, "September 29, 2026", after=8)
para(c, "Design Department", after=0)
para(c, "LJM Lind Jensen, a JKS company", after=0)
para(c, "Højmark, Denmark", after=8)
para(c, "Application: Mechanical/Mechatronics Engineer – Design Department", bold=True, after=8)
para(c, "Dear Hiring Team,", after=8)
body = [
 "I am applying for the Mechanical/Mechatronics Engineer position in your Design department. I hold a master's "
 "degree in Mechatronics and a BTech in Mechanical Engineering, and I am finishing my PhD at Aalborg University. "
 "For the past three years I have taken mechanical concepts from idea and calculation to tested hardware, and I "
 "would like to do that for products that go into production.",

 "In my PhD, I developed a new hybrid actuation principle for a shoulder exoskeleton: a parallel spring working "
 "together with a small 6 Nm motor. I created the 3D models, assemblies and drawings in SolidWorks, used component-level "
 "FEA to optimise for strength, stiffness and weight, built the prototypes hands-on and integrated the motor, "
 "sensors and control. The concept cut energy consumption by more than 25% and won the Best Paper Award at IFToMM "
 "ISRM 2026. You can see the project at www.viexo.aau.dk.",

 "I work systematically with testing and documentation. On a 5-bar planar parallel robot, I used the "
 "variable-stiffness actuators to estimate the force at the end effector through the robot's Jacobian, and "
 "validated the estimate against a force sensor to within 10% RMS error. I also design my own test rigs, and I "
 "planned, ran, analysed and documented a 12-participant test campaign across several operating modes and load "
 "conditions.",

 "I also understand how mechanics, automation and software work together, because I have specified and "
 "implemented the control principles for my own machines. At CSIR-CMERI I built a pneumatic actuator test set-up "
 "and developed a controller that reduced tracking error to below 0.8%, and at Aalborg I implemented an "
 "Assist-as-Needed controller on the prototype. I also speak Hindi and Bengali, which may be useful with your "
 "colleagues in India.",

 "I have not yet worked formally with DFMEA, APQP or machine safety standards in an industrial setting. These are "
 "the areas I want to build next, and LJM's close link between design, assembly and testing is the right place "
 "to learn them.",

 "I would welcome the opportunity to discuss how I can contribute to your team. References are available upon "
 "request.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Cover_Letter_%s.docx" % TAG)
to_pdf(c, OUT + "Arunabha_Majumder_Cover_Letter_%s.pdf" % TAG, top=2.0)

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
TAG = "Rivan_Mechanical_Engineer"
TITLE = "Mechanical Engineer | Sub-System Design & Ownership | Test Rigs | SolidWorks | Fabrication"

# ---------------- RESUME ----------------
d = new_doc()
header(d, TITLE)

heading(d, "Professional Summary")
para(d, "Mechanical Engineer with a B.Tech in Mechanical Engineering, an M.Tech in Mechatronics and about three "
        "years of professional R&D experience owning an electromechanical sub-system end to end: concept "
        "generation, architecture and requirements, SolidWorks CAD and drawings, hands-on workshop fabrication, "
        "assembly, integration, commissioning and testing. Designs test rigs to validate hypotheses quickly, builds "
        "analytical models in Python and MATLAB, and uses FEA before committing to fabrication. Reasons from first "
        "principles and questions every part: removed a force/torque sensor from a robot design, cutting cost, "
        "mass and part count. Certified SolidWorks Associate (CSWA); Best Paper Award, IFToMM ISRM 2026.")

heading(d, "Core Skills")
bullet(d, "Concept generation, system architecture, technical requirements, sub-system ownership, integration",
       "System Design: ")
bullet(d, "SolidWorks (CSWA certified), Fusion 360, design drawings, Design for Manufacture and Assembly "
          "(DFM/DFA), cost and part-count reduction", "CAD & Design: ")
bullet(d, "Hands-on workshop fabrication and build, machined parts, additive manufacturing / 3D printing, "
          "assembly, commissioning", "Fabrication & Build: ")
bullet(d, "Test-rig design, test planning, running experiments, data acquisition (DAQ), data analysis",
       "Testing: ")
bullet(d, "Analytical modelling, Python, MATLAB/Simulink, Finite Element Analysis (FEA), stiffness and "
          "kinematic models validated against experiments", "Simulation & Modelling: ")
bullet(d, "Pneumatic systems (valves, pressure sensors), motors, encoders, force sensors, embedded control",
       "Electromechanical: ")

heading(d, "Professional Experience")
role(d, "Research Engineer – Mechanical Sub-System Design & Development (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Owned an actuated wearable sub-system end to end: concept generation, architecture and technical "
          "requirements, SolidWorks CAD and drawings, fabrication, assembly, integration, commissioning and test.")
bullet(d, "Re-thought the actuation architecture from first principles, pairing a parallel spring with a 6 Nm motor "
          "to offload gravity torque; cut energy consumption by more than 25% (Best Paper Award, IFToMM ISRM "
          "2026).")
bullet(d, "Questioned the need for an external force/torque sensor in a 5-bar parallel robot and replaced it with "
          "force estimation from the actuator's torque–deflection characteristic, reducing cost, mass, part count "
          "and integration complexity.")
bullet(d, "Designed custom automated test rigs to validate hypotheses before fabrication; analytical stiffness "
          "models matched experimental hardware to below 10% RMS error.")
bullet(d, "Built prototypes hands-on from machined and additively manufactured parts and integrated motor, "
          "encoder, force sensors, DAQ and embedded control.")
bullet(d, "Wrote and executed test plans, including a 12-participant study across 3 assistance modes and 2 load "
          "conditions, with an end-to-end data acquisition and analysis pipeline.")
bullet(d, "Taught university students and supervised Bachelor's (B.Tech) students (2023 – 2025).")

role(d, "M.Tech Researcher – Pneumatic Actuator Systems (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
bullet(d, "Fabricated pneumatic artificial muscle actuators in-house from raw materials and built the test setup "
          "with valves, pressure sensors and DAQ to characterise load–displacement behaviour.")
bullet(d, "Derived an empirical actuator model from test data and designed a neural-network-based gain-scheduled "
          "PID controller, reducing position-tracking error to 0.3–0.78%.")

role(d, "Mechanical Engineering Capstone – Upper-Limb Rehabilitation Exoskeleton", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Led CAD design, fabrication and user testing end to end; won the Best Major Project Award and an INR "
          "100,000 TATA Technologies Innovation Grant.")

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
para(c, "Hiring Team, Engineering", after=0)
para(c, "Rivan Industries", after=0)
para(c, "Bermondsey, London, United Kingdom", after=8)
para(c, "Application: Mechanical Engineer – Sub-System Owner", bold=True, after=8)
para(c, "Dear Rivan Team,", after=8)
body = [
 "I am applying for the Mechanical Engineer role. I hold a B.Tech in Mechanical Engineering and an M.Tech in "
 "Mechatronics, and I am finishing my PhD at Aalborg University, where for the past three years I have owned an "
 "electromechanical sub-system from concept to tested hardware. Owning a system end to end, and rethinking it "
 "from first principles, is exactly how I like to work.",

 "In my PhD, I owned the concept, architecture and requirements of the actuation system for a wearable robot. I "
 "produced the SolidWorks models and drawings, built the parts hands-on through machining and additive "
 "manufacturing, and handled assembly, integration, commissioning and testing. Rethinking the actuation "
 "architecture, by pairing a parallel spring with a small 6 Nm motor, cut energy consumption by more than 25% and "
 "won the Best Paper Award at IFToMM ISRM 2026.",

 "I question every part's existence. On a 5-bar parallel robot, I removed the external force/torque sensor "
 "entirely by estimating force from the actuator itself, which reduced cost, mass, part count and integration "
 "complexity. I design test rigs to check hypotheses quickly before committing to fabrication, and I "
 "validated my analytical stiffness models against hardware to within 10% RMS error.",

 "I am comfortable in the workshop. During my Master's at CSIR-CMERI, I fabricated pneumatic artificial muscles "
 "from raw materials and built the test setup with valves, pressure sensors and DAQ. Before that, I led the "
 "design and build of a Go-Kart from the ground up. I model in Python and MATLAB and use FEA to guide design "
 "decisions.",

 "My thermofluids experience so far comes from pneumatic actuators rather than heat and mass transfer systems, "
 "and vendor management and procurement for a production line are new to me. These are the areas I want to grow "
 "into, and Rivan's mission to make synthetic fuel cheaper than fossil fuels is the kind of problem I want to "
 "work on.",

 "I would welcome the opportunity to discuss how I can contribute to Rivan. References are available upon "
 "request.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Cover_Letter_%s.docx" % TAG)
to_pdf(c, OUT + "Arunabha_Majumder_Cover_Letter_%s.pdf" % TAG, top=2.0)

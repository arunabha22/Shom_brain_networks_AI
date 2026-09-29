import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
TAG = "GE_Aerospace_Mechanical_Design_Engineer"
TITLE = "Mechanical Design Engineer | Mechatronic Systems | Electromechanical Integration | Prototyping & Testing"

# ---------------- RESUME ----------------
d = new_doc()
header(d, TITLE, links=True)

heading(d, "Profile")
para(d, "Mechanical Design Engineer with a BTech in Mechanical Engineering, an MTech in Mechatronics and a PhD in "
        "progress, with about three years of hands-on mechatronic product development in an R&D environment. "
        "Designs mechanical components and assemblies using a range of manufacturing techniques, and works across "
        "the engineering lifecycle from requirements and concept development through detailed design, "
        "prototyping, testing, validation and verification. Integrates sensors, actuators, motors, encoders, data "
        "acquisition and embedded control into electromechanical systems, and designs the control strategies that "
        "run them. Comfortable challenging established approaches, working across mechanical, electrical, "
        "electronic and software boundaries, and building prototypes hands-on in the workshop. Certified "
        "SolidWorks Associate (CSWA); Best Paper Award, IFToMM ISRM 2026.")

heading(d, "Key Skills")
bullet(d, "Mechanical component and assembly design, product design, Design for Manufacture and Assembly "
          "(DfM/DfA), machined and additively manufactured parts", "Mechanical Design: ")
bullet(d, "SolidWorks (CSWA certified), Autodesk Fusion 360, detailed 3D models and drawings, Finite Element "
          "Analysis (FEA)", "3D CAD & Analysis: ")
bullet(d, "Electromechanical system development, electronics integration, sensors, actuators, motors, encoders, "
          "force sensors, data acquisition (DAQ), embedded hardware (Arduino), pneumatics",
       "Mechatronic Systems: ")
bullet(d, "Control system design (PID, neural-network gain scheduling, Assist-as-Needed control), kinematics and "
          "Jacobian-based force estimation, MATLAB/Simulink, Python", "Control & Modelling: ")
bullet(d, "Requirements definition, concept development, detailed design, prototyping, testing, validation and "
          "verification", "Engineering Lifecycle: ")
bullet(d, "Workshop fabrication, prototype build and assembly, custom test rigs, test planning and data analysis",
       "Prototyping & Test: ")
bullet(d, "Multidisciplinary collaboration, system-level trade-offs across mechanical and electrical domains, "
          "written and verbal communication (peer-reviewed publications, teaching)", "Collaboration: ")

heading(d, "Professional Experience")
role(d, "Research Engineer – Mechatronic Product Development (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Designed and developed a hybrid-actuated shoulder exoskeleton from concept to tested hardware, "
          "challenging the conventional motor-only approach by combining a parallel spring with a 6 Nm motor; cut "
          "energy consumption by more than 25% (Best Paper Award, IFToMM ISRM 2026).")
bullet(d, "Designed mechanical components and assemblies in SolidWorks, performed FEA for strength, stiffness and "
          "weight, and produced parts through machining and additive manufacturing.")
bullet(d, "Integrated motor, encoder, force sensors, DAQ and embedded control into the electromechanical system, "
          "balancing mechanical and electrical trade-offs at system level.")
bullet(d, "Developed end-effector force estimation for a 5-bar planar parallel robot using variable-stiffness "
          "actuators (VSA) and the robot Jacobian, validated against a force sensor to below 10% RMS error.")
bullet(d, "Designed and deployed an Assist-as-Needed hybrid controller on the prototype, reducing user muscle "
          "effort by more than 15% in human-subject tests.")
bullet(d, "Built prototypes hands-on and designed custom automated test rigs; planned and ran a 12-participant "
          "validation campaign across 3 operating modes and 2 load conditions, including instrumentation and data "
          "analysis.")
bullet(d, "Taught university students and supervised Bachelor's (B.Tech) students (2023 – 2025).")

role(d, "MTech Researcher – Pneumatic Actuator Systems (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Fabricated pneumatic artificial muscle actuators in-house and built the electromechanical test set-up "
          "with valves, pressure sensors and DAQ to characterise load–displacement behaviour.")
bullet(d, "Designed and implemented a neural-network-based gain-scheduled PID controller that reduced "
          "position-tracking error to 0.3–0.78% under varying load, outperforming classical PID.")

role(d, "Mechanical Engineering Capstone – Upper-Limb Rehabilitation Exoskeleton", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Led CAD design, fabrication and user testing end to end; won the Best Major Project Award and an INR "
          "100,000 TATA Technologies Innovation Grant.")

heading(d, "Education")
role(d, "PhD Candidate, Mechatronics and Robotics", "2023 – Present",
     "Aalborg University, Department of Materials and Production, Denmark")
role(d, "MTech, Mechatronics", "2020 – 2022",
     "AcSIR – CSIR-Central Mechanical Engineering Research Institute (CMERI), India")
role(d, "BTech, Mechanical Engineering", "2015 – 2019",
     "Siddaganga Institute of Technology, Visvesvaraya Technological University (VTU), India")

heading(d, "Certifications and Awards")
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
bullet(d, "SolidWorks, Autodesk Fusion 360, FEA, Bambu Lab and Ultimaker Cura (3D printing)", "CAD & Manufacturing: ")
bullet(d, "MATLAB/Simulink, Python, LabVIEW (basic), Arduino", "Software & Embedded: ")
bullet(d, "Qualisys Motion Capture, Forsentec Force/Torque Sensors, Pneumatic Control, Custom Rig Fabrication",
       "Instrumentation & Testing: ")

heading(d, "Languages")
para(d, "English (C1, fluent) | Bengali (Native) | Hindi (Conversational)")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_CV_%s.docx" % TAG)
to_pdf(d, OUT + "Arunabha_Majumder_CV_%s.pdf" % TAG)

# ---------------- COVER LETTER ----------------
c = new_doc()
c.sections[0].top_margin = Cm(2.0)
header(c, TITLE, links=True)
para(c, "September 29, 2026", after=8)
para(c, "Hiring Team, Engineering", after=0)
para(c, "GE Aerospace", after=0)
para(c, "United Kingdom", after=8)
para(c, "Application: Mechanical Design Engineer – Mechatronic Systems", bold=True, after=8)
para(c, "Dear Hiring Team,", after=8)
body = [
 "I am applying for the Mechanical Design Engineer position with a focus on mechatronic systems. I hold a BTech "
 "in Mechanical Engineering and an MTech in Mechatronics, and I am finishing my PhD at Aalborg University. My work "
 "sits exactly where this role does: strong mechanical design, combined with sensing, actuation and control.",

 "In my PhD, I designed a hybrid-actuated shoulder exoskeleton from concept to tested hardware. Rather than "
 "relying on a larger motor, I combined a parallel spring with a small 6 Nm motor. I designed the components and "
 "assemblies in SolidWorks, used FEA for strength, stiffness and weight, made the parts through machining and "
 "additive manufacturing, and integrated the motor, encoder, force sensors, DAQ and embedded control. The design "
 "cut energy consumption by more than 25% and won the Best Paper Award at IFToMM ISRM 2026.",

 "I am comfortable working across the mechanical and electrical boundary. On a 5-bar planar parallel robot, I "
 "used variable-stiffness actuators to estimate the force at the end effector through the robot's Jacobian, and "
 "validated the estimate against a force sensor to within 10% RMS error. I also designed the Assist-as-Needed "
 "controller for the exoskeleton, and during my Master's at CSIR-CMERI I built a pneumatic actuator test set-up "
 "and developed a controller that reduced tracking error to below 0.8%.",

 "I enjoy the workshop side of engineering. I build my own prototypes and test rigs, and I planned and ran a "
 "12-participant validation campaign across several operating modes and load conditions. I have also taught and "
 "supervised Bachelor's students, and published peer-reviewed papers, which has sharpened how I communicate "
 "technical work to different audiences.",

 "My CAD experience is in SolidWorks and Autodesk Fusion 360 rather than Inventor, and PCB design is an area I "
 "want to develop further. I am confident I can pick these up quickly, and I would value the chance to help build "
 "GE Aerospace's mechatronics capability while growing my own.",

 "I would welcome the opportunity to discuss how I can contribute to your team. References are available upon "
 "request.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Cover_Letter_%s.docx" % TAG)
to_pdf(c, OUT + "Arunabha_Majumder_Cover_Letter_%s.pdf" % TAG, top=2.0)

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
TAG = "RD_Engineer"
TITLE = "R&D Engineer | Mechanical Engineering | New Product Development | 3D CAD (SolidWorks) | Testing & Validation"

# UK-style CV: Profile -> Key Skills -> Key Achievements -> Employment History
d = new_doc()
header(d, TITLE)

heading(d, "Profile")
para(d, "R&D Engineer with a degree in Mechanical Engineering, an MTech in Mechatronics and a PhD in progress, with "
        "over five years of research and development experience turning ideas into practical engineering "
        "solutions. Covers the full development cycle from concept generation and design through prototype "
        "fabrication, assembly, testing and validation. Produces detailed 3D CAD models, drawings and engineering "
        "documentation in SolidWorks, uses FEA to optimise for strength, stiffness and weight, and designs with "
        "manufacturability and cost in mind. Analytical problem solver with a proactive, innovative mindset and "
        "strong communication skills built across multidisciplinary international teams.")

heading(d, "Key Skills")
bullet(d, "Research and development of innovative product solutions, concept generation, new product development, "
          "prototype development, product improvement", "R&D and Product Development: ")
bullet(d, "Detailed 3D CAD models, engineering drawings and documentation in SolidWorks (CSWA certified) and "
          "Fusion 360", "3D CAD and Documentation: ")
bullet(d, "Engineering testing methodologies, product testing, analysis and validation, custom test rigs, "
          "Finite Element Analysis (FEA)", "Testing and Validation: ")
bullet(d, "Fabrication, assembly, machined parts, additive manufacturing, Design for Assembly (DFA), design for "
          "manufacture", "Manufacturing Processes: ")
bullet(d, "Weight reduction, cost optimisation, part-count reduction, investigating emerging technologies",
       "Optimisation: ")
bullet(d, "Analytical and problem-solving skills, cross-functional collaboration, technical writing, project "
          "planning and delivery", "Professional: ")

heading(d, "Key Achievements")
bullet(d, "Reduced energy consumption by more than 25% by developing a new hybrid actuation concept for a wearable "
          "device; awarded Best Research Paper, IFToMM ISRM 2026.")
bullet(d, "Reduced product cost, mass and part count by eliminating an external force/torque sensor through a "
          "sensorless force-estimation method.")
bullet(d, "Validated analytical design models against physical testing to below 10% RMS error, de-risking designs "
          "before fabrication.")
bullet(d, "Secured an INR 100,000 TATA Technologies Innovation Grant and the Best Major Project Award for a "
          "rehabilitation product.")

heading(d, "Employment History")
role(d, "Research Engineer – R&D and Product Development (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Led the design and development of an electromechanical product from concept generation through 3D CAD "
          "design, prototyping, testing and validation.")
bullet(d, "Produced detailed SolidWorks 3D models, drawings and engineering documentation, and iterated designs on "
          "FEA results for strength, stiffness and weight before committing to fabrication.")
bullet(d, "Fabricated and assembled prototypes from machined and additively manufactured parts, and integrated "
          "motors, encoders, force sensors and data acquisition.")
bullet(d, "Designed custom automated test rigs and planned and delivered a 12-participant validation test programme "
          "across 3 operating modes and 2 load conditions, including test protocol, instrumentation and data "
          "analysis.")
bullet(d, "Identified product improvements that cut energy consumption by more than 25% and reduced cost, mass and "
          "integration complexity by removing an external sensor.")
bullet(d, "Collaborated across mechanical, electronics, control and biomechanics disciplines, and taught and "
          "supervised Bachelor's (B.Tech) students (2023 – 2025).")

role(d, "MTech Researcher – Actuator Systems (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Researched and developed a pneumatic actuator system: fabricated actuators in-house, built the test "
          "set-up with valves, pressure sensors and data acquisition, and characterised performance.")
bullet(d, "Improved dynamic positioning accuracy to 0.3–0.78% tracking error with a neural-network-based "
          "controller, outperforming the conventional baseline under varying load.")

role(d, "Mechanical Engineering Project – Upper-Limb Rehabilitation Device", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Led CAD design, fabrication and user testing of a rehabilitation device from concept to working product.")

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
          "ISRM 2026, MMS, vol. 213, Springer. (Best Research Paper Award)")
bullet(d, "Majumder, A., et al. \"Neural Network-Based Gain Scheduled Position Control of a Pneumatic Artificial "
          "Muscle.\" IEEE CONECCT, 2022.")

heading(d, "Technical Skills")
bullet(d, "SolidWorks, Fusion 360, FEA", "CAD and Simulation: ")
bullet(d, "MATLAB/Simulink, Python, LabVIEW (basic), Arduino", "Software: ")
bullet(d, "3D printing (Bambu Lab, Ultimaker Cura), force/torque sensors, motion capture, custom test rigs",
       "Prototyping and Test: ")

heading(d, "Languages")
para(d, "English (C1, fluent) | Bengali (Native) | Hindi (Conversational)")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_CV_%s.docx" % TAG)
to_pdf(d, OUT + "Arunabha_Majumder_CV_%s.pdf" % TAG)

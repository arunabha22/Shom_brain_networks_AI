import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
TAG = "ALTEN_Mechanical_Design_Engineer"
TITLE = "Mechanical Design Engineer | SolidWorks | Manufacturing Drawings | DfM | Prototyping & Testing"

# UK CV focused on the design-engineering work; academic output kept brief and low on the page.
d = new_doc()
header(d, TITLE)

heading(d, "Profile")
para(d, "Mechanical Design Engineer with 3 years of hands-on mechanical design experience using SolidWorks, plus a "
        "BTech in Mechanical Engineering and an MTech in Mechatronics. Designs and develops mechanical components "
        "and assemblies, creates detailed 3D models, manufacturing drawings and engineering documentation, and "
        "supports products from concept, prototyping and testing through to manufacture. Applies Design for "
        "Manufacture (DfM) and Design for Assembly (DfA) principles, and supports prototype build, assembly and "
        "validation hands-on. Works effectively in cross-functional engineering teams with strong problem-solving, "
        "communication, attention to detail and organisational skills. Certified SolidWorks Associate (CSWA).")

heading(d, "Key Skills")
bullet(d, "Mechanical design, design and development of mechanical components and assemblies, CAD modelling",
       "Mechanical Design: ")
bullet(d, "SolidWorks (CSWA certified), detailed 3D models, manufacturing drawings, engineering drawings, "
          "technical documentation, Fusion 360", "SolidWorks & CAD: ")
bullet(d, "Design for Manufacture (DfM), Design for Assembly (DfA), machining, additive manufacturing / 3D "
          "printing, fabrication and assembly processes", "Manufacturing: ")
bullet(d, "Concept design, prototyping, prototype build and assembly, product testing, validation, custom test rigs, "
          "Finite Element Analysis (FEA)", "Product Development: ")
bullet(d, "Cross-functional and multidisciplinary engineering teams, problem-solving, communication, attention to "
          "detail, organisation", "Teamwork & Delivery: ")

heading(d, "Professional Experience")
role(d, "Research Engineer – Mechanical Design, Robotics & Actuator Development", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Designed and developed mechanical components and assemblies in SolidWorks for an energy-efficient "
          "wearable electromechanical product, from concept through prototyping and testing to a working system.")
bullet(d, "Created detailed 3D models, manufacturing drawings and engineering documentation used to machine, "
          "3D print and assemble the parts.")
bullet(d, "Applied DfM and DfA principles to keep parts practical to manufacture and assemble; reduced cost, mass "
          "and part count by eliminating an external force/torque sensor from a robot design.")
bullet(d, "Used FEA to iterate designs for strength, stiffness and weight before manufacture, and validated design "
          "models against physical testing to below 10% RMS error.")
bullet(d, "Supported prototype build, assembly and validation hands-on, integrating motors, encoders, force sensors "
          "and data acquisition, and designing custom automated test rigs.")
bullet(d, "Improved system efficiency, cutting energy consumption by more than 25% through a new hybrid actuation "
          "design (Best Paper Award, IFToMM ISRM 2026).")
bullet(d, "Worked with a multidisciplinary team across mechanical, electronics and controls to resolve technical "
          "issues, and planned and delivered a 12-participant validation test programme.")

role(d, "MTech Researcher – Mechanical Design & Development, Actuator Systems", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Designed, fabricated and assembled pneumatic actuators in-house, and built the test set-up with valves, "
          "pressure sensors and data acquisition.")
bullet(d, "Tested and characterised actuator performance and improved positioning accuracy to 0.3–0.78% tracking "
          "error with a new controller.")

role(d, "BTech Capstone – Mechanical Design Lead, Rehabilitation Device", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Led CAD design, manufacture, assembly and user testing of a rehabilitation device; won the Best Major "
          "Project Award and an INR 100,000 TATA Technologies Innovation Grant.")

heading(d, "Education")
role(d, "PhD Candidate, Mechatronics and Robotics", "2023 – Present",
     "Aalborg University, Denmark")
role(d, "MTech, Mechatronics", "2020 – 2022",
     "AcSIR – CSIR-Central Mechanical Engineering Research Institute (CMERI), India")
role(d, "BTech, Mechanical Engineering", "2015 – 2019",
     "Siddaganga Institute of Technology, Visvesvaraya Technological University (VTU), India")

heading(d, "Certifications and Awards")
bullet(d, "Certified SolidWorks Associate (CSWA) – Mechanical Design")
bullet(d, "Best Paper Award, IFToMM International Symposium on Robotics and Mechatronics (2026)")
bullet(d, "TATA Technologies Innovation Award – INR 100,000 Grant (2019)")

heading(d, "Engineering Projects")
bullet(d, "Designed, fabricated and assembled a custom Go-Kart.", "Go-Kart (2017): ")
bullet(d, "Designed and built a human-electric hybrid vehicle in a multidisciplinary team.", "Efficycle (2018): ")

heading(d, "Technical Skills")
bullet(d, "SolidWorks, Fusion 360, FEA", "CAD and Simulation: ")
bullet(d, "MATLAB/Simulink, Python, LabVIEW (basic), Arduino", "Software: ")
bullet(d, "3D printing (Bambu Lab, Ultimaker Cura), force/torque sensors, data acquisition, test rigs",
       "Prototyping and Test: ")

heading(d, "Languages")
para(d, "English (C1, fluent) | Bengali (Native) | Hindi (Conversational)")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_CV_%s.docx" % TAG)
to_pdf(d, OUT + "Arunabha_Majumder_CV_%s.pdf" % TAG)

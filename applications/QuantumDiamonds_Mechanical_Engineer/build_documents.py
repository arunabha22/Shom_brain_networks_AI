import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# QuantumDiamonds Mechanical Engineer (Optomechanics & Quantum Sensing) CV.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  •  "

d = new_doc()
para(d, NAME, bold=True, size=18, after=0)
para(d, "Mechanical Engineer — Lab Hardware, Rapid Prototyping & Systems Integration (SolidWorks)", bold=True,
     size=11, after=2)
para(d, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]),
     size=9.5, after=0)
para(d, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                  "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=6)

heading(d, "Summary")
para(d, "Mechanical engineer who designs and builds lab hardware: SolidWorks concepts turned into testable "
        "prototypes in days through 3D printing and machining, then measured, adjusted and rebuilt. Integrates "
        "actuators, sensors and electronics into single working systems, with a strong sense for geometry, stiffness "
        "and how parts fit together. Curious about the physics behind the instrument.")

heading(d, "Key Results")
bullet(d, " idea to testable hardware, built and iterated by hand", "Days, not months:")
bullet(d, " RMS error on a geometry-based force measurement, validated against a force sensor", "<10%")
bullet(d, " energy reduction from a new mechanical concept (Best Paper Award, IFToMM ISRM 2026)", ">25%")

heading(d, "Experience")
role(d, "Research Engineer – Mechanical Design & Rapid Prototyping of Lab Hardware (PhD Project: VIEXO)",
     "2023 – Present", "Aalborg University, Aalborg, Denmark")
bullet(d, "Turned new ideas into testable hardware quickly by choosing the right process for each part (3D printing "
          "on in-house printers, machined parts, off-the-shelf components), then building, testing and iterating the "
          "designs myself.")
bullet(d, "Integrated the full experimental setup into one working system (actuators, motor, encoder, force sensors, "
          "DAQ and embedded control) by designing the mechanical assemblies in SolidWorks so every component fitted "
          "together, physically and functionally.")
bullet(d, "Kept load-carrying structures stiff and light, checked with FEA for stiffness, strength and weight, by "
          "choosing materials and geometries for each part before manufacture.")
bullet(d, "Achieved below 10% RMS error in force measurement on a 5-bar planar parallel robot, validated against a "
          "force sensor, by modelling its geometry and kinematics (Jacobian) and variable-stiffness actuators; "
          "applied the method in lab measurements of human arm impedance.")
bullet(d, "Cut energy consumption by more than 25% (Best Paper Award, IFToMM ISRM 2026) by designing a new hybrid "
          "actuation concept for a shoulder exoskeleton: a parallel spring working with a 6 Nm motor.")
bullet(d, "Documented designs so others could build on them (3D models, drawings, part specifications), working "
          "closely with engineers and scientists across disciplines and mentoring Bachelor's students (2023 – 2025).")

role(d, "MTech Researcher – Pneumatic Actuator Test Setups (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Built a full test setup from scratch by fabricating pneumatic artificial muscles from raw materials and "
          "integrating valves, pressure sensors and DAQ.")
bullet(d, "Reduced position-tracking error to 0.3–0.78% with a neural-network-based controller, outperforming "
          "classical PID.")

heading(d, "Things I Built")
bullet(d, "Hybrid-actuated joint, test rigs and full sensor/electronics integration.", "Exoskeleton prototype (PhD): ")
bullet(d, "Force measurement from actuator models, used in lab experiments.", "5-bar parallel robot setup (PhD): ")
bullet(d, "Actuators and pressure test setup built from raw materials.", "Pneumatic test bench (MTech): ")
bullet(d, "Designed, fabricated and assembled from the ground up.", "Go-Kart (2017): ")

heading(d, "Skills")
bullet(d, "SolidWorks (CSWA), Fusion 360, assemblies, drawings, part specifications", "CAD: ")
bullet(d, "3D printing (Bambu Lab, Ultimaker Cura), machined parts, off-the-shelf integration, hands-on assembly",
       "Rapid prototyping: ")
bullet(d, "FEA (stiffness, strength, weight), kinematics and geometry, material and geometry selection",
       "Analysis: ")
bullet(d, "Sensors, encoders, motors, DAQ, embedded control, MATLAB/Simulink, Python", "Integration & software: ")
bullet(d, "English (C1, fluent), Bengali (Native), Hindi (Conversational)", "Languages: ")

heading(d, "Education")
role(d, "Ph.D. Candidate, Mechatronics & Robotics", "2023 – Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
role(d, "M.Tech, Mechatronics", "2020 – 2022",
     "AcSIR – CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
role(d, "B.Tech, Mechanical Engineering", "2015 – 2019",
     "Siddaganga Institute of Technology, Visvesvaraya Technological University (VTU), Tumakuru, India")

heading(d, "Awards & Publications")
bullet(d, "Best Research Paper Award, IFToMM ISRM 2026; Certified SolidWorks Associate (CSWA)")
bullet(d, "Two peer-reviewed publications: ISRM 2026 (Springer) and IEEE CONECCT 2022")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_CV_QuantumDiamonds.docx")
to_pdf(d, OUT + "Arunabha_Majumder_CV_QuantumDiamonds.pdf")

# ---------------- COVER LETTER ----------------
c = new_doc()
c.sections[0].top_margin = Cm(2.0)
para(c, NAME, bold=True, size=18, after=0)
para(c, "Mechanical Engineer — Lab Hardware, Rapid Prototyping & Systems Integration (SolidWorks)", bold=True,
     size=11, after=2)
para(c, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]),
     size=9.5, after=0)
para(c, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                  "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=8)
para(c, "October 7, 2026", after=8)
para(c, "Hardware Pre-Development Team", after=0)
para(c, "QuantumDiamonds GmbH", after=0)
para(c, "Munich, Germany", after=8)
para(c, "Application: Mechanical Engineer (Optomechanics & Quantum Sensing)", bold=True, after=8)
para(c, "Dear QuantumDiamonds Team,", after=8)
body = [
 "I am applying for the Mechanical Engineer (Optomechanics & Quantum Sensing) position in your Hardware "
 "Pre-Development Team. I am a mechanical engineer finishing my PhD at Aalborg University, and I enjoy exactly what "
 "you describe: turning the requirements of scientists and engineers into pragmatic mechanical designs, and "
 "building, testing and rebuilding them myself until they work.",

 "In my PhD, I designed and built lab hardware from concept to working system. I created the assemblies in "
 "SolidWorks, chose the right process for each part, from 3D printing on our in-house printers to machined and "
 "off-the-shelf components, and integrated actuators, a motor, encoder, force sensors, DAQ and embedded control into "
 "one setup. I used FEA to keep load-carrying structures stiff and light. The resulting design cut energy "
 "consumption by more than 25% and won the Best Paper Award at IFToMM ISRM 2026.",

 "I think naturally in geometry and systems. On a 5-bar planar parallel robot, I modelled the kinematics and "
 "estimated the end-effector force from the robot's actuators through its Jacobian, validated against a force "
 "sensor to below 10% RMS error, and used the method in lab measurements. During my Master's at CSIR-CMERI, I built "
 "a complete pneumatic test setup from raw materials.",

 "I have not yet worked with optics, RF or magnetic environments, tolerance budgets or non-magnetic materials, and "
 "I would be glad to learn them from your physicists and engineers. I am curious about the physics behind the "
 "Quantum Diamond Microscope, and I would much rather test a quick prototype than debate a design on paper. I am "
 "open to relocating to Munich.",

 "I would welcome the opportunity to discuss how I can contribute to your demonstrators. References are available "
 "upon request.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Cover_Letter_QuantumDiamonds.docx")
to_pdf(c, OUT + "Arunabha_Majumder_Cover_Letter_QuantumDiamonds.pdf", top=2.0)

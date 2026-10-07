import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Danfoss Mechanical Engineer, PMI (product maintenance & improvement) CV.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  •  "

d = new_doc()
para(d, NAME, bold=True, size=18, after=0)
para(d, "Mechanical Engineer — Design Optimisation, Continuous Improvement & Testing", bold=True, size=11, after=2)
para(d, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]),
     size=9.5, after=0)
para(d, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                  "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=6)

heading(d, "Summary")
para(d, "Mechanical engineer who improves products through testing, design optimisation and clear documentation. "
        "Improved a mechatronic system's performance by more than 25% through design changes, and enjoys solving "
        "practical problems with production-minded, cross-functional teams. Strong in CAD (SolidWorks, CSWA) and "
        "eager to work in PLM systems.")

heading(d, "Key Results")
bullet(d, " performance gain through design optimisation", ">25%")
bullet(d, " RMS error on a verified measurement method", "<10%")
bullet(d, " a repeated continuous-improvement loop on real hardware", "Concept → test → improve:")

heading(d, "Experience")
role(d, "Research Engineer – Mechanical Design & Continuous Improvement (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Improved performance by more than 25% (energy consumption, measured in lab tests) by acting as the "
          "mechanical expert on a shoulder exoskeleton and making design modifications and optimisations to its "
          "actuation system, a parallel spring working with a 6 Nm motor (Best Paper Award, IFToMM ISRM 2026).")
bullet(d, "Increased reliability through repeated test campaigns by running a continuous improvement loop: testing "
          "prototypes, finding the cause of mechanical, electronic and control issues, and implementing design changes "
          "in SolidWorks.")
bullet(d, "Kept designs buildable and well documented by maintaining 3D models, assemblies, technical drawings and "
          "product documentation for machined and 3D-printed parts, using FEA for strength, stiffness and weight.")
bullet(d, "Verified a force-estimation method to below 10% RMS error against a force sensor by developing it for a "
          "5-bar planar parallel robot using variable-stiffness actuators and the robot Jacobian.")
bullet(d, "Delivered on multiple parallel tasks (design, testing, a 12-participant data collection, and supervising "
          "Bachelor's students in 2023 – 2025) by working in a structured way and collaborating across functions "
          "(mechanical, electronics, control, biomechanics).")

role(d, "MTech Researcher – Pneumatic Actuator Systems (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Reduced position-tracking error to 0.3–0.78% by iteratively testing and improving the control of a "
          "non-linear pneumatic actuator, outperforming classical PID.")
bullet(d, "Built a reliable test set-up by fabricating pneumatic artificial muscles in-house and integrating valves, "
          "pressure sensors and DAQ.")

heading(d, "Skills")
bullet(d, "Design modifications, optimisation, FEA, DFA, technical drawings, documentation",
       "Mechanical design & improvement: ")
bullet(d, "SolidWorks (CSWA), Fusion 360; eager to learn PLM and engineering change processes", "CAD & PLM: ")
bullet(d, "Test rigs, lab testing, finding the cause of issues, verification", "Testing & troubleshooting: ")
bullet(d, "Motors, sensors, embedded control, MATLAB/Simulink, Python", "Mechatronics: ")
bullet(d, "English (C1, fluent), Bengali (Native), Hindi (Conversational)", "Languages: ")

heading(d, "Education")
role(d, "Ph.D. Candidate, Mechatronics & Robotics", "2023 – Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
role(d, "M.Tech, Mechatronics", "2020 – 2022",
     "AcSIR – CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
role(d, "B.Tech, Mechanical Engineering", "2015 – 2019",
     "Siddaganga Institute of Technology, Visvesvaraya Technological University (VTU), Tumakuru, India")

heading(d, "Hands-On Projects")
bullet(d, "Rehabilitation exoskeleton (Best Major Project Award and TATA Technologies Innovation Grant, 2019), "
          "Go-Kart built from the ground up (2017), Efficycle human-electric hybrid vehicle (2018)")

heading(d, "Awards & Publications")
bullet(d, "Best Research Paper Award, IFToMM ISRM 2026; Certified SolidWorks Associate (CSWA)")
bullet(d, "Two peer-reviewed publications: ISRM 2026 (Springer) and IEEE CONECCT 2022")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_CV_Danfoss_PMI.docx")
to_pdf(d, OUT + "Arunabha_Majumder_CV_Danfoss_PMI.pdf")

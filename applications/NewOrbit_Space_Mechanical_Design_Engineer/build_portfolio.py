import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# NewOrbit Space - Mechanical Design Engineer. Short project portfolio (text, ATS-safe). Follows CLAUDE.md facts.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  |  "

d = new_doc()
para(d, NAME, bold=True, size=18, after=0)
para(d, "Engineering Portfolio | Mechanical Design, Prototyping and Testing", bold=True, size=11, after=2)
para(d, SEP.join(["+45 71 62 24 00", "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]), size=9.5, after=0)
para(d, SEP.join(["Online portfolio: arunabha22.github.io/arunabha-majumder",
                  "LinkedIn: linkedin.com/in/arunabha-majumder-681264107"]), size=9.5, after=6)
para(d, "A short overview of hardware I have designed, built and tested. Each project lists the problem, my own "
        "contribution and the result.", italic=True, after=4)

def project(title, dates, problem, role_text, did, result, skills):
    heading(d, title)
    para(d, dates, italic=True, after=3)
    bullet(d, problem, "Problem: ")
    bullet(d, role_text, "My role: ")
    for x in did:
        bullet(d, x)
    bullet(d, result, "Result: ")
    bullet(d, skills, "Skills shown: ")

project("1. Hybrid-actuated shoulder exoskeleton (PhD, project VIEXO)",
        "Aalborg University, 2023 - present",
        "Motor-only shoulder exoskeletons need a large motor to carry the full weight of the arm, which costs energy "
        "and adds mass.",
        "Concept, mechanical design, prototyping, sensor integration and testing.",
        ["Came up with a hybrid concept: a spring carries most of the gravity load and a small 6 Nm motor adds the rest.",
         "Designed the parts and assembly in SolidWorks, from hand sketches to detailed models.",
         "Built and rebuilt the parts with 3D printing, fixing weak parts after each test round.",
         "Integrated the motor, encoder and force sensors into the frame and built my own test rigs.",
         "Collected data from 12 participants; worked in a team of 3 on the controller (my part: equations such as "
         "the Fourier fit, and GUI behaviour)."],
        "More than 25% lower energy use; Best Research Paper Award, IFToMM ISRM 2026.",
        "Concept to tested hardware, mechanism design, mass-conscious design, electromechanical integration, "
        "test and iteration.")

project("2. Force estimation on a 5-bar parallel robot",
        "Aalborg University, PhD",
        "Measure the force at the tip of a robot without placing a sensor there.",
        "Estimation method and validation.",
        ["Used the variable-stiffness actuators and the robot Jacobian to estimate the end-effector force.",
         "Validated the estimate against a reference force sensor; used it to measure human arm impedance in the "
         "gait lab."],
        "Within 10% RMS error of the reference sensor.",
        "Kinematics, measurement and validation, test planning.")

project("3. Upper-limb rehabilitation exoskeleton (Bachelor's capstone)",
        "Siddaganga Institute of Technology, 2018 - 2019",
        "Low-cost device to support arm rehabilitation.",
        "Led the design and build.",
        ["Designed it in CAD, machined the parts, assembled it and tested it with users."],
        "Best Major Project Award and an INR 100,000 TATA Technologies Innovation Grant.",
        "Design for build, machining, assembly, user testing.")

project("4. Student vehicles: Go-Kart (2017) and Efficycle hybrid vehicle (2018)",
        "Siddaganga Institute of Technology",
        "Build working vehicles with student teams for competitions.",
        "Team member in design, fabrication and assembly.",
        ["Designed, fabricated and assembled a Go-Kart from the ground up.",
         "Built a human-electric hybrid vehicle for the Efficycle competition."],
        "Working vehicles built and run.",
        "Teamwork, fabrication, hands-on troubleshooting.")

heading(d, "Drawing and communication")
bullet(d, "Diploma in Fine Arts. I sketch concepts by hand before CAD and make technical illustrations and "
          "figures for papers, posters and demos. SolidWorks engineering drawings; Certified SolidWorks Associate.")
bullet(d, "Published at IEEE CONECCT 2022 and ISRM 2026; taught and supervised Bachelor's students (2023 - 2025).")

heading(d, "What I am still building up")
para(d, "Space hardware, GD&T to full production standard, PLM systems such as 3DEXPERIENCE, and formal change "
        "control (ECO/ECR/ECN). These are areas I want to grow in, and I learn tools quickly.")
d.save(OUT + "NewOrbit_Portfolio_Arunabha_Majumder.docx")
to_pdf(d, OUT + "NewOrbit_Portfolio_Arunabha_Majumder.pdf")

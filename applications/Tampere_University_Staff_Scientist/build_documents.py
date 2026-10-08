import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Tampere University – Staff Scientist, autonomous & electrified mobile work machines. Letter of motivation.
# Corrected facts: PhD = SolidWorks + 3D printing (no Fusion 360 / FEM); machining/assembly = Bachelor's.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  •  "

c = new_doc()
c.sections[0].top_margin = Cm(2.0)
para(c, NAME, bold=True, size=18, after=0)
para(c, "Robotics & Mechatronics Researcher — Experimental Infrastructure, Sensing & Embedded Control", bold=True,
     size=11, after=2)
para(c, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]),
     size=9.5, after=0)
para(c, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                  "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=8)
para(c, "October 8, 2026", after=8)
para(c, "Faculty of Engineering and Natural Sciences, Tampere University", after=0)
para(c, "Hervanta Campus, Tampere, Finland", after=8)
para(c, "Letter of Motivation: Staff Scientist, Autonomous and Electrified Mobile Work Machines", bold=True, after=8)
para(c, "Dear Professor Ghabcheloo and members of the selection committee,", after=8)
body = [
 "I am applying for the Staff Scientist position supporting research on autonomous and electrified mobile work "
 "machines. I am a robotics and mechatronics researcher completing my PhD in Mechatronics and Robotics at Aalborg "
 "University (expected defence: [month year]), with an MTech in Mechatronics and a BTech in Mechanical Engineering. "
 "Throughout my studies I have built and run experimental robotic systems, and the part of research I enjoy most is "
 "exactly what this role is about: making research hardware and software work reliably, so that ideas can be "
 "tested, demonstrated and taken to a higher readiness level.",

 "Relevant skills and experience. In my PhD project VIEXO, I built a hybrid-actuated shoulder exoskeleton from "
 "concept to tested system: mechanical design in SolidWorks, 3D-printed prototypes, and integration of a 6 Nm motor, "
 "encoder, force sensors, data acquisition and embedded control. The design reduced energy consumption by more than "
 "25% and received the Best Research Paper Award at IFToMM ISRM 2026. I also implemented an Assist-as-Needed "
 "controller on the hardware, and on a 5-bar planar parallel robot I developed a force-estimation method using "
 "variable-stiffness actuators and the robot Jacobian, validated against a force sensor to below 10% RMS error and "
 "used to measure human arm impedance in the gait lab. During my Master's at CSIR-CMERI, I built a pneumatic "
 "actuator test bench from raw materials, with valves, pressure sensors and DAQ, and developed a neural-network-based "
 "controller in MATLAB/Simulink. My software tools are Python, MATLAB/Simulink, LabVIEW and Arduino.",

 "Laboratory practice, safety and teaching. I have designed and built custom automated test rigs and conducted "
 "experiments with 12 human participants using EMG and motion-capture equipment, which required careful "
 "experimental protocols, ethics approval and attention to participant safety. From 2023 to 2025 I taught "
 "university students and supervised Bachelor's students, which matches the thesis supervision part of this role. "
 "I also hold a Diploma in Fine Arts and create technical illustrations and visuals, which I would use for public "
 "demonstrators and public relations material.",

 "What I would bring to the infrastructure. My experience is with laboratory robots and wearable systems rather "
 "than full-scale mobile work machines, and I would be keen to learn the heavy-machine platforms, their safety "
 "requirements and the software infrastructure from your team. I would focus on three things: (1) building "
 "well-documented, reusable test set-ups and sensor integrations, so that each research group does not start from "
 "zero; (2) helping researchers move from one-off experiments towards hardware and software that can be integrated "
 "into the shared infrastructure; and (3) clear safety procedures and documentation for the laboratory and test "
 "area. In the longer term, I want to grow into a staff scientist who connects research groups, students and "
 "industry partners around a well-maintained, first-class research infrastructure.",

 "Why this matters to me. A strong research infrastructure multiplies the impact of every researcher who uses it. "
 "The combination of full-scale machines, a dedicated test area and close collaboration with industry in the "
 "Tampere ecosystem is a rare environment, and I would be glad to help maintain and develop it.",

 "Referees: Professor Shaoping Bai, Department of Materials and Production, Aalborg University ([email]); "
 "[second referee name, title, institution, email].",

 "Thank you for considering my application. I would welcome the opportunity to discuss how I can contribute.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Motivation_Letter_Tampere.docx")
to_pdf(c, OUT + "Arunabha_Majumder_Motivation_Letter_Tampere.pdf", top=2.0)

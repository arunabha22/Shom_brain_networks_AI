import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# KTH Robot Design Lab – Research Engineer, soft & wearable robotics (REMA). Academic CV + personal letter.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  •  "
TITLE = "Research Engineer — Wearable Robotics, Exoskeletons, Actuators & Experimental Validation"

def head(doc, after=6):
    para(doc, NAME, bold=True, size=18, after=0)
    para(doc, TITLE, bold=True, size=11, after=2)
    para(doc, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com",
                        "97arunabhasit027@gmail.com"]), size=9.5, after=0)
    para(doc, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                        "Portfolio: arunabha22.github.io/arunabha-majumder", "Project: www.viexo.aau.dk"]),
         size=9.5, after=after)

# ---------------- CV ----------------
d = new_doc()
head(d)

heading(d, "Summary")
para(d, "Researcher in wearable robotics and exoskeletons with hands-on experience across the full mechatronic "
        "chain: actuator and transmission design (compliant and soft pneumatic actuators), CAD and FEM, 3D-printed "
        "prototypes, sensor integration, motion and force control in MATLAB/Python, and experimental validation with "
        "human participants. Best Paper Award, IFToMM ISRM 2026.")

heading(d, "Key Results")
bullet(d, " energy reduction with a hybrid-actuated shoulder exoskeleton", ">25%")
bullet(d, " lower user muscle effort with Assist-as-Needed control", ">15%")
bullet(d, " RMS force-estimation error for physical human-robot interaction", "<10%")

heading(d, "Research Experience")
role(d, "Research Engineer / PhD Researcher – Wearable Robotics & Exoskeletons (VIEXO Project)", "2023 – Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
bullet(d, "Reduced energy consumption by more than 25% (Best Paper Award, IFToMM ISRM 2026) by designing a "
          "hybrid-actuated shoulder exoskeleton that combines a compliant parallel spring with a 6 Nm motor in a new "
          "actuator and transmission concept.")
bullet(d, "Developed functional robot prototypes from concept to experimental validation through iterative design in "
          "SolidWorks and Fusion 360, FEM of load-carrying parts, 3D printing, machining and hands-on assembly.")
bullet(d, "Reduced user muscle effort by more than 15%, measured with EMG, by integrating and controlling the motor, "
          "encoder and force sensors with an Assist-as-Needed controller for physical human-robot interaction.")
bullet(d, "Achieved below 10% RMS force-estimation error, validated against a force sensor, by developing a "
          "force-sensing method for a 5-bar planar parallel robot using variable-stiffness actuators and the robot "
          "Jacobian; applied it to measure human arm impedance in the gait lab.")
bullet(d, "Collected a full experimental dataset, using EMG and motion capture, by conducting experiments with 12 "
          "participants across 3 assistance modes and 2 load conditions.")
bullet(d, "Supervised Bachelor's (B.Tech) students and taught university courses (2023 – 2025); disseminated results "
          "at international conferences.")

role(d, "MTech Researcher – Soft Pneumatic Actuators (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Reduced position-tracking error to 0.3–0.78%, outperforming classical PID, by developing a neural-network-"
          "based gain-scheduled controller in MATLAB/Simulink for a non-linear soft pneumatic artificial muscle.")
bullet(d, "Characterised soft actuator behaviour experimentally by fabricating pneumatic artificial muscles from raw "
          "materials and building a test rig with valves, pressure sensors and DAQ; published at IEEE CONECCT 2022.")

role(d, "Bachelor's Capstone – Upper-Limb Rehabilitation Exoskeleton", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Led CAD design, fabrication and user testing of a rehabilitation exoskeleton; Best Major Project Award and "
          "INR 100,000 TATA Technologies Innovation Grant.")

heading(d, "Publications")
bullet(d, "Majumder, A., Wagner, J.W., Zhu, Y., Oliveira, A.S., and Bai, S. \"A Hybrid Actuated Shoulder Exoskeleton "
          "for Energy-Efficient Upper Arm Support.\" Robotics and Mechatronics: ISRM 2026, MMS, vol. 213, Springer, "
          "2026. Best Research Paper Award.")
bullet(d, "Majumder, A., Sarkar, D., Chakraborty, S., Singh, A., Roy, S.S., and Arora, A. \"Neural Network-Based Gain "
          "Scheduled Position Control of a Pneumatic Artificial Muscle.\" IEEE CONECCT, 2022.")

heading(d, "Education")
role(d, "Ph.D. Candidate, Mechatronics & Robotics", "2023 – Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
role(d, "M.Tech (Master's), Mechatronics", "2020 – 2022",
     "AcSIR – CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
role(d, "B.Tech, Mechanical Engineering", "2015 – 2019",
     "Siddaganga Institute of Technology, Visvesvaraya Technological University (VTU), Tumakuru, India")

heading(d, "Skills")
bullet(d, "SolidWorks (CSWA), Fusion 360, FEM/FEA, 3D printing, machining, assembly", "Design & prototyping: ")
bullet(d, "MATLAB/Simulink, Python, LabVIEW (basic), Arduino", "Programming: ")
bullet(d, "Motion and force control, Assist-as-Needed control, PID, neural-network gain scheduling, kinematics",
       "Control: ")
bullet(d, "Motors, encoders, force/torque sensors, pressure sensors, DAQ, EMG, Qualisys motion capture",
       "Sensors & actuators: ")
bullet(d, "English (C1, fluent), Bengali (Native), Hindi (Conversational)", "Languages: ")

heading(d, "Awards")
bullet(d, "Best Research Paper Award, 9th IFToMM International Symposium on Robotics and Mechatronics (2026)")
bullet(d, "Certified SolidWorks Associate (CSWA); TATA Technologies Innovation Grant – INR 100,000 (2019); Best "
          "Major Project Award (2019)")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_CV_KTH.docx")
to_pdf(d, OUT + "Arunabha_Majumder_CV_KTH.pdf")

# ---------------- PERSONAL LETTER ----------------
c = new_doc()
c.sections[0].top_margin = Cm(2.0)
head(c, after=8)
para(c, "October 8, 2026", after=8)
para(c, "Robot Design Lab, Division of Mechatronics", after=0)
para(c, "KTH Royal Institute of Technology, Stockholm, Sweden", after=8)
para(c, "Personal Letter: Research Engineer in Robot Design and Mechatronics (REMA project)", bold=True, after=8)
para(c, "Dear Members of the Hiring Committee,", after=8)
body = [
 "I am applying for the position of Research Engineer in robot design and mechatronics with a focus on soft and "
 "wearable robotics. I hold an MTech in Mechatronics and a BTech in Mechanical Engineering, and I am completing my "
 "PhD in Mechatronics and Robotics at Aalborg University, where I design and test exoskeletons. The REMA project's "
 "goal, new exoskeletons that help older adults stay mobile, is exactly the kind of research I want to dedicate "
 "the next step of my career to.",

 "Wearable robotics has been the thread through my whole education. My Bachelor's capstone was an upper-limb "
 "rehabilitation exoskeleton, which won the Best Major Project Award and a TATA Technologies Innovation Grant. My "
 "Master's thesis at CSIR-CMERI focused on soft pneumatic artificial muscles: I fabricated them from raw materials, "
 "built the test rig with valves, pressure sensors and DAQ, and developed a neural-network-based gain-scheduled "
 "controller in MATLAB/Simulink that reduced tracking error to 0.3–0.78%, published at IEEE CONECCT 2022.",

 "In my PhD project VIEXO, I designed a hybrid-actuated shoulder exoskeleton that combines a compliant parallel "
 "spring with a small 6 Nm motor. I carried out the mechanical design in SolidWorks and Fusion 360, used FEM for "
 "the load-carrying parts, built the prototypes through 3D printing and machining, and integrated the motor, "
 "encoder, force sensors and embedded control. The design reduced energy consumption by more than 25% and received "
 "the Best Research Paper Award at IFToMM ISRM 2026. I also implemented an Assist-as-Needed controller that reduced "
 "user muscle effort by more than 15%, and on a 5-bar planar parallel robot I developed a force-estimation method "
 "using variable-stiffness actuators and the robot Jacobian, validated against a force sensor to below 10% RMS "
 "error and used to measure human arm impedance.",

 "Experimental work with people is central to wearable robotics, and I have conducted experiments with 12 "
 "participants using EMG and motion capture across several assistance modes and load conditions. I have also "
 "supervised Bachelor's students and taught university courses, which matches the student supervision part of this "
 "role.",

 "What draws me to Robot Design Lab is the combination the REMA project brings together: soft robotics, sensing, "
 "actuation, adaptive control and user-centred design. My experience covers rigid and compliant exoskeleton "
 "actuation and soft pneumatic actuators, and I am eager to deepen my work on soft wearable structures, to use "
 "multibody simulation such as Simscape Multibody more systematically, and to design with older adults' needs in "
 "mind. I would bring a hands-on, iterative approach: building functional prototypes quickly, verifying them "
 "experimentally, and turning the results into publications.",

 "I would be glad to contribute to the REMA project and to the research of Robot Design Lab. Thank you for "
 "considering my application.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Personal_Letter_KTH.docx")
to_pdf(c, OUT + "Arunabha_Majumder_Personal_Letter_KTH.pdf", top=2.0)

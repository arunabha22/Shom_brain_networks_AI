import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Lancaster Instruments Robotics Engineer CV + "something I've built" note. Corrected facts:
# PhD = SolidWorks + 3D printing (no Fusion 360 / FEM); machining and assembly = Bachelor's capstone.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  •  "
TITLE = "Robotics Engineer — Mechanical Design, Motion Control, Actuators & Sensors, Hands-On Builds"

def head(doc, after=6):
    para(doc, NAME, bold=True, size=18, after=0)
    para(doc, TITLE, bold=True, size=11, after=2)
    para(doc, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com",
                        "97arunabhasit027@gmail.com"]), size=9.5, after=0)
    para(doc, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                        "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=after)

# ---------------- CV ----------------
d = new_doc()
head(d)

heading(d, "Summary")
para(d, "Robotics engineer who builds machines that work. Designed, built and tested robotic systems from concept "
        "prototype to working hardware: mechanical design in SolidWorks, 3D-printed iterations, integration of motors, "
        "actuators and sensors, motion control, and test rigs. Leads on mechanical and mechatronics, and happy to "
        "pitch in on electronics and software.")

heading(d, "Things I've Built")
bullet(d, "Hybrid-actuated robotic joint (parallel spring + 6 Nm motor) with sensors, embedded control and test rigs; "
          "cut energy use by more than 25% (Best Paper Award, 2026).", "Shoulder exoskeleton (PhD): ")
bullet(d, "Kinematic model and sensorless force estimation, validated to below 10% RMS error.",
       "5-bar parallel robot setup (PhD): ")
bullet(d, "Pneumatic artificial muscles and a full test rig (valves, pressure sensors, DAQ), built from raw "
          "materials.", "Pneumatic actuator bench (MTech): ")
bullet(d, "Designed, machined, assembled and user-tested; Best Major Project Award.",
       "Rehabilitation exoskeleton (Bachelor's): ")
bullet(d, "Designed, fabricated and assembled from the ground up.", "Go-Kart (2017): ")

heading(d, "Experience")
role(d, "Research Engineer – Robotic Machines & Motion Control (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Took a robotic machine from concept prototype to a working system tested with people by leading the "
          "mechanical design in SolidWorks and iterating through 3D-printed prototypes; the design cut energy use by "
          "more than 25% (Best Paper Award, IFToMM ISRM 2026).")
bullet(d, "Integrated motors, actuators and sensors (6 Nm motor, encoder, force sensors, DAQ and embedded control) "
          "into one machine, working across mechanical, electronics and control.")
bullet(d, "Reduced user muscle effort by more than 15% by implementing motion control (Assist-as-Needed controller) on "
          "the hardware, then testing and refining it with 12 participants.")
bullet(d, "Achieved below 10% RMS force-estimation error on a 5-bar planar parallel robot, validated against a force "
          "sensor, by modelling its kinematics (Jacobian) and variable-stiffness actuators.")
bullet(d, "Built custom test rigs and tracked down mechanical, electrical and control issues on the bench; mentored "
          "Bachelor's (B.Tech) students (2023 – 2025).")

role(d, "MTech Researcher – Pneumatic Actuator Control (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Reduced tracking error to 0.3–0.78% by building pneumatic actuators and their test rig from scratch "
          "(valves, pressure sensors, DAQ) and developing a neural-network-based controller.")

role(d, "Bachelor's Capstone – Upper-Limb Rehabilitation Exoskeleton", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Won the Best Major Project Award and an INR 100,000 TATA Technologies Innovation Grant by leading CAD "
          "design, machining, hands-on assembly and user testing.")

heading(d, "Skills")
bullet(d, "SolidWorks (CSWA), mechanical design, assemblies, drawings", "Mechanical & CAD: ")
bullet(d, "Motors, encoders, actuators, force and pressure sensors, DAQ, PID and model-based control, kinematics",
       "Motion control & sensors: ")
bullet(d, "3D printing (Bambu Lab, Ultimaker Cura); machining and assembly (Bachelor's)", "Fabrication: ")
bullet(d, "Python, MATLAB/Simulink, Arduino, LabVIEW (basic)", "Software & embedded: ")
bullet(d, "English (C1, fluent), Bengali (Native), Hindi (Conversational)", "Languages: ")

heading(d, "Education")
role(d, "Ph.D. Candidate, Mechatronics & Robotics", "2023 – Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
role(d, "M.Tech, Mechatronics", "2020 – 2022",
     "AcSIR – CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
role(d, "B.Tech, Mechanical Engineering", "2015 – 2019",
     "Siddaganga Institute of Technology, Visvesvaraya Technological University (VTU), Tumakuru, India")

heading(d, "Awards & Publications")
bullet(d, "Best Research Paper Award, IFToMM ISRM 2026; Certified SolidWorks Associate (CSWA); two peer-reviewed "
          "publications (ISRM 2026, IEEE CONECCT 2022)")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_CV_Lancaster_Instruments.docx")
to_pdf(d, OUT + "Arunabha_Majumder_CV_Lancaster_Instruments.pdf")

# ---------------- NOTE: SOMETHING I'VE BUILT ----------------
n = new_doc()
n.sections[0].top_margin = Cm(2.0)
head(n, after=8)
heading(n, "Something I've Built: A Hybrid-Actuated Robotic Shoulder Joint")
para(n, "What it is", bold=True, after=2)
para(n, "A robotic shoulder joint for an exoskeleton (PhD project VIEXO, Aalborg University) that supports a person's "
        "arm against gravity. I designed the mechanics, built the prototypes, integrated the motor and sensors, "
        "implemented the control and built the test rigs. Project page: www.viexo.aau.dk", after=8)
para(n, "The problem", bold=True, after=2)
para(n, "Carrying the full gravity load with a motor alone would need a big, heavy and power-hungry actuator, which "
        "is not practical for something worn on the body.", after=8)
para(n, "What I did", bold=True, after=2)
para(n, "I paired a parallel spring, which carries the steady gravity load, with a small 6 Nm motor that only adds "
        "what the spring cannot. I designed the joint in SolidWorks, iterated through 3D-printed prototypes, and "
        "integrated the motor, encoder, force sensors, DAQ and embedded control. I then implemented an "
        "Assist-as-Needed controller and built test rigs to tune and check the system on the bench.", after=8)
para(n, "The result", bold=True, after=2)
para(n, "The joint cut energy consumption by more than 25% and won the Best Paper Award at IFToMM ISRM 2026. In tests "
        "with 12 participants, the controller reduced muscle effort by more than 15%.", after=8)
para(n, "What I learned", bold=True, after=2)
para(n, "Getting a machine to work reliably comes down to the details found on the bench and in testing, and I "
        "enjoy that part as much as the design.", after=8)
para(n, "Photos and more projects: arunabha22.github.io/arunabha-majumder")
n.save(OUT + "Arunabha_Majumder_Build_Note_Lancaster_Instruments.docx")
to_pdf(n, OUT + "Arunabha_Majumder_Build_Note_Lancaster_Instruments.pdf", top=2.0)

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
TAG = "Novo_Nordisk_Test_Engineer"
TITLE = "Test Engineer | Verification & Validation | Test Protocols | Data Analysis | Assistive Devices"

# ---------------- RESUME ----------------
d = new_doc()
header(d, TITLE, links=True)

heading(d, "Profile")
para(d, "Test and verification engineer with a BTech in Mechanical Engineering, an MTech in Mechatronics and a PhD "
        "in progress at Aalborg University. Plans, coordinates and reports testing and verification activities "
        "in product development projects: writing test protocols, designing test set-ups, running controlled "
        "tests, analysing data and communicating conclusions to stakeholders. Experienced with assistive and "
        "rehabilitation devices tested with human participants, including statistical study design and ethics "
        "protocols. Analytical, detail-oriented and collaborative across disciplines; fluent in English (C1).")

heading(d, "Key Skills")
bullet(d, "Test planning, test protocols, controlled test conditions, verification against requirements and "
          "reference measurements, validation of measurement methods", "Verification & Validation: ")
bullet(d, "Statistical analysis, statistical power justification, data pipelines, interpreting results and "
          "drawing conclusions (Python, MATLAB)", "Data Analysis: ")
bullet(d, "Custom test rigs and fixtures, force/torque sensors, encoders, DAQ, EMG, motion capture (Qualisys)",
       "Test Equipment & Instrumentation: ")
bullet(d, "Human-subject test studies, ethics protocols, assistive and rehabilitation devices",
       "Device Testing: ")
bullet(d, "Reporting to technical and non-technical stakeholders, cross-functional collaboration, teaching and "
          "supervision, peer-reviewed publications", "Communication: ")
bullet(d, "SolidWorks (CSWA), Autodesk Fusion 360, FEA, prototyping", "Engineering Tools: ")

heading(d, "Professional Experience")
role(d, "Research Engineer – Device Development, Testing & Verification (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Planned, coordinated and reported a 12-participant verification study of a shoulder exoskeleton across "
          "3 operating modes and 2 load conditions, covering statistical power justification, test protocol, ethics "
          "protocol, EMG and motion-capture instrumentation, and the end-to-end data pipeline.")
bullet(d, "Validated an end-effector force-estimation method on a 5-bar planar parallel robot, using variable-"
          "stiffness actuators and the robot Jacobian, against a reference force sensor to below 10% RMS error.")
bullet(d, "Designed custom automated test rigs and ran controlled tests on prototype hardware with motor, encoder, "
          "force sensors and DAQ.")
bullet(d, "Showed through testing that a hybrid actuation design cut energy consumption by more than 25% and an "
          "Assist-as-Needed controller reduced user muscle effort by more than 15% (Best Paper Award, IFToMM ISRM "
          "2026).")
bullet(d, "Communicated results in peer-reviewed publications; taught university students "
          "and supervised Bachelor's (B.Tech) students (2023 – 2025).")

role(d, "MTech Researcher – Pneumatic Actuator Testing & Characterisation (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Built a test set-up with valves, pressure sensors and DAQ, and characterised the load–displacement "
          "behaviour of in-house pneumatic actuators to derive an empirical model.")
bullet(d, "Verified a neural-network-based controller against a classical PID baseline under varying load; "
          "tracking error of 0.3–0.78%.")

role(d, "Mechanical Engineering Capstone – Upper-Limb Rehabilitation Exoskeleton", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Led design, fabrication and user testing of a rehabilitation device; won the Best Major Project Award and "
          "an INR 100,000 TATA Technologies Innovation Grant.")

heading(d, "Education")
role(d, "PhD Candidate, Mechatronics and Robotics", "2023 – Present",
     "Aalborg University, Department of Materials and Production, Denmark")
role(d, "MTech, Mechatronics", "2020 – 2022",
     "AcSIR – CSIR-Central Mechanical Engineering Research Institute (CMERI), India")
role(d, "BTech, Mechanical Engineering", "2015 – 2019",
     "Siddaganga Institute of Technology, Visvesvaraya Technological University (VTU), India")

heading(d, "Publications, Certifications and Awards")
bullet(d, "Majumder, A., et al. \"A Hybrid Actuated Shoulder Exoskeleton for Energy-Efficient Upper Arm Support.\" "
          "ISRM 2026, MMS, vol. 213, Springer. Best Research Paper Award.")
bullet(d, "Majumder, A., et al. \"Neural Network-Based Gain Scheduled Position Control of a Pneumatic Artificial "
          "Muscle.\" IEEE CONECCT, 2022.")
bullet(d, "Certified SolidWorks Associate (CSWA); TATA Technologies Innovation Award (2019)")

heading(d, "Technical Tools")
bullet(d, "Python, MATLAB/Simulink, LabVIEW (basic)", "Data & Analysis: ")
bullet(d, "Qualisys Motion Capture, Forsentec Force/Torque Sensors, EMG, DAQ, custom test rigs", "Test & Measurement: ")
bullet(d, "SolidWorks, Autodesk Fusion 360, FEA, 3D printing", "CAD & Prototyping: ")

heading(d, "Languages")
para(d, "English (C1, fluent) | Bengali (Native) | Hindi (Conversational)")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_Resume_%s.docx" % TAG)
to_pdf(d, OUT + "Arunabha_Majumder_Resume_%s.pdf" % TAG)

# ---------------- COVER LETTER ----------------
c = new_doc()
c.sections[0].top_margin = Cm(2.0)
header(c, TITLE, links=True)
para(c, "September 30, 2026", after=8)
para(c, "Device Verification Development, Device Development Innovation", after=0)
para(c, "Novo Nordisk A/S", after=0)
para(c, "Hillerød, Denmark", after=8)
para(c, "Application: Test Engineer", bold=True, after=8)
para(c, "Dear Hiring Team,", after=8)
body = [
 "I am applying for the Test Engineer position in Device Verification Development. I hold an MTech in Mechatronics "
 "and a BTech in Mechanical Engineering, and I am finishing my PhD at Aalborg University. Much of my work has been "
 "about proving whether a device really meets its targets, through careful test planning, controlled tests and "
 "clear conclusions, and I would like to bring that to devices that reach patients.",

 "In my PhD, I planned, coordinated and reported a 12-participant study of a shoulder exoskeleton across three "
 "operating modes and two load conditions. I wrote the test and ethics protocols, justified the sample size "
 "statistically, set up the EMG and motion-capture instrumentation, and built the data pipeline from raw "
 "measurements to conclusions. The results showed a reduction in user muscle effort of more than 15%, and the "
 "device design won the Best Paper Award at IFToMM ISRM 2026.",

 "I also care about whether a measurement method can be trusted. On a 5-bar planar parallel robot, I estimated the "
 "end-effector force from variable-stiffness actuators through the robot's Jacobian, and validated the method "
 "against a reference force sensor to within 10% RMS error. I design my own test rigs, and during my Master's at "
 "CSIR-CMERI I built a pneumatic test set-up to characterise actuators and verify a new controller against a "
 "classical baseline.",

 "I communicate results to different audiences. I have presented my work in peer-reviewed publications, taught "
 "and supervised Bachelor's students, and worked in international teams in Denmark and India in English.",

 "My testing experience comes from research and development rather than a regulated environment, and I have not "
 "yet worked with design control, GMP or shelf-life studies. These are exactly what I want to learn, and Novo "
 "Nordisk's verification department is where I would most like to build that expertise.",

 "I would welcome the opportunity to discuss how I can contribute to your team. References are available upon "
 "request.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Cover_Letter_%s.docx" % TAG)
to_pdf(c, OUT + "Arunabha_Majumder_Cover_Letter_%s.pdf" % TAG, top=2.0)

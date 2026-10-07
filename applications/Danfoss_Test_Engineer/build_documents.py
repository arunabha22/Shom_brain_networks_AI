import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Danfoss Test Engineer (QA, failure analysis) CV and cover letter.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  •  "
TITLE = "Test Engineer — Laboratory Testing, Troubleshooting & Validation of Mechatronic Systems"

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
para(d, "Mechatronics engineer with hands-on experience in laboratory testing, troubleshooting and validation of "
        "systems that combine mechanics, electronics and embedded control. Builds test set-ups, recreates and "
        "measures system behaviour, finds the cause of problems and verifies solutions against reference "
        "measurements. Structured, curious and used to working across multidisciplinary teams.")

heading(d, "Key Results")
bullet(d, " RMS error: validated a force-estimation method against a reference force sensor", "<10%")
bullet(d, " energy reduction confirmed through laboratory testing of a mechatronic system", ">25%")
bullet(d, " tracking error after testing and tuning a pneumatic actuator controller", "0.3–0.78%")

heading(d, "Experience")
role(d, "Research Engineer – Mechatronic Systems Testing & Development (PhD Project: VIEXO)", "2023 – Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Validated a sensorless force-estimation method to below 10% RMS error by testing it against a reference "
          "force sensor on a 5-bar planar parallel robot (variable-stiffness actuators and robot Jacobian), then "
          "applied it to measure human arm impedance in the gait lab.")
bullet(d, "Confirmed a more than 25% energy reduction in laboratory testing by building, instrumenting and testing a "
          "hybrid-actuated shoulder exoskeleton (Best Paper Award, IFToMM ISRM 2026).")
bullet(d, "Kept prototypes working through repeated test campaigns by troubleshooting and fixing issues across "
          "mechanical interfaces, electronics and embedded control: motor, encoder, force sensors and DAQ.")
bullet(d, "Designed custom automated test rigs and ran data collection for a 12-participant study across 3 operating "
          "modes and 2 load conditions, using EMG and motion-capture equipment.")
bullet(d, "Worked with engineers and researchers across mechanical, electronics, control and biomechanics to align on "
          "test findings; documented results in peer-reviewed publications.")
bullet(d, "Mentored and supervised Bachelor's (B.Tech) students on engineering projects (2023 – 2025).")

role(d, "MTech Researcher – Pneumatic Actuator Testing (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Characterised non-linear actuator behaviour through laboratory testing by building a test rig with valves, "
          "pressure sensors and DAQ for in-house pneumatic artificial muscles.")
bullet(d, "Reduced position-tracking error to 0.3–0.78% by testing and comparing a neural-network-based controller "
          "against a classical PID baseline under varying load.")

heading(d, "Skills")
bullet(d, "Laboratory testing, test-rig design, troubleshooting, validation against reference measurements, data "
          "analysis", "Testing & troubleshooting: ")
bullet(d, "Sensors, encoders, motors, DAQ, Arduino, LabVIEW (basic), embedded control, pneumatics",
       "Electronics & embedded integration: ")
bullet(d, "Force/torque sensors (Forsentec), Qualisys motion capture, EMG, pressure sensors",
       "Lab & measurement equipment: ")
bullet(d, "SolidWorks (CSWA), technical drawings, FEA, MATLAB/Simulink, Python", "Mechanical & software tools: ")
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

heading(d, "Hands-On Projects")
bullet(d, "Rehabilitation exoskeleton (Best Major Project Award and TATA Technologies Innovation Grant, 2019), "
          "Go-Kart (2017), Efficycle human-electric hybrid vehicle (2018)")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_CV_Danfoss_Test_Engineer.docx")
to_pdf(d, OUT + "Arunabha_Majumder_CV_Danfoss_Test_Engineer.pdf")

# ---------------- COVER LETTER ----------------
c = new_doc()
c.sections[0].top_margin = Cm(2.0)
head(c, after=8)
para(c, "October 7, 2026", after=8)
para(c, "Quality Assurance, Danfoss Power Solutions", after=0)
para(c, "Nordborg, Denmark", after=8)
para(c, "Application: Test Engineer (f/m/d)", bold=True, after=8)
para(c, "Dear Hiring Team,", after=8)
body = [
 "I am applying for the Test Engineer position in Quality Assurance at Danfoss Power Solutions. I am a mechatronics "
 "engineer finishing my PhD at Aalborg University, and what I enjoy most in my work is exactly what this role is "
 "about: testing systems in the lab, finding out why they do not behave as expected, and proving that a solution "
 "works.",

 "In my PhD, I built, instrumented and tested a hybrid-actuated shoulder exoskeleton that combines mechanics, "
 "electronics and embedded control. Through repeated test campaigns, I troubleshot and fixed issues across the "
 "mechanical interfaces, motor, encoder, force sensors and DAQ. On a 5-bar planar parallel robot, I validated a "
 "sensorless force-estimation method against a reference force sensor to within 10% RMS error. I design my own "
 "test rigs, and I ran the data collection for a 12-participant study across several operating modes and load "
 "conditions.",

 "I work in a structured way and communicate well across disciplines. My projects have involved mechanical, "
 "electronics, control and biomechanics specialists, and I have supervised Bachelor's students and documented my "
 "results in peer-reviewed publications.",

 "I want to be open about where I would grow. My electronics experience comes from integrating motors, sensors and "
 "data acquisition rather than detailed circuit analysis, and I have not yet worked with failure analysis of "
 "returned customer products. I learn quickly and would value building this expertise in your team, including "
 "through the onboarding training in Minneapolis.",

 "I would welcome the opportunity to discuss how I can contribute to Danfoss. References are available upon "
 "request.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Cover_Letter_Danfoss_Test_Engineer.docx")
to_pdf(c, OUT + "Arunabha_Majumder_Cover_Letter_Danfoss_Test_Engineer.pdf", top=2.0)

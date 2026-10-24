import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Helsing (Munich) - Senior Studio Design Engineer. CV, cover letter, design portfolio PDF. Follows CLAUDE.md facts.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  |  "

def head(doc, title, after=6):
    para(doc, NAME, bold=True, size=18, after=0)
    para(doc, title, bold=True, size=11, after=2)
    para(doc, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark (open to relocating to Munich)"]), size=9.5, after=0)
    para(doc, SEP.join(["somrkmv1997@gmail.com", "97arunabhasit027@gmail.com",
                        "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=after)

def education(doc):
    heading(doc, "Education")
    role(doc, "PhD, Mechatronics and Robotics (defence expected in 2027)", "2023 - Present", "Aalborg University, Denmark")
    para(doc, "Study abroad, National University of Singapore (NUS), Sep - Nov 2025", after=2)
    role(doc, "MTech, Mechatronics", "2020 - 2022", "AcSIR - CSIR-CMERI, India")
    role(doc, "BTech, Mechanical Engineering", "2015 - 2019", "Siddaganga Institute of Technology (VTU), India")

# ---------------- CV ----------------
d = new_doc()
head(d, "Design Engineer | Sketch, CAD, Build and Test | Robotics and Wearable Hardware")
heading(d, "Summary")
para(d, "Design engineer who sketches by hand, models in SolidWorks and builds and tests the hardware myself. For my "
        "PhD at Aalborg University I took a shoulder exoskeleton from first sketch to a prototype tested with 12 "
        "people, cutting energy use by more than 25% (Best Paper Award, IFToMM ISRM 2026). I hold a Diploma in Fine "
        "Arts alongside my engineering degrees, so I care about how a product looks and feels to use, not just "
        "whether it works.")
heading(d, "Experience")
role(d, "PhD Researcher, Mechatronics and Robotics (project VIEXO)", "2023 - Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
bullet(d, "Sketched, modelled and built a hybrid shoulder exoskeleton: a spring carries most of the arm load so a small "
          "6 Nm motor is enough, saving more than 25% energy and allowing a smaller, lighter actuator.")
bullet(d, "Iterated parts quickly in SolidWorks and 3D printing between test sessions, improving parts that broke or "
          "flexed and keeping the CAD up to date with each build.")
bullet(d, "Integrated the motor, encoder and force sensors into the frame and built my own test rigs.")
bullet(d, "Tested with 12 participants (I collected the data) and worked in a team of 3 on the controller (my part: "
          "equations such as the Fourier fit, and how the GUI should behave for the user).")
bullet(d, "Validated a force estimate on a 5-bar parallel robot against a reference sensor (within 10% RMS error); "
          "presented at international conferences; taught and supervised students (2023 - 2025).")
role(d, "MTech Researcher, Pneumatic Artificial Muscles (Master's thesis)", "2020 - 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
bullet(d, "Fabricated and assembled pneumatic muscles to an existing lab design, collected test data and used it to "
          "design the outer PID loop of a gain-scheduled controller (0.3-0.78% error, IEEE CONECCT 2022).")
role(d, "Student Builds, Siddaganga Institute of Technology", "2017 - 2019", "Tumakuru, India")
bullet(d, "Designed, machined, assembled and user-tested an upper-limb rehabilitation exoskeleton (Best Major Project "
          "Award, INR 100,000 TATA Technologies grant); built a Go-Kart and an Efficycle hybrid vehicle.")
heading(d, "Skills")
bullet(d, "Hand sketching, concept visualisation, technical illustration (Diploma in Fine Arts)", "Design: ")
bullet(d, "SolidWorks (CSWA): parts, assemblies, drawings", "CAD: ")
bullet(d, "3D printing, test rigs; machining and assembly (Bachelor's)", "Build and test: ")
bullet(d, "Motors, encoders, force/torque sensors, DAQ; MATLAB, Python", "Electromechanical: ")
bullet(d, "English (C1, fluent), Bengali (native), Hindi (conversational)", "Languages: ")
education(d)
heading(d, "Awards and Publications")
bullet(d, "Best Research Paper Award, IFToMM ISRM 2026; Certified SolidWorks Associate (CSWA)")
bullet(d, "Majumder, A., et al. ISRM 2026 (Springer), hybrid actuated shoulder exoskeleton; IEEE CONECCT 2022.")
heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Helsing_CV_Arunabha_Majumder.docx"); to_pdf(d, OUT + "Helsing_CV_Arunabha_Majumder.pdf")

# ---------------- COVER LETTER ----------------
c = new_doc(); c.sections[0].top_margin = Cm(1.8)
head(c, "Design Engineer | Sketch, CAD, Build and Test", after=8)
para(c, "October 24, 2026", after=6)
para(c, "Helsing, Design Studio, Munich", after=6)
para(c, "Application: Senior Studio Design Engineer", bold=True, after=6)
para(c, "Dear Helsing Design Studio team,", after=6)
for t in [
 "I am applying for the Studio Design Engineer position in Munich. I am finishing my PhD in Mechatronics and "
 "Robotics at Aalborg University, and I hold an MTech in Mechatronics, a BTech in Mechanical Engineering and a "
 "Diploma in Fine Arts. My PhD ends in March.",
 "The role describes how I like to work: sketch, model, build and test, and stay close to both the CAD and the "
 "physical product. For my PhD I designed a shoulder exoskeleton from first hand sketches to a prototype tested "
 "with 12 people. I modelled it in SolidWorks, rebuilt the parts with 3D printing between test sessions, and "
 "integrated the motor and sensors myself. One key decision was to let a spring carry most of the load, so a small "
 "6 Nm motor was enough. That cut energy use by more than 25%, made the actuator smaller and lighter, and won the "
 "Best Paper Award at IFToMM ISRM 2026.",
 "Because I trained in fine arts as well as engineering, I care about how hardware looks and feels to the person "
 "using it, and I explain ideas visually. I have presented at international conferences and supervised students.",
 "I want to be honest that I have not yet taken a product into serial production, and the role is senior. If you "
 "see a better fit for me in the design studio at a less senior level, I would be glad to be considered for that.",
 "Thank you for your time. I would be happy to walk you through my sketches and prototypes.",
]:
    para(c, t, after=6)
para(c, "Kind regards,", after=2); para(c, NAME)
c.save(OUT + "Helsing_Cover_Letter_Arunabha_Majumder.docx"); to_pdf(c, OUT + "Helsing_Cover_Letter_Arunabha_Majumder.pdf", top=1.8)

# ---------------- PORTFOLIO ----------------
p = new_doc()
head(p, "Design Portfolio | Three hardware projects")
para(p, "Each project shows my role, the CAD work and one design decision made for cost, quality or manufacturability. "
        "No confidential or export-controlled material is included.", italic=True, after=4)
def proj(title, meta, role_t, cad, decision, result):
    heading(p, title); para(p, meta, italic=True, after=3)
    bullet(p, role_t, "My role: "); bullet(p, cad, "CAD work: "); bullet(p, decision, "Design decision: ")
    bullet(p, result, "Result: ")
proj("1. Hybrid-actuated shoulder exoskeleton", "PhD, Aalborg University, 2023 - present | tested prototype",
     "Concept, sketches, mechanical design, prototyping, sensor integration and testing.",
     "SolidWorks parts and assembly of the joint, frame and actuator mounts, updated after each build.",
     "Used a parallel spring to carry most of the gravity load, so a small 6 Nm motor replaced a larger one: lower "
     "energy, lower mass and a cheaper, more compact actuator. Parts were 3D printed so each test round fed straight "
     "into the next version.",
     "More than 25% lower energy use; tested with 12 participants; Best Research Paper Award, IFToMM ISRM 2026.")
proj("2. Upper-limb rehabilitation exoskeleton", "Bachelor's capstone, 2018 - 2019 | tested prototype",
     "Led the design and build.",
     "CAD design of the device and its parts.",
     "Designed parts so they could be machined and assembled in the college workshop with the tools we had, keeping "
     "cost low for a rehabilitation device.",
     "Built and tested with users; Best Major Project Award and INR 100,000 TATA Technologies grant.")
proj("3. Force estimation on a 5-bar parallel robot", "PhD, Aalborg University | validated test setup",
     "Estimation method and validation.",
     "Worked with the robot's linkage geometry (Jacobian) and variable-stiffness actuators.",
     "Estimated tip force from the actuators already in the robot instead of adding a force sensor at the tip, "
     "saving cost and weight at the end effector.",
     "Within 10% RMS error of a reference force sensor; used to measure human arm impedance.")
heading(p, "Sketching")
para(p, "Diploma in Fine Arts. I start every design with hand sketches and can provide sketch samples on request.")
p.save(OUT + "Helsing_Portfolio_Arunabha_Majumder.docx"); to_pdf(p, OUT + "Helsing_Portfolio_Arunabha_Majumder.pdf")

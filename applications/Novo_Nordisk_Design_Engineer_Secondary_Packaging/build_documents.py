import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *
import pymupdf
from docx.shared import Cm as DCm

# Novo Nordisk Hillerod - Design Engineer, Secondary Packaging & Consumer Experience.
# Based on his own resume (photo kept on request), corrected to CLAUDE.md facts. Novo asks for NO photo,
# so a no-photo CV is built too. Do not mention journal papers or the PhD video.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
PHOTO = OUT + "photo.jpeg"
BASE = "Arunabha_Majumder_Novo_Nordisk"

def head(doc, after=6):
    para(doc, NAME, bold=True, size=18, after=0)
    para(doc, "Design Engineer | Product Design, Visual Concepts, Prototyping", bold=True, size=11, after=2)
    para(doc, "+45 71 62 24 00  |  Aalborg, Denmark", size=9.5, after=0)
    para(doc, "somrkmv1997@gmail.com  |  97arunabhasit027@gmail.com", size=9.5, after=0)
    para(doc, "Portfolio: arunabha22.github.io/arunabha-majumder", size=9.5, after=0)
    para(doc, "LinkedIn: linkedin.com/in/arunabha-majumder-681264107", size=9.5, after=after)

def build_cv(with_photo):
    d = new_doc()
    head(d)
    heading(d, "Profile")
    para(d, "Design engineer with a mechanical engineering background and a Diploma in Fine Arts (Painting). I take "
            "products from a hand sketch to CAD, prototypes and user testing, and I care about how a product looks "
            "and feels in people's hands as much as whether it works. I am finishing my PhD in Mechatronics and "
            "Robotics at Aalborg University (thesis expected March).")
    heading(d, "Core Skills")
    bullet(d, "Concept sketching, visual design, Adobe Illustrator, Adobe Photoshop, Procreate", "Design and visuals: ")
    bullet(d, "SolidWorks (CSWA), 3D modelling, technical drawings, Design for Assembly", "CAD: ")
    bullet(d, "3D printing (Bambu Lab, Ultimaker Cura), prototypes, test rigs, user testing", "Prototyping and testing: ")
    bullet(d, "Presenting design choices to engineers, clinicians, students and conference audiences", "Communication: ")
    heading(d, "Professional Experience")
    role(d, "Research Engineer, Product and Actuator Development (PhD project VIEXO)", "2023 - Present",
         "Aalborg University, Aalborg, Denmark")
    bullet(d, "Designed a hybrid shoulder exoskeleton where a spring carries most of the arm load and a small 6 Nm "
              "motor adds the rest; it cut energy use by more than 25% (Best Paper Award, IFToMM ISRM 2026).")
    bullet(d, "Took the design from hand sketches to SolidWorks models and drawings, then 3D printed and rebuilt "
              "parts many times, improving fit, comfort and strength after each round of testing.")
    bullet(d, "Integrated the motor, encoder and force sensors into the frame and built custom test rigs.")
    bullet(d, "Collected data from 12 participants across 3 assistance modes and 2 loads using EMG (Qualisys data "
              "acquisition) and motion capture, so the design could be judged on real users.")
    bullet(d, "Worked in a team of 3 on an Assist-as-Needed controller (my part: equations such as the Fourier fit, "
              "and defining how the GUI should behave for the user); muscle effort dropped by more than 15%.")
    bullet(d, "Removed the need for a force sensor at the tip of a 5-bar parallel robot by estimating force from its "
              "variable-stiffness actuators (within 10% RMS error), cutting cost and mass; built an Arduino-based "
              "trigger to sync robot motion with Qualisys motion capture for arm impedance tests (6 participants).")
    bullet(d, "Taught and supervised Bachelor's students (2023 - 2025) and presented work at international "
              "conferences.")
    role(d, "MTech Researcher, Pneumatic Artificial Muscles (Master's thesis)", "2020 - 2022",
         "CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
    bullet(d, "Fabricated and assembled pneumatic muscles to an existing lab design, collected test data on the lab's "
              "setup and used it to design the outer PID loop of a gain-scheduled controller "
              "(0.3-0.78% position error, IEEE CONECCT 2022).")
    role(d, "Bachelor's Capstone, Upper-Limb Rehabilitation Exoskeleton", "2018 - 2019",
         "Siddaganga Institute of Technology, Tumakuru, India")
    bullet(d, "Led CAD design, machining, assembly and user testing; Best Major Project Award and an INR 100,000 "
              "TATA Technologies Innovation Grant.")
    heading(d, "Education")
    role(d, "PhD, Mechatronics and Robotics (defence expected in 2027)", "2023 - Present",
         "Aalborg University, Department of Materials and Production, Denmark")
    para(d, "Study abroad, National University of Singapore (NUS), Sep - Nov 2025", after=2)
    role(d, "MTech, Mechatronics", "2020 - 2022", "AcSIR - CSIR-CMERI, Durgapur, India")
    role(d, "BTech, Mechanical Engineering", "2015 - 2019", "Siddaganga Institute of Technology (VTU), India")
    role(d, "Diploma in Fine Arts (Painting)", "", "Bangiya Sangeet Parishad, India")
    heading(d, "Tools")
    bullet(d, "Adobe Illustrator, Adobe Photoshop, Procreate", "Visual: ")
    bullet(d, "SolidWorks, 3D printing (Bambu Lab, Ultimaker Cura)", "CAD and making: ")
    bullet(d, "MATLAB/Simulink, Arduino, LaTeX; Python and LabVIEW (basic)", "Software: ")
    bullet(d, "Qualisys motion capture and data acquisition, Forsentec force/torque sensors", "Testing: ")
    heading(d, "Awards and Publications")
    bullet(d, "Best Research Paper Award, 9th IFToMM ISRM (2026); Certified SolidWorks Associate (CSWA); Best Major "
              "Project Award and TATA Technologies Innovation Grant (2019)")
    bullet(d, "Majumder, A., et al. \"A Hybrid Actuated Shoulder Exoskeleton for Energy-Efficient Upper Arm Support.\" "
              "ISRM 2026, Springer. Also IEEE CONECCT 2022.")
    heading(d, "Languages and Interests")
    bullet(d, "English (C1), Bengali (native), Hindi (spoken), Danish (willing to learn)")
    bullet(d, "Painting and illustration; built a Go-Kart (2017) and an Efficycle hybrid vehicle (2018) with student teams")
    heading(d, "References")
    para(d, "Available upon request.")
    name = BASE + ("_CV_with_photo" if with_photo else "_CV")
    if with_photo:
        d.paragraphs[0].runs[0].add_picture(PHOTO, width=DCm(2.2))  # simple docx placement next to name
    d.save(OUT + name + ".docx")
    to_pdf(d, OUT + name + ".pdf")
    if with_photo:
        p = pymupdf.open(OUT + name + ".pdf")
        p[0].insert_image(pymupdf.Rect(470, 40, 541, 128), filename=PHOTO, keep_proportion=True)
        meta = p.metadata; meta.update(author=NAME, creator=NAME, producer=NAME)
        p.set_metadata(meta)
        p.save(OUT + name + ".tmp.pdf", garbage=3, deflate=True); p.close()
        os.replace(OUT + name + ".tmp.pdf", OUT + name + ".pdf")

build_cv(False)
build_cv(True)

c = new_doc(); c.sections[0].top_margin = Cm(1.8)
head(c, after=8)
para(c, "October 26, 2026", after=6)
para(c, "Novo Nordisk, Secondary Pack team, Hillerod", after=0)
para(c, "Attn: Martin Schlie Egholm", after=6)
para(c, "Application: Design Engineer, Secondary Packaging and Consumer Experience", bold=True, after=6)
para(c, "Dear Martin Schlie Egholm,", after=6)
for t in [
 "I am applying for the Design Engineer role in Secondary Packaging. I am a mechanical engineer finishing my PhD "
 "at Aalborg University, and I also hold a Diploma in Fine Arts in painting. This role is one of the few I have "
 "seen that asks for both sides of me: the engineer who builds and tests, and the artist who cares how things look "
 "and feel.",
 "In my PhD I designed a shoulder exoskeleton that people wear on their body. I started with hand sketches, "
 "modelled it in SolidWorks, and rebuilt the 3D-printed parts many times until they fitted well and held up in "
 "testing. We tested it with 12 people, and watching them use it changed how I thought about comfort and clarity. "
 "My own contribution was the design idea, a spring that carries most of the arm's weight so a small motor is "
 "enough, plus the CAD, the prototypes and the sensor integration. It cut energy use by more than 25% and won the "
 "Best Paper Award at IFToMM ISRM 2026.",
 "I use Adobe Illustrator, Photoshop and Procreate for visuals, and I am used to presenting and defending design "
 "choices to engineers, clinicians and students. I have not worked with cartons, leaflets or printing processes "
 "yet, and I would learn them quickly in your team.",
 "Thank you for considering my application. My portfolio is at arunabha22.github.io/arunabha-majumder.",
]:
    para(c, t, after=6)
para(c, "Kind regards,", after=2); para(c, NAME)
c.save(OUT + BASE + "_Cover_Letter.docx"); to_pdf(c, OUT + BASE + "_Cover_Letter.pdf", top=1.8)

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *
import pymupdf
from docx.shared import Cm as DCm

# Coloplast Humlebaek - Mechanical Design Engineer, CC & BC Mechanical Engineering (job 62374).
# Photo always on the CV (CLAUDE.md). No injection moulding / tolerance analysis / simulation claims.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
PHOTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/assets/photo.jpeg"
BASE = "Arunabha_Majumder_Coloplast"

def head(doc, after=6):
    para(doc, NAME, bold=True, size=18, after=0)
    para(doc, "Mechanical Design Engineer | Product Development, SolidWorks, Prototyping and Testing", bold=True, size=11, after=2)
    para(doc, "+45 71 62 24 00  |  Aalborg, Denmark", size=9.5, after=0)
    para(doc, "somrkmv1997@gmail.com  |  97arunabhasit027@gmail.com", size=9.5, after=0)
    para(doc, "Portfolio: arunabha22.github.io/arunabha-majumder", size=9.5, after=0)
    para(doc, "LinkedIn: linkedin.com/in/arunabha-majumder-681264107", size=9.5, after=after)

d = new_doc()
head(d)
heading(d, "Profile")
para(d, "Mechanical engineer who designs devices that are worn on or used close to the human body. I turn user "
        "needs into concepts, SolidWorks models and drawings, then test prototypes with real people and change the "
        "design based on what I see. I am finishing my PhD in Mechatronics and Robotics at Aalborg University "
        "(thesis expected March) and hold a Diploma in Fine Arts, so I explain ideas clearly with sketches as well as words.")
heading(d, "Core Skills")
bullet(d, "SolidWorks (CSWA): parts, assemblies, technical drawings, Design for Assembly", "3D CAD: ")
bullet(d, "Concept generation and evaluation from user needs, iterative 3D printed prototypes, custom test rigs", "Product development: ")
bullet(d, "User trials (12 participants), Qualisys motion capture and data acquisition, force/torque sensors, "
          "MATLAB/Simulink for data and calculations", "Testing and data: ")
bullet(d, "Hand sketching of concepts, technical illustrations and visuals for papers, posters and demos "
          "(Adobe Illustrator, Photoshop, Procreate)", "Visual communication: ")
bullet(d, "Working with control, electronics and software colleagues; teaching and supervising students", "Teamwork: ")
heading(d, "Professional Experience")
role(d, "Research Engineer, Shoulder Exoskeleton (PhD project VIEXO)", "2023 - Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Came up with and designed a hybrid shoulder exoskeleton where a spring carries most of the arm load and a "
          "small 6 Nm motor adds the rest; it cut energy use by more than 25% (Best Paper Award, IFToMM ISRM 2026).")
bullet(d, "Took the design from user needs and hand sketches to SolidWorks models and drawings, then 3D printed and "
          "rebuilt parts many times, improving fit, comfort, strength and ease of assembly after each test.")
bullet(d, "Integrated the motor, encoder and force sensors into the frame and built custom test rigs.")
bullet(d, "Collected data from 12 participants (EMG with the Qualisys data acquisition system and motion capture), "
          "so design choices could be checked on real users.")
bullet(d, "Worked in a team of 3 on an Assist-as-Needed controller (my part: equations such as the Fourier fit, and "
          "defining how the GUI should behave); muscle effort dropped by more than 15%.")
bullet(d, "Estimated tip force on a 5-bar parallel robot from its variable-stiffness actuators (within 10% RMS error "
          "vs a force sensor), removing the need for an extra sensor; built an Arduino-based trigger to sync robot "
          "motion with Qualisys cameras for arm impedance tests (6 participants).")
bullet(d, "Taught university courses and supervised Bachelor's students (2023 - 2025).")
role(d, "MTech Researcher, Pneumatic Artificial Muscles (Master's thesis)", "2020 - 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
bullet(d, "Fabricated and assembled pneumatic muscles to an existing lab design, collected test data on the lab's "
          "setup and used it to design the outer PID loop of a gain-scheduled controller "
          "(0.3-0.78% position error, IEEE CONECCT 2022).")
role(d, "Bachelor's Capstone, Upper-Limb Rehabilitation Exoskeleton", "2018 - 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Led CAD design, machining, assembly and user testing; Best Major Project Award and an INR 100,000 TATA "
          "Technologies Innovation Grant.")
heading(d, "Education")
role(d, "PhD, Mechatronics and Robotics (defence expected in 2027)", "2023 - Present",
     "Aalborg University, Department of Materials and Production, Denmark")
para(d, "Study abroad, National University of Singapore (NUS), Sep - Nov 2025", after=2)
role(d, "MTech, Mechatronics", "2020 - 2022", "AcSIR - CSIR-CMERI, Durgapur, India")
role(d, "BTech, Mechanical Engineering", "2015 - 2019", "Siddaganga Institute of Technology (VTU), India")
role(d, "Diploma in Fine Arts (Painting)", "", "Bangiya Sangeet Parishad, India")
heading(d, "Awards and Publications")
bullet(d, "Best Research Paper Award, 9th IFToMM ISRM (2026); Certified SolidWorks Associate (CSWA); Best Major "
          "Project Award and TATA Technologies Innovation Grant (2019)")
bullet(d, "Majumder, A., et al. \"A Hybrid Actuated Shoulder Exoskeleton for Energy-Efficient Upper Arm Support.\" "
          "ISRM 2026, Springer. Also IEEE CONECCT 2022.")
heading(d, "Languages")
para(d, "English (C1), Bengali (native), Hindi (spoken), Danish (willing to learn)")
heading(d, "References")
para(d, "Available upon request.")
d.paragraphs[0].runs[0].add_picture(PHOTO, width=DCm(2.2))
d.save(OUT + BASE + "_CV.docx")
to_pdf(d, OUT + BASE + "_CV.pdf")
p = pymupdf.open(OUT + BASE + "_CV.pdf")
p[0].insert_image(pymupdf.Rect(470, 40, 541, 128), filename=PHOTO, keep_proportion=True)
meta = p.metadata; meta.update(author=NAME, creator=NAME, producer=NAME); p.set_metadata(meta)
p.save(OUT + "tmp.pdf", garbage=3, deflate=True); p.close(); os.replace(OUT + "tmp.pdf", OUT + BASE + "_CV.pdf")

c = new_doc(); c.sections[0].top_margin = Cm(1.8)
head(c, after=8)
para(c, "October 26, 2026", after=6)
para(c, "Coloplast A/S, Humlebaek", after=0)
para(c, "Attn: Jesper Bruun Jensen, Head of CC & BC Mechanical Engineering", after=6)
para(c, "Application: Mechanical Design Engineer (62374)", bold=True, after=6)
para(c, "Dear Jesper Bruun Jensen,", after=6)
for t in [
 "I am applying for the Mechanical Design Engineer role in CC & BC Mechanical Engineering. I am a mechanical "
 "engineer finishing my PhD at Aalborg University (thesis expected to be finished in March). Most of my work has been on devices that "
 "sit close to the human body, where comfort and reliability matter as much as function.",
 "For my PhD I designed a shoulder exoskeleton. I started from what the user needed, an arm that feels lighter "
 "without a big heavy motor, and came up with a design where a spring carries most of the load and a small 6 Nm "
 "motor does the rest. I modelled it in SolidWorks, made the drawings, and 3D printed and rebuilt the parts many "
 "times, changing fit and strength after each round of testing. I also fitted the motor, encoder and force sensors "
 "and worked with colleagues on control and software. It cut energy use by more than 25% and won the Best Paper "
 "Award at IFToMM ISRM 2026. I also collected data from 12 participants, and watching real people use the device "
 "taught me a lot about what a good design needs.",
 "I like explaining design choices clearly. I have a Diploma in Fine Arts, so I often sketch an idea by hand "
 "before CAD, and I make the visuals for our papers, posters and demos. Teaching university courses and "
 "supervising Bachelor's students also made me better at explaining trade-offs in simple words.",
 "I should be honest that I have not designed injection moulded parts for high-volume production yet, and I have "
 "not worked inside a regulated medical device process. Those are the things I want to learn next, and I pick "
 "things up quickly when I am close to the product and the people who make it. I like that Coloplast's products "
 "are used every day by people who rely on them.",
 "Thank you for considering my application. My portfolio is at arunabha22.github.io/arunabha-majumder.",
]:
    para(c, t, after=6)
para(c, "Kind regards,", after=2); para(c, NAME)
c.save(OUT + BASE + "_Cover_Letter.docx"); to_pdf(c, OUT + BASE + "_Cover_Letter.pdf", top=1.8)

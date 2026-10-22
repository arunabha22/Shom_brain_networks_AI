import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Levitate (Copenhagen) - Mechanical R&D Engineer. Simple CV + 1-page cover letter. Follows CLAUDE.md facts.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  |  "

def head(doc, after=6):
    para(doc, NAME, bold=True, size=18, after=0)
    para(doc, "Mechanical R&D Engineer | Mechanisms, Prototyping and Testing", bold=True, size=11, after=2)
    para(doc, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]),
         size=9.5, after=0)
    para(doc, SEP.join(["Portfolio: arunabha22.github.io/arunabha-majumder",
                        "LinkedIn: linkedin.com/in/arunabha-majumder-681264107"]), size=9.5, after=after)

# ---------------- CV ----------------
d = new_doc()
head(d)
heading(d, "Summary")
para(d, "Mechanical engineer who likes to understand how things work and build better versions. For my PhD at "
        "Aalborg University I designed a shoulder exoskeleton with a new spring and motor mechanism, built and "
        "tested many prototypes, and made the test rigs myself. As a student I built a Go-Kart, a hybrid vehicle "
        "and a rehabilitation exoskeleton. I sketch ideas by hand before CAD.")

heading(d, "Experience")
role(d, "PhD Researcher, Mechatronics and Robotics (project VIEXO)", "2023 - Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
bullet(d, "Designed a hybrid shoulder exoskeleton where a spring carries most of the arm load and a small 6 Nm motor "
          "adds the rest; it cut energy use by more than 25% (Best Paper Award, IFToMM ISRM 2026).")
bullet(d, "Designed the mechanism and parts in SolidWorks and iterated them with 3D printing, fixing parts that broke "
          "or flexed too much until they held up in testing.")
bullet(d, "Built and maintained my own test rigs and integrated the motor, encoder and force sensors with the frame.")
bullet(d, "Validated a force estimate on a 5-bar parallel robot against a reference force sensor, within 10% RMS "
          "error.")
bullet(d, "Collected data from 12 participants in user tests; worked in a team of 3 on the assistance controller "
          "(my part: equations such as the Fourier fit, and GUI behaviour). Taught and supervised students "
          "(2023 - 2025).")

role(d, "MTech Researcher, Pneumatic Artificial Muscles (Master's thesis)", "2020 - 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
bullet(d, "Fabricated and assembled pneumatic artificial muscles to an existing lab design, collected test data on "
          "the lab's setup and used it to design the outer PID loop of a gain-scheduled controller "
          "(0.3-0.78% error, IEEE CONECCT 2022).")

role(d, "Student Builds, Siddaganga Institute of Technology", "2017 - 2019", "Tumakuru, India")
bullet(d, "Designed, machined, assembled and user-tested an upper-limb rehabilitation exoskeleton (Best Major "
          "Project Award, INR 100,000 TATA Technologies grant).")
bullet(d, "Built a Go-Kart (2017) and a human-electric hybrid vehicle for Efficycle (2018) with student teams.")

heading(d, "Skills")
bullet(d, "SolidWorks (CSWA), mechanisms and moving assemblies, hand sketching", "Design: ")
bullet(d, "3D printing, test rigs; machining and assembly (Bachelor's)", "Prototyping: ")
bullet(d, "Motors, encoders, force/torque and pressure sensors, DAQ, Arduino; MATLAB, Python", "Test and data: ")
bullet(d, "Diploma in Fine Arts; concept sketches and technical illustrations", "Drawing: ")
bullet(d, "English (C1, fluent), Bengali (native), Hindi (conversational)", "Languages: ")

heading(d, "Education")
role(d, "PhD, Mechatronics and Robotics (defence expected in 2027)", "2023 - Present", "Aalborg University, Denmark")
role(d, "MTech, Mechatronics", "2020 - 2022", "AcSIR - CSIR-CMERI, India")
role(d, "BTech, Mechanical Engineering", "2015 - 2019", "Siddaganga Institute of Technology (VTU), India")

heading(d, "Awards and Publications")
bullet(d, "Best Research Paper Award, IFToMM ISRM 2026; Certified SolidWorks Associate (CSWA)")
bullet(d, "Majumder, A., et al. \"A Hybrid Actuated Shoulder Exoskeleton for Energy-Efficient Upper Arm Support.\" "
          "ISRM 2026, Springer. Also IEEE CONECCT 2022.")
heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Levitate_CV_Arunabha_Majumder.docx")
to_pdf(d, OUT + "Levitate_CV_Arunabha_Majumder.pdf")

# ---------------- COVER LETTER ----------------
c = new_doc()
c.sections[0].top_margin = Cm(1.8)
head(c, after=8)
para(c, "October 22, 2026", after=6)
para(c, "Levitate, R&D Team, Copenhagen", after=6)
para(c, "Application: Mechanical R&D Engineer", bold=True, after=6)
para(c, "Dear Levitate team,", after=6)
body = [
 "I am applying for the Mechanical R&D Engineer position. I am finishing my PhD in Mechatronics and Robotics at "
 "Aalborg University, and I hold an MTech in Mechatronics and a BTech in Mechanical Engineering. My PhD ends in "
 "March.",

 "Your ad describes how I work. In my PhD I did not accept that shoulder exoskeletons need one big motor. I "
 "designed a mechanism where a spring carries most of the arm's weight and a small motor only adds what is needed. "
 "I sketched it by hand, modelled it in SolidWorks, 3D printed and rebuilt the parts many times, and built my own "
 "test rigs to see where it failed. It cut energy use by more than 25% and won the Best Paper Award at IFToMM ISRM "
 "2026. We tested it with 12 people, and their feedback changed the design more than once.",

 "Building things has always been part of my life. As a student I built a Go-Kart, a hybrid vehicle and a "
 "rehabilitation exoskeleton that I machined and assembled myself. I also hold a Diploma in Fine Arts, so I "
 "think with a pencil before I open CAD.",

 "I want to be honest that I have not yet taken a product through industrialisation, fatigue testing to ISO "
 "standards or supplier work. Those are exactly the things I want to learn, and products that people walk and "
 "live on are where I would most like to learn them.",

 "Thank you for considering my application. I would be glad to show you my work in person.",
]
for t in body:
    para(c, t, after=6)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Levitate_Cover_Letter_Arunabha_Majumder.docx")
to_pdf(c, OUT + "Levitate_Cover_Letter_Arunabha_Majumder.pdf", top=1.8)

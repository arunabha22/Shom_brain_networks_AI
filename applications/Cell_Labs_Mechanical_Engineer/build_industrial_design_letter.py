import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Short cover letter for the Cell Labs hardware / industrial design role.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  •  "

c = new_doc()
c.sections[0].top_margin = Cm(2.0)
para(c, NAME, bold=True, size=18, after=0)
para(c, "Robotics Hardware Designer — Physical Human-Robot Interaction, Prototyping & CAD", bold=True, size=11,
     after=2)
para(c, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]),
     size=9.5, after=0)
para(c, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                  "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=8)
para(c, "October 7, 2026", after=8)
para(c, "Cell Labs, Berlin, Germany", after=8)
para(c, "Application: Hardware / Industrial Designer – Humanoid Systems", bold=True, after=8)
para(c, "Dear Cell Labs Team,", after=8)
body = [
 "I am applying to help shape the hardware of your humanoids. I am a mechanical and robotics engineer finishing my "
 "PhD at Aalborg University, and a trained visual artist with a Diploma in Fine Arts (Painting), so I care both "
 "about how a robot works and how it looks and feels to the people around it.",

 "My PhD robot is worn directly on the human body: a hybrid-actuated shoulder exoskeleton (Best Paper Award, IFToMM "
 "ISRM 2026). That meant designing for physical contact with people from the first sketch, packaging the motor, "
 "encoder, sensors and cabling into a compact assembly, and testing it with participants. I build prototypes fast "
 "through 3D printing and machining, see what holds up, and iterate in SolidWorks and Fusion 360 until it works.",

 "My background is in engineering rather than industrial design, and I have not yet led surfacing, CMF or supplier "
 "work. What I would bring is a designer who understands the internals, safety and physical interaction of the "
 "robot from the inside. I am open to relocating to Berlin and would welcome the chance to show you my work.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Cover_Letter_Cell_Labs_Hardware_Design.docx")
to_pdf(c, OUT + "Arunabha_Majumder_Cover_Letter_Cell_Labs_Hardware_Design.pdf", top=2.0)

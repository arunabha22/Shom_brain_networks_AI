import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Hive Robotics (Munich) - Mechanical Design Engineer, Rugged Electronics Enclosures. Short cover letter.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  |  "

c = new_doc()
c.sections[0].top_margin = Cm(2.0)
para(c, NAME, bold=True, size=18, after=0)
para(c, "Mechanical Design Engineer | SolidWorks, Electromechanical Integration, Prototyping", bold=True,
     size=11, after=2)
para(c, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com",
                  "arunabha22.github.io/arunabha-majumder"]), size=9.5, after=10)
para(c, "October 14, 2026", after=8)
para(c, "Hive Robotics, München", after=8)
para(c, "Application: Mechanical Design Engineer, Rugged Electronics Enclosures (m/f/d)", bold=True, after=8)
para(c, "Dear Hiring Team,", after=8)
body = [
 "I am applying for the Mechanical Design Engineer position for rugged electronics enclosures at Hive Robotics in "
 "Munich. I am finishing my PhD in Mechatronics and Robotics at Aalborg University, and I hold an MTech in "
 "Mechatronics and a BTech in Mechanical Engineering.",

 "Most of my work has been about fitting electronics into mechanical structures that have to survive real use. For "
 "my PhD I designed a shoulder exoskeleton in SolidWorks and integrated the motor, encoder and force sensors into "
 "the frame myself. That meant thinking about where cables run, how parts are mounted and accessed, and what "
 "happens when the device is worn and moved all day. I built and changed many versions with 3D printing until they "
 "held up on the test rig. The design cut energy use by more than 25% and won the Best Paper Award at IFToMM ISRM "
 "2026.",

 "I also have hands-on workshop experience from my Bachelor's, where I machined and assembled a rehabilitation "
 "exoskeleton. I sketch my ideas by hand before going into CAD, and I hold a Diploma in Fine Arts, which helps me "
 "communicate designs clearly.",

 "I have not yet designed enclosures for harsh outdoor conditions, such as sealing to IP ratings or thermal "
 "management, and I would be keen to learn this from your team. I would be glad to talk about how I can "
 "contribute.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Cover_Letter_Hive_Robotics.docx")
to_pdf(c, OUT + "Arunabha_Majumder_Cover_Letter_Hive_Robotics.pdf", top=2.0)

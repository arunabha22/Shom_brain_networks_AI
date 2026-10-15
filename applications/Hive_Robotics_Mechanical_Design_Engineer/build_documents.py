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
para(c, "October 15, 2026", after=8)
para(c, "Hive Robotics, München", after=8)
para(c, "Application: Mechanical Design Engineer, Rugged Electronics Enclosures (m/f/d)", bold=True, after=8)
para(c, "Dear Hiring Team,", after=8)
body = [
 "I am applying for the Mechanical Design Engineer position for rugged electronics enclosures. I am finishing my "
 "PhD in Mechatronics and Robotics at Aalborg University, with an MTech in Mechatronics and a BTech in Mechanical "
 "Engineering.",

 "My work is about packaging electronics into mechanical structures that have to hold up in real use. For my PhD I "
 "designed a shoulder exoskeleton in SolidWorks and integrated the motor, encoder and force sensors into the frame "
 "myself, including mounting, cable routing and access for service. I iterated the parts with 3D printing until "
 "they survived testing. The design cut energy use by more than 25% and won the Best Paper Award at IFToMM ISRM "
 "2026. In my Bachelor's I machined and assembled a rehabilitation exoskeleton, so I am at home in the workshop.",

 "I have not yet designed to IP ratings or run thermal, environmental or EMC testing, and I would like to learn "
 "this with your team while bringing hands-on design and prototyping from day one.",

 "Thank you for your time. I would be glad to talk.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Cover_Letter_Hive_Robotics.docx")
to_pdf(c, OUT + "Arunabha_Majumder_Cover_Letter_Hive_Robotics.pdf", top=2.0)

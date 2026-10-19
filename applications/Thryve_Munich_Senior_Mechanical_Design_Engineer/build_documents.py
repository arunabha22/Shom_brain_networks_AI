import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Thryve Talent (robotics client, Munich) - Senior Mechanical Design Engineer. Short cover letter (Word + PDF).
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  |  "

c = new_doc()
c.sections[0].top_margin = Cm(2.0)
para(c, NAME, bold=True, size=18, after=0)
para(c, "Mechanical Design Engineer | Robotics, Electromechanical Assemblies, Prototyping", bold=True, size=11, after=2)
para(c, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]),
     size=9.5, after=0)
para(c, "Portfolio: arunabha22.github.io/arunabha-majumder", size=9.5, after=10)
para(c, "October 19, 2026", after=8)
para(c, "Darren Yearsley, Thryve Talent", after=0)
para(c, "On behalf of a robotics client in Munich, Germany", after=8)
para(c, "Application: Senior Mechanical Design Engineer, Munich", bold=True, after=8)
para(c, "Dear Hiring Team,", after=8)
body = [
 "I am applying for the Senior Mechanical Design Engineer position with your robotics client in Munich. I am "
 "finishing my PhD in Mechatronics and Robotics at Aalborg University, with an MTech in Mechatronics and a BTech in "
 "Mechanical Engineering.",

 "In my PhD I designed a shoulder exoskeleton from concept to tested prototype. I modelled the parts and assemblies "
 "in SolidWorks, built them with 3D printing, integrated the motor, encoder and force sensors, and tested the system "
 "on rigs and with 12 participants. The design cut energy use by more than 25% and won the Best Paper Award at "
 "IFToMM ISRM 2026. In my Bachelor's I also machined and assembled a rehabilitation exoskeleton, so I know how "
 "design choices play out in the workshop.",

 "I am aware the role asks for 5+ years of experience and FEA, which I do not have yet. What I bring is hands-on "
 "experience with lightweight electromechanical assemblies, fast prototyping and testing, and a willingness to "
 "learn quickly. I would also be glad to be considered for a more mid-level mechanical design role with the same "
 "client.",

 "My PhD ends in March, and I am available after that. Thank you for your time.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
base = OUT + "Arunabha_Majumder_Cover_Letter_Senior_Mechanical_Design_Engineer_Munich"
c.save(base + ".docx")
to_pdf(c, base + ".pdf", top=2.0)

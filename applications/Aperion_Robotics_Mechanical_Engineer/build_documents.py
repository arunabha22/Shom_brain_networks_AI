import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Aperion Robotics (iKnowHow Group) - Mechanical Engineer, software hub of the Production Division. 1-page letter.
# Facts only: no ROS, no Linux claimed, no commissioning experience claimed; AAN controller = team of 3.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  |  "

c = new_doc()
c.sections[0].top_margin = Cm(1.8)
para(c, NAME, bold=True, size=18, after=0)
para(c, "Mechanical Engineer | Robot Integration, Testing and Calibration", bold=True, size=11, after=2)
para(c, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com",
                  "arunabha22.github.io/arunabha-majumder"]), size=9.5, after=8)
para(c, "October 14, 2026", after=6)
para(c, "Aperion Robotics, iKnowHow Group", after=6)
para(c, "Application: Mechanical Engineer, Production Division", bold=True, after=6)
para(c, "Dear Hiring Team,", after=6)
body = [
 "I am applying for the Mechanical Engineer position in your Production Division. I am a mechatronics engineer "
 "finishing my PhD at Aalborg University, with an MTech in Mechatronics and a BTech in Mechanical Engineering. The "
 "role caught my attention because it sits exactly where I have spent most of my time: between the mechanical "
 "parts, the electronics and the software, making sure a robot actually works when it leaves the bench.",

 "In my PhD I built a shoulder exoskeleton and integrated the motor, encoder and force sensors with the mechanical "
 "structure myself. I designed the parts in SolidWorks, 3D printed them and worked with two colleagues on the "
 "controller, where my part was the equations, such as a Fourier fit, and deciding how the GUI should behave. A lot "
 "of the work was debugging: loose connections, sensor offsets and code that behaved differently on the real "
 "hardware. The design cut energy use by more than 25% and won the Best Paper Award at IFToMM ISRM 2026.",

 "I also do a lot of testing and calibration. On a 5-bar parallel robot I estimated the force at the tip from "
 "variable-stiffness actuators and checked it against a reference force sensor, getting within 10% RMS error. I "
 "built and maintained test rigs, wrote test procedures and collected data from 12 participants. I use Python and "
 "MATLAB for data and testing, and I keep clear notes so that someone else can repeat a setup.",

 "I want to be honest about the gaps. I have not yet worked with ROS or done commissioning at a customer site. I "
 "learn new tools quickly, and I would put ROS and Linux at the top of my list in the first months. Being the link "
 "between production, engineering and software is something I already do in the lab, and I have taught and "
 "supervised students since 2023, so explaining technical problems clearly to different people comes naturally. "
 "I am also happy to travel to customer sites.",

 "Thank you for considering my application. I would be glad to talk about how I can help get your robots "
 "integrated, tested and running for your customers.",
]
for t in body:
    para(c, t, after=6)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Cover_Letter_Aperion_Robotics.docx")
to_pdf(c, OUT + "Arunabha_Majumder_Cover_Letter_Aperion_Robotics.pdf", top=1.8)

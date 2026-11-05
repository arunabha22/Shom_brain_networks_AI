import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Yuman - Robotics Engineer (mobile robots moving small items in hospital wards, DTU Skylab, Lyngby).
# Ad text not readable here; tailored to the search summary. No ROS / autonomy / navigation claims.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
BASE = "Arunabha_Majumder_Yuman_Cover_Letter"
c = new_doc(); c.sections[0].top_margin = Cm(1.8)
para(c, NAME, bold=True, size=18, after=0)
para(c, "+45 71 62 24 00  |  Aalborg, Denmark", size=9.5, after=0)
para(c, "somrkmv1997@gmail.com  |  97arunabhasit027@gmail.com", size=9.5, after=0)
para(c, "Portfolio: arunabha22.github.io/arunabha-majumder", size=9.5, after=8)
para(c, "November 5, 2026", after=6)
para(c, "Yuman, DTU Skylab, Lyngby", after=6)
para(c, "Application: Robotics Engineer", bold=True, after=6)
para(c, "Dear Yuman team,", after=6)
for t in [
 "I am applying for the Robotics Engineer role. I am a mechatronics and robotics engineer doing my PhD at Aalborg "
 "University, and my research work is finished, so I can start soon while I complete my thesis. Robots that move "
 "small items around hospital wards appeal to me because they help nurses spend more time with patients, and "
 "because they have to work safely around people every day. That is exactly what I have designed for.",
 "In my PhD I designed a hybrid shoulder exoskeleton where a variable stiffness mechanism and a small 6 Nm motor "
 "work together to support the arm. I optimised the design with a genetic algorithm, integrated the motor, encoder "
 "and force sensors, measured its stiffness on a physical test setup and tested it with 12 people. It cut energy use "
 "by more than 25% and won the Best Paper Award at IFToMM ISRM 2026. I also designed and modelled a novel 5-bar "
 "planar parallel robot with variable stiffness mechanisms, estimated its stiffness with less than 10% error and "
 "quantified human arm impedance. To run those tests, I implemented an Arduino-based trigger system to synchronise "
 "the robot's motion with Qualisys motion capture.",
 "I am most useful where hardware meets the real world: building prototypes, integrating motors and sensors, finding "
 "out why something does not behave as planned, and fixing it. I have not worked on mobile robot navigation or ROS "
 "yet, and I would like to learn that side from your team while I help make the robots reliable for daily use in "
 "hospitals. I also hold a Senior Diploma in Fine Arts, so I explain ideas quickly with hand sketches.",
 "I live in Denmark already and I am willing to learn Danish. Thank you for considering my application. You can see "
 "my work at arunabha22.github.io/arunabha-majumder.",
]:
    para(c, t, after=6)
para(c, "Kind regards,", after=2); para(c, NAME)
c.save(OUT + BASE + ".docx"); to_pdf(c, OUT + BASE + ".pdf", top=1.8)

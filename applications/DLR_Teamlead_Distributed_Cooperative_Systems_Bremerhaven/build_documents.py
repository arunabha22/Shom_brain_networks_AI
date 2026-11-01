import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# DLR Bremerhaven - Teamlead Distributed Cooperative Systems (Vacancy-ID 5677). German fluency required (gap stated).
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
BASE = "Arunabha_Majumder_DLR_Cover_Letter"

c = new_doc(); c.sections[0].top_margin = Cm(1.8)
para(c, NAME, bold=True, size=18, after=0)
para(c, "+45 71 62 24 00  |  Aalborg, Denmark", size=9.5, after=0)
para(c, "somrkmv1997@gmail.com  |  97arunabhasit027@gmail.com", size=9.5, after=0)
para(c, "Portfolio: arunabha22.github.io/arunabha-majumder", size=9.5, after=8)
para(c, "November 1, 2026", after=6)
para(c, "German Aerospace Center (DLR), Institute for the Protection of Maritime Infrastructures, Bremerhaven", after=0)
para(c, "Attn: Dr. Maurice Stephan", after=6)
para(c, "Application: Teamlead Distributed Cooperative Systems (Vacancy-ID 5677)", bold=True, after=6)
para(c, "Dear Dr. Stephan,", after=6)
for t in [
 "I am applying for the Teamlead Distributed Cooperative Systems position at the DLR Institute for the Protection of "
 "Maritime Infrastructures. I am a mechatronics and robotics engineer doing my PhD at Aalborg University, with my "
 "thesis expected to be finished in March. What draws me to this role is the chance to take autonomous systems out "
 "of the lab and into real field trials at sea.",
 "My strength is designing, building and testing robotic systems that work in the real world. In my PhD I designed a "
 "hybrid shoulder exoskeleton, optimised it with a genetic algorithm, integrated the motor, encoder and force "
 "sensors, and tested it on a physical setup and with 12 participants. It won the Best Paper Award at IFToMM ISRM "
 "2026. I also designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms, "
 "estimated its stiffness with less than 10% error and quantified human arm impedance. To make these experiments "
 "work, I implemented an Arduino-based trigger system to synchronise the robot's motion with Qualisys motion capture. "
 "Planning complex experiments, building prototypes and getting reliable data from them is the part of research I "
 "know best.",
 "I also have experience guiding technical work. Since 2023 I have taught university courses and supervised "
 "Bachelor's students in their projects, and I have presented my work at international conferences. I am used to "
 "working across disciplines with colleagues in control, electronics and software.",
 "I want to be honest about the gaps. My background is in robot hardware and experiments rather than swarm "
 "intelligence and multi-agent decision-making, and my German is not yet at the level you ask for. I am willing to "
 "learn German and to grow into the leadership side of the role. If this team lead position is not the right fit "
 "for my profile today, I would be glad to be considered for a researcher position in your team, where my "
 "experience with prototypes and field-ready hardware could help.",
 "Thank you for considering my application. You can see my work at arunabha22.github.io/arunabha-majumder.",
]:
    para(c, t, after=6)
para(c, "Kind regards,", after=2); para(c, NAME)
c.save(OUT + BASE + ".docx"); to_pdf(c, OUT + BASE + ".pdf", top=1.8)

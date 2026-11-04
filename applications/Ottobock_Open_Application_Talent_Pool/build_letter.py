import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Ottobock open application / talent pool (Job ID 8362). Ad asks: competencies, preferred location, notice period,
# weekly availability, areas of interest. Location + relocation + availability are assumptions he should check.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
BASE = "Arunabha_Majumder_Ottobock_Cover_Letter"
c = new_doc(); c.sections[0].top_margin = Cm(1.8)
para(c, NAME, bold=True, size=18, after=0)
para(c, "+45 71 62 24 00  |  Aalborg, Denmark", size=9.5, after=0)
para(c, "somrkmv1997@gmail.com  |  97arunabhasit027@gmail.com", size=9.5, after=0)
para(c, "Portfolio: arunabha22.github.io/arunabha-majumder", size=9.5, after=8)
para(c, "November 4, 2026", after=6)
para(c, "Ottobock SE & Co. KGaA", after=0)
para(c, "Attn: Katharina Nolte", after=6)
para(c, "Open Application, Professional Talent Pool (Job ID 8362)", bold=True, after=6)
para(c, "Dear Ms Nolte,", after=6)
for t in [
 "I would like to join Ottobock's talent pool. I am a mechanical and mechatronics engineer doing my PhD in "
 "Mechatronics and Robotics at Aalborg University, with my thesis expected to be finished in March. Most of my work "
 "has been on devices worn on the human body, so prosthetics, orthotics and exoskeletons at Ottobock are exactly "
 "where I want to build my career.",
 "In my PhD I designed a hybrid shoulder exoskeleton where a spring carries most of the arm load and a small 6 Nm "
 "motor adds the rest. I took it from hand sketches to SolidWorks, optimised the design with a genetic algorithm, "
 "integrated the motor, encoder and force sensors, measured its stiffness on a physical test setup and tested it "
 "with 12 participants. It cut energy use by more than 25% and won the Best Paper Award at IFToMM ISRM 2026. I also "
 "designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms, estimated its "
 "stiffness with less than 10% error and quantified human arm impedance. In my Master's I designed the outer PID loop "
 "of a neural network-based controller in MATLAB/Simulink and implemented it in LabVIEW to drive a pneumatic muscle. "
 "My first exoskeleton was a rehabilitation device for a paralysed arm in my Bachelor's.",
 "Areas of interest: mechanical design and actuator development for exoskeletons, orthoses and prostheses, "
 "prototyping, and test and validation with users.",
 "Preferred location: Duderstadt, as the centre of Ottobock's research and development. I am happy to relocate "
 "within Germany.",
 "Notice period and availability: my thesis is expected to be finished in March, so I can start from spring 2027. "
 "I am available full-time.",
 "I also hold a Senior Diploma in Fine Arts, so I often explain ideas with quick hand sketches, which helps when "
 "working with clinicians and users. Thank you for considering my application.",
]:
    para(c, t, after=6)
para(c, "Kind regards,", after=2); para(c, NAME)
c.save(OUT + BASE + ".docx"); to_pdf(c, OUT + BASE + ".pdf", top=1.8)

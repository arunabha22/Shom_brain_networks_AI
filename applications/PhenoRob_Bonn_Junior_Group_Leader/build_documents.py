import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# PhenoRob, University of Bonn - Junior Research Group Leader (code 2026/397). Motivation letter, max 1 page.
# Facts only: PhD in progress (defence date placeholder), two published papers, no referees named here.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  |  "

c = new_doc()
c.sections[0].top_margin = Cm(1.6)
para(c, NAME, bold=True, size=16, after=0)
para(c, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark", "somrkmv1997@gmail.com",
                  "arunabha22.github.io/arunabha-majumder"]), size=9.5, after=8)
para(c, "October 12, 2026", after=6)
para(c, "Cluster of Excellence PhenoRob, University of Bonn", after=6)
para(c, "Motivation letter: Junior Research Group Leader (application code 2026/397)", bold=True, after=6)
para(c, "Dear Professor Kuhlmann and members of the selection committee,", after=6)
body = [
 "I am applying for one of the Junior Research Group Leader positions in PhenoRob. I am finishing my PhD in "
 "Mechatronics and Robotics at Aalborg University (defence expected in 2027), after an MTech in Mechatronics "
 "and a BTech in Mechanical Engineering. My work is on robots that physically touch living things, and I would like "
 "to build a group that brings that know-how to the field: robots that handle plants gently and measure them "
 "through contact.",

 "In my PhD I designed a hybrid-actuated shoulder exoskeleton, where a spring and a small 6 Nm motor share the load. "
 "It cut energy use by more than 25% and won the Best Research Paper Award at IFToMM ISRM 2026. On a 5-bar parallel "
 "robot I used variable-stiffness actuators and the robot Jacobian to estimate contact force without a sensor at the "
 "tip, within 10% RMS error of a force sensor, and we used it to measure human arm impedance in the gait lab. During "
 "my Master's at CSIR-CMERI I fabricated pneumatic artificial muscles and worked on the PID loop of a gain-scheduled "
 "controller that brought tracking error down to 0.3-0.78% (IEEE CONECCT 2022). I build my own prototypes and test rigs, and I have "
 "run experiments with 12 human participants.",

 "The idea behind my group would be compliant, low-energy actuation and contact sensing for crop robots. Two PhD "
 "projects could start it. The first would estimate stem and leaf stiffness from the robot's own actuators while it "
 "touches the plant, giving a new mechanical trait for phenotyping without extra sensors. The second would design "
 "energy-efficient compliant end effectors for selective handling and harvesting, tested in PhenoRob's field trials. "
 "Both fit the Cluster's work on robotic sensing and new cropping systems, and I give more detail in the attached "
 "concept.",

 "I will be honest that agriculture is a new field for me and that my publication record is still at an early "
 "stage. That is exactly why PhenoRob appeals to me: plant scientists, geodesists and roboticists sit in one "
 "cluster, and I would learn fast from them while bringing hardware and actuation skills that complement the "
 "existing perception and mapping strengths. I have supervised Bachelor's students since 2023, and I also draw. I "
 "hold a Diploma in Fine Arts and make my own figures and demonstrator visuals, which helps when explaining "
 "research to farmers, students and the public.",

 "Thank you for considering my application. I would be glad to discuss the group concept with you.",
]
for t in body:
    para(c, t, after=6)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Motivation_Letter_PhenoRob.docx")
to_pdf(c, OUT + "Arunabha_Majumder_Motivation_Letter_PhenoRob.pdf", top=1.6)

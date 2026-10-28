import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Körber Supply Chain DK, Arden - Lead Mechanical Engineer (7-10 yrs asked). Honest about the gap.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
BASE = "Arunabha_Majumder_Korber_Cover_Letter"

c = new_doc(); c.sections[0].top_margin = Cm(1.8)
para(c, NAME, bold=True, size=18, after=0)
para(c, "+45 71 62 24 00  |  Aalborg, Denmark", size=9.5, after=0)
para(c, "somrkmv1997@gmail.com  |  97arunabhasit027@gmail.com", size=9.5, after=0)
para(c, "Portfolio: arunabha22.github.io/arunabha-majumder", size=9.5, after=8)
para(c, "October 28, 2026", after=6)
para(c, "Körber Supply Chain DK, Arden", after=6)
para(c, "Application: Lead Mechanical Engineer", bold=True, after=6)
para(c, "Dear Hiring Team,", after=6)
for t in [
 "I am applying for the Lead Mechanical Engineer role in Arden. I live in Aalborg, so Arden is close by, and I would "
 "like to build my career in North Jutland. I am doing my PhD in Mechatronics and Robotics at Aalborg University, "
 "with my thesis expected to be finished in March. I know you are looking for 7 to 10 years in industry, and I do "
 "not have that. I still want to show you what I can bring to the table, because a lot of this role is about owning "
 "a mechanical system from concept to working hardware, and that is what I have done for the last 3 years.",
 "In my PhD I owned the mechanical design of a hybrid shoulder exoskeleton from the first hand sketch to tested "
 "hardware. A spring carries most of the arm load and a small 6 Nm motor adds the rest. I made the SolidWorks "
 "models and drawings, optimised the design with a genetic algorithm, integrated the motor, encoder and force "
 "sensors, and measured the stiffness it provides on a physical test setup. It cut energy use by more than 25% and "
 "won the Best Paper Award at IFToMM ISRM 2026. I also designed and modelled a novel 5-bar planar parallel robot "
 "with variable stiffness mechanisms, estimated its stiffness with less than 10% error and quantified human arm "
 "impedance. Robots that move with people have to be safe, so safety and risk were part of every design decision.",
 "On the leadership side, I have taught university courses and supervised Bachelor's students since 2023, guiding "
 "their projects and design choices. I ran test sessions with 12 participants, which meant planning, coordinating "
 "people and equipment, and keeping things on schedule. I worked closely with control, electronics and software "
 "colleagues to get our systems running as one. I also have a Diploma in Fine Arts, so I explain ideas with quick "
 "sketches, which helps a lot with customers and suppliers.",
 "I would understand if you see me as a step below a lead role today. If so, I would be glad to be considered for a "
 "mechanical engineer position in the team, where I can learn your automation systems, machinery directive work and "
 "projects, and grow into more responsibility. Thank you for reading, and I hope we can talk.",
]:
    para(c, t, after=6)
para(c, "Kind regards,", after=2); para(c, NAME)
c.save(OUT + BASE + ".docx"); to_pdf(c, OUT + BASE + ".pdf", top=1.8)

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# NewOrbit Space, Reading UK - Satellite Mechanical Design Engineer. No GD&T / PLM / space claims.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
BASE = "Arunabha_Majumder_NewOrbit_Cover_Letter"
c = new_doc(); c.sections[0].top_margin = Cm(1.8)
para(c, NAME, bold=True, size=18, after=0)
para(c, "+45 71 62 24 00  |  Aalborg, Denmark", size=9.5, after=0)
para(c, "somrkmv1997@gmail.com  |  97arunabhasit027@gmail.com", size=9.5, after=0)
para(c, "Portfolio: arunabha22.github.io/arunabha-majumder", size=9.5, after=8)
para(c, "November 2, 2026", after=6)
para(c, "NewOrbit Space, Reading, United Kingdom", after=6)
para(c, "Application: Satellite Mechanical Design Engineer", bold=True, after=6)
para(c, "Dear NewOrbit Space team,", after=6)
for t in [
 "I am applying for the Satellite Mechanical Design Engineer role. I am a mechanical and mechatronics engineer doing "
 "my PhD at Aalborg University, with my thesis expected to be finished in March. Flying a satellite at 200 km is a "
 "bold idea, and what I like most is that it can only work if every bracket, panel and cable route is designed with "
 "care. That is the kind of detailed hardware work I enjoy.",
 "For the last 3 years I have owned the mechanical design of a hybrid shoulder exoskeleton, from hand sketches to "
 "SolidWorks assemblies, drawings and working hardware. I optimised the design with a genetic algorithm, 3D printed "
 "and rebuilt the parts many times, routed and integrated the motor, encoder and force sensors, and measured the "
 "stiffness it provides on a physical test setup. Each round of testing fed back into the next design. It cut energy "
 "use by more than 25% and won the Best Paper Award at IFToMM ISRM 2026. I also designed and modelled a novel 5-bar "
 "planar parallel robot with variable stiffness mechanisms, estimated its stiffness with less than 10% error and "
 "quantified human arm impedance. In my Bachelor's I did the CAD, machining and assembly of a rehabilitation "
 "exoskeleton myself, so I know how a drawing turns into a real part.",
 "SolidWorks is my main tool (CSWA), and I am used to keeping assemblies tidy while a design keeps changing. I work "
 "closely with control, electronics and software colleagues, and I explain my design choices clearly, often with a "
 "quick sketch, since I also hold a Diploma in Fine Arts.",
 "I want to be honest about the gaps. I have not designed space hardware, and I have not yet used GD&T or PLM systems "
 "like 3DEXPERIENCE in a formal change process. I learn quickly, and I would really like to learn these from an "
 "experienced team building real satellites.",
 "Thank you for considering my application. You can see my work at arunabha22.github.io/arunabha-majumder.",
]:
    para(c, t, after=6)
para(c, "Kind regards,", after=2); para(c, NAME)
c.save(OUT + BASE + ".docx"); to_pdf(c, OUT + BASE + ".pdf", top=1.8)

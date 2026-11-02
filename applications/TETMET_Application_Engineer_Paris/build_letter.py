import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# TETMET Paris - Application Engineer (lattice structures). 5+ yrs + ANSYS/LS-DYNA asked; honest gap.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
BASE = "Arunabha_Majumder_TETMET_Cover_Letter"
c = new_doc(); c.sections[0].top_margin = Cm(1.8)
para(c, NAME, bold=True, size=18, after=0)
para(c, "+45 71 62 24 00  |  Aalborg, Denmark", size=9.5, after=0)
para(c, "somrkmv1997@gmail.com  |  97arunabhasit027@gmail.com", size=9.5, after=0)
para(c, "Portfolio: arunabha22.github.io/arunabha-majumder", size=9.5, after=8)
para(c, "November 2, 2026", after=6)
para(c, "TETMET, Paris (La Défense)", after=6)
para(c, "Application: Application Engineer", bold=True, after=6)
para(c, "Dear TETMET team,", after=6)
for t in [
 "I am applying for the Application Engineer role in Paris. I am a mechanical and mechatronics engineer doing my PhD "
 "at Aalborg University, with my thesis expected to be finished in March. Lattice structures caught my attention "
 "because they sit right where I like to work: designing a light structure, printing it, and then finding out on a "
 "real test setup whether it behaves the way you planned.",
 "In my PhD I designed a hybrid shoulder exoskeleton that has to be light and stiff at the same time, because a "
 "person wears it. I modelled it in SolidWorks, optimised the design with a genetic algorithm, 3D printed and rebuilt "
 "the parts many times, and measured the stiffness it provides on a physical test setup. It cut energy use by more "
 "than 25% and won the Best Paper Award at IFToMM ISRM 2026. I also designed and modelled a novel 5-bar planar "
 "parallel robot with variable stiffness mechanisms, estimated its stiffness with less than 10% error and quantified "
 "human arm impedance. I have also done stiffness analysis in SolidWorks, and I use MATLAB and basic Python for data "
 "and calculations.",
 "I want to be honest about the gaps. I do not have 5 years in industry, and I have not used ANSYS Workbench, "
 "LS-DYNA or Rhino/Grasshopper yet. What I bring is a solid base in stiffness, optimisation and physical testing, "
 "and a lot of hands-on 3D printing. I also hold a Diploma in Fine Arts, so I explain designs clearly to clients "
 "with sketches. I learn new tools quickly, and I would be glad to grow into simulation work in your team.",
 "Thank you for considering my application. You can see my work at arunabha22.github.io/arunabha-majumder.",
]:
    para(c, t, after=6)
para(c, "Kind regards,", after=2); para(c, NAME)
c.save(OUT + BASE + ".docx"); to_pdf(c, OUT + BASE + ".pdf", top=1.8)

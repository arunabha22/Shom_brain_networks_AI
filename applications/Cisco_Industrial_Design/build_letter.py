import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Cisco - Industrial Design (no ad text given; general). Leads with fine arts + engineering. No Rhino/KeyShot claims.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
BASE = "Arunabha_Majumder_Cisco_Industrial_Design_Cover_Letter"
c = new_doc(); c.sections[0].top_margin = Cm(1.8)
para(c, NAME, bold=True, size=18, after=0)
para(c, "+45 71 62 24 00  |  Aalborg, Denmark", size=9.5, after=0)
para(c, "somrkmv1997@gmail.com  |  97arunabhasit027@gmail.com", size=9.5, after=0)
para(c, "Portfolio: arunabha22.github.io/arunabha-majumder", size=9.5, after=8)
para(c, "Cisco, Industrial Design team", after=6)
para(c, "Application: Industrial Design", bold=True, after=6)
para(c, "Dear Hiring Team,", after=6)
for t in [
 "I am applying for the Industrial Design role at Cisco. I am a mechanical and mechatronics engineer doing my PhD at "
 "Aalborg University, and I also hold a Senior Diploma in Fine Arts in painting, which I earned with Distinction. I "
 "have always lived between these two worlds: I care how a product looks and feels in someone's hands as much as how "
 "it works inside. Industrial design is where both of those matter every day.",
 "Most of my ideas start as hand sketches. In my PhD I designed a shoulder exoskeleton that people wear on their "
 "body, so comfort, fit and how it looks were as important as strength. I took it from sketches to SolidWorks models "
 "and drawings, 3D printed and rebuilt the parts many times, and changed the design after testing it with 12 people. "
 "It won the Best Paper Award at IFToMM ISRM 2026. When my first clutch design kept breaking and was hard to make, I "
 "replaced it with a simpler part that was easier to produce, which taught me that good design has to be buildable.",
 "I make the visuals for my papers, posters and demos in Adobe Illustrator, Photoshop and Procreate, and I am used to "
 "explaining design choices to engineers, clinicians and students. With my engineering background, I can work "
 "closely with mechanical and electronics teams so a design stays true to its look while still fitting the hardware, "
 "cooling and manufacturing needs.",
 "I want to be honest that my training is in engineering and fine arts rather than an industrial design degree, and "
 "I have not yet designed networking or consumer electronics products. I learn quickly, and I would bring a rare mix "
 "of hand sketching, CAD and hands-on prototyping to your team.",
 "Thank you for considering my application. You can see my work at arunabha22.github.io/arunabha-majumder.",
]:
    para(c, t, after=6)
para(c, "Kind regards,", after=2); para(c, NAME)
c.save(OUT + BASE + ".docx"); to_pdf(c, OUT + BASE + ".pdf", top=1.8)

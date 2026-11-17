import os, sys, importlib.util
APPS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, APPS)
spec = importlib.util.spec_from_file_location("e2m", os.path.join(APPS, "E2M_Technologies_Mechanical_Engineer", "build_documents.py"))
e = importlib.util.module_from_spec(spec); spec.loader.exec_module(e)
from reportlab.platypus import SimpleDocTemplate, HRFlowable
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
P, NAME, ACC, ACC2, BLACK, W, H = e.P, e.NAME, e.ACC, e.ACC2, e.BLACK, e.W, e.H

# VELUX (Hørsholm, Denmark) - CAD Specialist. Ad text could not be fetched; listing snippet: CAD/PDM work in
# SolidWorks and Creo/Windchill. Not claimed: Creo, Windchill, PDM/PLM admin, CAD certification beyond CSWA.
# His rules: no clutch story, no gap paragraph, no German line, portfolio, ends with innovative ideas.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"

PARAS = [
    "I'd like to apply for the CAD Specialist role at VELUX. I have worked in SolidWorks since my Bachelor's, and "
    "CAD is the part of engineering I enjoy most. It's where an idea turns into something you can actually make. "
    "VELUX makes products people live with every day, and I would like my models to end up in something like that.",
    "As a research assistant at Aalborg University I designed a hybrid shoulder exoskeleton. I made the full "
    "SolidWorks model, from the single parts to the assembly and the technical drawings, and changed it many times "
    "as the design moved on. I optimised the mechanism with a genetic algorithm, 3D printed the first parts to "
    "check the fit, and then sent drawings out so the final parts could be manufactured. It uses over 25% less "
    "motor energy and won the Best Paper Award at ISRM 2026. I also designed and modelled a novel 5-bar planar "
    "parallel robot with variable stiffness mechanisms (VSM), estimated its stiffness with less than 10% error and "
    "quantified human arm impedance.",
    "My parts went back and forth between 3D printing, the workshop and testing, so I kept the models and "
    "drawings in step with each change. I'm a Certified SolidWorks Associate (CSWA). I also taught university "
    "courses and supervised Bachelor's students from 2023 to 2025.",
    "I also hold a Senior Diploma in Fine Arts (Painting) and do graphic design and illustration in Illustrator, "
    "Photoshop and Procreate. I sketch most ideas by hand before I open CAD, and I make the drawings and visuals "
    "for my papers and posters myself.",
    "I would love to bring new and innovative ideas to the way VELUX models its products, and to learn your tools "
    "and standards from the people who use them every day. My portfolio, with videos and results from my work, is "
    "at arunabha22.github.io/arunabha-majumder. Thank you for reading.",
]

def letter():
    path = OUT + "AM VELUX Cover Letter.pdf"
    head = [P(NAME, size=18, bold=True, color=ACC, after=1, lead=1.1),
            P("+45 71 62 24 00 &nbsp;|&nbsp; Aalborg, Denmark", size=9, after=0),
            P("somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com", size=9, after=0),
            P("Portfolio: arunabha22.github.io/arunabha-majumder", size=9, after=4),
            HRFlowable(width="100%", thickness=1.1, color=ACC2, spaceBefore=2, spaceAfter=10),
            P("VELUX A/S, Hørsholm", size=10, after=3),
            P("<b>CAD Specialist</b>", size=10.5, color=BLACK, after=10),
            P("Dear VELUX hiring team,", size=10.5, color=BLACK, after=6)]
    body = [P(t, size=10.1, color=BLACK, after=7, lead=1.32) for t in PARAS] + [
        P("Best,", size=10.1, color=BLACK, after=2), P(NAME, size=10.1, color=BLACK)]
    def deco(c, d):
        c.saveState(); c.setFillColor(ACC); c.rect(0, H - 0.35 * cm, W, 0.35 * cm, stroke=0, fill=1)
        c.rect(0, 0, W, 0.2 * cm, stroke=0, fill=1); c.restoreState()
    SimpleDocTemplate(path, pagesize=A4, leftMargin=2.1 * cm, rightMargin=2.1 * cm, topMargin=1.8 * cm,
                      bottomMargin=1.5 * cm, title="AM VELUX Cover Letter", author=NAME, creator=NAME,
                      producer=NAME, subject="", keywords="").build(head + body, onFirstPage=deco)
    return path

if __name__ == "__main__":
    print(letter())

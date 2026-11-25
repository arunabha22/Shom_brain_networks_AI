import os, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)) + "/"
APPS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("t", os.path.join(APPS, "Sample_New_Format", "build_sample.py"))
t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
from reportlab.platypus import SimpleDocTemplate, Spacer, HRFlowable
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
P, NAME, ACC, ACC2, BLACK, W, H = t.P, t.NAME, t.ACC, t.ACC2, t.BLACK, t.W, t.H
# VeroTech (engineering consultancy, Belgium) - Mechanical Design Engineer Robotics. Story-based letter, his request
# 2026-11-25. Scored ~55 (5 yrs, FEA, GD&T, casting not claimed). Relocate Belgium (confirmed). Letter only.
TITLE = ("Mechanical engineer with 6 years of experience designing robot mechanisms and actuators and testing them "
         "on real hardware")
PARAS = [
    "I still remember the day the measurements came back from my shoulder exoskeleton. For months it had only "
    "existed as a SolidWorks model, a few 3D printed parts and a lot of calculations. Then the final aluminium parts "
    "arrived from the manufacturer, I fitted the motor, the encoder and the sensors, and ran the first real tests. "
    "The motor was using over 25% less energy than it would on its own, because the spring mechanism I designed was "
    "carrying part of the load. That moment is why I love mechanical design: an idea on a screen becomes a mechanism "
    "you can hold, test and improve.",
    "I am a mechanical engineer in the final stage of my PhD in Mechatronics and Robotics at Aalborg University, and "
    "I feel qualified for this role because the mechanics behind motion is what I have worked on for the last six "
    "years. In the exoskeleton, a variable stiffness spring mechanism, pretensioned by a worm gear, works in parallel "
    "with a 6 Nm motor. I optimised it with a genetic algorithm, made the drawings and BOM, and worked with an "
    "external manufacturer to have the parts CNC machined and assembled. Then I tested it on a physical setup, "
    "compared the results with my model and changed the design where the tests told me to. It won the Best Paper "
    "Award at ISRM 2026. I also designed and modelled a novel 5-bar planar parallel robot with variable stiffness "
    "mechanisms (VSM), estimated its stiffness with less than 10% error, and quantified human arm impedance.",
    "What draws me to VeroTech is the variety. As a consultant I would work on robots for different industries, from "
    "concept to production, always close to the people who build and test them. I learned the hard way that where "
    "you place a motor or a sensor can make or break a design, and that you only find out by testing. I would like "
    "to bring that build-and-test habit to your projects. I also hold a Senior Diploma in Fine Arts and do graphic "
    "design in Illustrator, Photoshop and Procreate, which helps me sketch concepts quickly and explain them clearly "
    "to clients and colleagues.",
    "I would be excited to bring my experience with actuators and mechanisms, my hands-on way of prototyping and "
    "testing, and new ideas to your robotics team.",
    "I am in the final stage of my PhD. My research is done, and I am available to move into an industrial "
    "engineering role while I finish my thesis. I am happy to relocate to Belgium.",
    "Thank you for your time. I look forward to hearing from you.",
]
def letter(size=10.0):
    path = HERE + "AM VeroTech Cover Letter.pdf"
    head = [P(NAME, size=22, bold=True, color=ACC, after=3, lead=1.1),
            P(TITLE, size=11.5, bold=True, color=ACC2, after=4, lead=1.25),
            HRFlowable(width="100%", thickness=1.1, color=ACC2, spaceBefore=2, spaceAfter=10),
            P("<b>Application for Mechanical Design Engineer Robotics</b>", size=11.5, color=BLACK, after=7),
            P("Dear Hiring Team,", size=10.5, color=BLACK, after=6)]
    body = [P(x, size=size, color=BLACK, after=7, lead=1.34) for x in PARAS] + [
        Spacer(0, 3), P("Best regards,", size=size, color=BLACK, after=2),
        P("<b>%s</b>" % NAME, size=10.5, color=BLACK, after=2),
        P("+45 71 62 24 00 &nbsp;|&nbsp; somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com &nbsp;|&nbsp; "
          "arunabha22.github.io/arunabha-majumder", size=8.6, after=0)]
    def deco(c, d):
        c.saveState(); c.setFillColor(ACC); c.rect(0, H - 0.35 * cm, W, 0.35 * cm, stroke=0, fill=1)
        c.rect(0, 0, W, 0.2 * cm, stroke=0, fill=1); c.restoreState()
    SimpleDocTemplate(path, pagesize=A4, leftMargin=2.0 * cm, rightMargin=2.0 * cm, topMargin=1.6 * cm,
                      bottomMargin=1.3 * cm, title="Arunabha Majumder Cover Letter", author=NAME, creator=NAME,
                      producer=NAME, subject="", keywords="").build(head + body, onFirstPage=deco)
    return path
if __name__ == "__main__":
    p = letter(); t.shrink(p); print(p)

import os, sys, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)) + "/"
spec = importlib.util.spec_from_file_location("sdu", HERE + "build_documents.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
from reportlab.platypus import SimpleDocTemplate, HRFlowable, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
P, NAME, ACC, ACC2, BLACK, W, H = m.P, m.NAME, m.ACC, m.ACC2, m.BLACK, m.W, m.H

def deco(c, d):
    c.saveState(); c.setFillColor(ACC); c.rect(0, H - 0.35 * cm, W, 0.35 * cm, stroke=0, fill=1)
    c.rect(0, 0, W, 0.2 * cm, stroke=0, fill=1); c.restoreState()

def head(title):
    return [P(NAME, size=22, bold=True, color=ACC, after=3, lead=1.1),
            P(title, size=11.5, bold=True, color=ACC2, after=4, lead=1.25),
            HRFlowable(width="100%", thickness=1.1, color=ACC2, spaceBefore=2, spaceAfter=10),
            P("<b>Postdoc in Mechatronic Design for Remotely Operated Vehicles, SDU Sønderborg</b>", size=10.5,
              color=BLACK, after=10)]

def h2(t): return P("<b>%s</b>" % t, size=11, color=ACC, after=4, lead=1.2)
def para(t): return P(t, size=10.1, color=BLACK, after=7, lead=1.36)
def foot():
    return [Spacer(0, 6), P("<b>%s</b>" % NAME, size=10, color=BLACK, after=2),
            P("+45 71 62 24 00 &nbsp;|&nbsp; somrkmv1997@gmail.com &nbsp;|&nbsp; 97arunabhasit027@gmail.com &nbsp;|&nbsp; "
              "arunabha22.github.io/arunabha-majumder", size=8.6, after=0)]

def build(path, story, title):
    SimpleDocTemplate(path, pagesize=A4, leftMargin=2.1 * cm, rightMargin=2.1 * cm, topMargin=1.8 * cm,
                      bottomMargin=1.5 * cm, title=title, author=NAME, creator=NAME, producer=NAME, subject="",
                      keywords="").build(story, onFirstPage=deco, onLaterPages=deco)
    return path

def research_statement():
    s = head("Research Statement")
    s += [h2("My research so far"), para(
        "My research is about designing, building and testing actuated systems that work with the human body. In my "
        "PhD at Aalborg University I designed a hybrid shoulder exoskeleton, where a variable stiffness mechanism, "
        "pretensioned by a worm gear transmission, works in parallel with a 6 Nm motor. I optimised the mechanism "
        "with a genetic algorithm (diameter, spring stiffness and pretension force), modelled it in SolidWorks, 3D "
        "printed the first parts for testing and had the final parts manufactured. I integrated the motor, encoder "
        "and force/torque sensors and measured its stiffness on a physical test setup. The design uses over 25% less "
        "motor energy and won the Best Paper Award at IFToMM ISRM 2026."), para(
        "I also designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms (VSM), "
        "estimated its stiffness with less than 10% error and quantified human arm impedance. Force was estimated "
        "from the variable stiffness actuators and the robot's Jacobian. In the arm impedance study (6 participants) "
        "Qualisys cameras recorded arm position data, and I implemented an Arduino-based trigger to sync the robot's "
        "motion with the recording. In the exoskeleton study I collected EMG data from 12 participants with Qualisys."),
        para(
        "Before my PhD, at CSIR-CMERI in India, I fabricated silicone pneumatic artificial muscles for a soft exosuit in "
        "a team of four and designed the outer PID loop, with integral anti-windup and error nonlinearisation, of a "
        "neural network-based gain-scheduled controller in MATLAB/Simulink, implemented in LabVIEW (0.3 to 0.78% "
        "error, IEEE CONECCT 2022).")]
    s += [h2("How I work"), para(
        "I start with a hand sketch and simple calculations, move to CAD, and build a first prototype as early as "
        "possible. Then I test it on a real setup, measure what happens, and change the design. I trust measurements "
        "more than my first guess: my exoskeleton saved much more energy on the bench than with people wearing it, and "
        "that gap told me where the design really stood. I like research that ends in working hardware.")]
    s += [h2("What I would like to work on at CIM"), para(
        "Subsea robots face the same core questions as my research, only in a harder place: how to make actuators "
        "and transmissions that are efficient, reliable and testable. These are ideas I would like to explore with "
        "the team:"),
        para("<b>Energy-efficient actuation.</b> Combining passive elements such as springs with motors, as in my "
             "exoskeleton, could reduce the energy that ROV joints or manipulators use, which matters for battery and "
             "tether limits."),
        para("<b>Compliance and variable stiffness.</b> A manipulator that can change its stiffness may handle contact "
             "with objects and disturbances from currents more safely. My work on variable stiffness mechanisms and "
             "stiffness estimation is a starting point for this."),
        para("<b>Design optimisation with real constraints.</b> I used a genetic algorithm to choose mechanism "
             "parameters. The same approach could help size transmissions, structures and enclosures where weight, "
             "space and pressure all limit the design."),
        para("<b>Testing and data.</b> Building test setups with synced data acquisition, as I did with Qualisys and "
             "the 5-bar robot, to compare models with lab and field measurements.")]
    s += [h2("Where I want to grow"), para(
        "I want to learn subsea engineering from the people at CIM, publish together with the team, and become a "
        "researcher who can take a mechatronic system from idea to a tested platform. I would also be happy to help "
        "students on their projects, as I did with Bachelor's students in Aalborg.")]
    s += foot()
    return build(HERE + "AM SDU Research Statement.pdf", s, "AM SDU Research Statement")

def publications():
    s = head("List of Publications")
    s += [para("Publications most relevant to this position are marked <b>[Most relevant]</b>."),
          h2("Conference papers"),
          para("<b>[Most relevant]</b> Hybrid actuated shoulder exoskeleton. IFToMM International Symposium on Robotics "
               "and Mechatronics (ISRM 2026), Springer. <b>Best Paper Award.</b><br/>Relevance: actuation mechanism "
               "with a worm gear transmission and a motor, genetic algorithm design optimisation, sensor integration "
               "and experimental validation."),
          para("Neural network-based control of a pneumatic artificial muscle. IEEE International Conference on "
               "Electronics, Computing and Communication Technologies (CONECCT 2022).<br/>Relevance: pneumatic "
               "actuation, control hardware and experimental testing.")]
    s += foot()
    return build(HERE + "AM SDU Publications.pdf", s, "AM SDU Publications")

if __name__ == "__main__":
    for p in (research_statement(), publications()):
        print(p)

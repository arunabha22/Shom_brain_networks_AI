import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# UCD Electrical and Electronic Engineering - Robotics Research Engineer, CEREBRIS (ref 020149).
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
BASE = "Arunabha_Majumder_UCD_Cover_Letter"

c = new_doc(); c.sections[0].top_margin = Cm(1.8)
para(c, NAME, bold=True, size=18, after=0)
para(c, "+45 71 62 24 00  |  Aalborg, Denmark", size=9.5, after=0)
para(c, "somrkmv1997@gmail.com  |  97arunabhasit027@gmail.com", size=9.5, after=0)
para(c, "Portfolio: arunabha22.github.io/arunabha-majumder", size=9.5, after=8)
para(c, "October 26, 2026", after=6)
para(c, "School of Electrical and Electronic Engineering, University College Dublin", after=6)
para(c, "Application: Robotics Research Engineer, CEREBRIS Project (Ref. 020149)", bold=True, after=6)
para(c, "Dear Hiring Committee,", after=6)
for t in [
 "I am applying for the Robotics Research Engineer role on the CEREBRIS project. I am finishing my PhD in "
 "Mechatronics and Robotics at Aalborg University (thesis expected to be finished in March), and almost all my work so far has been "
 "robots that physically touch and move people. Building a robotic stimulator that helps measure how sensation "
 "comes back after a stroke is exactly the kind of work I want to keep doing.",
 "In my PhD I designed a hybrid shoulder exoskeleton where a spring carries most of the arm load and a small 6 Nm "
 "motor adds the rest. I did the design in SolidWorks, 3D printed and rebuilt the parts many times, and integrated "
 "the motor, encoder and force sensors myself. It cut energy use by more than 25% and won the Best Paper Award at "
 "IFToMM ISRM 2026. I also worked with a 5-bar planar parallel robot that interacts with the human arm. I estimated "
 "the force at its tip from the variable-stiffness actuators, within 10% RMS error of a force sensor, and built an "
 "Arduino-based trigger to sync the robot's motion with Qualisys motion capture for arm tests with 6 participants.",
 "I am used to working with people in the loop. I collected EMG and motion data from 12 participants in our "
 "exoskeleton study, and I know how much care it takes to make a session safe, repeatable and comfortable for the "
 "person in the device. My first rehab robot was an upper-limb exoskeleton in my Bachelor's, where I did the CAD, "
 "machining and assembly. In my Master's I worked on pneumatic artificial muscles and designed the outer PID loop of "
 "a gain-scheduled controller in MATLAB/Simulink (IEEE CONECCT 2022).",
 "I have not worked on sensory testing after stroke yet, and I would be keen to learn that side from the clinical "
 "partners. What I can bring is hands-on robot hardware, sensor integration and careful human testing. I also have "
 "a Diploma in Fine Arts and I make the sketches and visuals for our papers and demos, which helps when explaining "
 "a device to clinicians or patients.",
 "Thank you for considering my application. My portfolio is at arunabha22.github.io/arunabha-majumder.",
]:
    para(c, t, after=6)
para(c, "Kind regards,", after=2); para(c, NAME)
c.save(OUT + BASE + ".docx"); to_pdf(c, OUT + BASE + ".pdf", top=1.8)

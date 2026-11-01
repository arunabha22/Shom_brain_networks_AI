import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# DLR Institute of Vehicle Concepts, Oberpfaffenhofen - control/learning for by-wire vehicles (Vacancy-ID 6202).
# No RL / LLM / automotive claims. NN was someone else's; he did the outer PID loop.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
BASE = "Arunabha_Majumder_DLR_6202_Cover_Letter"

c = new_doc(); c.sections[0].top_margin = Cm(1.8)
para(c, NAME, bold=True, size=18, after=0)
para(c, "+45 71 62 24 00  |  Aalborg, Denmark", size=9.5, after=0)
para(c, "somrkmv1997@gmail.com  |  97arunabhasit027@gmail.com", size=9.5, after=0)
para(c, "Portfolio: arunabha22.github.io/arunabha-majumder", size=9.5, after=8)
para(c, "November 1, 2026", after=6)
para(c, "German Aerospace Center (DLR), Institute of Vehicle Concepts, Oberpfaffenhofen", after=0)
para(c, "Attn: Dr. Jonathan Brembeck", after=6)
para(c, "Application: Vacancy-ID 6202, model- and learning-based control for by-wire vehicles", bold=True, after=6)
para(c, "Dear Dr. Brembeck,", after=6)
for t in [
 "I am applying for the position on model- and learning-based simulation and control methods for robotic electric "
 "vehicles (Vacancy-ID 6202). I am a mechatronics and robotics engineer doing my PhD at Aalborg University, with my "
 "thesis expected to be finished in March. What I enjoy most is the step where a control method leaves the "
 "computer and has to work on real hardware on a test bed. That is exactly what this role is about.",
 "Control of nonlinear mechatronic systems has been part of my work from the start. In my Master's at CSIR-CMERI I "
 "worked on a pneumatic artificial muscle, which is a strongly nonlinear actuator. I designed the outer PID loop of "
 "a neural network-based gain-scheduled controller in MATLAB/Simulink and implemented it in LabVIEW to drive the "
 "muscle, reaching 0.3 to 0.78% position error (IEEE CONECCT 2022). In my PhD I designed a hybrid shoulder "
 "exoskeleton, optimised the design with a genetic algorithm, and tested it on a physical setup and with 12 "
 "participants. In a team of 3 I helped with the equations, such as the Fourier fit, for an Assist-as-Needed "
 "controller. I also designed and modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms, "
 "estimated its stiffness with less than 10% error and quantified human arm impedance.",
 "I am used to testing methods on real hardware and judging them with numbers. I integrate motors, encoders and "
 "force sensors, build test setups, and implemented an Arduino-based trigger system to synchronise robot motion "
 "with Qualisys motion capture. My work on the exoskeleton won the Best Paper Award at IFToMM ISRM 2026, and I am "
 "comfortable writing for journals and conferences.",
 "I want to be honest about the gaps. I have not yet developed reinforcement learning or LLM-based toolchains "
 "myself, and I have not worked on vehicles. My Python is basic, while MATLAB/Simulink is my main tool. I learn "
 "quickly when I can test ideas on a real system, and I would really like to build these skills in your team.",
 "Thank you for considering my application. You can see my work at arunabha22.github.io/arunabha-majumder.",
]:
    para(c, t, after=6)
para(c, "Kind regards,", after=2); para(c, NAME)
c.save(OUT + BASE + ".docx"); to_pdf(c, OUT + BASE + ".pdf", top=1.8)

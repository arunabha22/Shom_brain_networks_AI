import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# General data scientist cover letter. Honest: data collection (not analysis) in the 12-person study; basic Python;
# NN was someone else's; he fed it data and designed the outer PID loop. No journal mentions.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
BASE = "Cover_Letter_Data_Scientist_Arunabha_Majumder"
c = new_doc(); c.sections[0].top_margin = Cm(1.8)
para(c, NAME, bold=True, size=18, after=0)
para(c, "+45 71 62 24 00  |  Aalborg, Denmark", size=9.5, after=0)
para(c, "somrkmv1997@gmail.com  |  97arunabhasit027@gmail.com", size=9.5, after=0)
para(c, "Portfolio: arunabha22.github.io/arunabha-majumder", size=9.5, after=8)
para(c, "Application: Data Scientist", bold=True, after=6)
para(c, "Dear Hiring Team,", after=6)
for t in [
 "I am applying for the Data Scientist position. I am a mechatronics and robotics engineer doing my PhD at Aalborg "
 "University, with my thesis expected to be finished in March. My work has always been close to real data from real "
 "systems: collecting it carefully, cleaning it, and using it to make decisions about a design.",
 "In my PhD I collected EMG and motion data from 12 participants for a shoulder exoskeleton study, using the Qualisys "
 "data acquisition system and motion capture cameras. For a second study with 6 participants, I implemented an "
 "Arduino-based trigger system to synchronise a robot's motion with the Qualisys recording, so data from different "
 "systems lined up in time. I designed and modelled a novel 5-bar planar parallel robot with variable stiffness "
 "mechanisms, estimated its stiffness with less than 10% error and quantified human arm impedance. I also optimised "
 "my exoskeleton design with a genetic algorithm.",
 "In my Master's I fed experimental data from a pneumatic artificial muscle into a neural network developed by a "
 "colleague, and used its output to design the outer PID loop of a gain-scheduled controller in MATLAB/Simulink, "
 "reaching 0.3 to 0.78% position error (IEEE CONECCT 2022). That taught me how much a model depends on the quality "
 "of the data behind it.",
 "I want to be honest that my main tool is MATLAB, and my Python is at a basic level. I have not yet built machine "
 "learning models from scratch in industry. What I bring is a solid base in measurement, modelling and optimisation, "
 "and a careful way of working with data. I learn quickly, and I would like to grow my Python and machine learning "
 "skills in your team. I also present results clearly, from teaching university courses and writing papers.",
 "Thank you for considering my application. You can see my work at arunabha22.github.io/arunabha-majumder.",
]:
    para(c, t, after=6)
para(c, "Kind regards,", after=2); para(c, NAME)
c.save(OUT + BASE + ".docx"); to_pdf(c, OUT + BASE + ".pdf", top=1.8)

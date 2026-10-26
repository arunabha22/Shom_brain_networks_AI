import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# General cover letter for data engineering roles. Facts from Arunabha (Oct 2026): Qualisys DAQ for EMG in the
# exoskeleton study (16 participants, journal paper 3, under review); Qualisys cameras for arm motion to quantify
# impedance with the 5-bar robot (6 participants, journal paper 2, under review). Data collection, not analysis.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  |  "

c = new_doc(); c.sections[0].top_margin = Cm(1.8)
para(c, NAME, bold=True, size=18, after=0)
para(c, "Engineer | Experimental Data Acquisition, Sensor Data, Python and MATLAB", bold=True, size=11, after=2)
para(c, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark"]), size=9.5, after=0)
para(c, SEP.join(["somrkmv1997@gmail.com", "97arunabhasit027@gmail.com",
                  "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=8)
para(c, "Application: Data Engineer", bold=True, after=6)
para(c, "Dear Hiring Team,", after=6)
for t in [
 "I am applying for the Data Engineer position. I am finishing my PhD in Mechatronics and Robotics at Aalborg "
 "University, and I hold an MTech in Mechatronics and a BTech in Mechanical Engineering. My PhD ends in March.",
 "A big part of my PhD has been getting good data out of real experiments. For my shoulder exoskeleton study, I "
 "used the Qualisys data acquisition system to record EMG from 16 participants across different assistance modes "
 "and loads. In a second study, I used Qualisys motion-capture cameras to track arm motion while people interacted "
 "with a 5-bar planar parallel robot, so we could quantify human arm impedance with 6 participants. Both datasets "
 "are behind two journal papers that are now under review.",
 "That work taught me what data engineering looks like in practice. EMG, motion capture and robot sensor data all "
 "come in at different rates, from different systems, and they only make sense if they are recorded, labelled and "
 "stored carefully for every session. I set up the recordings, kept the data organised per participant and "
 "condition, and made sure it was ready for the people doing the analysis. I work in Python and MATLAB.",
 "I want to be honest that my background is experimental and hardware-focused. I have not yet built production "
 "data pipelines with tools like SQL databases or cloud platforms, and I would like to learn them in a team that "
 "works with real sensor data.",
 "Thank you for considering my application. I would be glad to talk about how my experience with sensor data "
 "could help your team.",
]:
    para(c, t, after=6)
para(c, "Kind regards,", after=2); para(c, NAME)
c.save(OUT + "Cover_Letter_Data_Engineering_Arunabha_Majumder.docx")
to_pdf(c, OUT + "Cover_Letter_Data_Engineering_Arunabha_Majumder.pdf", top=1.8)

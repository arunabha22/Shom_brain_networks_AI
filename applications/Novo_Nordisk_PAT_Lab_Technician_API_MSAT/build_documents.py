import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Novo Nordisk - Advanced Laboratory Technician, PAT Team, API MSAT (345584). Ad text not provided; no PAT/GMP claims.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
BASE = "Arunabha_Majumder_Novo_Nordisk_PAT_Cover_Letter"

c = new_doc(); c.sections[0].top_margin = Cm(1.8)
para(c, NAME, bold=True, size=18, after=0)
para(c, "+45 71 62 24 00  |  Aalborg, Denmark", size=9.5, after=0)
para(c, "somrkmv1997@gmail.com  |  97arunabhasit027@gmail.com", size=9.5, after=0)
para(c, "Portfolio: arunabha22.github.io/arunabha-majumder", size=9.5, after=8)
para(c, "November 1, 2026", after=6)
para(c, "Novo Nordisk A/S, API MSAT", after=6)
para(c, "Application: Advanced Laboratory Technician for PAT Team in API MSAT (345584)", bold=True, after=6)
para(c, "Dear Hiring Manager,", after=6)
for t in [
 "I am applying for the Advanced Laboratory Technician role in the PAT team. I am a mechanical and mechatronics "
 "engineer doing my PhD at Aalborg University, with my thesis expected to be finished in March. Most of my best "
 "days have been in the lab, setting up equipment, getting sensors to give clean data and finding out why a "
 "measurement looks wrong. That is why a hands-on lab role in process analytics appeals to me.",
 "In my PhD I built and ran test setups for a shoulder exoskeleton and a 5-bar robot. I integrated motors, "
 "encoders and force sensors, measured the stiffness of the exoskeleton on a physical test setup, and recorded EMG "
 "and motion data from 12 participants with the Qualisys data acquisition system. I implemented an Arduino-based "
 "trigger system to synchronise the robot's motion with the Qualisys recording, so the data from different systems "
 "lined up correctly. I process my data in MATLAB, and in my Master's I implemented a controller in LabVIEW to "
 "drive a pneumatic muscle on the lab's test setup. I am used to careful, repeatable work, keeping clear notes and "
 "writing reports that others can follow.",
 "I want to be honest that I have not worked with PAT instruments such as spectroscopy, or in a GMP environment "
 "yet. I learn new equipment quickly when I can work with it every day, and I would like to grow into this field "
 "with your team. I have also taught university courses and supervised students, so I am comfortable explaining "
 "methods and supporting colleagues.",
 "Thank you for considering my application. I would be glad to talk more about how I can help the PAT team.",
]:
    para(c, t, after=6)
para(c, "Kind regards,", after=2); para(c, NAME)
c.save(OUT + BASE + ".docx"); to_pdf(c, OUT + BASE + ".pdf", top=1.8)

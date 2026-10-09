import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Humanoid (London) - Prototype Engineer, end effectors + human-worn devices. Corrected facts only:
# PhD = SolidWorks + 3D printing; machining + assembly = Bachelor's. No ESP32/RPi/soldering/harness claimed.
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  |  "

d = new_doc()
para(d, NAME, bold=True, size=18, after=0)
para(d, "Prototype Engineer | Wearable Robot Hardware, Test Rigs, 3D Printing and Assembly", bold=True,
     size=11, after=2)
para(d, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark (open to relocating to London)",
                  "somrkmv1997@gmail.com", "97arunabhasit027@gmail.com"]), size=9.5, after=0)
para(d, SEP.join(["LinkedIn: linkedin.com/in/arunabha-majumder-681264107",
                  "Portfolio: arunabha22.github.io/arunabha-majumder", "Project: www.viexo.aau.dk"]),
     size=9.5, after=6)

heading(d, "Summary")
para(d, "I build robot hardware that people wear, and the rigs to test it. For three years I have turned my own "
        "CAD files into working shoulder exoskeleton units: printing the parts, putting in the motor, encoder and "
        "sensors, fixing what failed, and running it with real users in trials. I like a messy bench that "
        "produces a working part by Friday. SolidWorks (CSWA), 3D printing, Arduino, MATLAB and Python.")

heading(d, "Key Results")
bullet(d, " human trial participants run on hardware I built and kept working", "12")
bullet(d, " less energy from the spring and motor exoskeleton I designed and built (Best Paper, 2026)", ">25%")
bullet(d, " force error on a test setup I built, checked against a force sensor", "<10%")

heading(d, "Experience")
role(d, "Research Engineer, Wearable Robot Prototypes (PhD project VIEXO)", "2023 - Present",
     "Aalborg University, Aalborg, Denmark")
bullet(d, "Kept a human-worn shoulder exoskeleton running through trials with 12 participants, 3 assist modes "
          "and 2 loads by building the units from my own CAD files and BOMs, and repairing and refitting them "
          "between sessions.")
bullet(d, "Went through several versions of each part in weeks rather than months by 3D printing them in house, "
          "fitting them on the rig the same day and sending what I learned straight back into the CAD.")
bullet(d, "Cut energy use by more than 25% (Best Paper Award, IFToMM ISRM 2026) with a spring plus 6 Nm motor "
          "actuator that I designed in SolidWorks, then built and assembled myself.")
bullet(d, "Got force readings within 10% RMS of a reference sensor by building a test setup around a 5-bar "
          "parallel robot with variable-stiffness actuators and calibrating it against a force sensor.")
bullet(d, "Wired motors, encoders, force sensors and DAQ into test rigs and an Arduino-based setup for "
          "functional, calibration and durability checks, and helped run lab demos. Supervised Bachelor's "
          "students (2023 - 2025).")

role(d, "MTech Researcher, Pneumatic Actuators (Master's thesis)", "2020 - 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
bullet(d, "Made pneumatic artificial muscles by hand from raw materials and built the test bench around them "
          "(valves, pressure sensors, DAQ), then used it to tune a controller that brought position error down "
          "to 0.3-0.78%.")

role(d, "Bachelor's Capstone and Student Builds", "2017 - 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Designed, machined, assembled and user-tested an upper-limb rehabilitation exoskeleton. Best Major "
          "Project Award and an INR 100,000 TATA Technologies grant.")
bullet(d, "Built a Go-Kart from scratch (2017) and a human-electric hybrid vehicle for Efficycle (2018) in the "
          "college workshop.")

heading(d, "Skills")
bullet(d, "3D printing (Bambu Lab, Ultimaker Cura), hand tools, machining and assembly (Bachelor's), "
          "test rigs and jigs", "Workshop: ")
bullet(d, "SolidWorks (CSWA): reading and making parts, fixtures, assemblies and BOMs", "CAD: ")
bullet(d, "Arduino, motors, encoders, force/torque and pressure sensors, DAQ, pneumatic valves",
       "Electronics and MCUs: ")
bullet(d, "MATLAB/Simulink, Python, LabVIEW (basic) for test scripts and data", "Software: ")
bullet(d, "English (C1, fluent), Bengali (native), Hindi (conversational)", "Languages: ")

heading(d, "Education")
role(d, "PhD, Mechatronics and Robotics (in progress)", "2023 - Present", "Aalborg University, Denmark")
role(d, "MTech, Mechatronics", "2020 - 2022", "AcSIR - CSIR-CMERI, Durgapur, India")
role(d, "BTech, Mechanical Engineering", "2015 - 2019", "Siddaganga Institute of Technology (VTU), India")

heading(d, "Awards and Publications")
bullet(d, "Best Research Paper Award, IFToMM ISRM 2026; Certified SolidWorks Associate (CSWA)")
bullet(d, "Majumder, A., et al. \"A Hybrid Actuated Shoulder Exoskeleton for Energy-Efficient Upper Arm Support.\" "
          "ISRM 2026, Springer. Also IEEE CONECCT 2022 (pneumatic muscle control).")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_CV_Humanoid_Prototype.docx")
to_pdf(d, OUT + "Arunabha_Majumder_CV_Humanoid_Prototype.pdf")

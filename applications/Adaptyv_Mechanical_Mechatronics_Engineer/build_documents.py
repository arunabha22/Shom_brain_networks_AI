import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

# Adaptyv (Lausanne) - Mechanical / Mechatronics Engineer, lab automation hardware. CV.
# Follows CLAUDE.md facts (both emails, drawing, no FEA/Fusion/force control, machining = Bachelor's, Master's and
# AAN controller credit as confirmed, study = data collection).
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
SEP = "  |  "

d = new_doc()
para(d, NAME, bold=True, size=18, after=0)
para(d, "Mechanical / Mechatronics Engineer | Prototyping, Fixtures, Sensor and Actuator Integration", bold=True,
     size=11, after=2)
para(d, SEP.join(["+45 71 62 24 00", "Aalborg, Denmark (open to relocating to Lausanne)"]), size=9.5, after=0)
para(d, SEP.join(["somrkmv1997@gmail.com", "97arunabhasit027@gmail.com",
                  "Portfolio: arunabha22.github.io/arunabha-majumder"]), size=9.5, after=0)
para(d, "LinkedIn: linkedin.com/in/arunabha-majumder-681264107", size=9.5, after=6)

heading(d, "Summary")
para(d, "I like building things and making them work reliably. During my PhD at Aalborg University I took a shoulder "
        "exoskeleton from hand sketches and CAD to tested hardware: SolidWorks parts, 3D-printed prototypes, motor, "
        "encoder and force sensor integration, and test rigs that had to run session after session. I have built "
        "a Go-Kart, a hybrid vehicle and a rehabilitation exoskeleton as a student, and I am happiest in the "
        "workshop solving practical problems.")

heading(d, "Key Results")
bullet(d, " less energy from a spring and motor actuator I designed and built (Best Paper Award, IFToMM ISRM 2026)", ">25%")
bullet(d, " force estimate on a 5-bar robot, validated against a reference force sensor", "<10% error")
bullet(d, " participants in experiments where I collected EMG and motion-capture data", "12")

heading(d, "Experience")
role(d, "PhD Researcher, Mechatronics and Robotics (project VIEXO)", "2023 - Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
bullet(d, "Designed parts, mounts and fixtures in SolidWorks and iterated them quickly with 3D printing until they held "
          "up in testing; the resulting exoskeleton cut energy use by more than 25%.")
bullet(d, "Integrated the motor, encoder and force sensors with the mechanical frame myself, and found and fixed "
          "faults in mounting, wiring, sensors and data logging so the test rigs gave repeatable results.")
bullet(d, "Validated a force estimate on a 5-bar parallel robot (variable-stiffness actuators, robot Jacobian) against "
          "a reference force sensor, within 10% RMS error.")
bullet(d, "Worked in a team of 3 on an Assist-as-Needed controller: I helped with the equations, such as the Fourier "
          "fit, and defined how the GUI should behave. User muscle effort dropped by more than 15%.")
bullet(d, "Collected data from 12 participants using EMG and motion capture; taught and supervised Bachelor's "
          "students (2023 - 2025).")

role(d, "MTech Researcher, Pneumatic Artificial Muscles (Master's thesis)", "2020 - 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
bullet(d, "Fabricated and assembled pneumatic artificial muscles to an existing lab design and ran experiments on the "
          "lab's setup with valves, pressure sensors and DAQ.")
bullet(d, "Collected the data, fed it into the lab's existing neural network and used its output to design the outer "
          "PID loop of a gain-scheduled controller in MATLAB/Simulink (0.3-0.78% error, IEEE CONECCT 2022).")

role(d, "Student Builds, Siddaganga Institute of Technology", "2017 - 2019", "Tumakuru, India")
bullet(d, "Bachelor's capstone: designed, machined, assembled and tested an upper-limb rehabilitation exoskeleton. "
          "Best Major Project Award and an INR 100,000 TATA Technologies grant.")
bullet(d, "Built a Go-Kart from scratch (2017) and a human-electric hybrid vehicle for the Efficycle competition "
          "(2018) with student teams, using workshop tools.")

heading(d, "Skills")
bullet(d, "SolidWorks (CSWA), parts, assemblies, fixtures and mounts", "CAD: ")
bullet(d, "3D printing (Bambu Lab, Ultimaker Cura), hand and power tools; machining and assembly (Bachelor's)",
       "Building: ")
bullet(d, "Motors, encoders, force/torque and pressure sensors, pneumatic valves, DAQ, Arduino", "Sensors and actuators: ")
bullet(d, "Python, MATLAB/Simulink, LabVIEW (basic)", "Programming: ")
bullet(d, "Diploma in Fine Arts; hand sketching of concepts and technical illustrations", "Drawing: ")
bullet(d, "English (C1, fluent), Bengali (native), Hindi (conversational)", "Languages: ")

heading(d, "Education")
role(d, "PhD, Mechatronics and Robotics (defence expected in 2027)", "2023 - Present", "Aalborg University, Denmark")
role(d, "MTech, Mechatronics", "2020 - 2022", "AcSIR - CSIR-CMERI, Durgapur, India")
role(d, "BTech, Mechanical Engineering", "2015 - 2019", "Siddaganga Institute of Technology (VTU), India")

heading(d, "Awards and Publications")
bullet(d, "Best Research Paper Award, IFToMM ISRM 2026; Certified SolidWorks Associate (CSWA)")
bullet(d, "Majumder, A., et al. \"A Hybrid Actuated Shoulder Exoskeleton for Energy-Efficient Upper Arm Support.\" "
          "ISRM 2026, Springer. Also IEEE CONECCT 2022 (pneumatic muscle control).")
heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Adaptyv_CV_Arunabha_Majumder.docx")
to_pdf(d, OUT + "Adaptyv_CV_Arunabha_Majumder.pdf")

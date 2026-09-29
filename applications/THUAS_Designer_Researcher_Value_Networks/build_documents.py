import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc_helpers import *

OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
TAG = "THUAS_Designer_Researcher"
TITLE = "Designer and Researcher | Multidisciplinary Research | Quantitative Methods | Data Visualization"

# ---------------- RESUME ----------------
d = new_doc()
header(d, TITLE)

heading(d, "Professional Summary")
para(d, "Designer and researcher with a Master's degree (M.Tech) in Mechatronics and a PhD in progress at Aalborg "
        "University, with more than five years of research experience in multidisciplinary projects that combine "
        "design, human-subject research and data analysis. Experienced in contributing to the implementation of "
        "research plans end to end: study design, ethics protocols, quantitative data collection and statistical "
        "analysis, through to peer-reviewed publications (Best Research Paper Award, 2026). Secured an INR 100,000 "
        "innovation grant. Trained visual artist (Diploma in Fine Arts) who creates illustrations, technical visuals "
        "and data visualizations. Experienced in international research environments in Denmark and India; fluent "
        "in English (C1).")

heading(d, "Core Competencies")
bullet(d, "Contributing to the implementation of research plans, multidisciplinary research, experimental study "
          "design, human-subject studies, ethics protocols", "Research: ")
bullet(d, "Quantitative research methods, statistical power analysis, statistical analysis, data collection "
          "(EMG, motion capture), end-to-end data pipelines", "Research Methods: ")
bullet(d, "Python, MATLAB, visualization of experimental results; Adobe Illustrator and Photoshop for figures "
          "and visuals", "Data Analysis & Visualization: ")
bullet(d, "Concept development, iterative design, prototyping, system design, testing with users",
       "Design: ")
bullet(d, "Scientific writing and peer-reviewed publications, grant funding (TATA Technologies Innovation Grant), "
          "illustration and graphic design, English (C1)", "Communication & Content: ")
bullet(d, "Collaboration in multidisciplinary and international teams (engineering, controls, biomechanics)",
       "Collaboration: ")

heading(d, "Research Experience")
role(d, "PhD Researcher – Design and Research of Assistive Robotic Systems (VIEXO Project)", "2023 – Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
bullet(d, "Contribute to implementing the research plan of the VIEXO research project, taking research questions "
          "from concept and design through experimental validation to publication.")
bullet(d, "Designed and conducted a 12-participant human study across 3 assistance modes and 2 load conditions, "
          "covering statistical power justification, EMG and motion-capture instrumentation, ethics protocol and "
          "the end-to-end data pipeline; the dataset supports two journal submissions.")
bullet(d, "Conduct multidisciplinary research that combines mechanical design, electronics, control and "
          "biomechanics, working with co-authors from several disciplines.")
bullet(d, "Designed a hybrid-actuated shoulder exoskeleton that cut energy consumption by more than 25%; the work "
          "won the Best Research Paper Award at IFToMM ISRM 2026.")
bullet(d, "Reduced user muscle effort by more than 15% with an Assist-as-Needed controller, validated with human "
          "participants.")
bullet(d, "Developed analytical models and validated them against experimental data to below 10% RMS error, and "
          "proposed a sensorless force-estimation method that reduced system cost, mass and complexity.")

role(d, "M.Tech Researcher – Actuator Systems (Master's Thesis)", "2020 – 2022",
     "CSIR-Central Mechanical Engineering Research Institute (CMERI), National Laboratory, Durgapur, India")
bullet(d, "Carried out a quantitative experimental research project: built test setups, collected and analysed "
          "data, and developed an empirical actuator model.")
bullet(d, "Developed a neural-network-based controller that reduced position-tracking error to 0.3–0.78%; "
          "published at IEEE CONECCT 2022.")

role(d, "Bachelor's Capstone Project – Upper-Limb Rehabilitation Exoskeleton", "2018 – 2019",
     "Siddaganga Institute of Technology, Tumakuru, India")
bullet(d, "Secured an INR 100,000 TATA Technologies Innovation Grant and won the Best Major Project Award for a "
          "rehabilitation device, leading design, fabrication and user testing end to end.")

heading(d, "Education")
role(d, "Ph.D. Candidate, Mechatronics & Robotics", "2023 – Present",
     "Aalborg University, Department of Materials and Production, Aalborg, Denmark")
role(d, "Master's Degree (M.Tech), Mechatronics", "2020 – 2022",
     "AcSIR – CSIR-Central Mechanical Engineering Research Institute (CMERI), Durgapur, India")
role(d, "Bachelor's Degree (B.Tech), Mechanical Engineering", "2015 – 2019",
     "Siddaganga Institute of Technology, Visvesvaraya Technological University (VTU), Tumakuru, India")
role(d, "Diploma in Fine Arts (Painting)", "",
     "Bangiya Sangeet Parishad, India")

heading(d, "Publications")
bullet(d, "Majumder, A., Wagner, J.W., Zhu, Y., Oliveira, A.S., and Bai, S. \"A Hybrid Actuated Shoulder Exoskeleton "
          "for Energy-Efficient Upper Arm Support.\" Robotics and Mechatronics: ISRM 2026, MMS, vol. 213, Springer. "
          "(Best Research Paper Award)")
bullet(d, "Majumder, A., Sarkar, D., Chakraborty, S., Singh, A., Roy, S.S., and Arora, A. \"Neural Network-Based Gain "
          "Scheduled Position Control of a Pneumatic Artificial Muscle.\" IEEE CONECCT, 2022.")

heading(d, "Grants & Awards")
bullet(d, "Best Research Paper Award, 9th IFToMM International Symposium on Robotics and Mechatronics (2026)")
bullet(d, "TATA Technologies Innovation Grant – INR 100,000 (2019)")
bullet(d, "Best Major Project Award, Department of Mechanical Engineering (2019)")
bullet(d, "Certified SolidWorks Associate (CSWA)")

heading(d, "Team Projects")
bullet(d, "Worked in a multidisciplinary team to design a human-electric hybrid vehicle for the Efficycle "
          "competition.", "Efficycle (2018): ")
bullet(d, "Led end-to-end design and fabrication of a custom Go-Kart.", "Go-Kart (2017): ")

heading(d, "Tools")
bullet(d, "Python, MATLAB/Simulink, LabVIEW (basic), LaTeX", "Data & Analysis: ")
bullet(d, "Adobe Illustrator, Adobe Photoshop, Procreate (basic)", "Visual Content: ")
bullet(d, "Qualisys Motion Capture, EMG, force/torque sensors", "Research Instrumentation: ")
bullet(d, "SolidWorks, Fusion 360, 3D printing", "Design & Prototyping: ")

heading(d, "Languages")
para(d, "English (C1, fluent) | Bengali (Native) | Hindi (Conversational)")

heading(d, "References")
para(d, "Available upon request.")
d.save(OUT + "Arunabha_Majumder_Resume_%s.docx" % TAG)
to_pdf(d, OUT + "Arunabha_Majumder_Resume_%s.pdf" % TAG)

# ---------------- COVER LETTER ----------------
c = new_doc()
c.sections[0].top_margin = Cm(2.0)
header(c, TITLE)
para(c, "September 29, 2026", after=8)
para(c, "Prof. Liliya Terzieva, Professor Designing Value Networks", after=0)
para(c, "Faculty of Business, Finance and Marketing", after=0)
para(c, "The Hague University of Applied Sciences", after=0)
para(c, "The Hague, Netherlands", after=8)
para(c, "Application: Designer and Researcher – Designing Value Networks (0.4 FTE)", bold=True, after=8)
para(c, "Dear Professor Terzieva,", after=8)
body = [
 "I am applying for the position of Designer and Researcher in the Designing Value Networks research group. I "
 "hold a Master's degree in Mechatronics and am finishing my PhD at Aalborg University. For more than five years "
 "I have worked on multidisciplinary research projects that combine design, research with people and data "
 "analysis, and I would like to bring this experience to research on value networks and societal transitions.",

 "I have experience contributing to the implementation of research plans. In the VIEXO project at Aalborg "
 "University, I took research questions from concept and design through experimental validation to publication. "
 "I designed and ran a 12-participant human study, including the statistical power justification, the ethics "
 "protocol, the data collection and the analysis pipeline, and the resulting dataset supports two journal "
 "submissions. Our work on energy-efficient assistive technology won the Best Research Paper Award at IFToMM "
 "ISRM 2026.",

 "My research is multidisciplinary by nature. It brings together mechanical design, electronics, control and "
 "biomechanics, and it has meant working with colleagues from different disciplines and backgrounds in Denmark "
 "and India. During my Bachelor's, I secured an INR 100,000 innovation grant from TATA Technologies for a "
 "rehabilitation device, which gave me early experience with funding applications.",

 "I also enjoy turning complex work into clear content. I hold a Diploma in Fine Arts and create illustrations, "
 "technical visuals and data visualizations with Python, MATLAB and Adobe Illustrator, and I have written and "
 "co-authored peer-reviewed publications.",

 "My background is in engineering design rather than business, and my working language is English; I am not "
 "yet proficient in Dutch. I see the move into design research on value networks as a natural next step, and I "
 "would bring a structured, quantitative and creative approach to your research group.",

 "I would welcome the opportunity to discuss how I can contribute to the Designing Value Networks research "
 "group. References are available upon request.",
]
for t in body:
    para(c, t, after=8)
para(c, "Kind regards,", after=2)
para(c, NAME)
c.save(OUT + "Arunabha_Majumder_Cover_Letter_%s.docx" % TAG)
to_pdf(c, OUT + "Arunabha_Majumder_Cover_Letter_%s.pdf" % TAG, top=2.0)

# My standing rules (Arunabha Majumder) – apply to every chat and every document

## Voice (top priority)
- Everything must sound like I wrote it myself: simple, warm, direct, a little imperfect. Plain words, short and
  medium sentences, some starting with "I". If something sounds polished or generic, rewrite it plainer.
- Never use: leverage, spearhead, seamless, robust, cutting-edge, passionate, delve, dynamic, synergy, pivotal,
  foster, navigate, realm, elevate, harness, showcase, meticulous, "I am excited to", "I am confident that".
- No em dashes (—). No hidden characters. Facts and numbers over adjectives.

## Outreach
- My name is Arunabha Majumder (never "Shom"). Keep messages short.
- Always include my portfolio: https://arunabha22.github.io/arunabha-majumder/
- Always sign with both emails: somrkmv1997@gmail.com | 97arunabhasit027@gmail.com, and +45 71 62 24 00.
- Never mention automated rejections or frustration with applications.
- Never write "FEA"; say "analysis" or "mechanical analysis" (only where true).
- Friend recommendations: no technical claims.

## My facts (never exaggerate, never add skills I have not confirmed)
- PhD in Mechatronics and Robotics, Aalborg University (2023 - present, thesis expected to be finished in March, defence 2027; never "I finish in March";
  keep the thesis timing out of the profile/summary of short CVs).
  MTech Mechatronics (CSIR-CMERI, India), BTech Mechanical Engineering (Siddaganga Institute of Technology).
- Study abroad at the National University of Singapore (NUS), Sep - Nov 2025 (one line only, no claims).
- PhD: shoulder exoskeleton (never "wearable machines"). SolidWorks + 3D printing. I designed the hybrid
  spring + 6 Nm motor concept (>25% less energy, Best Paper Award, IFToMM ISRM 2026) and integrated the motor,
  encoder and force sensors. I optimised the design with a genetic algorithm and measured the stiffness it can
  provide on a PHYSICAL test setup (it was not tested in SolidWorks). "Stiffness analysis in SolidWorks" only as a
  general skill, never tied to the exoskeleton. Never write "FEA"; no Abaqus/Ansys. Fusion 360: basic only (I know it a little, last used in 2019), never professional.
- Exoskeleton detail: a variable stiffness mechanism (VSM) stores energy over an adjustable range, with a motor
  working in parallel; together they provide the lifting torque. A secondary worm gear system pretensions the spring.
  The genetic algorithm optimised the VSM diameter, spring stiffness and pretension force.
- Clutch story: NEVER use it in CVs, letters or answers unless I ask for it.
- CV job title for the PhD: "Research Assistant, Aalborg University".
- Outer PID loop: not a simple PID; it has integral anti-windup and error nonlinearisation.
- 6 participants = arm impedance study with the 5-bar robot (always say which robot).
- German: just "willing to learn German", no gap sentences. Always include GATE qualified, a Study Abroad heading
  (NUS 2025) and my portfolio. End cover letters with a line about bringing innovative ideas.
- Assist-as-Needed controller: team of 3; my part = equations (e.g. Fourier fit) and GUI behaviour.
  Muscle effort: ">15%" only.
- 5-bar robot, exact wording: "Designed and modelled a novel 5-bar planar parallel robot with variable stiffness
  mechanisms (VSM), estimated its stiffness with less than 10% error, and quantified human arm impedance."
  Never shorten it to just "estimated force". NO force control.
- 12-participant study: I did the data collection (EMG with Qualisys data acquisition), not the analysis.
  Do not share my PhD video. Do not mention the journal papers under review.
- Arm impedance study (5-bar robot, 6 participants): I IMPLEMENTED (not built) an Arduino-based trigger system
  to sync the robot's motion with Qualisys motion capture.
- Master's: I fabricated/assembled pneumatic muscles to someone else's design on the lab's existing setup;
  the neural network was someone else's; my part = data collection and the outer PID loop (0.3-0.78% error).
  I designed the outer PID loop of the neural network-based controller in MATLAB/Simulink and implemented it in
  LabVIEW to drive the pneumatic muscle (one point, never repeated).
- Machining and hands-on assembly: Bachelor's only (Go-Kart, Efficycle). My Bachelor's capstone was an
  upper-limb rehabilitation EXOSKELETON for a paralysed arm; always name it as an exoskeleton.
- Senior Diploma in Fine Arts (Painting), Bangiya Sangeet Parishad, 2008, First Division with Distinction.
- Taught courses and supervised Bachelor's students (2023 - 2025). Diploma in Fine Arts: always include my
  drawing skills (hand sketching, technical illustrations).
- ALWAYS keep both my fine arts diploma AND my graphic design (Adobe Illustrator, Photoshop, Procreate) in
  every CV and cover letter.
- Publications: only IEEE CONECCT 2022 and ISRM 2026. Never list the ASME JMR paper.
- GATE exam qualified (no score given). The INR 100,000 TATA Technologies grant was through "Prayatna".
- Willing to relocate to France, Lausanne (Switzerland) and Germany; no French yet but willing to learn.
- Exoskeleton parts: GA-optimised, SolidWorks, 3D printed for initial tests, then manufactured. >25% less motor
  energy (better battery life). Master's muscles were part of a soft exosuit. Bachelor's: arm exoskeleton and
  exo glove, TATA Technologies Prayatna Innovation Fund grant, Best Major Project.
- Start date: as soon as possible, allowing time for the visa and relocation. My PhD research is finished; I can
  write my thesis alongside a job.
- No PLC, ROS or Danish experience. List Danish ("willing to learn") only for jobs in Denmark.
- References on every CV: (1) Shaoping Bai, PhD, Professor, Dept. of Materials and Production, Aalborg University,
  sbh@mp.aau.dk; (2) Lars Rosgaard Jensen, Associate Professor, Head of Section (Physics, Mechanics and Materials),
  Head of Labs, Dept. of Materials and Production, Aalborg University; (3) Anderson de Souza Castelo Oliveira,
  Associate Professor, Dept. of Materials and Production, Aalborg University. Not named in cover letters unless I ask.

## Documents
- CV and cover letter as separate PDFs, named like "<Company>_CV_Arunabha_Majumder" and
  "<Company>_Cover_Letter_Arunabha_Majumder". Cover letters usually 1 page. ATS-friendly.
- File properties show only my name.
- Always put my photo on every CV (top right); keep the headline under my name short so it never touches the photo.
- Both emails in every CV, letter and signature: somrkmv1997@gmail.com and 97arunabhasit027@gmail.com,
  plus +45 71 62 24 00 and my portfolio link.

## Humanize every text, then run remove-ai-marks
1. Write it the way I would say it out loud: plain words, mixed sentence lengths, some sentences start with "I",
   one small concrete detail from my real work, no buzzwords, no em dashes, no perfect three-item lists, no tidy
   summary line at the end of each paragraph.
2. Before giving me the final text, reread it once and rewrite any sentence that sounds polished, generic or
   "AI-like" in simpler words.
3. Then run /anthropic-skills:remove-ai-marks on the final text or file (check the cleaning service first).
   If the service is down, tell me in one short line. Never say it ran if it did not.
4. Never invent facts to make text sound more human. Only use my confirmed facts.

## Keep these rules up to date
- Whenever I correct a fact or add a new one, save it in these rules straight away and fix the documents
  you are working on, so the same mistake never happens again.
- File names: "AM <Company> CV.pdf" and "AM <Company> Cover Letter.pdf", never my full name.
- My portfolio has only videos and results from my work (no CAD, drawings or photos); describe it that way.
- Master's: silicone-based pneumatic muscles; team of 4 (electronics + mechanical) on the LabVIEW control architecture.
- Bachelor's exo arm and exo glove: motor assistance with Arduino-based control and manual switching.
- My art Instagram: surreal_art_engine. GitHub: github.com/arunabha22.
- EMG (12 participants) = exoskeleton study. 5-bar robot study (6 participants) = arm position data with Qualisys, no EMG.
- Cover letters: do not write "willing to learn German" (CV Languages line only).
- Willing to relocate to the Netherlands (will apply for a Dutch permit); no Dutch.
- Built small hexapods in 2017; Bachelor's project used servo motors; Master's: pneumatic muscles and pressure valves.
- NUS study abroad (Sep to end of Nov 2025) was independent research during my PhD.
- Exoskeleton energy numbers (his words, 2026-11-17): about 20% motor energy saving WITH a human wearing it (with load);
  40-50% WITHOUT a human, with a different spring. Keep ">25%" in CVs and letters (his decision, 2026-11-17): some
  participants saved over 25%, and with the different spring it was 25%. If asked in an interview, explain the range:
  about 20% on average with a person and load, over 25% for some participants, 40-50% on the bench without a person.
- Exoskeleton arm cuff (his words, 2026-11-17): adjustable. A rigid hard base carries the arm (holds it for overhead
  work); a hinged (flip) upper part closes over the arm with straps and locks it; the cuff slides along the arm and
  locks at different positions to fit different arm sizes.
- Assist-as-Needed details (his words, 2026-11-17): the AAN controller itself was built long ago by another professor.
  The team of 3 built the GUI and test setup around it: a Fourier fit of each participant's own arm trace becomes the
  controller's reference, the controller learns, then data is collected (data logged to a memory card). His part:
  the Fourier fit equations and defining what the GUI should do. Still never say he developed the AAN controller.
- Relocation to Prague, Czech Republic (REVEL, 2026-11-17): he plans to move (needs a visa; the visa appointment is
  likely in Copenhagen while he lives in Aalborg). No Czech.
- Master's soft exosuit / pneumatic muscle project (his words, 2026-11-18): it is under a patent, so its details
  cannot be fully disclosed. In interviews explain only the general principle of pneumatic muscles and his role;
  never add design details of the exosuit or muscles to documents beyond what is already published (IEEE CONECCT 2022).
- Replies to people who have already seen his CV/portfolio (his order, 2026-11-18): do NOT re-explain his exoskeleton
  or projects in detail; keep the reply short and point to what they already have.
- Skelex follow-up plan (his order, 2026-11-18): Duncan Treffers (d.treffers@skelex.com, cc Gert Maass g.maass@skelex.com)
  said no openings now, new positions planned mid 2027. In the FIRST WEEK OF JUNE 2027, if he has no job yet, he emails
  Duncan again with an updated CV. Draft: applications/Skelex_Follow_Up/email_draft_june_2027.md (also a Gmail draft in
  that thread). Scheduled tasks: one-shot reminder 1 Jun 2027 10:00 CET (push + email) and a monthly Skelex job check
  (3rd of each month). Never send the email without his OK.

## VERY VERY VERY IMPORTANT (his order, 2026-11-25) - every CV and cover letter
- Before drafting: CHECK whether the job asks for a motivation letter and/or a research statement (and use his
  existing ones as a base, e.g. applications/SDU_Postdoc_Mechatronic_Design_ROV/ research statement).
- Draft the cover letter BASED ON HIS PORTFOLIO (https://arunabha22.github.io/arunabha-majumder/): its headline
  "Mechanical & Robotics R&D Engineer", its key numbers (>25% lower exoskeleton motor energy; <10% stiffness model
  error; 0.3-0.78% tracking error on the pneumatic muscle; Best Paper ISRM 2026) and its projects (VIEXO shoulder
  exoskeleton, 5-bar robot, soft exosuit). Only use portfolio claims that also pass the Facts rules in this file
  (e.g. >15% muscle effort = team AAN result, journal under review, so not in documents).
- Make the necessary changes to the CV for every job so it matches the letter and the job.

## NEW DOCUMENT FORMAT (his approval, 2026-11-18) - use for ALL new CVs and cover letters
Template builder: applications/Sample_New_Format/build_sample.py (Laerdal sample). Two-column design with photo.
CV:
- Length: 2 pages ONLY for R&D positions (job title or ad clearly R&D / Research / Development engineering);
  every other job gets 1 page.
- Profile: SHORT (2-3 lines), about what he can contribute and how, written so it fits the job's asks; NO company
  name in the profile (he may reuse the CV); end with one short motivation line.
- Directly under the profile: section "Core Engineering Competencies" with about 5 one-line items picked to match
  the job description (only real skills). No "Why I fit this role" section.
- Experience: max 5 bullets per role. Do NOT list teaching/supervising in CVs anymore (his words: no one cares).
- Portfolio link in the header in colour (blue, underlined, clickable).
- Whole CV should make them want to invite him to an interview.
Cover letter:
- No contact block at the top. Top: his name big; under it a job-specific title line, smaller, in blue
  (e.g. "Mechatronics engineer with 6 years of experience building pneumatic and motor-driven systems that move
  with the human body"; change it for every job; "6 years" = research since 2019, approved).
- Then bold, slightly bigger: "Application for <job title>". Then "Dear <named person>," or "Dear Hiring Team,".
- Paragraph 1: who he is and why he feels qualified ("I feel qualified to ... because I did ...").
- Paragraph 2: what motivated him to apply (it is about building a connection, not only about him); fine arts +
  graphic design go here when they fit.
- Paragraph 3: "I would be excited to bring my <experience>, <approach> and new ideas to your <team>." ("excited"
  is allowed in this one closing line; this replaces the old "innovative ideas" ending.)
- Paragraph 4: final stage of PhD; research done; available to move into an industrial engineering role while
  finishing the thesis.
- Then "Thank you for your time. I look forward to hearing from you." / "Best regards," / his name, and ONE small
  contact line under the name (phone | both emails | portfolio).

## ATS rules (his approval, 2026-11-18, after the Reddit ATS post)
- KEEP the two-column design (his order). Do not switch to single-column unless he asks.
- Headline under the name: keep the approved headline. Change it to the exact job title ONLY when he says OK.
- Keywords: reuse the job ad's exact words in Core Engineering Competencies and bullets ONLY where they truly match
  his experience and skills. If an ad keyword does not match his real experience, TELL HIM first and ask before
  adding it. Never keyword-stuff, never hidden text.
- One date format everywhere in a document (currently years, e.g. "2023 - Present").
- Standard section names only (Profile, Core Engineering Competencies, Experience, Education, Skills, Publications,
  Languages, References); contact info in the page body, never in a header/footer; no icons or emojis.
- Known ATS risk (tested 2026-11-18): text extracted in stream order reads cleanly column by column, but layout-based
  readers (e.g. pdftotext) mix the two columns line by line; a wider gutter did not fix it reliably. If a big company
  portal (Workday, Taleo, iCIMS) is used, mention this risk to him in one line and offer a plain copy; do not make one
  unless he asks.
- Workshop facts (his words, 2026-11-20): in his Bachelor's he used a LATHE and did some WELDING. Laser cutting:
  a technician cut the parts; do NOT mention laser cutting or laser-cut parts at all (his order, 2026-11-20).
  3D printing he did himself (Ultimaker Cura, Bambu Lab). No Creo. He has NOT built a gripper, but has
  ideas for one with silicone and mechanical design (may be mentioned as an idea only). His exoskeletons may be
  described as proof-of-concept (POC) prototypes. Control systems (PID with integral anti-windup and error
  nonlinearisation) are research topics he has worked on.
- Interview reminders (his order, 2026-11-20): for EVERY interview, always schedule a reminder (send_later, push)
  on the DAY BEFORE the interview, with the cheat sheet and an offer to run a mock interview. NXAI: reminder set for
  Sun 22 Nov 2026 11:00 CET (interview Mon 23 Nov 13:30 CET).
- Languages for GERMAN companies/jobs (his order, 2026-11-21): ALWAYS add "German (willing to learn)" to the CV
  Languages line (like Danish for Denmark). Still never write it in cover letters.
- English test (his words, 2026-11-21): IELTS overall band 7. May be listed in the CV Languages line, e.g.
  "English (C1, IELTS 7.0)", especially for UK/visa-related applications.
- New facts (his words, 2026-11-21): in his Bachelor's (2017-19) he did a strength test of the go-kart frame with
  SolidWorks Simulation (write "strength analysis in SolidWorks Simulation"; still avoid the word "FEA" unless he
  says otherwise). He designed the Efficycle trike (with the student team). The exoskeleton's manufactured parts
  were ALUMINIUM. His PhD counts as design and fabrication experience. He is willing to move to the UK (London).
- New facts (his words, 2026-11-21): basic C/C++ through Arduino coding (write "Arduino programming in C/C++
  (basic)"); basic wiring and soldering; he made BOMs for his exoskeleton; he has an INDIAN driving licence
  (not UK/EU). Still no PCB design, no embedded firmware beyond Arduino.
- Go-Kart (2017) and Efficycle trike (2018) were SIDE PROJECTS during his BTech (his words, 2026-11-22), not part of
  the capstone. Label them as side projects (e.g. "Side projects during BTech: ...").
- ALWAYS ASK FIRST (his order, 2026-11-22): before drafting ANY CV or cover letter, first ask him the relevant
  questions (gaps vs the ad, skills he may have, page count, headline, language lines, cover letter needed, addressee,
  relocation/visa) and wait for his answers. Do not draft until he answers.
- MATCH PERCENTAGE (his order, 2026-11-22): every time a new job comes in, show the match percentage (out of 100)
  with a short breakdown of what matches and what is missing, together with the questions, BEFORE drafting.
- Manufacturing facts (his words, 2026-11-22): exoskeleton aluminium parts were CNC MACHINED by an external
  manufacturer (he talked with the manufacturer) plus 3D printed parts. BTech: he worked with an external 3D printing
  business that delivered parts; he did the wiring/connectors on the BTech project; sheet metal parts on the go-kart
  (sometimes). Master's: hands-on experience with SILICONE CASTING/fabrication of the pneumatic muscles in the group
  (design and technique were not his). Motor drivers: basic experience with Maxon ESCON drivers (did the first basic
  wiring himself, with help from the internet). No NX, no Creo. Danish: willing to learn only.
- CV design note (2026-11-22): he did not like the 2-page layout with a full-width plain page 2; use the two-column
  layout with the shaded left panel on BOTH pages.
- Bachelor's capstone exoskeleton (his correction, 2026-11-22): NO lathe/machined parts. Never write lathe, machining
  or welding for the capstone; lathe and welding were BTech skills used elsewhere (list only as general Bachelor's skills).
- Exoskeleton facts (his words in mock interview, 2026-11-22): the parts were manufactured AND assembled in China
  by the external manufacturer, from his BOM; all mechanical testing (stiffness tests) was done by him in Aalborg,
  and he matched his mathematical model with the experimental data. The same Arduino-based trigger approach synced
  the exoskeleton data with the Qualisys/EMG recording. The motor is mounted on the exoskeleton frame (not a fixed
  base). He mentioned TWO motors (not yet confirmed; CVs still say one 6 Nm motor until he confirms).
- Clutch detail (his words, mock interview 2026-11-22; still NEVER in documents unless he asks): clutch engaged =
  hybrid mode (spring + motor), disengaged = motor-only mode. The 3D printed plastic clutch kept breaking under arm
  forces during prototype tests; instead of waiting for the manufacturer to redesign it, he switched to a bolt-locking
  system that locks at 8 angles (8 assistive conditions).
- Availability (his words, 2026-11-22): his supervisor has given permission for him to leave the lab because his
  experiments are done; only thesis writing remains. He can start as soon as the visa allows. He only has permission
  to stay/work in Denmark, so jobs outside Denmark need visa support.
- ROS 2 (his words, 2026-11-22): he had STARTED learning ROS 2, but paused when his supervisor decided to focus on
  finishing the final journal paper and the thesis. Write/say "started learning ROS 2" (beginner), never proficiency.
  (Still do not mention the journal under review in documents.)
- ROS 2 (his words, 2026-11-22): he had started learning ROS 2 (beginner tutorials, a couple of videos) but paused
  when his supervisor prioritised the final journal paper and thesis. Never claim ROS experience; he may say he started
  learning ROS 2 and paused for the thesis.
- LESSONS FROM REJECTIONS (keep updating): Danfoss Mechanical Engineer PMI (product maintenance & improvement)
  rejected 2026-11-23 ("profiles matched our role requirements more closely"; standard reply, CV kept on file).
  Earlier: Marble (wanted experience deploying robotic systems), LEGO internship, Helsing Robotics Mech Engineer.
  Wandercraft Mechanical Design R&D Engineer rejected 2026-11-24 after the video interview with Fabien Guerin
  (660+ applicants, 70+ video interviews, comparative assessment of experience). Lesson: big-name exoskeleton
  roles attract hundreds of applicants; reaching interview shows the profile fits, so keep targeting exoskeleton/
  wearable roles but spread applications to smaller startups and research-engineer roles too.
  Pattern: industry/production roles that list years of industry experience, production processes (plastics,
  sheet metal, casting), NX/Creo or Danish/German screen him out early. When scoring, lower such roles (cap ~45) and
  tell him so; push him toward roles where research prototypes, testing with people, actuators/mechatronics and
  R&D count (research engineer, R&D/prototyping, wearables/exoskeleton, robotics startups). In CVs for production
  roles, lead with the real production-facing facts: BOMs, drawings, CNC-machined aluminium parts with an external
  manufacturer, working with suppliers, testing and documentation.
- DANFOSS (his words, 2026-11-23): Danfoss rejected ALL his applications (Mechanical Engineer PMI, Mechatronics Engineer,
  Production Engineer Actuator Silkeborg, Test Engineer; Development Engineer Graasten status to confirm). Do not suggest
  more Danfoss roles for about 6 months unless he has a referral/contact inside or the match is clearly strong.
- Test setups (his answer, 2026-11-23): he did NOT design or build the physical test setups/rigs for the exoskeleton
  stiffness tests or the 5-bar robot; he used existing lab setups. Write "tested on a physical test setup", never
  "built test rigs". No Onshape. Wiring/soldering: basic only, no harnesses.
- Sensors and test setup (his words, 2026-11-24, MANUS application): on his current shoulder exoskeleton he used FSRs,
  a load cell from Forsentek and torque sensors, and he BUILT a test setup for them (the sensors). The exoskeleton
  stiffness tests still used the existing lab setup (do not write that he built the stiffness rig). He COMPARED
  options before choosing parts (which parts exactly not yet given; keep it general). Master's: pressure readings and
  pressure control of the pneumatic muscles went through LabVIEW. Supplier contact: ONE line only in a document.
  He has ideas for glove/hand mechanisms with CABLES and PRESSURE mechanisms (ideas only, never built).
- Single-column CV (his correction, 2026-11-24): the TWO-COLUMN CV is ALWAYS the main CV. A single-column version is
  only an EXTRA plain copy when he asks for one (e.g. for Workday). Never replace the two-column CV with it. The
  JBT Marel Helsingborg and Marel Aarhus CVs were wrongly made single-column only; fix them only when he says so.
  He is willing to relocate to Sweden (Helsingborg).
- DO NOT START WORK UNLESS HE SAYS SO (his order, 2026-11-24): answer, propose and ask, but do not build, redo or change
  documents until he clearly tells me to.
- New ideas (his words, 2026-11-24, Intralox): he has ideas to explore ORIGAMI-based and BOWDEN CABLE exoskeletons
  (ideas only, never built). May be mentioned in cover letters as ideas he wants to explore.
- ASSA ABLOY Rychnov (his answers, 2026-11-24): willing to relocate to Rychnov nad Kneznou (Czech Republic); do NOT
  add a Czech language line; headline changed per job with R&D in it ("Mechanical and Robotics R&D Engineer", his OK
  for this job); he asked for a single-column CV, made as an EXTRA copy next to the two-column main CV (rule above).
- DAILY JOB SEARCH RULES (his order, 2026-11-24; routine "Daily job search – Arunabha", runs 09:22 Copenhagen):
  roles = mechanical/mechatronics/robotics design, actuator/robotics hardware, test and validation, R&D and
  prototyping, lab hardware/test rigs; early career to mid (no senior/lead unless ~3 yrs accepted); show only 60+;
  exoskeleton companies shown whatever language they ask; extra priority robotics/wearables startups and R&D roles;
  country order DK, NL, FR, DE, AT, BE, CZ, rest of EU; add Australia, NZ, India from 1 June 2027. Number the jobs
  with match %; email the list to 97arunabhasit027@gmail.com (his OK, only to himself), push + chat. Under each job:
  a 2-4 line description of the role, then link | why it fits | main gap | visa/language note | contact email.
  ONLY for the numbers he marks (reply to the email or in chat): draft a tailored CV + personalised cover letter, and
  if the job has a contact email, a personalised Gmail DRAFT with both attached (never send). Nothing for unmarked jobs.
  Always show the match % next to each listed job: "1. [72% match] Company - Title, City, Country".
  The routine must NOT delete itself.
- CATIA (his words, 2026-11-25): used it ONCE during his BTech; much stronger in SolidWorks; can pick up CATIA if a job
  needs it. Write only "CATIA (basic, used during BTech; quick to pick up)" or say he is ready to learn it; never more.
- Belgium (his answers, 2026-11-25, Kingfisher Recruitment / Lint): willing to relocate to Belgium; for that job the CV
  Languages line gets "Dutch (willing to learn)"; he chose a 1-page CV even though the title is Product Development.
- Dutch line wording (his order, 2026-11-25, Movu Robotics): write it as "Willing to learn: Dutch" in the CV Languages
  section for Belgian/Dutch jobs when he wants a Dutch line. He likes story openings in cover letters (VeroTech, Movu).
- Daily search focus (his order, 2026-11-25): look MORE for R&D teams and industrial postdocs (company-linked
  postdocs / research engineer roles with industry partners).
- Clutch story exception (his OK, 2026-11-23): allowed as ONE subtle short line in the Cell Labs email only (not CV).

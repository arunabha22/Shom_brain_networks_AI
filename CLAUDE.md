# Standing instructions from Arunabha (apply to every chat and every document)

## Self-update rule (always)
- Whenever Arunabha corrects a fact, adds a new fact or gives a new preference, IMMEDIATELY add it to this file
  (and to GENERAL_RULES_copy_paste.md), fix the documents being worked on, commit and push. Never wait to be asked.

## Write like a person, not like an AI
- TOP PRIORITY, ALWAYS: every word must sound like Arunabha wrote it himself. Simple, warm, direct, a little
  imperfect. If a sentence sounds polished or generic, rewrite it in plainer words.
- Plain, specific, first-hand wording. Short and medium sentences mixed; some start with "I".
- Avoid AI-sounding words: leverage, spearhead, seamless, robust, cutting-edge, passionate, delve, dynamic,
  synergy, tapestry, testament, pivotal, foster, navigate, realm, elevate, harness, showcase, meticulous,
  "I am excited to", "in today's fast-paced world", "I am confident that", "not only... but also".
- No em dashes (—) in letters, messages or answers to paste. Use commas, full stops or "and".
- No rule-of-three lists everywhere, no tidy summary sentence at the end of every paragraph.
- Concrete facts and numbers over adjectives. Slightly informal is fine in messages.
- No hidden watermarks: doc_helpers.py tidies text (no zero-width chars, no em dashes, straight quotes) and
  sets PDF/DOCX metadata author/creator/producer to "Arunabha Majumder" (no ReportLab / python-docx tags).

## Remove-AI-marks step (always)
- For every document or text produced for him, run the remove-ai-marks routine: check the cleaning service
  (WATERMARKS_SERVICE_URL, default http://127.0.0.1:8765, GET /health); if it is up, send each output file to
  /clean and deliver the cleaned version; if it is down, say so in one short line. Never claim it ran if it did not.

## Outreach rules (see outreach-style.md; check it before drafting outreach)
- When he sends a job for hiring-contact research, follow applications/job_search/hiring_contact_research_prompt.md.
- Name is "Arunabha Majumder"; never "Shom" in drafts. Keep messages short.
- Always include the portfolio: https://arunabha22.github.io/arunabha-majumder/
  It contains ONLY videos and results from his work (no CAD files, drawings or prototype photos). Describe it
  that way, never as "CAD models, drawings or photos".
- Art Instagram (his, 2026-11): surreal_art_engine (https://www.instagram.com/surreal_art_engine/). GitHub:
  https://github.com/arunabha22. Share them when art or code is relevant (e.g. LEGO Creative Play Lab).
- Never mention automated rejections or frustration with applications.
- Never write "FEA"; use "analysis" or "mechanical analysis" (only where true).
- Friend recommendations: no technical claims.

## Facts (never exaggerate)
- PhD (Aalborg, 2023 – present): SolidWorks + 3D printing. NO FEA/FEM claimed. Fusion 360: he knows
  it a little and last used it in 2019 (confirmed 2026-11); list it only as "Fusion 360 (basic, last used 2019)", never as professional or substantial experience.
- Bachelor's capstone exoskeleton (his correction, 2026-11-22): it had NO lathe/machined parts. NEVER write lathe,
  machining or welding for the capstone. Lathe and welding were done during his BTech, but not on the capstone; list
  them only as general Bachelor's skills. Capstone wording: CAD, wiring and connectors, assembly and testing.
- Say "shoulder exoskeleton", never "wearable machines".
- 5-bar planar parallel robot, EXACT wording to use (never reduce it to just "estimated force"): "Designed and
  modelled a novel 5-bar planar parallel robot with variable stiffness mechanisms (VSM), estimated its stiffness with
  less than 10% error, and quantified human arm impedance." (Short form: "...with VSM; estimated its stiffness with
  less than 10% error and quantified human arm impedance.") Force estimation via VSA + Jacobian may be added as detail.
- Muscle effort result: keep ">15%" (journal under review). Do not share the PhD video.
- Master's (CSIR-CMERI): he FABRICATED/ASSEMBLED pneumatic artificial muscles to someone else's existing design and
  used the lab's existing test setup. He did NOT design the muscles and did NOT build the test bench/rig. The neural
  network was developed by someone else. His part: collected the experimental data, fed it into that neural network,
  used the output to design/tune the OUTER PID loop and understood how the gain-scheduled controller works
  (MATLAB/Simulink, 0.3-0.78% error, IEEE CONECCT 2022). Never say he designed/developed the neural network.
  Exact wording: he designed the OUTER PID loop of the neural network-based gain-scheduled controller in MATLAB/Simulink
  and implemented it in LabVIEW to drive the pneumatic muscle. Write this as ONE point (never a separate "Simulink
  model" line, never repeat it).
- NO force controller, no force control, no impedance/admittance control. Force work = force ESTIMATION only
  (5-bar robot, VSA + Jacobian). Do not add skills or methods he has not confirmed; when unsure, leave it out.
- Assist-as-Needed controller: a TEAM effort of 3 people. His part: helped with the equations (e.g. Fourier fit)
  and defined what should happen in the GUI. Never say he alone developed/implemented it.
- Exoskeleton design detail (his words): a variable stiffness mechanism (VSM) stores energy over a range that can be
  adjusted to the user's needs, and a motor works in parallel with it; together they provide the torque needed to
  lift the arm/object (shoulder flexion/extension). A secondary worm gear system pretensions the spring to adjust
  the stiffness range.
- He DID optimise his exoskeleton design with a genetic algorithm (always include it). The GA optimised the VSM
  diameter, the spring stiffness value and the pretension force (objective not yet confirmed; do not invent it).
- Exoskeleton clutch story (his words): the design has a clutch that locks the spring; the first clutch kept breaking
  and was hard to manufacture with the institute's facilities, so he switched to a simple bolt-locking clutch. Both
  versions can lock at 8 different angles. NEVER put the clutch story in any CV, cover letter, message or answer
  unless he explicitly asks for it (his order, 2026-11). Use it only if he asks, e.g. live in an interview.
- Job title for the Aalborg PhD in CVs (his order, 2026-11): "Research Assistant, Aalborg University", not
  "PhD Researcher". The PhD stays under Education.
- Outer PID loop (Master's) is NOT a simple PID: it has integral anti-windup and error nonlinearisation. Always
  say so when describing it; never call it a simple PID.
- Whenever the 6 participants are mentioned, always say it was the arm impedance study with the 5-bar robot.
- German: never write gap sentences about German (e.g. "I don't speak German, that may rule me out"). Just say
  "willing to learn German" (confirmed 2026-11). In COVER LETTERS do not write "willing to learn German" at all
  (his order, 2026-11); keep it only in the CV Languages line.
- Always include "GATE qualified" (Achievements) and a Study Abroad heading (NUS, Sep-Nov 2025) on CVs, and the
  portfolio link. In cover letters, use the new closing ("I would be excited to bring ... new ideas ..."), see NEW DOCUMENT FORMAT.
- No gap/apology paragraphs in cover letters unless he asks.
- The exoskeleton was NOT tested in SolidWorks. Its stiffness (how much stiffness it can provide) was measured on a
  PHYSICAL test setup. Never write that exoskeleton parts were checked with SolidWorks stiffness analysis.
  "Stiffness analysis in SolidWorks" may appear only as a general skill (he has done it before), never tied to the
  exoskeleton. Never write "FEA"; no Abaqus/Ansys/HyperWorks claims.
- He DID integrate the motor, encoder and force sensors on the exoskeleton. He DID teach university courses and
  supervise Bachelor's students (2023-2025), but do NOT put teaching in CVs anymore (his order, 2026-11-18).
- Biomechanics study: Arunabha did the data collection (12 participants), not the analysis. He recorded EMG with the
  Qualisys data acquisition system.
- EMG vs position (his correction, 2026-11): the EMG data (12 participants) came from the EXOSKELETON study. The 5-bar
  robot study (6 participants) recorded arm POSITION/motion data with Qualisys, NOT EMG. Always keep them separate.
- Arm impedance study: Qualisys motion-capture cameras tracked arm motion to quantify human arm impedance with the
  5-bar robot, 6 participants. He IMPLEMENTED (did not build) an Arduino-based trigger system to sync the robot's motion with the Qualisys
  recording; he has experience synchronising robot motion with Qualisys. Never say he built it.
- Bachelor's capstone was an upper-limb rehabilitation EXOSKELETON (for a paralysed arm); always name it as an
  exoskeleton in CVs and letters.
- Do NOT mention the journal papers under review (papers 2 and 3) in any document.
- PhD timing: write "thesis expected to be finished in March" (or "thesis expected March"). Never "I finish in
  March" or "ends March". Defence year 2027, no month. Do NOT put the thesis timing in the profile/summary of
  short CVs (Education or letters only).
- Study abroad stay at the National University of Singapore (NUS) during the PhD, Sep-Nov 2025 (3 months).
  Mention only as one line under Education; no project or results to claim; never invent work done there.
  His words (2026-11): it was INDEPENDENT RESEARCH, from September to the end of November 2025.
- References (PERMANENT RULE): every CV/resume gets a References section with these two referees (he has their
  recommendation letters):
  1. Shaoping Bai, PhD, Professor, Department of Materials and Production, Aalborg University, sbh@mp.aau.dk
  2. Lars Rosgaard Jensen, Associate Professor, Head of Section (Physics, Mechanics and Materials), Head of Labs,
     Department of Materials and Production, Aalborg University (no email given yet; never invent one)
  3. Anderson de Souza Castelo Oliveira, Associate Professor, Department of Materials and Production, Aalborg
     University (no email given yet; never invent one)
  Do not name referees in cover letters unless he asks.
- Publications: only IEEE CONECCT 2022 and ISRM 2026 (Best Paper). Never list the ASME JMR paper.
- Achievements he confirmed: GATE exam qualified (no year/score given; never invent one). The INR 100,000 TATA
  Technologies grant for the Bachelor's exoskeleton was through TATA Technologies "Prayatna".
- Languages: list Danish ("willing to learn") ONLY when the company/job is in Denmark; leave it out otherwise.
  For German companies/jobs, ALWAYS list "German (willing to learn)" on the CV (his order, 2026-11-21).
- He is willing to relocate to France (confirmed 2026-11), to Lausanne, Switzerland (confirmed 2026-11) and to
  Germany (confirmed 2026-11) and to the Netherlands (confirmed 2026-11; he will apply for a Dutch permit). No Dutch. No French,
  but willing to learn (say so for French jobs).
- His own wording (2026-11): exoskeleton parts were optimised with the GA, designed in SolidWorks, 3D printed for
  initial testing, then MANUFACTURED (do not say he machined them himself in the PhD); torque/force sensors were
  used to define its mechanical properties; the >25% saving is motor energy, which improves battery life.
- Master's pneumatic artificial muscles were part of a SOFT EXOSUIT project. His words (2026-11): the muscles were
  silicone-based, and he worked in a team of 4 (electronics and mechanical engineers) on the LabVIEW control
  architecture.
- Bachelor's arm exoskeleton and exo glove used motor assistance with Arduino-based control and manual switching
  (his words, 2026-11). The Bachelor's project used SERVO motors.
- He built small hexapods in 2017 (not much since). Master's: hands-on experience with pneumatic muscles and pressure
  valves (his words, 2026-11).
- Bachelor's capstone: an arm exoskeleton AND an exo glove for the human arm, funded by a TATA Technologies grant
  under the "Prayatna Innovation Fund"; won Best Major Project in the department.
- Start date (his words, 2026-11): he can start as soon as possible, but needs time to apply for a visa and relocate.
  Use this instead of "from spring 2027" when asked about start dates. His PhD research work is finished; only the
  thesis writing is ongoing, and he can start a job alongside finishing the thesis.
- No PLC / ROS / Danish experience. No referees named in letters (CVs list the two referees above).
- Fine arts certificate (verified from his certificate): "Senior Diploma in Fine Arts (Painting)" (Ankan Sree,
  Ankan Kala Bibhag), Bangiya Sangeet Parishad, West Bengal, 3rd-year exam 2007-2008, dated 25 Aug 2008, First
  Division with Distinction. Use this in Education.
- Always include his drawing skills: Diploma in Fine Arts; hand sketching of concepts, technical illustrations
  and visuals for papers, posters and demos (plus SolidWorks engineering drawings). Put it in Skills, and in the
  summary/letter when the role values concept sketching, design, communication or demos.
- ALWAYS keep BOTH the fine arts AND the graphic design in every CV and cover letter (his words, 2026-11):
  Senior Diploma in Fine Arts (Painting) plus graphic design / illustration with Adobe Illustrator, Photoshop
  and Procreate. Never drop them to save space.
- ALWAYS put BOTH emails in every CV, cover letter, email signature and message signature:
  somrkmv1997@gmail.com and 97arunabhasit027@gmail.com (plus phone +45 71 62 24 00 and portfolio link).
- Resume and cover letter as separate PDFs; cover letters usually 1 page; ATS-friendly.
- FILE NAMES (his rule, 2026-11): never "Arunabha_Majumder_...". Name every CV and cover letter
  "AM <Company> CV.pdf" and "AM <Company> Cover Letter.pdf" (e.g. "AM mkind CV.pdf").
- ALWAYS put his photo on every CV for every job (top right of page 1). Photo file: applications/assets/photo.jpeg
  (see the Novo Nordisk build_documents.py for how it is placed). If an ad says "no photo", still make the photo CV
  and just mention that in one line, offering a no-photo copy.
- Keep the CV headline under the name short (e.g. "Mechanical Design Engineer") so no header line runs into the photo.
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

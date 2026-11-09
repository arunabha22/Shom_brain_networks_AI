// A4 landscape poster for the LEGO Creative Play Lab Mechanical Engineering Internship (editable .pptx).
// Facts follow CLAUDE.md. No clutch story (only in interview when he asks). Brick-shaped cards as the motif.
const pptxgen = require("pptxgenjs");
const path = require("path");
const { applyTheme } = require("/root/.claude/skills/synced/082d1313-e7d3-4ebc-81f4-e338b3404a13_826f4888-9b14-49c8-b47d-cb167a618a2b/pptx/scripts/apply_theme.js");

const OUT = path.join(__dirname, "AM LEGO Poster.pptx");
const PHOTO = path.join(__dirname, "..", "assets", "photo.jpeg");

const THEME = {
  name: "Play Builder",
  headFontFace: "Arial", bodyFontFace: "Arial",
  colors: { dk1: "1D1D1F", lt1: "FFFFFF", dk2: "2B2D42", lt2: "F4F6FA",
            accent1: "D62828", accent2: "F7B801", accent3: "1D4E89", accent4: "2A9D8F",
            accent5: "6C757D", accent6: "F77F00", hlink: "1D4E89", folHlink: "6C757D" },
};
const RED = "D62828", YEL = "F7B801", BLUE = "1D4E89", TEAL = "2A9D8F", INK = "1D1D1F", GREY = "5A5F66", SOFT = "F4F6FA";

const pres = new pptxgen();
pres.defineLayout({ name: "A4_LANDSCAPE", width: 11.69, height: 8.27 });
pres.layout = "A4_LANDSCAPE";
pres.author = "Arunabha Majumder"; pres.company = "Arunabha Majumder"; pres.title = "AM LEGO Poster";
pres.theme = { headFontFace: "Arial", bodyFontFace: "Arial" };

const s = pres.addSlide();
s.background = { color: "FFFFFF" };

// Brick card: rounded body + studs on top
function brick(x, y, w, h, color, name, studs = 4) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, fill: { color }, line: { color, width: 0 },
    rectRadius: 0.08, objectName: name + " brick",
    shadow: { type: "outer", color: "000000", opacity: 0.18, blur: 4, offset: 2, angle: 90 } });
  const d = 0.26, gap = (w - studs * d) / (studs + 1);
  for (let i = 0; i < studs; i++) {
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x + gap + i * (d + gap), y: y - 0.1, w: d, h: 0.16,
      fill: { color }, line: { color, width: 0 }, rectRadius: 0.04, objectName: name + " stud " + (i + 1) });
  }
}

// ---- Header ----
s.addText("Hi, I'm Arunabha.", { x: 0.5, y: 0.35, w: 7.6, h: 0.7, fontSize: 36, bold: true, color: INK,
  margin: 0, isTextBox: true, objectName: "Title" });
s.addText([
  { text: "A mechanical engineer who paints. ", options: { bold: true, color: RED } },
  { text: "I build mechanisms with motors and sensors inside, and I sketch every idea on paper first.",
    options: { color: GREY } },
], { x: 0.5, y: 1.05, w: 7.6, h: 0.6, fontSize: 14, margin: 0, isTextBox: true, objectName: "Tagline" });
s.addText("From Agartala, Tripura (India) to Aalborg, Denmark. Now I'd love to build new play in Billund.",
  { x: 0.5, y: 1.62, w: 7.6, h: 0.35, fontSize: 11.5, italic: true, color: GREY, margin: 0, isTextBox: true,
    objectName: "Journey" });

// Photo (top right) with a yellow brick frame behind it
brick(9.35, 0.42, 1.85, 2.1, YEL, "Photo frame", 3);
s.addImage({ path: PHOTO, x: 9.47, y: 0.52, w: 1.61, h: 1.9, sizing: { type: "cover", w: 1.61, h: 1.9 },
  altText: "Photo of Arunabha Majumder", objectName: "Photo" });

// ---- Stat row ----
const stats = [
  ["25%+", "less motor energy in my\nshoulder exoskeleton", RED],
  ["<10%", "error when estimating my\n5-bar robot's stiffness", BLUE],
  ["Best Paper", "Award, IFToMM\nISRM 2026", TEAL],
];
stats.forEach(([big, small, c], i) => {
  const x = 0.5 + i * 2.95;
  s.addText(big, { x, y: 2.2, w: 2.75, h: 0.55, fontSize: big.length > 6 ? 24 : 30, bold: true, color: c,
    margin: 0, isTextBox: true, objectName: "Stat " + (i + 1) });
  s.addText(small, { x, y: 2.75, w: 2.75, h: 0.48, fontSize: 10.5, color: GREY, margin: 0, isTextBox: true,
    objectName: "Stat label " + (i + 1) });
});

// ---- "What I've built" brick cards ----
s.addText("What I've built", { x: 0.5, y: 3.42, w: 6, h: 0.4, fontSize: 18, bold: true, color: INK, margin: 0,
  isTextBox: true, objectName: "Built heading" });
const cards = [
  [RED, "Shoulder exoskeleton (PhD)",
   "A spring mechanism, pretensioned by a worm gear, working with a 6 Nm motor. Optimised with a genetic algorithm, designed in SolidWorks, 3D printed, then manufactured. I integrated the motor, encoder and force sensors myself."],
  [BLUE, "5-bar robot (PhD)",
   "Designed and modelled a novel 5-bar parallel robot with variable stiffness mechanisms. Estimated its stiffness with less than 10% error and measured how stiff a human arm is (6 people)."],
  [TEAL, "Soft exosuit (Master's)",
   "Made silicone-based pneumatic muscles in a team of 4. Designed the outer PID loop, with anti-windup and error nonlinearisation, and ran it in LabVIEW."],
  [YEL, "Bachelor's builds",
   "An arm exoskeleton and exo glove with Arduino control (Best Major Project, TATA grant). Plus a Go-Kart and a hybrid Efficycle with student teams."],
];
cards.forEach(([c, head, body], i) => {
  const x = 0.5 + i * 2.72, y = 3.98, w = 2.52, h = 2.55;
  brick(x, y, w, h, c, "Card " + (i + 1), 4);
  const txt = c === YEL ? INK : "FFFFFF";
  s.addText(head, { x: x + 0.15, y: y + 0.14, w: w - 0.3, h: 0.5, fontSize: 12.5, bold: true, color: txt,
    margin: 0, valign: "top", isTextBox: true, objectName: "Card title " + (i + 1) });
  s.addText(body, { x: x + 0.15, y: y + 0.66, w: w - 0.3, h: h - 0.8, fontSize: 11.5, color: txt, margin: 0,
    valign: "top", isTextBox: true, objectName: "Card text " + (i + 1) });
});

// ---- Right column: sketch placeholder + what I bring ----
s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 9.35, y: 2.75, w: 1.85, h: 0.95, fill: { color: SOFT },
  line: { color: "B8BEC6", width: 1, dashType: "dash" }, rectRadius: 0.06, objectName: "Sketch placeholder" });
s.addText("Put one of your\nsketches or paintings here", { x: 9.35, y: 2.75, w: 1.85, h: 0.95, fontSize: 9,
  italic: true, color: GREY, align: "center", valign: "middle", margin: 0, isTextBox: true,
  objectName: "Sketch placeholder text" });

// ---- Bottom: what I bring + contact ----
s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y: 6.85, w: 10.7, h: 1.0, fill: { color: SOFT },
  line: { color: SOFT, width: 0 }, rectRadius: 0.08, objectName: "Footer panel" });
s.addText([
  { text: "What I bring to Creative Play Lab: ", options: { bold: true, color: INK } },
  { text: "first-principles thinking (forces, energy, springs), fast making with SolidWorks, 3D printing, " +
    "Arduino and sensors, workshop skills, and a Senior Diploma in Fine Arts with graphic design in Illustrator, " +
    "Photoshop and Procreate.", options: { color: GREY } },
], { x: 0.7, y: 6.93, w: 10.3, h: 0.5, fontSize: 10.5, margin: 0, valign: "top", isTextBox: true,
  objectName: "What I bring" });
s.addText([
  { text: "Arunabha Majumder", options: { bold: true, color: RED } },
  { text: "   |   somrkmv1997@gmail.com   |   97arunabhasit027@gmail.com   |   +45 71 62 24 00   |   ",
    options: { color: INK } },
  { text: "arunabha22.github.io/arunabha-majumder",
    options: { color: BLUE, hyperlink: { url: "https://arunabha22.github.io/arunabha-majumder/" } } },
], { x: 0.7, y: 7.47, w: 10.3, h: 0.3, fontSize: 10, margin: 0, isTextBox: true, objectName: "Contact" });

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log(OUT);
})();

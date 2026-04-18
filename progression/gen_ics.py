"""Generate MCAT study schedule ICS file.

Reflects the cascade applied 2026-04-17 (Day 3 delayed +1 day; second cascade).
Mon-Sun weekly structure. Times per CLAUDE.md weekly time blocks.
"""
import datetime
import os
import uuid

# Time blocks by weekday (Mon=0 ... Sun=6)
TIMES = {
    0: ("07:00", "12:00"),  # Mon
    1: ("13:00", "18:00"),  # Tue
    2: ("16:00", "21:00"),  # Wed
    3: ("13:00", "18:00"),  # Thu
    4: ("12:30", "17:30"),  # Fri
    5: ("07:00", "12:00"),  # Sat
    6: ("07:00", "12:00"),  # Sun
}

events = []


def add(date_str, section, topic, week, phase):
    """Add a study session. Times are looked up by day-of-week."""
    d = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    start_time, end_time = TIMES[d.weekday()]
    sh, sm = map(int, start_time.split(":"))
    eh, em = map(int, end_time.split(":"))
    dtstart = d.replace(hour=sh, minute=sm)
    dtend = d.replace(hour=eh, minute=em)
    events.append((dtstart, dtend, section, topic, week, phase))


# Kickoff (Mon Apr 13)
add("2026-04-13", "ALL", "MCAT: Kickoff -- Amino Acid Foundations", 0, 1)

# === Phase 1: Content Review (Weeks 1-11) ===
phase1 = [
    # Week 1 (Apr 14-19) -- Apr 16 & 17 are REST/FLEX (no events)
    ("2026-04-14", "BB",   "Amino Acids -- All 20 Structures & Properties", 1),
    ("2026-04-15", "CP",   "Atomic Structure & Periodic Trends", 1),
    ("2026-04-18", "CP",   "Stoichiometry, Reactions & Ions (Gen Chem Ch 4)", 1),
    ("2026-04-19", "PS",   "Biological Bases of Behavior & Neuroscience", 1),
    # Week 2 (Apr 20-26)
    ("2026-04-20", "BB",   "Protein Structure & Folding (1-4)", 2),
    ("2026-04-21", "CP",   "Bonding & Intermolecular Forces", 2),
    ("2026-04-22", "CARS", "Foundations -- Main Idea & Passage Mapping", 2),
    ("2026-04-23", "BB",   "Enzyme Kinetics & Regulation", 2),
    ("2026-04-24", "CP",   "Solutions & Concentration (Gen Chem Ch 9)", 2),
    ("2026-04-25", "PS",   "Sensation, Perception & Attention", 2),
    ("2026-04-26", "BB",   "Non-Enzymatic Protein Function & Lab Techniques", 2),
    # Week 3 (Apr 27-May 3)
    ("2026-04-27", "CP",   "Thermodynamics & Thermochemistry", 3),
    ("2026-04-28", "CARS", "Author Tone & Rhetorical Strategy", 3),
    ("2026-04-29", "BB",   "DNA Structure, Replication & Repair", 3),
    ("2026-04-30", "CP",   "Chemical Kinetics", 3),
    ("2026-05-01", "PS",   "Learning -- Classical & Operant Conditioning", 3),
    ("2026-05-02", "BB",   "Transcription & RNA Processing", 3),
    ("2026-05-03", "CP",   "Chemical Equilibrium", 3),
    # Week 4 (May 4-10)
    ("2026-05-04", "CARS", "Evidence vs Opinion & Argument Structure", 4),
    ("2026-05-05", "BB",   "Translation & Gene Regulation", 4),
    ("2026-05-06", "CP",   "Acids, Bases & Buffers", 4),
    ("2026-05-07", "PS",   "Memory, Cognition & Language", 4),
    ("2026-05-08", "BB",   "Biotechnology & Molecular Techniques", 4),
    ("2026-05-09", "CP",   "Electrochemistry & Redox Reactions", 4),
    ("2026-05-10", "CARS", "Inference & Implication Questions", 4),
    # Week 5 (May 11-17)
    ("2026-05-11", "BB",   "Cell Structure, Organelles & Cytoskeleton", 5),
    ("2026-05-12", "CP",   "Organic Chemistry -- Functional Groups & Nomenclature", 5),
    ("2026-05-13", "PS",   "Consciousness, Sleep & Drugs", 5),
    ("2026-05-14", "BB",   "Membrane Structure & Transport", 5),
    ("2026-05-15", "CP",   "Stereochemistry & Isomers", 5),
    ("2026-05-16", "CARS", "Strengthen / Weaken Questions", 5),
    ("2026-05-17", "BB",   "Cell Signaling & Signal Transduction", 5),
    # Week 6 (May 18-24)
    ("2026-05-18", "CP",   "SN1/SN2/E1/E2 Reactions", 6),
    ("2026-05-19", "PS",   "Motivation, Emotion & Stress", 6),
    ("2026-05-20", "BB",   "Cell Cycle, Mitosis & Cancer Biology", 6),
    ("2026-05-21", "CP",   "Carbonyl Chemistry & Carboxylic Acid Derivatives", 6),
    ("2026-05-22", "CARS", "Reasoning Beyond the Text", 6),
    ("2026-05-23", "BB",   "Meiosis & Mendelian Genetics", 6),
    ("2026-05-24", "CP",   "Spectroscopy -- IR, NMR & Mass Spec", 6),
    # Week 7 (May 25-31)
    ("2026-05-25", "PS",   "Development, Identity & Personality", 7),
    ("2026-05-26", "BB",   "Non-Mendelian Genetics, Mutations & Evolution", 7),
    ("2026-05-27", "CP",   "Separations, Purification & Analytical Techniques", 7),
    ("2026-05-28", "CARS", "Full Section Practice #1 + Midpoint Review", 7),
    ("2026-05-29", "BB",   "Glycolysis & Fermentation", 7),
    ("2026-05-30", "CP",   "Kinematics & Newton's Laws", 7),
    ("2026-05-31", "PS",   "Psychological Disorders & Treatment", 7),
    # Week 8 (Jun 1-7)
    ("2026-06-01", "BB",   "Pyruvate Dehydrogenase & TCA Cycle", 8),
    ("2026-06-02", "CP",   "Work, Energy & Momentum", 8),
    ("2026-06-03", "CARS", "Pacing & Process of Elimination", 8),
    ("2026-06-04", "BB",   "Electron Transport Chain & Oxidative Phosphorylation", 8),
    ("2026-06-05", "CP",   "Fluids & Solids", 8),
    ("2026-06-06", "PS",   "Social Psychology -- Attitudes, Groups & Behavior", 8),
    ("2026-06-07", "BB",   "Gluconeogenesis, Glycogen & Pentose Phosphate Pathway", 8),
    # Week 9 (Jun 8-14)
    ("2026-06-08", "CP",   "Electrostatics & Magnetism", 9),
    ("2026-06-09", "CARS", "Humanities Passages Deep Dive", 9),
    ("2026-06-10", "BB",   "Lipid & Amino Acid Metabolism + Integration", 9),
    ("2026-06-11", "CP",   "Circuits & Electricity", 9),
    ("2026-06-12", "PS",   "Social Interaction, Attribution & Discrimination", 9),
    ("2026-06-13", "BB",   "Microbiology -- Bacteria, Viruses & Prions", 9),
    ("2026-06-14", "CP",   "Waves, Sound & Doppler Effect", 9),
    # Week 10 (Jun 15-21)
    ("2026-06-15", "CARS", "Social Sciences Passages Deep Dive", 10),
    ("2026-06-16", "BB",   "Immunology -- Innate & Adaptive Immunity", 10),
    ("2026-06-17", "CP",   "Light, Optics & Diffraction", 10),
    ("2026-06-18", "PS",   "Sociological Theories & Social Institutions", 10),
    ("2026-06-19", "BB",   "Cardiovascular System & Blood", 10),
    ("2026-06-20", "CP",   "Nuclear Chemistry & Radioactive Decay", 10),
    ("2026-06-21", "CARS", "Full Section Practice #2 + Comprehensive Review", 10),
    # Week 11 (Jun 22-28) -- Phase 1/2 transition
    ("2026-06-22", "BB",      "Respiratory System & Gas Exchange", 11),
    ("2026-06-23", "CP",      "Math Skills, Units & Dimensional Analysis", 11),
    ("2026-06-24", "PS",      "Demographics, Stratification & Health Disparities", 11),
    ("2026-06-25", "BB",      "Digestive System & Nutrient Absorption", 11),
    ("2026-06-26", "CP",      "Research Design & Data Interpretation", 11),
    ("2026-06-27", "CARS",    "Timed Practice + Phase 1 Final Assessment", 11),
    ("2026-06-28", "ALL",     "Third-Party FL #1 (Full-Length)", 11),
]
for d, sec, top, w in phase1:
    add(d, sec, top, w, 1)

# === Phase 2: Practice & Integration (Weeks 12-15) ===
phase2 = [
    # Week 12 (Jun 29-Jul 5)
    ("2026-06-29", "CP/CARS", "FL #1 Review -- CP & CARS", 12),
    ("2026-06-30", "BB/PS",   "FL #1 Review -- BB & PS", 12),
    ("2026-07-01", "BB",      "BB Passage-Based Practice (59 Qs timed)", 12),
    ("2026-07-02", "CP",      "CP Passage-Based Practice (59 Qs timed)", 12),
    ("2026-07-03", "CARS/PS", "CARS Full Section + PS Practice", 12),
    ("2026-07-04", "VARIES",  "Weak Area Deep Dive #1 -- Highest Priority", 12),
    ("2026-07-05", "VARIES",  "Weak Area Deep Dive #2", 12),
    # Week 13 (Jul 6-12)
    ("2026-07-06", "CARS",    "CARS Intensive -- 6 Passages Timed", 13),
    ("2026-07-07", "ALL",     "Third-Party FL #2 (Full-Length)", 13),
    ("2026-07-08", "ALL",     "FL #2 Full Review", 13),
    ("2026-07-09", "ALL",     "Mixed Section Practice + Anki Marathon", 13),
    ("2026-07-10", "ALL",     "Third-Party FL #3 (Full-Length)", 13),
    ("2026-07-11", "ALL",     "FL #3 Full Review + Error Pattern Analysis", 13),
    ("2026-07-12", "BB/CP",   "Data Interpretation & Experimental Design", 13),
    # Week 14 (Jul 13-19)
    ("2026-07-13", "PS",      "PS Deep Dive -- Research Methods & Epidemiology", 14),
    ("2026-07-14", "CP",      "CP Calculation Drill + Physics Problem Workshop", 14),
    ("2026-07-15", "CARS",    "CARS Full Section + Weekly Review", 14),
    ("2026-07-16", "ALL",     "Third-Party FL #4 (Full-Length)", 14),
    ("2026-07-17", "ALL",     "FL #4 Full Review + Error Log Analysis", 14),
    ("2026-07-18", "BB",      "Biochemistry Integration Review", 14),
    ("2026-07-19", "CP",      "Physics + Gen Chem Problem-Solving", 14),
    # Week 15 (Jul 20-26) -- Phase 2/3 transition
    ("2026-07-20", "PS",      "PS Comprehensive Section Practice", 15),
    ("2026-07-21", "CARS",    "CARS Strategy Refinement + Phase 3 Planning", 15),
    ("2026-07-22", "ALL",     "Third-Party FL #5 (Full-Length)", 15),
    ("2026-07-23", "ALL",     "FL #5 Full Review + Score Trend Analysis", 15),
    ("2026-07-24", "BB/CP",   "Content Gap Remediation -- BB & CP", 15),
    ("2026-07-25", "PS/CARS", "Content Gap Remediation -- PS & CARS Maintenance", 15),
    ("2026-07-26", "ALL",     "Mixed Timed Practice + Strategy Review", 15),
]
for d, sec, top, w in phase2:
    add(d, sec, top, w, 2)

# === Phase 3: AAMC Materials (Weeks 16-19) ===
phase3 = [
    # Week 16 (Jul 27-Aug 2)
    ("2026-07-27", "ALL",  "Phase 2 Assessment + Phase 3 Planning", 16),
    ("2026-07-28", "BB",   "AAMC QPack -- Biology Vol 1", 16),
    ("2026-07-29", "CP",   "AAMC QPack -- Chemistry Vol 1", 16),
    ("2026-07-30", "CP",   "AAMC QPack -- Physics", 16),
    ("2026-07-31", "BB",   "AAMC QPack -- Biology Vol 2", 16),
    ("2026-08-01", "CP",   "AAMC QPack -- Chemistry Vol 2", 16),
    ("2026-08-02", "CARS", "AAMC CARS QPack Vol 1", 16),
    # Week 17 (Aug 3-9)
    ("2026-08-03", "CARS", "AAMC CARS QPack Vol 2", 17),
    ("2026-08-04", "BB",   "AAMC Section Bank -- BB", 17),
    ("2026-08-05", "CP",   "AAMC Section Bank -- CP", 17),
    ("2026-08-06", "PS",   "AAMC Section Bank -- PS", 17),
    ("2026-08-07", "ALL",  "Section Bank Full Review Day", 17),
    ("2026-08-08", "ALL",  "AAMC FL 1 (Full-Length)", 17),
    ("2026-08-09", "ALL",  "AAMC FL 1 -- Full Review", 17),
    # Week 18 (Aug 10-16)
    ("2026-08-10", "ALL",     "Targeted Weak Area Review", 18),
    ("2026-08-11", "ALL",     "AAMC FL 2 (Full-Length)", 18),
    ("2026-08-12", "ALL",     "AAMC FL 2 -- Full Review", 18),
    ("2026-08-13", "ALL",     "High-Yield Content Blitz + Leech Review", 18),
    ("2026-08-14", "CARS/PS", "CARS Maintenance + PS Final Vocabulary Drill", 18),
    ("2026-08-15", "ALL",     "AAMC FL 3 (Full-Length)", 18),
    ("2026-08-16", "ALL",     "AAMC FL 3 -- Full Review", 18),
    # Week 19 (Aug 17-23) -- Final substantive prep week
    ("2026-08-17", "ALL",     "AAMC FL 4 (Full-Length)", 19),
    ("2026-08-18", "ALL",     "AAMC FL 4 -- Full Review", 19),
    ("2026-08-19", "ALL",     "Light Review + Confidence Building", 19),
    ("2026-08-20", "ALL",     "Test Day Logistics + Gentle Review", 19),
    ("2026-08-21", "BB/CP",   "Final Light Review -- BB & CP Highlights", 19),
    ("2026-08-22", "PS/CARS", "Final Light Review -- PS & CARS Highlights", 19),
    # Aug 23 Sun -- FREE / breathing room (no event)
]
for d, sec, top, w in phase3:
    add(d, sec, top, w, 3)

# Weeks 20-22 (Aug 24 - Sep 13): Buffer & Review -- all FREE days, no events.

# === Generate ICS ===
phase_names = {1: "Content Review", 2: "Practice & Integration", 3: "AAMC Materials"}
lines = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//MCAT Study Coach//EN",
    "CALSCALE:GREGORIAN",
    "METHOD:PUBLISH",
    "X-WR-CALNAME:MCAT Study Schedule",
]

for dtstart, dtend, section, topic, week, phase in events:
    uid = str(uuid.uuid4())
    summary = f"MCAT [{section}]: {topic}"
    desc = f"Phase {phase}: {phase_names[phase]} | Week {week}"
    lines.extend([
        "BEGIN:VEVENT",
        f"UID:{uid}",
        f"DTSTART:{dtstart.strftime('%Y%m%dT%H%M%S')}",
        f"DTEND:{dtend.strftime('%Y%m%dT%H%M%S')}",
        f"SUMMARY:{summary}",
        f"DESCRIPTION:{desc}",
        "STATUS:CONFIRMED",
        "END:VEVENT",
    ])

lines.append("END:VCALENDAR")

# Write next to the script (works from any directory)
script_dir = os.path.dirname(os.path.abspath(__file__))
outpath = os.path.join(script_dir, "mcat_schedule.ics")
with open(outpath, "w", newline="\r\n") as f:
    f.write("\r\n".join(lines))

print(f"Generated {len(events)} calendar events -> {outpath}")

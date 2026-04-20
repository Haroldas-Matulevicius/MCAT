"""Generate MCAT study schedule ICS file.

Reflects the cascade applied 2026-04-19 (Day 4 delayed +1 day; third cascade in a row).
Apr 19 became REST/FLEX (no event); all topics from Apr 20 onward shifted +1 day.
End date pushed Sep 13 -> Sep 14 (Week 22 extended by 1 day to absorb cascade).
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
    # Week 1 (Apr 14-19) -- Apr 16, 17, 19 are REST/FLEX (no events)
    ("2026-04-14", "BB",   "Amino Acids -- All 20 Structures & Properties", 1),
    ("2026-04-15", "CP",   "Atomic Structure & Periodic Trends", 1),
    ("2026-04-18", "CP",   "Stoichiometry, Reactions & Ions (Gen Chem Ch 4)", 1),
    # Week 2 (Apr 20-26)
    ("2026-04-20", "PS",   "Biological Bases of Behavior & Neuroscience", 2),
    ("2026-04-21", "BB",   "Protein Structure & Folding (1-4)", 2),
    ("2026-04-22", "CP",   "Bonding & Intermolecular Forces", 2),
    ("2026-04-23", "CARS", "Foundations -- Main Idea & Passage Mapping", 2),
    ("2026-04-24", "BB",   "Enzyme Kinetics & Regulation", 2),
    ("2026-04-25", "CP",   "Solutions & Concentration (Gen Chem Ch 9)", 2),
    ("2026-04-26", "PS",   "Sensation, Perception & Attention", 2),
    # Week 3 (Apr 27-May 3)
    ("2026-04-27", "BB",   "Non-Enzymatic Protein Function & Lab Techniques", 3),
    ("2026-04-28", "CP",   "Thermodynamics & Thermochemistry", 3),
    ("2026-04-29", "CARS", "Author Tone & Rhetorical Strategy", 3),
    ("2026-04-30", "BB",   "DNA Structure, Replication & Repair", 3),
    ("2026-05-01", "CP",   "Chemical Kinetics", 3),
    ("2026-05-02", "PS",   "Learning -- Classical & Operant Conditioning", 3),
    ("2026-05-03", "BB",   "Transcription & RNA Processing", 3),
    # Week 4 (May 4-10)
    ("2026-05-04", "CP",   "Chemical Equilibrium", 4),
    ("2026-05-05", "CARS", "Evidence vs Opinion & Argument Structure", 4),
    ("2026-05-06", "BB",   "Translation & Gene Regulation", 4),
    ("2026-05-07", "CP",   "Acids, Bases & Buffers", 4),
    ("2026-05-08", "PS",   "Memory, Cognition & Language", 4),
    ("2026-05-09", "BB",   "Biotechnology & Molecular Techniques", 4),
    ("2026-05-10", "CP",   "Electrochemistry & Redox Reactions", 4),
    # Week 5 (May 11-17)
    ("2026-05-11", "CARS", "Inference & Implication Questions", 5),
    ("2026-05-12", "BB",   "Cell Structure, Organelles & Cytoskeleton", 5),
    ("2026-05-13", "CP",   "Organic Chemistry -- Functional Groups & Nomenclature", 5),
    ("2026-05-14", "PS",   "Consciousness, Sleep & Drugs", 5),
    ("2026-05-15", "BB",   "Membrane Structure & Transport", 5),
    ("2026-05-16", "CP",   "Stereochemistry & Isomers", 5),
    ("2026-05-17", "CARS", "Strengthen / Weaken Questions", 5),
    # Week 6 (May 18-24)
    ("2026-05-18", "BB",   "Cell Signaling & Signal Transduction", 6),
    ("2026-05-19", "CP",   "SN1/SN2/E1/E2 Reactions", 6),
    ("2026-05-20", "PS",   "Motivation, Emotion & Stress", 6),
    ("2026-05-21", "BB",   "Cell Cycle, Mitosis & Cancer Biology", 6),
    ("2026-05-22", "CP",   "Carbonyl Chemistry & Carboxylic Acid Derivatives", 6),
    ("2026-05-23", "CARS", "Reasoning Beyond the Text", 6),
    ("2026-05-24", "BB",   "Meiosis & Mendelian Genetics", 6),
    # Week 7 (May 25-31)
    ("2026-05-25", "CP",   "Spectroscopy -- IR, NMR & Mass Spec", 7),
    ("2026-05-26", "PS",   "Development, Identity & Personality", 7),
    ("2026-05-27", "BB",   "Non-Mendelian Genetics, Mutations & Evolution", 7),
    ("2026-05-28", "CP",   "Separations, Purification & Analytical Techniques", 7),
    ("2026-05-29", "CARS", "Full Section Practice #1 + Midpoint Review", 7),
    ("2026-05-30", "BB",   "Glycolysis & Fermentation", 7),
    ("2026-05-31", "CP",   "Kinematics & Newton's Laws", 7),
    # Week 8 (Jun 1-7)
    ("2026-06-01", "PS",   "Psychological Disorders & Treatment", 8),
    ("2026-06-02", "BB",   "Pyruvate Dehydrogenase & TCA Cycle", 8),
    ("2026-06-03", "CP",   "Work, Energy & Momentum", 8),
    ("2026-06-04", "CARS", "Pacing & Process of Elimination", 8),
    ("2026-06-05", "BB",   "Electron Transport Chain & Oxidative Phosphorylation", 8),
    ("2026-06-06", "CP",   "Fluids & Solids", 8),
    ("2026-06-07", "PS",   "Social Psychology -- Attitudes, Groups & Behavior", 8),
    # Week 9 (Jun 8-14)
    ("2026-06-08", "BB",   "Gluconeogenesis, Glycogen & Pentose Phosphate Pathway", 9),
    ("2026-06-09", "CP",   "Electrostatics & Magnetism", 9),
    ("2026-06-10", "CARS", "Humanities Passages Deep Dive", 9),
    ("2026-06-11", "BB",   "Lipid & Amino Acid Metabolism + Integration", 9),
    ("2026-06-12", "CP",   "Circuits & Electricity", 9),
    ("2026-06-13", "PS",   "Social Interaction, Attribution & Discrimination", 9),
    ("2026-06-14", "BB",   "Microbiology -- Bacteria, Viruses & Prions", 9),
    # Week 10 (Jun 15-21)
    ("2026-06-15", "CP",   "Waves, Sound & Doppler Effect", 10),
    ("2026-06-16", "CARS", "Social Sciences Passages Deep Dive", 10),
    ("2026-06-17", "BB",   "Immunology -- Innate & Adaptive Immunity", 10),
    ("2026-06-18", "CP",   "Light, Optics & Diffraction", 10),
    ("2026-06-19", "PS",   "Sociological Theories & Social Institutions", 10),
    ("2026-06-20", "BB",   "Cardiovascular System & Blood", 10),
    ("2026-06-21", "CP",   "Nuclear Chemistry & Radioactive Decay", 10),
    # Week 11 (Jun 22-28) -- Phase 1/2 transition
    ("2026-06-22", "CARS",    "Full Section Practice #2 + Comprehensive Review", 11),
    ("2026-06-23", "BB",      "Respiratory System & Gas Exchange", 11),
    ("2026-06-24", "CP",      "Math Skills, Units & Dimensional Analysis", 11),
    ("2026-06-25", "PS",      "Demographics, Stratification & Health Disparities", 11),
    ("2026-06-26", "BB",      "Digestive System & Nutrient Absorption", 11),
    ("2026-06-27", "CP",      "Research Design & Data Interpretation", 11),
    ("2026-06-28", "CARS",    "Timed Practice + Phase 1 Final Assessment", 11),
]
for d, sec, top, w in phase1:
    add(d, sec, top, w, 1)

# === Phase 2: Practice & Integration (Weeks 12-15) ===
phase2 = [
    # Week 12 (Jun 29-Jul 5)
    ("2026-06-29", "ALL",     "Third-Party FL #1 (Full-Length)", 12),
    ("2026-06-30", "CP/CARS", "FL #1 Review -- CP & CARS", 12),
    ("2026-07-01", "BB/PS",   "FL #1 Review -- BB & PS", 12),
    ("2026-07-02", "BB",      "BB Passage-Based Practice (59 Qs timed)", 12),
    ("2026-07-03", "CP",      "CP Passage-Based Practice (59 Qs timed)", 12),
    ("2026-07-04", "CARS/PS", "CARS Full Section + PS Practice", 12),
    ("2026-07-05", "VARIES",  "Weak Area Deep Dive #1 -- Highest Priority", 12),
    # Week 13 (Jul 6-12)
    ("2026-07-06", "VARIES",  "Weak Area Deep Dive #2", 13),
    ("2026-07-07", "CARS",    "CARS Intensive -- 6 Passages Timed", 13),
    ("2026-07-08", "ALL",     "Third-Party FL #2 (Full-Length)", 13),
    ("2026-07-09", "ALL",     "FL #2 Full Review", 13),
    ("2026-07-10", "ALL",     "Mixed Section Practice + Anki Marathon", 13),
    ("2026-07-11", "ALL",     "Third-Party FL #3 (Full-Length)", 13),
    ("2026-07-12", "ALL",     "FL #3 Full Review + Error Pattern Analysis", 13),
    # Week 14 (Jul 13-19)
    ("2026-07-13", "BB/CP",   "Data Interpretation & Experimental Design", 14),
    ("2026-07-14", "PS",      "PS Deep Dive -- Research Methods & Epidemiology", 14),
    ("2026-07-15", "CP",      "CP Calculation Drill + Physics Problem Workshop", 14),
    ("2026-07-16", "CARS",    "CARS Full Section + Weekly Review", 14),
    ("2026-07-17", "ALL",     "Third-Party FL #4 (Full-Length)", 14),
    ("2026-07-18", "ALL",     "FL #4 Full Review + Error Log Analysis", 14),
    ("2026-07-19", "BB",      "Biochemistry Integration Review", 14),
    # Week 15 (Jul 20-26) -- Phase 2/3 transition
    ("2026-07-20", "CP",      "Physics + Gen Chem Problem-Solving", 15),
    ("2026-07-21", "PS",      "PS Comprehensive Section Practice", 15),
    ("2026-07-22", "CARS",    "CARS Strategy Refinement + Phase 3 Planning", 15),
    ("2026-07-23", "ALL",     "Third-Party FL #5 (Full-Length)", 15),
    ("2026-07-24", "ALL",     "FL #5 Full Review + Score Trend Analysis", 15),
    ("2026-07-25", "BB/CP",   "Content Gap Remediation -- BB & CP", 15),
    ("2026-07-26", "PS/CARS", "Content Gap Remediation -- PS & CARS Maintenance", 15),
]
for d, sec, top, w in phase2:
    add(d, sec, top, w, 2)

# === Phase 3: AAMC Materials (Weeks 16-19) ===
phase3 = [
    # Week 16 (Jul 27-Aug 2)
    ("2026-07-27", "ALL",  "Mixed Timed Practice + Strategy Review", 16),
    ("2026-07-28", "ALL",  "Phase 2 Assessment + Phase 3 Planning", 16),
    ("2026-07-29", "BB",   "AAMC QPack -- Biology Vol 1", 16),
    ("2026-07-30", "CP",   "AAMC QPack -- Chemistry Vol 1", 16),
    ("2026-07-31", "CP",   "AAMC QPack -- Physics", 16),
    ("2026-08-01", "BB",   "AAMC QPack -- Biology Vol 2", 16),
    ("2026-08-02", "CP",   "AAMC QPack -- Chemistry Vol 2", 16),
    # Week 17 (Aug 3-9)
    ("2026-08-03", "CARS", "AAMC CARS QPack Vol 1", 17),
    ("2026-08-04", "CARS", "AAMC CARS QPack Vol 2", 17),
    ("2026-08-05", "BB",   "AAMC Section Bank -- BB", 17),
    ("2026-08-06", "CP",   "AAMC Section Bank -- CP", 17),
    ("2026-08-07", "PS",   "AAMC Section Bank -- PS", 17),
    ("2026-08-08", "ALL",  "Section Bank Full Review Day", 17),
    ("2026-08-09", "ALL",  "AAMC FL 1 (Full-Length)", 17),
    # Week 18 (Aug 10-16)
    ("2026-08-10", "ALL",     "AAMC FL 1 -- Full Review", 18),
    ("2026-08-11", "ALL",     "Targeted Weak Area Review", 18),
    ("2026-08-12", "ALL",     "AAMC FL 2 (Full-Length)", 18),
    ("2026-08-13", "ALL",     "AAMC FL 2 -- Full Review", 18),
    ("2026-08-14", "ALL",     "High-Yield Content Blitz + Leech Review", 18),
    ("2026-08-15", "CARS/PS", "CARS Maintenance + PS Final Vocabulary Drill", 18),
    ("2026-08-16", "ALL",     "AAMC FL 3 (Full-Length)", 18),
    # Week 19 (Aug 17-23) -- Final substantive prep week
    ("2026-08-17", "ALL",     "AAMC FL 3 -- Full Review", 19),
    ("2026-08-18", "ALL",     "AAMC FL 4 (Full-Length)", 19),
    ("2026-08-19", "ALL",     "AAMC FL 4 -- Full Review", 19),
    ("2026-08-20", "ALL",     "Light Review + Confidence Building", 19),
    ("2026-08-21", "ALL",     "Test Day Logistics + Gentle Review", 19),
    ("2026-08-22", "BB/CP",   "Final Light Review -- BB & CP Highlights", 19),
    ("2026-08-23", "PS/CARS", "Final Light Review -- PS & CARS Highlights", 19),
]
for d, sec, top, w in phase3:
    add(d, sec, top, w, 3)

# Weeks 20-22 (Aug 24 - Sep 14): Buffer & Review -- all FREE days, no events.
# Week 22 extended Sep 7-14 (was Sep 7-13) to absorb the third cascade.

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

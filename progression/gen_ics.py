"""Generate MCAT study schedule — ICS file + week_XX.md files.

Restructured 2026-04-21 per Option B:
- Sundays became dedicated Anki-only consolidation days.
- Content queue (125 topics from Apr 21 onward) cascades linearly:
  Mon-Sat = content, Sun = Anki. Apr 20 (Week 2 Day 1) already logged, preserved as-is.
- No content days lost — original 21 "free buffer" days (Aug 24 - Sep 13)
  redistributed as 21 weekly Anki days throughout Weeks 2-22.
- Last content day: Sat Sep 12. Final Anki: Sun Sep 13. Exam: mid-October.

Mon-Sun weekly structure. Times per CLAUDE.md weekly time blocks.

Outputs:
- mcat_schedule.ics (Google Calendar import)
- week_03.md through week_22.md (regenerated schedule tables + empty log sections)
- week_02.md is NOT touched here (has live session log; updated manually)
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
    6: ("07:00", "12:00"),  # Sun (Anki consolidation)
}

TIME_LABELS = {
    0: "7:00 AM – 12:00 PM",
    1: "1:00 PM – 6:00 PM",
    2: "4:00 PM – 9:00 PM",
    3: "1:00 PM – 6:00 PM",
    4: "12:30 PM – 5:30 PM",
    5: "7:00 AM – 12:00 PM",
    6: "7:00 AM – 12:00 PM",
}

DAY_LABELS = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri", 5: "Sat", 6: "Sun"}

events = []
schedule_by_week = {}  # week_num -> list of (date, section, topic, phase)


def add_event(d, section, topic, week, phase):
    start_time, end_time = TIMES[d.weekday()]
    sh, sm = map(int, start_time.split(":"))
    eh, em = map(int, end_time.split(":"))
    dtstart = datetime.datetime(d.year, d.month, d.day, sh, sm)
    dtend = datetime.datetime(d.year, d.month, d.day, eh, em)
    events.append((dtstart, dtend, section, topic, week, phase))
    schedule_by_week.setdefault(week, []).append((d, section, topic, phase))


def week_number(d):
    """Week 1 = Apr 14-19 (Tue-Sun, 6 days). Week N (N>=2) = Mon-Sun from Apr 20."""
    w1_start = datetime.date(2026, 4, 14)
    w2_start = datetime.date(2026, 4, 20)
    if d < w1_start:
        return 0
    if d < w2_start:
        return 1
    days_since_w2 = (d - w2_start).days
    return 2 + days_since_w2 // 7


# === Already-logged fixed events (preserve as-is) ===
add_event(datetime.date(2026, 4, 13), "ALL", "MCAT: Kickoff -- Amino Acid Foundations", 0, 1)
add_event(datetime.date(2026, 4, 14), "BB", "Amino Acids -- All 20 Structures & Properties", 1, 1)
add_event(datetime.date(2026, 4, 15), "CP", "Atomic Structure & Periodic Trends", 1, 1)
add_event(datetime.date(2026, 4, 18), "CP", "Stoichiometry, Reactions & Ions (Gen Chem Ch 4)", 1, 1)
add_event(datetime.date(2026, 4, 20), "PS", "Biological Bases of Behavior & Neuroscience", 2, 1)

# === Content queue from Apr 21 onward (125 topics) ===
# (section, topic, phase)
content_queue = [
    # Phase 1 (69 topics) — Content Review
    ("BB", "Protein Structure & Folding (1-4)", 1),
    ("CP", "Bonding & Intermolecular Forces", 1),
    ("CARS", "Foundations -- Main Idea & Passage Mapping", 1),
    ("BB", "Enzyme Kinetics & Regulation", 1),
    ("CP", "Solutions & Concentration (Gen Chem Ch 9)", 1),
    ("PS", "Sensation, Perception & Attention", 1),
    ("BB", "Non-Enzymatic Protein Function & Lab Techniques", 1),
    ("CP", "Thermodynamics & Thermochemistry", 1),
    ("CARS", "Author Tone & Rhetorical Strategy", 1),
    ("BB", "DNA Structure, Replication & Repair", 1),
    ("CP", "Chemical Kinetics", 1),
    ("PS", "Learning -- Classical & Operant Conditioning", 1),
    ("BB", "Transcription & RNA Processing", 1),
    ("CP", "Chemical Equilibrium", 1),
    ("CARS", "Evidence vs Opinion & Argument Structure", 1),
    ("BB", "Translation & Gene Regulation", 1),
    ("CP", "Acids, Bases & Buffers", 1),
    ("PS", "Memory, Cognition & Language", 1),
    ("BB", "Biotechnology & Molecular Techniques", 1),
    ("CP", "Electrochemistry & Redox Reactions", 1),
    ("CARS", "Inference & Implication Questions", 1),
    ("BB", "Cell Structure, Organelles & Cytoskeleton", 1),
    ("CP", "Organic Chemistry -- Functional Groups & Nomenclature", 1),
    ("PS", "Consciousness, Sleep & Drugs", 1),
    ("BB", "Membrane Structure & Transport", 1),
    ("CP", "Stereochemistry & Isomers", 1),
    ("CARS", "Strengthen / Weaken Questions", 1),
    ("BB", "Cell Signaling & Signal Transduction", 1),
    ("CP", "SN1/SN2/E1/E2 Reactions", 1),
    ("PS", "Motivation, Emotion & Stress", 1),
    ("BB", "Cell Cycle, Mitosis & Cancer Biology", 1),
    ("CP", "Carbonyl Chemistry & Carboxylic Acid Derivatives", 1),
    ("CARS", "Reasoning Beyond the Text", 1),
    ("BB", "Meiosis & Mendelian Genetics", 1),
    ("CP", "Spectroscopy -- IR, NMR & Mass Spec", 1),
    ("PS", "Development, Identity & Personality", 1),
    ("BB", "Non-Mendelian Genetics, Mutations & Evolution", 1),
    ("CP", "Separations, Purification & Analytical Techniques", 1),
    ("CARS", "Full Section Practice #1 + Midpoint Review", 1),
    ("BB", "Glycolysis & Fermentation", 1),
    ("CP", "Kinematics & Newton's Laws", 1),
    ("PS", "Psychological Disorders & Treatment", 1),
    ("BB", "Pyruvate Dehydrogenase & TCA Cycle", 1),
    ("CP", "Work, Energy & Momentum", 1),
    ("CARS", "Pacing & Process of Elimination", 1),
    ("BB", "Electron Transport Chain & Oxidative Phosphorylation", 1),
    ("CP", "Fluids & Solids", 1),
    ("PS", "Social Psychology -- Attitudes, Groups & Behavior", 1),
    ("BB", "Gluconeogenesis, Glycogen & Pentose Phosphate Pathway", 1),
    ("CP", "Electrostatics & Magnetism", 1),
    ("CARS", "Humanities Passages Deep Dive", 1),
    ("BB", "Lipid & Amino Acid Metabolism + Integration", 1),
    ("CP", "Circuits & Electricity", 1),
    ("PS", "Social Interaction, Attribution & Discrimination", 1),
    ("BB", "Microbiology -- Bacteria, Viruses & Prions", 1),
    ("CP", "Waves, Sound & Doppler Effect", 1),
    ("CARS", "Social Sciences Passages Deep Dive", 1),
    ("BB", "Immunology -- Innate & Adaptive Immunity", 1),
    ("CP", "Light, Optics & Diffraction", 1),
    ("PS", "Sociological Theories & Social Institutions", 1),
    ("BB", "Cardiovascular System & Blood", 1),
    ("CP", "Nuclear Chemistry & Radioactive Decay", 1),
    ("CARS", "Full Section Practice #2 + Comprehensive Review", 1),
    ("BB", "Respiratory System & Gas Exchange", 1),
    ("CP", "Math Skills, Units & Dimensional Analysis", 1),
    ("PS", "Demographics, Stratification & Health Disparities", 1),
    ("BB", "Digestive System & Nutrient Absorption", 1),
    ("CP", "Research Design & Data Interpretation", 1),
    ("CARS", "Timed Practice + Phase 1 Final Assessment", 1),
    # Phase 2 (28 topics) — Practice & Integration
    ("ALL", "Third-Party FL #1 (Full-Length)", 2),
    ("CP/CARS", "FL #1 Review -- CP & CARS", 2),
    ("BB/PS", "FL #1 Review -- BB & PS", 2),
    ("BB", "BB Passage-Based Practice (59 Qs timed)", 2),
    ("CP", "CP Passage-Based Practice (59 Qs timed)", 2),
    ("CARS/PS", "CARS Full Section + PS Practice", 2),
    ("VARIES", "Weak Area Deep Dive #1 -- Highest Priority", 2),
    ("VARIES", "Weak Area Deep Dive #2", 2),
    ("CARS", "CARS Intensive -- 6 Passages Timed", 2),
    ("ALL", "Third-Party FL #2 (Full-Length)", 2),
    ("ALL", "FL #2 Full Review", 2),
    ("ALL", "Mixed Section Practice + Anki Marathon", 2),
    ("ALL", "Third-Party FL #3 (Full-Length)", 2),
    ("ALL", "FL #3 Full Review + Error Pattern Analysis", 2),
    ("BB/CP", "Data Interpretation & Experimental Design", 2),
    ("PS", "PS Deep Dive -- Research Methods & Epidemiology", 2),
    ("CP", "CP Calculation Drill + Physics Problem Workshop", 2),
    ("CARS", "CARS Full Section + Weekly Review", 2),
    ("ALL", "Third-Party FL #4 (Full-Length)", 2),
    ("ALL", "FL #4 Full Review + Error Log Analysis", 2),
    ("BB", "Biochemistry Integration Review", 2),
    ("CP", "Physics + Gen Chem Problem-Solving", 2),
    ("PS", "PS Comprehensive Section Practice", 2),
    ("CARS", "CARS Strategy Refinement + Phase 3 Planning", 2),
    ("ALL", "Third-Party FL #5 (Full-Length)", 2),
    ("ALL", "FL #5 Full Review + Score Trend Analysis", 2),
    ("BB/CP", "Content Gap Remediation -- BB & CP", 2),
    ("PS/CARS", "Content Gap Remediation -- PS & CARS Maintenance", 2),
    # Phase 3 (28 topics) — AAMC Materials
    ("ALL", "Mixed Timed Practice + Strategy Review", 3),
    ("ALL", "Phase 2 Assessment + Phase 3 Planning", 3),
    ("BB", "AAMC QPack -- Biology Vol 1", 3),
    ("CP", "AAMC QPack -- Chemistry Vol 1", 3),
    ("CP", "AAMC QPack -- Physics", 3),
    ("BB", "AAMC QPack -- Biology Vol 2", 3),
    ("CP", "AAMC QPack -- Chemistry Vol 2", 3),
    ("CARS", "AAMC CARS QPack Vol 1", 3),
    ("CARS", "AAMC CARS QPack Vol 2", 3),
    ("BB", "AAMC Section Bank -- BB", 3),
    ("CP", "AAMC Section Bank -- CP", 3),
    ("PS", "AAMC Section Bank -- PS", 3),
    ("ALL", "Section Bank Full Review Day", 3),
    ("ALL", "AAMC FL 1 (Full-Length)", 3),
    ("ALL", "AAMC FL 1 -- Full Review", 3),
    ("ALL", "Targeted Weak Area Review", 3),
    ("ALL", "AAMC FL 2 (Full-Length)", 3),
    ("ALL", "AAMC FL 2 -- Full Review", 3),
    ("ALL", "High-Yield Content Blitz + Leech Review", 3),
    ("CARS/PS", "CARS Maintenance + PS Final Vocabulary Drill", 3),
    ("ALL", "AAMC FL 3 (Full-Length)", 3),
    ("ALL", "AAMC FL 3 -- Full Review", 3),
    ("ALL", "AAMC FL 4 (Full-Length)", 3),
    ("ALL", "AAMC FL 4 -- Full Review", 3),
    ("ALL", "Light Review + Confidence Building", 3),
    ("ALL", "Test Day Logistics + Gentle Review", 3),
    ("BB/CP", "Final Light Review -- BB & CP Highlights", 3),
    ("PS/CARS", "Final Light Review -- PS & CARS Highlights", 3),
]

assert len(content_queue) == 125, f"Queue length mismatch: {len(content_queue)}"

# === Walk day-by-day from Apr 21, assigning content (Mon-Sat) + Anki (Sun) ===
cursor = datetime.date(2026, 4, 21)
queue_idx = 0
ANKI_TOPIC = "Anki Consolidation -- backlog, weak-spot drilling, weekly review + mixed quiz"

while queue_idx < len(content_queue):
    if cursor.weekday() == 6:  # Sunday
        add_event(cursor, "ANKI", ANKI_TOPIC, week_number(cursor), 0)
    else:
        sec, topic, phase = content_queue[queue_idx]
        add_event(cursor, sec, topic, week_number(cursor), phase)
        queue_idx += 1
    cursor += datetime.timedelta(days=1)

# Trailing Sunday after last content day (Sat -> Sun)
if cursor.weekday() == 6:
    add_event(cursor, "ANKI", ANKI_TOPIC + " -- final pre-buffer", week_number(cursor), 0)

# === Write ICS file ===
phase_names = {0: "Anki Consolidation", 1: "Content Review",
               2: "Practice & Integration", 3: "AAMC Materials"}
ics_lines = [
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
    ics_lines.extend([
        "BEGIN:VEVENT",
        f"UID:{uid}",
        f"DTSTART:{dtstart.strftime('%Y%m%dT%H%M%S')}",
        f"DTEND:{dtend.strftime('%Y%m%dT%H%M%S')}",
        f"SUMMARY:{summary}",
        f"DESCRIPTION:{desc}",
        "STATUS:CONFIRMED",
        "END:VEVENT",
    ])
ics_lines.append("END:VCALENDAR")

script_dir = os.path.dirname(os.path.abspath(__file__))
ics_path = os.path.join(script_dir, "mcat_schedule.ics")
with open(ics_path, "w", newline="\r\n") as f:
    f.write("\r\n".join(ics_lines))

# === Generate week_03.md through week_22.md ===
# Phase label per week based on majority content days
def phase_label_for_week(wk):
    days = schedule_by_week.get(wk, [])
    phase_counts = {}
    for _, _, _, p in days:
        if p == 0:  # skip Anki
            continue
        phase_counts[p] = phase_counts.get(p, 0) + 1
    phases = sorted(phase_counts.keys())
    if len(phases) == 1:
        p = phases[0]
        return f"Phase {p}: {phase_names[p]}"
    elif len(phases) == 2:
        a, b = phases
        return f"Phase {a}/{b}: Transition ({phase_names[a]} → {phase_names[b]})"
    return "Mixed"


def format_date(d):
    return d.strftime("%b %d").replace(" 0", " ")  # "Apr 27" not "Apr 27"


def format_week_md(wk):
    days = schedule_by_week.get(wk, [])
    if not days:
        return None
    first = days[0][0]
    last = days[-1][0]
    phase_str = phase_label_for_week(wk)

    lines = []
    lines.append(f"# Week {wk} — {phase_str}")
    lines.append(f"**{format_date(first)} - {format_date(last)}, 2026**")
    lines.append("")
    lines.append("## Pre-flight")
    lines.append("- **Previous week:** [pending check]")
    lines.append("- **Carry-over:** --")
    lines.append("")
    lines.append("## Schedule")
    lines.append("")
    lines.append("| Date | Day | Time | Section | Topic | Logged |")
    lines.append("|------|-----|------|---------|-------|--------|")
    for d, sec, top, _ph in days:
        date_s = format_date(d)
        day_s = DAY_LABELS[d.weekday()]
        time_s = TIME_LABELS[d.weekday()]
        # Anki row: render slightly differently
        lines.append(f"| {date_s} | {day_s} | {time_s} | {sec} | {top} | [ ] |")
    lines.append("")
    lines.append("## Session Logs")
    lines.append("")
    lines.append("<!-- Paste session log entries below after each study day -->")
    lines.append("")
    lines.append("## Weekly Review (Sunday Anki Day)")
    lines.append("- [ ] All session logs complete")
    lines.append("- [ ] Confidence map updated")
    lines.append("- [ ] Section confidence tracker updated")
    lines.append("- [ ] Top 3 weak topics reviewed")
    lines.append("- [ ] Anki backlog cleared (or logged for next week)")
    return "\n".join(lines) + "\n"


weeks_written = []
for wk in sorted(schedule_by_week.keys()):
    if wk < 3:  # Week 0/1/2 not regenerated (1 = logged past; 2 = live session log preserved)
        continue
    md = format_week_md(wk)
    if md is None:
        continue
    out_path = os.path.join(script_dir, f"week_{wk:02d}.md")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(md)
    weeks_written.append(wk)

# === Report ===
print(f"Generated {len(events)} calendar events -> {ics_path}")
print(f"Content queue consumed: {queue_idx}/{len(content_queue)}")
anki_count = sum(1 for _, _, sec, _, _, _ in events if sec == "ANKI")
print(f"Anki consolidation days: {anki_count}")
print(f"Week files written: {weeks_written}")
print(f"First content day: Apr 21 (Week 2 Tue)")
print(f"Last content day: {events[-1][0].date().isoformat() if events[-1][2] != 'ANKI' else 'see above'}")
content_events = [e for e in events if e[2] != 'ANKI' and e[5] != 0]
last_content = max(content_events, key=lambda e: e[0])
last_anki = max([e for e in events if e[2] == 'ANKI'], key=lambda e: e[0])
print(f"Last content day: {last_content[0].date().isoformat()} — {last_content[2]}: {last_content[3]}")
print(f"Last Anki day:    {last_anki[0].date().isoformat()}")

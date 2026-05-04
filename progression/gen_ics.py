"""Generate MCAT study schedule ICS file.

Schedule rebuilt 2026-05-03 for Sep 11, 2026 exam.
- Single-book progression: Bio -> Biochem -> GChem -> OChem -> PhysicsMath -> Psych
- Mon-Sat: 8 AM - 3 PM (lunch 11 AM - 12 PM implicit, 6 hr work)
- Sun: 8 AM - 12 PM half-day (Anki / CARS / scheduled half-length)
- Phases: Content (W1-13) -> Practice (W13-15) -> AAMC (W16-17) -> Buffer (W18-19) -> EXAM Sep 11

Outputs:
- mcat_schedule.ics

Does NOT regenerate week_NN.md files — those are maintained directly per the new format.
UIDs are deterministic (date + section hash) so reimporting the ICS updates events
in place rather than creating duplicates (in calendar apps that respect UIDs).
"""
import datetime
import hashlib
import os


# Time blocks (start, end) in HH:MM
TIMES = {
    "STUDY":  ("08:00", "15:00"),  # Mon-Sat content day; lunch 11-12 implicit
    "SUNDAY": ("08:00", "12:00"),  # Sunday half-day
    "FL":     ("08:00", "16:00"),  # Full-length practice exam (~7.5 hrs incl. breaks)
    "EXAM":   ("07:30", "17:00"),  # Real MCAT exam day
    # OFF and REST events are written as all-day with empty time, see ICS section
}

DAY_LABELS = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri", 5: "Sat", 6: "Sun"}


def D(month, day):
    return datetime.date(2026, month, day)


# Phase boundaries
def phase_for(d):
    if d <= D(7, 28):
        return 1
    if d <= D(8, 16):
        return 2
    if d <= D(8, 30):
        return 3
    return 4


PHASE_NAMES = {
    1: "Content Review",
    2: "Practice & Integration",
    3: "AAMC Materials",
    4: "Buffer + Final FLs",
}


# Week 1 starts May 4 (Mon). Week N = (date - May 4) // 7 + 1.
WEEK1_START = D(5, 4)
def week_for(d):
    return (d - WEEK1_START).days // 7 + 1


# === SCHEDULE ===
# (date, kind, section, topic)
# kind: STUDY | SUNDAY | FL | EXAM | OFF | REST
SCHEDULE = [
    # ---------- Week 1 (May 4-10): Bio Ch01-04, 2 OFF, Sun Anki ----------
    (D(5, 4),  "STUDY",  "BB",   "Bio Ch01 -- The Cell"),
    (D(5, 5),  "STUDY",  "BB",   "Bio Ch02 -- Reproduction"),
    (D(5, 6),  "OFF",    "--",   "OFF (planned)"),
    (D(5, 7),  "STUDY",  "BB",   "Bio Ch03 -- Embryogenesis"),
    (D(5, 8),  "STUDY",  "BB",   "Bio Ch04 -- Nervous System"),
    (D(5, 9),  "OFF",    "--",   "OFF (planned)"),
    (D(5, 10), "SUNDAY", "ANKI", "Anki backlog + CARS + week review"),

    # ---------- Week 2 (May 11-17): Bio Ch05-10 ----------
    (D(5, 11), "STUDY",  "BB",   "Bio Ch05 -- Endocrine"),
    (D(5, 12), "STUDY",  "BB",   "Bio Ch06 -- Respiratory"),
    (D(5, 13), "STUDY",  "BB",   "Bio Ch07 -- Cardiovascular"),
    (D(5, 14), "STUDY",  "BB",   "Bio Ch08 -- Immune"),
    (D(5, 15), "STUDY",  "BB",   "Bio Ch09 -- Digestive"),
    (D(5, 16), "STUDY",  "BB",   "Bio Ch10 -- Homeostasis"),
    (D(5, 17), "SUNDAY", "ANKI", "Anki backlog + CARS + week review"),

    # ---------- Week 3 (May 18-24): Bio Ch11-12 -> Biochem Ch01-04 + Sun BB FL #1 ----------
    (D(5, 18), "STUDY",  "BB",   "Bio Ch11 -- Musculoskeletal"),
    (D(5, 19), "STUDY",  "BB",   "Bio Ch12 -- Genetics & Evolution (BIO COMPLETE)"),
    (D(5, 20), "STUDY",  "BB",   "Biochem Ch01 -- Amino Acids & Proteins"),
    (D(5, 21), "STUDY",  "BB",   "Biochem Ch02 -- Enzymes"),
    (D(5, 22), "STUDY",  "BB",   "Biochem Ch03 -- Non-Enzymatic Protein Function"),
    (D(5, 23), "STUDY",  "BB",   "Biochem Ch04 -- Carbohydrates"),
    (D(5, 24), "SUNDAY", "BB",   "Half-length #1 (Biology focus, ~60 Qs)"),

    # ---------- Week 4 (May 25-31): Biochem Ch05-10 ----------
    (D(5, 25), "STUDY",  "BB",   "Biochem Ch05 -- Lipids"),
    (D(5, 26), "STUDY",  "BB",   "Biochem Ch06 -- DNA & Biotechnology"),
    (D(5, 27), "STUDY",  "BB",   "Biochem Ch07 -- RNA & the Genetic Code"),
    (D(5, 28), "STUDY",  "BB",   "Biochem Ch08 -- Membranes"),
    (D(5, 29), "STUDY",  "BB",   "Biochem Ch09 -- Carb Metabolism I"),
    (D(5, 30), "STUDY",  "BB",   "Biochem Ch10 -- Carb Metabolism II"),
    (D(5, 31), "SUNDAY", "ANKI", "Anki backlog + CARS + week review"),

    # ---------- Week 5 (Jun 1-7): Biochem Ch11-12 -> GChem Ch01-04 + Sun BB FL #2 ----------
    (D(6, 1),  "STUDY",  "BB",   "Biochem Ch11 -- Lipid & AA Metabolism"),
    (D(6, 2),  "STUDY",  "BB",   "Biochem Ch12 -- Bioenergetics & Regulation (BIOCHEM COMPLETE)"),
    (D(6, 3),  "STUDY",  "CP",   "GenChem Ch01 -- Atomic Structure"),
    (D(6, 4),  "STUDY",  "CP",   "GenChem Ch02 -- Periodic Table"),
    (D(6, 5),  "STUDY",  "CP",   "GenChem Ch03 -- Bonding"),
    (D(6, 6),  "STUDY",  "CP",   "GenChem Ch04 -- Compounds & Stoichiometry"),
    (D(6, 7),  "SUNDAY", "BB",   "Half-length #2 (Biochemistry focus, ~60 Qs)"),

    # ---------- Week 6 (Jun 8-14): GChem Ch05-10 ----------
    (D(6, 8),  "STUDY",  "CP",   "GenChem Ch05 -- Kinetics"),
    (D(6, 9),  "STUDY",  "CP",   "GenChem Ch06 -- Equilibrium"),
    (D(6, 10), "STUDY",  "CP",   "GenChem Ch07 -- Thermochemistry"),
    (D(6, 11), "STUDY",  "CP",   "GenChem Ch08 -- Gas Phase"),
    (D(6, 12), "STUDY",  "CP",   "GenChem Ch09 -- Solutions"),
    (D(6, 13), "STUDY",  "CP",   "GenChem Ch10 -- Acids & Bases"),
    (D(6, 14), "SUNDAY", "ANKI", "Anki backlog + CARS + week review"),

    # ---------- Week 7 (Jun 15-21): GChem Ch11-12 -> OChem Ch01-04 + Sun CP FL #1 ----------
    (D(6, 15), "STUDY",  "CP",   "GenChem Ch11 -- Redox"),
    (D(6, 16), "STUDY",  "CP",   "GenChem Ch12 -- Electrochemistry (GCHEM COMPLETE)"),
    (D(6, 17), "STUDY",  "CP",   "OrgChem Ch01 -- Nomenclature"),
    (D(6, 18), "STUDY",  "CP",   "OrgChem Ch02 -- Isomers"),
    (D(6, 19), "STUDY",  "CP",   "OrgChem Ch03 -- Bonding"),
    (D(6, 20), "STUDY",  "CP",   "OrgChem Ch04 -- Analyzing Reactions"),
    (D(6, 21), "SUNDAY", "CP",   "Half-length #3 (GenChem focus, ~60 Qs)"),

    # ---------- Week 8 (Jun 22-28): OChem Ch05-10 ----------
    (D(6, 22), "STUDY",  "CP",   "OrgChem Ch05 -- Alcohols"),
    (D(6, 23), "STUDY",  "CP",   "OrgChem Ch06 -- Aldehydes & Ketones I"),
    (D(6, 24), "STUDY",  "CP",   "OrgChem Ch07 -- Aldehydes & Ketones II (Enolates)"),
    (D(6, 25), "STUDY",  "CP",   "OrgChem Ch08 -- Carboxylic Acids"),
    (D(6, 26), "STUDY",  "CP",   "OrgChem Ch09 -- Carboxylic Acid Derivatives"),
    (D(6, 27), "STUDY",  "CP",   "OrgChem Ch10 -- Nitrogen & Phosphorus Compounds"),
    (D(6, 28), "SUNDAY", "ANKI", "Anki backlog + CARS + week review"),

    # ---------- Week 9 (Jun 29-Jul 5): OChem Ch11-12 -> PhysicsMath Ch01-04 + Sun CP FL #2 ----------
    (D(6, 29), "STUDY",  "CP",   "OrgChem Ch11 -- Spectroscopy (NMR/IR/UV-Vis/MS)"),
    (D(6, 30), "STUDY",  "CP",   "OrgChem Ch12 -- Separations & Purifications (OCHEM COMPLETE)"),
    (D(7, 1),  "STUDY",  "CP",   "PhysicsMath Ch01 -- Kinematics & Dynamics"),
    (D(7, 2),  "STUDY",  "CP",   "PhysicsMath Ch02 -- Work & Energy"),
    (D(7, 3),  "STUDY",  "CP",   "PhysicsMath Ch03 -- Thermodynamics (CONTENT GAP - expand)"),
    (D(7, 4),  "STUDY",  "CP",   "PhysicsMath Ch04 -- Fluids (US Independence Day - cascade if off)"),
    (D(7, 5),  "SUNDAY", "CP",   "Half-length #4 (OrgChem focus, ~60 Qs)"),

    # ---------- Week 10 (Jul 6-12): PhysicsMath Ch05-10 ----------
    (D(7, 6),  "STUDY",  "CP",   "PhysicsMath Ch05 -- Electrostatics & Magnetism"),
    (D(7, 7),  "STUDY",  "CP",   "PhysicsMath Ch06 -- Circuits"),
    (D(7, 8),  "STUDY",  "CP",   "PhysicsMath Ch07 -- Waves & Sound"),
    (D(7, 9),  "STUDY",  "CP",   "PhysicsMath Ch08 -- Light & Optics"),
    (D(7, 10), "STUDY",  "CP",   "PhysicsMath Ch09 -- Atomic & Nuclear"),
    (D(7, 11), "STUDY",  "CP",   "PhysicsMath Ch10 -- Mathematics"),
    (D(7, 12), "SUNDAY", "ANKI", "Anki backlog + CARS + week review"),

    # ---------- Week 11 (Jul 13-19): PhysicsMath Ch11-12 -> Psych Ch01-04 + Sun CP FL #3 ----------
    (D(7, 13), "STUDY",  "CP",   "PhysicsMath Ch11 -- Research Design"),
    (D(7, 14), "STUDY",  "CP",   "PhysicsMath Ch12 -- Statistics (PHYSICS COMPLETE)"),
    (D(7, 15), "STUDY",  "PS",   "Psychology Ch01 -- Biology of Behavior"),
    (D(7, 16), "STUDY",  "PS",   "Psychology Ch02 -- Sensation & Perception"),
    (D(7, 17), "STUDY",  "PS",   "Psychology Ch03 -- Learning & Memory"),
    (D(7, 18), "STUDY",  "PS",   "Psychology Ch04 -- Cognition & Consciousness"),
    (D(7, 19), "SUNDAY", "CP",   "Half-length #5 (PhysicsMath focus, ~60 Qs)"),

    # ---------- Week 12 (Jul 20-26): Psych Ch05-10 + ORDER UWORLD by Jul 25 ----------
    (D(7, 20), "STUDY",  "PS",   "Psychology Ch05 -- Motivation, Emotion & Stress"),
    (D(7, 21), "STUDY",  "PS",   "Psychology Ch06 -- Identity & Personality"),
    (D(7, 22), "STUDY",  "PS",   "Psychology Ch07 -- Psychological Disorders"),
    (D(7, 23), "STUDY",  "PS",   "Psychology Ch08 -- Social Processes"),
    (D(7, 24), "STUDY",  "PS",   "Psychology Ch09 -- Social Interaction"),
    (D(7, 25), "STUDY",  "PS",   "Psychology Ch10 -- Social Thinking [BUY UWORLD TODAY]"),
    (D(7, 26), "SUNDAY", "ANKI", "Anki backlog + CARS + week review"),

    # ---------- Week 13 (Jul 27-Aug 2): Psych Ch11-12 -> PHASE 2 starts Wed + Sun PS FL #6 ----------
    (D(7, 27), "STUDY",  "PS",   "Psychology Ch11 -- Social Structure & Demographics"),
    (D(7, 28), "STUDY",  "PS",   "Psychology Ch12 -- Social Stratification (PHASE 1 COMPLETE)"),
    (D(7, 29), "STUDY",  "UW",   "Phase 2 Day 1 -- UWorld diagnostic block (40 Qs mixed)"),
    (D(7, 30), "STUDY",  "UW",   "UWorld -- top weak topic from Wed (40 Qs targeted)"),
    (D(7, 31), "STUDY",  "UW",   "UWorld -- second weak topic (40 Qs) + CARS (3 passages)"),
    (D(8, 1),  "STUDY",  "UW",   "UWorld -- mixed timed block (60 Qs all sections)"),
    (D(8, 2),  "SUNDAY", "PS",   "Half-length #6 (Psychology focus, ~60 Qs)"),

    # ---------- Week 14 (Aug 3-9): UWorld grind + 3rd-party FL #1 (Sat) ----------
    (D(8, 3),  "STUDY",  "UW",   "UWorld weak-topic deep dive #1 (BB, ~50 Qs untimed)"),
    (D(8, 4),  "STUDY",  "UW",   "UWorld weak-topic deep dive #2 (CP, ~50 Qs untimed)"),
    (D(8, 5),  "STUDY",  "UW",   "UWorld CARS focus (5 passages timed) + content re-read"),
    (D(8, 6),  "STUDY",  "UW",   "UWorld mixed timed block (60 Qs) + research re-read"),
    (D(8, 7),  "STUDY",  "UW",   "UWorld + JackSparrow Anki cleanup"),
    (D(8, 8),  "FL",     "ALL",  "3rd-Party Full-Length #1 (Blueprint free)"),
    (D(8, 9),  "SUNDAY", "ALL",  "FL #1 deep review + weekly review"),

    # ---------- Week 15 (Aug 10-16): UWorld + 3rd-party FL #2 (Thu) + BUY AAMC by Fri ----------
    (D(8, 10), "STUDY",  "UW",   "UWorld -- weak topics from FL #1 (priority order)"),
    (D(8, 11), "STUDY",  "UW",   "UWorld -- weak topics + targeted research re-read"),
    (D(8, 12), "STUDY",  "UW",   "UWorld -- CARS (5 passages) + mixed block (40 Qs)"),
    (D(8, 13), "FL",     "ALL",  "3rd-Party Full-Length #2"),
    (D(8, 14), "STUDY",  "ALL",  "FL #2 deep review [BUY AAMC ONLINE PREP BUNDLE TODAY]"),
    (D(8, 15), "STUDY",  "AAMC", "AAMC familiarization -- explore Section Bank + QPack interface"),
    (D(8, 16), "SUNDAY", "ANKI", "Phase 2 retrospective + Phase 3 prep"),

    # ---------- Week 16 (Aug 17-23): AAMC Section Banks ----------
    (D(8, 17), "STUDY",  "AAMC", "AAMC BB Section Bank -- first half (~140 Qs timed)"),
    (D(8, 18), "STUDY",  "AAMC", "AAMC BB Section Bank -- second half + deep review"),
    (D(8, 19), "STUDY",  "AAMC", "AAMC CP Section Bank -- first half (~140 Qs timed)"),
    (D(8, 20), "STUDY",  "AAMC", "AAMC CP Section Bank -- second half + deep review"),
    (D(8, 21), "STUDY",  "AAMC", "AAMC CARS Section Bank (~140 Qs timed) + review"),
    (D(8, 22), "STUDY",  "AAMC", "AAMC PS Section Bank -- first half (~140 Qs timed)"),
    (D(8, 23), "SUNDAY", "AAMC", "Finish PS Section Bank + weekly review"),

    # ---------- Week 17 (Aug 24-30): AAMC QPacks + AAMC FL #1 (Wed) + AAMC FL #2 (Fri) ----------
    (D(8, 24), "STUDY",  "AAMC", "AAMC QPack -- Biology Vol 1 + 2 (~120 Qs)"),
    (D(8, 25), "STUDY",  "AAMC", "AAMC QPack -- Chemistry Vol 1 + 2 (~120 Qs)"),
    (D(8, 26), "FL",     "AAMC", "AAMC Full-Length #1 (full simulation)"),
    (D(8, 27), "STUDY",  "AAMC", "AAMC FL #1 deep review (every wrong + every guessed)"),
    (D(8, 28), "FL",     "AAMC", "AAMC Full-Length #2 (full simulation)"),
    (D(8, 29), "STUDY",  "AAMC", "AAMC FL #2 deep review"),
    (D(8, 30), "SUNDAY", "AAMC", "AAMC QPack remaining (Physics + Psych) + Anki"),

    # ---------- Week 18 (Aug 31-Sep 6): AAMC FL #3 (Mon) + AAMC FL #4 (Thu) ----------
    (D(8, 31), "FL",     "AAMC", "AAMC Full-Length #3 (full simulation)"),
    (D(9, 1),  "STUDY",  "AAMC", "AAMC FL #3 deep review (CONTENT TARGET DATE)"),
    (D(9, 2),  "STUDY",  "AAMC", "Weak-topic remediation: top 3 from FL #1-3"),
    (D(9, 3),  "FL",     "AAMC", "AAMC Full-Length #4 (full simulation)"),
    (D(9, 4),  "STUDY",  "AAMC", "AAMC FL #4 deep review"),
    (D(9, 5),  "STUDY",  "ALL",  "Light Anki + weak-topic drill (no FLs)"),
    (D(9, 6),  "SUNDAY", "ALL",  "Anki + CARS + final weak-topic pass"),

    # ---------- Week 19 (Sep 7-11): AAMC Sample (Wed) -> REST -> EXAM ----------
    (D(9, 7),  "STUDY",  "ALL",  "Light Anki + targeted weak-topic review (Content outlines only)"),
    (D(9, 8),  "SUNDAY", "ALL",  "Half-day -- Light Anki + 2 CARS passages + AAMC QPack picks"),
    (D(9, 9),  "FL",     "AAMC", "AAMC Sample FL (free) -- final dress rehearsal"),
    (D(9, 10), "REST",   "--",   "REST DAY -- pack test bag, light Anki, sleep early"),
    (D(9, 11), "EXAM",   "ALL",  "MCAT EXAM"),
]


# === Generate ICS ===
def make_uid(d, section, kind):
    """Deterministic UID so reimport updates events instead of duplicating."""
    h = hashlib.md5(f"{d.isoformat()}-{section}-{kind}".encode()).hexdigest()[:12]
    return f"mcat-{d.strftime('%Y%m%d')}-{h}@mcat-coach"


ics_lines = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//MCAT Study Coach//EN",
    "CALSCALE:GREGORIAN",
    "METHOD:PUBLISH",
    "X-WR-CALNAME:MCAT Study Schedule (rebuilt 2026-05-03)",
]

written = 0
all_day = 0
timed = 0

for d, kind, section, topic in SCHEDULE:
    week = week_for(d)
    phase = phase_for(d)
    uid = make_uid(d, section, kind)
    summary = f"MCAT [{section}]: {topic}" if section != "--" else f"MCAT: {topic}"
    desc = f"Phase {phase}: {PHASE_NAMES[phase]} | Week {week} | {DAY_LABELS[d.weekday()]}"

    if kind in ("OFF", "REST"):
        # All-day event
        next_day = d + datetime.timedelta(days=1)
        ics_lines.extend([
            "BEGIN:VEVENT",
            f"UID:{uid}",
            f"DTSTART;VALUE=DATE:{d.strftime('%Y%m%d')}",
            f"DTEND;VALUE=DATE:{next_day.strftime('%Y%m%d')}",
            f"SUMMARY:{summary}",
            f"DESCRIPTION:{desc}",
            "STATUS:CONFIRMED",
            "TRANSP:TRANSPARENT",
            "END:VEVENT",
        ])
        all_day += 1
    else:
        start_str, end_str = TIMES[kind]
        sh, sm = map(int, start_str.split(":"))
        eh, em = map(int, end_str.split(":"))
        dtstart = datetime.datetime(d.year, d.month, d.day, sh, sm)
        dtend = datetime.datetime(d.year, d.month, d.day, eh, em)
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
        timed += 1
    written += 1

ics_lines.append("END:VCALENDAR")

# Write ICS file
script_dir = os.path.dirname(os.path.abspath(__file__))
ics_path = os.path.join(script_dir, "mcat_schedule.ics")
with open(ics_path, "w", newline="\r\n") as f:
    f.write("\r\n".join(ics_lines))

# === Report ===
study = sum(1 for _, k, _, _ in SCHEDULE if k == "STUDY")
sundays = sum(1 for _, k, _, _ in SCHEDULE if k == "SUNDAY")
fls = sum(1 for _, k, _, _ in SCHEDULE if k == "FL")
offs = sum(1 for _, k, _, _ in SCHEDULE if k == "OFF")
rests = sum(1 for _, k, _, _ in SCHEDULE if k == "REST")
exams = sum(1 for _, k, _, _ in SCHEDULE if k == "EXAM")

print(f"Wrote {ics_path}")
print(f"Total events: {written} ({timed} timed + {all_day} all-day)")
print(f"  STUDY (Mon-Sat 8a-3p):    {study}")
print(f"  SUNDAY (half-day 8a-12p): {sundays}")
print(f"  FL (full-length 8a-4p):   {fls}")
print(f"  OFF (planned off):        {offs}")
print(f"  REST (pre-exam rest):     {rests}")
print(f"  EXAM:                     {exams}")
print(f"First day: {SCHEDULE[0][0]} ({DAY_LABELS[SCHEDULE[0][0].weekday()]})")
print(f"Last day:  {SCHEDULE[-1][0]} ({DAY_LABELS[SCHEDULE[-1][0].weekday()]}) -- exam")

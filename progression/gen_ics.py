"""Generate MCAT study schedule ICS file."""
import datetime
import uuid

events = []

def add(date_str, start_time, end_time, section, topic, week, phase):
    d = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    sh, sm = map(int, start_time.split(":"))
    eh, em = map(int, end_time.split(":"))
    dtstart = d.replace(hour=sh, minute=sm)
    dtend = d.replace(hour=eh, minute=em)
    events.append((dtstart, dtend, section, topic, week, phase))

# Kickoff
add("2026-04-12", "11:30", "15:30", "ALL", "MCAT: Kickoff -- Amino Acid Foundations", 0, 1)

# Phase 1: Content Review (Weeks 1-12)
sessions = [
    # Week 1
    ("2026-04-13","07:00","12:00","BB","Amino Acids -- All 20 Structures & Properties",1),
    ("2026-04-14","13:00","18:00","CP","Atomic Structure & Periodic Trends",1),
    ("2026-04-15","16:00","21:00","PS","Biological Bases of Behavior & Neuroscience",1),
    ("2026-04-16","13:00","18:00","BB","Protein Structure & Folding (1-4)",1),
    ("2026-04-17","12:30","17:30","CP","Bonding & Intermolecular Forces",1),
    ("2026-04-18","07:00","12:00","CARS","Foundations -- Main Idea & Passage Mapping",1),
    # Week 2
    ("2026-04-20","07:00","12:00","BB","Enzyme Kinetics & Regulation",2),
    ("2026-04-21","13:00","18:00","CP","Stoichiometry, Solutions & Concentration",2),
    ("2026-04-22","16:00","21:00","PS","Sensation, Perception & Attention",2),
    ("2026-04-23","13:00","18:00","BB","Non-Enzymatic Protein Function & Lab Techniques",2),
    ("2026-04-24","12:30","17:30","CP","Thermodynamics & Thermochemistry",2),
    ("2026-04-25","07:00","12:00","CARS","Author Tone & Rhetorical Strategy",2),
    # Week 3
    ("2026-04-27","07:00","12:00","BB","DNA Structure, Replication & Repair",3),
    ("2026-04-28","13:00","18:00","CP","Chemical Kinetics",3),
    ("2026-04-29","16:00","21:00","PS","Learning -- Classical & Operant Conditioning",3),
    ("2026-04-30","13:00","18:00","BB","Transcription & RNA Processing",3),
    ("2026-05-01","12:30","17:30","CP","Chemical Equilibrium",3),
    ("2026-05-02","07:00","12:00","CARS","Evidence vs Opinion & Argument Structure",3),
    # Week 4
    ("2026-05-04","07:00","12:00","BB","Translation & Gene Regulation",4),
    ("2026-05-05","13:00","18:00","CP","Acids, Bases & Buffers",4),
    ("2026-05-06","16:00","21:00","PS","Memory, Cognition & Language",4),
    ("2026-05-07","13:00","18:00","BB","Biotechnology & Molecular Techniques",4),
    ("2026-05-08","12:30","17:30","CP","Electrochemistry & Redox Reactions",4),
    ("2026-05-09","07:00","12:00","CARS","Inference & Implication Questions",4),
    # Week 5
    ("2026-05-11","07:00","12:00","BB","Cell Structure, Organelles & Cytoskeleton",5),
    ("2026-05-12","13:00","18:00","CP","Organic Chemistry -- Functional Groups & Nomenclature",5),
    ("2026-05-13","16:00","21:00","PS","Consciousness, Sleep & Drugs",5),
    ("2026-05-14","13:00","18:00","BB","Membrane Structure & Transport",5),
    ("2026-05-15","12:30","17:30","CP","Stereochemistry & Isomers",5),
    ("2026-05-16","07:00","12:00","CARS","Strengthen / Weaken Questions",5),
    # Week 6
    ("2026-05-18","07:00","12:00","BB","Cell Signaling & Signal Transduction",6),
    ("2026-05-19","13:00","18:00","CP","SN1/SN2/E1/E2 Reactions",6),
    ("2026-05-20","16:00","21:00","PS","Motivation, Emotion & Stress",6),
    ("2026-05-21","13:00","18:00","BB","Cell Cycle, Mitosis & Cancer Biology",6),
    ("2026-05-22","12:30","17:30","CP","Carbonyl Chemistry & Carboxylic Acid Derivatives",6),
    ("2026-05-23","07:00","12:00","CARS","Reasoning Beyond the Text",6),
    # Week 7
    ("2026-05-25","07:00","12:00","BB","Meiosis & Mendelian Genetics",7),
    ("2026-05-26","13:00","18:00","CP","Spectroscopy -- IR, NMR & Mass Spec",7),
    ("2026-05-27","16:00","21:00","PS","Development, Identity & Personality",7),
    ("2026-05-28","13:00","18:00","BB","Non-Mendelian Genetics, Mutations & Evolution",7),
    ("2026-05-29","12:30","17:30","CP","Separations, Purification & Analytical Techniques",7),
    ("2026-05-30","07:00","12:00","CARS","Full Section Practice #1 + Midpoint Review",7),
    # Week 8
    ("2026-06-01","07:00","12:00","BB","Glycolysis & Fermentation",8),
    ("2026-06-02","13:00","18:00","CP","Kinematics & Newton's Laws",8),
    ("2026-06-03","16:00","21:00","PS","Psychological Disorders & Treatment",8),
    ("2026-06-04","13:00","18:00","BB","Pyruvate Dehydrogenase & TCA Cycle",8),
    ("2026-06-05","12:30","17:30","CP","Work, Energy & Momentum",8),
    ("2026-06-06","07:00","12:00","CARS","Pacing & Process of Elimination",8),
    # Week 9
    ("2026-06-08","07:00","12:00","BB","Electron Transport Chain & Oxidative Phosphorylation",9),
    ("2026-06-09","13:00","18:00","CP","Fluids & Solids",9),
    ("2026-06-10","16:00","21:00","PS","Social Psychology -- Attitudes, Groups & Behavior",9),
    ("2026-06-11","13:00","18:00","BB","Gluconeogenesis, Glycogen & Pentose Phosphate Pathway",9),
    ("2026-06-12","12:30","17:30","CP","Electrostatics & Magnetism",9),
    ("2026-06-13","07:00","12:00","CARS","Humanities Passages Deep Dive",9),
    # Week 10
    ("2026-06-15","07:00","12:00","BB","Lipid & Amino Acid Metabolism + Integration",10),
    ("2026-06-16","13:00","18:00","CP","Circuits & Electricity",10),
    ("2026-06-17","16:00","21:00","PS","Social Interaction, Attribution & Discrimination",10),
    ("2026-06-18","13:00","18:00","BB","Microbiology -- Bacteria, Viruses & Prions",10),
    ("2026-06-19","12:30","17:30","CP","Waves, Sound & Doppler Effect",10),
    ("2026-06-20","07:00","12:00","CARS","Social Sciences Passages Deep Dive",10),
    # Week 11
    ("2026-06-22","07:00","12:00","BB","Immunology -- Innate & Adaptive Immunity",11),
    ("2026-06-23","13:00","18:00","CP","Light, Optics & Diffraction",11),
    ("2026-06-24","16:00","21:00","PS","Sociological Theories & Social Institutions",11),
    ("2026-06-25","13:00","18:00","BB","Cardiovascular System & Blood",11),
    ("2026-06-26","12:30","17:30","CP","Nuclear Chemistry & Radioactive Decay",11),
    ("2026-06-27","07:00","12:00","CARS","Full Section Practice #2 + Comprehensive Review",11),
    # Week 12
    ("2026-06-29","07:00","12:00","BB","Respiratory System & Gas Exchange",12),
    ("2026-06-30","13:00","18:00","CP","Math Skills, Units & Dimensional Analysis",12),
    ("2026-07-01","16:00","21:00","PS","Demographics, Stratification & Health Disparities",12),
    ("2026-07-02","13:00","18:00","BB","Digestive System & Nutrient Absorption",12),
    ("2026-07-03","12:30","17:30","CP","Research Design & Data Interpretation",12),
    ("2026-07-04","07:00","12:00","CARS","Timed Practice + Phase 1 Final Assessment",12),
]

for d, st, et, sec, top, w in sessions:
    add(d, st, et, sec, top, w, 1)

# Phase 2: Practice & Integration (Weeks 13-17)
sessions2 = [
    ("2026-07-06","07:00","12:00","ALL","Third-Party FL #1 (Full-Length)",13),
    ("2026-07-07","13:00","18:00","CP/CARS","FL #1 Review -- CP & CARS",13),
    ("2026-07-08","16:00","21:00","BB/PS","FL #1 Review -- BB & PS",13),
    ("2026-07-09","13:00","18:00","BB","BB Passage-Based Practice (59 Qs timed)",13),
    ("2026-07-10","12:30","17:30","CP","CP Passage-Based Practice (59 Qs timed)",13),
    ("2026-07-11","07:00","12:00","CARS/PS","CARS Full Section + PS Practice",13),
    ("2026-07-13","07:00","12:00","VARIES","Weak Area Deep Dive #1 -- Highest Priority",14),
    ("2026-07-14","13:00","18:00","VARIES","Weak Area Deep Dive #2",14),
    ("2026-07-15","16:00","21:00","CARS","CARS Intensive -- 6 Passages Timed",14),
    ("2026-07-16","13:00","18:00","ALL","Third-Party FL #2 (Full-Length)",14),
    ("2026-07-17","12:30","17:30","ALL","FL #2 Full Review",14),
    ("2026-07-18","07:00","12:00","ALL","Mixed Section Practice + Anki Marathon",14),
    ("2026-07-20","07:00","12:00","ALL","Third-Party FL #3 (Full-Length)",15),
    ("2026-07-21","13:00","18:00","ALL","FL #3 Full Review + Error Pattern Analysis",15),
    ("2026-07-22","16:00","21:00","BB/CP","Data Interpretation & Experimental Design",15),
    ("2026-07-23","13:00","18:00","PS","PS Deep Dive -- Research Methods & Epidemiology",15),
    ("2026-07-24","12:30","17:30","CP","CP Calculation Drill + Physics Problem Workshop",15),
    ("2026-07-25","07:00","12:00","CARS","CARS Full Section + Weekly Review",15),
    ("2026-07-27","07:00","12:00","ALL","Third-Party FL #4 (Full-Length)",16),
    ("2026-07-28","13:00","18:00","ALL","FL #4 Full Review + Error Log Analysis",16),
    ("2026-07-29","16:00","21:00","BB","Biochemistry Integration Review",16),
    ("2026-07-30","13:00","18:00","CP","Physics + Gen Chem Problem-Solving",16),
    ("2026-07-31","12:30","17:30","PS","PS Comprehensive Section Practice",16),
    ("2026-08-01","07:00","12:00","CARS","CARS Strategy Refinement + Phase 3 Planning",16),
    ("2026-08-03","07:00","12:00","ALL","Third-Party FL #5 (Full-Length)",17),
    ("2026-08-04","13:00","18:00","ALL","FL #5 Full Review + Score Trend Analysis",17),
    ("2026-08-05","16:00","21:00","BB/CP","Content Gap Remediation -- BB & CP",17),
    ("2026-08-06","13:00","18:00","PS/CARS","Content Gap Remediation -- PS & CARS Maintenance",17),
    ("2026-08-07","12:30","17:30","ALL","Mixed Timed Practice + Strategy Review",17),
    ("2026-08-08","07:00","12:00","ALL","Phase 2 Assessment + Phase 3 Planning",17),
]

for d, st, et, sec, top, w in sessions2:
    add(d, st, et, sec, top, w, 2)

# Phase 3: AAMC Materials (Weeks 18-22)
sessions3 = [
    ("2026-08-10","07:00","12:00","BB","AAMC QPack -- Biology Vol 1",18),
    ("2026-08-11","13:00","18:00","CP","AAMC QPack -- Chemistry Vol 1",18),
    ("2026-08-12","16:00","21:00","CP","AAMC QPack -- Physics",18),
    ("2026-08-13","13:00","18:00","BB","AAMC QPack -- Biology Vol 2",18),
    ("2026-08-14","12:30","17:30","CP","AAMC QPack -- Chemistry Vol 2",18),
    ("2026-08-15","07:00","12:00","CARS","AAMC CARS QPack Vol 1",18),
    ("2026-08-17","07:00","12:00","CARS","AAMC CARS QPack Vol 2",19),
    ("2026-08-18","13:00","18:00","BB","AAMC Section Bank -- BB",19),
    ("2026-08-19","16:00","21:00","CP","AAMC Section Bank -- CP",19),
    ("2026-08-20","13:00","18:00","PS","AAMC Section Bank -- PS",19),
    ("2026-08-21","12:30","17:30","ALL","Section Bank Full Review Day",19),
    ("2026-08-22","07:00","12:00","ALL","AAMC FL 1 (Full-Length)",19),
    ("2026-08-24","07:00","12:00","ALL","AAMC FL 1 -- Full Review",20),
    ("2026-08-25","13:00","18:00","ALL","Targeted Weak Area Review",20),
    ("2026-08-26","16:00","21:00","ALL","AAMC FL 2 (Full-Length)",20),
    ("2026-08-27","13:00","18:00","ALL","AAMC FL 2 -- Full Review",20),
    ("2026-08-28","12:30","17:30","ALL","High-Yield Content Blitz + Leech Review",20),
    ("2026-08-29","07:00","12:00","CARS/PS","CARS Maintenance + PS Final Vocabulary Drill",20),
    ("2026-08-31","07:00","12:00","ALL","AAMC FL 3 (Full-Length)",21),
    ("2026-09-01","13:00","18:00","ALL","AAMC FL 3 -- Full Review",21),
    ("2026-09-02","16:00","21:00","ALL","AAMC FL 4 (Full-Length)",21),
    ("2026-09-03","13:00","18:00","ALL","AAMC FL 4 -- Full Review",21),
    ("2026-09-04","12:30","17:30","ALL","Light Review + Confidence Building",21),
    ("2026-09-05","07:00","12:00","ALL","Test Day Logistics + Gentle Review",21),
    ("2026-09-07","07:00","12:00","BB/CP","Final Light Review -- BB & CP Highlights",22),
    ("2026-09-08","13:00","18:00","PS/CARS","Final Light Review -- PS & CARS Highlights",22),
    ("2026-09-09","16:00","21:00","REST","Complete Rest Day",22),
    ("2026-09-10","13:00","18:00","EXAM","EXAM DAY",22),
    ("2026-09-11","12:30","17:30","REST","REST & CELEBRATE",22),
    ("2026-09-12","07:00","12:00","ALL","Post-Exam Reflection (Optional)",22),
]

for d, st, et, sec, top, w in sessions3:
    add(d, st, et, sec, top, w, 3)

# Generate ICS
phase_names = {1: "Content Review", 2: "Practice & Integration", 3: "AAMC Materials"}
lines = []
lines.append("BEGIN:VCALENDAR")
lines.append("VERSION:2.0")
lines.append("PRODID:-//MCAT Study Coach//EN")
lines.append("CALSCALE:GREGORIAN")
lines.append("METHOD:PUBLISH")
lines.append("X-WR-CALNAME:MCAT Study Schedule")

for dtstart, dtend, section, topic, week, phase in events:
    uid = str(uuid.uuid4())
    summary = f"MCAT [{section}]: {topic}"
    desc = f"Phase {phase}: {phase_names[phase]} | Week {week}"
    lines.append("BEGIN:VEVENT")
    lines.append(f"UID:{uid}")
    lines.append(f"DTSTART:{dtstart.strftime('%Y%m%dT%H%M%S')}")
    lines.append(f"DTEND:{dtend.strftime('%Y%m%dT%H%M%S')}")
    lines.append(f"SUMMARY:{summary}")
    lines.append(f"DESCRIPTION:{desc}")
    lines.append("STATUS:CONFIRMED")
    lines.append("END:VEVENT")

lines.append("END:VCALENDAR")

outpath = "C:/Users/matul/ClaudeProjects/MCAT/progression/mcat_schedule.ics"
with open(outpath, "w", newline="\r\n") as f:
    f.write("\r\n".join(lines))

print(f"Generated {len(events)} calendar events -> {outpath}")

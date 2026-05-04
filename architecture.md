# Project File Architecture

Reference doc loaded on demand. CLAUDE.md points here for file routing rules.

## Top-level structure

```
MCAT/
├── CLAUDE.md                    Lean coach config + pointer to this file
├── architecture.md              (this file) File system + loading rules
├── Content/                     Topic outlines (lightweight)
├── research/                    Deep-dive teaching material
├── mnemonics/                   Memory aids (loaded only on explicit request)
└── progression/                 Schedule, logs, state
```

## The 1:1 Mirror Rule

`Content/`, `research/`, and `mnemonics/` mirror each other with identical filenames. Every topic file has a counterpart in all three tiers. This is invariant — do not create a file in one tier without creating its siblings.

| Tier | Purpose | Size per file |
|------|---------|---------------|
| Content | Outline / checklist | 15–90 lines |
| research | Full teaching material, mechanisms, MCAT tips | 100–800 lines |
| mnemonics | Verified memory aids | 60–130 lines |

## Folder layout (post-2026-05-03 Kaplan-book reorg, all 6 books restructured)

`Content/`, `research/`, and `mnemonics/` mirror this exact folder structure. Each subject folder has an `INDEX.md` (research/ side) with chapter-level routing.

```
Biology/         Ch01..Ch12 + INDEX.md   (Kaplan Biology 2024)
Biochemistry/    Ch01..Ch12 + INDEX.md   (Kaplan Biochem 2024)
GenChem/         Ch01..Ch12 + INDEX.md   (Kaplan General Chem 2024)
OrgChem/         Ch01..Ch12 + INDEX.md   (Kaplan Organic Chem 2024)
PhysicsMath/     Ch01..Ch12 + INDEX.md   (Kaplan Physics & Math 2024; Ch11–12 also hold the former ResearchMethods/ content)
Psychology/      Ch01..Ch12 + INDEX.md   (Kaplan Behavioral Sciences 2024)
CARS/            CARS.md
LabTechniques/   Lab_Techniques.md
KaplanMap/       Kaplan_Map_and_Gaps.md   (Content/ side only)
```

**Inside each chapter folder:** files are named `ChNN_Topic.md` with no book prefix (the folder name is the namespace). Example: `research/Biology/Ch04_Nervous_System.md`.

**Top-level Content/ overview files (kept):**

- `Content/BB_Bio_Biochem.md` — AAMC BB section overview (FC mix, blueprint)
- `Content/CP_Chemical_Physical.md` — AAMC CP section overview

These are not Kaplan-book content; they document the AAMC section as a whole.

## Progression tier

```
progression/
├── INDEX.md                             Date → week file lookup (read first every session)
├── TRACKER.md                           Confidence ratings + FL scores (state)
├── END_SESSION.md                       Session-end / schedule-shift protocol
├── PHASE_SUMMARIES.md                   Post-phase retrospectives
├── MCAT TOPIC CONFIDENCE MAP v2.txt     Topic-level 0-5 self-ratings
├── mcat_schedule.ics                    Google Calendar import (regen after shifts)
├── gen_ics.py                           ICS regenerator
├── week_00_kickoff.md
└── week_01.md ... week_NN.md            One per week: schedule, logs, pre-flight, review
```

## Index files (routing)

Each subject folder has an `INDEX.md` with trigger keywords for file routing:

- `research/INDEX.md` — top-level: subject folder routing
- `research/Biology/INDEX.md` — 12 Kaplan Biology chapters
- `research/Biochemistry/INDEX.md` — 12 Kaplan Biochem chapters
- `research/GenChem/INDEX.md` — 12 Kaplan GChem chapters
- `research/OrgChem/INDEX.md` — 12 Kaplan OChem chapters
- `research/PhysicsMath/INDEX.md` — topic files (pending Physics chapter restructure)
- `research/Psychology/INDEX.md` — single file pending split
- `mnemonics/` — same folder pattern when populated (load only on explicit request)

## Loading Rules

**Global rule:** Load the SMALLEST set of files needed. Never load all files at once.

**Routing flow:** week file → topic → `research/INDEX.md` → subject INDEX → Content + Research pair.

**Always load Content + Research as a pair** — outline + deep-dive together.

**By context:**

| Task | Files to load |
|------|---------------|
| Study / teach | Week file → routed Content + Research pair |
| Quiz | Content + Research for the section |
| Gaps / "what's left" | `Content/KaplanMap/Kaplan_Map_and_Gaps.md` + `progression/MCAT TOPIC CONFIDENCE MAP v2.txt` only |
| Schedule changes | Current + adjacent week files + gap map + confidence map |
| Progress / trends | Recent week files + confidence map (no content files unless asked) |

**Mnemonics:** Do NOT load unless the student explicitly asks for a memory aid. When loading, load only the single matching file.

**Cross-loading cap:** At most 1 cross-referenced file per session beyond the primary Content + Research pair. If lab techniques AND research methods both apply, pick the more relevant one.

**Context budget:** A typical study session should load ≤5 files beyond the week file and INDEX lookups.

**AAMC section overview files (load rarely):** `Content/BB_Bio_Biochem.md` (444 lines) and `Content/CP_Chemical_Physical.md` (344 lines) — AAMC FC blueprints, not Kaplan content. Only load for full-section overviews; default to chapter sub-files for topic-specific work.

**Pre-2026-04-28 path references in completed week files:** Old logs reference paths like `research/BB/BB_Ch01_*.md` that no longer resolve (files now at `research/Biochemistry/Ch01_*.md`). These are historical records — do not auto-update. If a completed day needs to be re-loaded, navigate to the new path manually via the relevant subject INDEX.

## Topic switch mid-session

When the student shifts subjects and new files would exceed the context budget:

1. Write a **mid-session snapshot** to the day's entry in the week file's Session Logs:
   - Topics covered so far
   - Key concepts explained
   - Mistakes or weak spots identified
   - Revisit-later flags
2. Tell the student: *"Snapshot saved to the week file. Safe to `/clear`."*
3. After `/clear`, pre-flight picks up the current week file — snapshot visible for continuity.

**Never raw-clear without saving a snapshot first.** The conversation is the raw material for the log.

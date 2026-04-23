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

## BB (Bio/Biochem) file layout

**Biochem side — Kaplan Biochem Ch 1-12 (since 2026-04-22):**

```
BB_Ch01_AminoAcids_Proteins.md
BB_Ch02_Enzymes.md
BB_Ch03_NonEnzymatic_Protein.md
BB_Ch04_Carbohydrates.md
BB_Ch05_Lipids.md
BB_Ch06_DNA_Biotech.md
BB_Ch07_RNA_GeneticCode.md
BB_Ch08_Membranes.md
BB_Ch09_CarbMetab1.md
BB_Ch10_CarbMetab2.md
BB_Ch11_Lipid_AA_Metab.md
BB_Ch12_Bioenergetics.md
```

**Bio side — legacy topic-based (pending Kaplan Biology restructure):**

```
BB_Cell_Biology.md            (membrane content dup'd in BB_Ch08 until bio restructure)
BB_Prokaryotes_Viruses.md
BB_Cell_Division.md
BB_Nervous_Endocrine.md
BB_Organ_Systems.md
BB_Heredity_Evolution.md
```

## CP (Chem/Phys) file layout

12 files under `Content/CP/` and `research/CP/`, organized by foundational concept. See `research/CP/INDEX.md` for routing keywords.

## Root-level files (no sub-splits)

`PS_Psych_Soc.md` — organized by Kaplan Behavioral Sciences Ch 1-12 (since 2026-04-19)
`CARS.md`
`Research_Methods.md`
`Lab_Techniques.md`

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

- `research/INDEX.md` — top-level: subject → subfolder
- `research/BB/INDEX.md` — 12 biochem chapters + 6 bio topic files (pending restructure)
- `research/CP/INDEX.md` — 12 CP files
- `mnemonics/BB/INDEX.md`, `mnemonics/CP/INDEX.md` — same routing pattern

## Loading Rules

**Global rule:** Load the SMALLEST set of files needed. Never load all files at once.

**Routing flow:** week file → topic → `research/INDEX.md` → subject INDEX → Content + Research pair.

**Always load Content + Research as a pair** — outline + deep-dive together.

**By context:**

| Task | Files to load |
|------|---------------|
| Study / teach | Week file → routed Content + Research pair |
| Quiz | Content + Research for the section |
| Gaps / "what's left" | `Content/Kaplan_Map_and_Gaps.md` + `progression/MCAT TOPIC CONFIDENCE MAP v2.txt` only |
| Schedule changes | Current + adjacent week files + gap map + confidence map |
| Progress / trends | Recent week files + confidence map (no content files unless asked) |

**Mnemonics:** Do NOT load unless the student explicitly asks for a memory aid. When loading, load only the single matching file.

**Cross-loading cap:** At most 1 cross-referenced file per session beyond the primary Content + Research pair. If lab techniques AND research methods both apply, pick the more relevant one.

**Context budget:** A typical study session should load ≤5 files beyond the week file and INDEX lookups.

**Monolith exception:** `Content/BB_Bio_Biochem.md` (444 lines) and `Content/CP_Chemical_Physical.md` (344 lines) — only load for full-section overviews; default to sub-files for topic-specific work.

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

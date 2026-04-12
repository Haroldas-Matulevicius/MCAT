# End Session Protocol

Read this file when the user says "done", "wrap up", "end session", "end study session", or similar.

## Steps

1. **Collect the session log.** Ask the user to paste their session log entry for today.
2. **Append to week file.** Once pasted, add it to the current week file's Session Logs section.
3. **Mark today as logged.** Change today's row from `[ ]` to `[x]` in the Logged column.
4. **Confidence rating.** Ask for a confidence rating (0-5) on today's topic.

## Saturday Escalation (Weekly Review)

If today is **Saturday**, also prompt the user for these weekly review items:
- Update `progression/MCAT TOPIC CONFIDENCE MAP v2.txt` for all topics covered this week
- Update the **Section Confidence Tracker** in CLAUDE.md based on confidence map trends
- Update **Top 3 weak topics** in CLAUDE.md based on recurring low scores or error patterns
- Mark the weekly review checklist items in the week file as `[x]`

## Milestone Escalation (Every 4 Weeks)

If this is a **4-week milestone** (weeks 4, 8, 12, 16, 20), also prompt to update **Strengths** and **Weaknesses** in the Student Profile section of CLAUDE.md based on accumulated session data.

## Full-Length Exam Day

If today was a **full-length practice exam**, update the **Practice Exam Scores** table in CLAUDE.md with the scores.

## Schedule Shift Protocol

Triggered when the user says "push back", "shift schedule", "I missed X days", "start [topic] on [new date]", or similar.

1. **Identify the shift:** Which week/day is the starting point, and how many days to push forward.
2. **Read `progression/INDEX.md`** to get current date ranges.
3. **For each affected week file** (from the shift point onward):
   - Recalculate all dates in the schedule table (shift by N days, preserving day-of-week pattern: Mon/Tue/Wed/Thu/Fri/Sat with Sun off).
   - Update the date range in the file header.
   - **Do NOT touch** the Session Logs section or any `[x]` checkmarks — completed work stays intact.
   - Update the Pre-flight block if it references specific dates.
4. **Update `progression/INDEX.md`** with new date ranges for all affected weeks.
5. **Regenerate the ICS file:** Update dates in `progression/gen_ics.py` to match the new schedule, then run `python progression/gen_ics.py` to regenerate `progression/mcat_schedule.ics`.
6. **Report:** Show the user what shifted, new date ranges, and remind them to reimport the ICS into Google Calendar.

**Important:** Week files are never renamed. `week_01.md` is always "week 1 of study" regardless of what dates it falls on. Only the dates inside change.

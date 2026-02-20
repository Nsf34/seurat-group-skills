---
name: survey-mapper
description: >
  Reads a quant survey document (.docx) and produces a structured Survey Map —
  a condensed reference file capturing every question's logic, routing, response
  options, variable assignments, piping dependencies, and programming notes.
  This map is the required foundation for the test-path-generator skill.
  Use this skill whenever a user provides a survey .docx and wants to generate
  test paths, or says things like "map the survey," "analyze the survey doc,"
  "read through the survey," or "let's start on the test plan." Always run
  survey-mapper FIRST before test-path-generator — the map is what makes
  accurate test path generation possible.
---

# Survey Mapper

Your job is to thoroughly read a quant survey document and produce a **Survey
Map** — a structured, condensed file that captures every question's logic so
that the test-path-generator can accurately simulate each test path without
re-reading the massive source document each time.

Survey documents can be enormous (50–200MB). Never try to load the whole thing
into context at once. Use Python to extract and parse systematically, building
the map as you go.

---

## Step 1 — Extract All Survey Text to a Working File

Use python-docx to pull every paragraph and table cell into a plain text file.
This becomes your working document for parsing.

```python
from docx import Document
from docx.oxml.ns import qn
import sys

def extract_survey(docx_path, out_path):
    doc = Document(docx_path)
    lines = []
    for el in doc.element.body:
        tag = el.tag.split('}')[-1]
        if tag == 'p':
            text = ''.join(r.text for r in el.findall('.//' + qn('w:t')))
            if text.strip():
                lines.append(text.strip())
        elif tag == 'tbl':
            lines.append('[TABLE]')
            for row in el.findall('.//' + qn('w:tr')):
                cells = [''.join(t.text for t in c.findall('.//' + qn('w:t'))).strip()
                         for c in row.findall('.//' + qn('w:tc'))]
                lines.append(' | '.join(cells))
            lines.append('[/TABLE]')
    with open(out_path, 'w') as f:
        f.write('\n'.join(lines))
    print(f"Done: {len(lines)} lines → {out_path}")

extract_survey(sys.argv[1], sys.argv[2])
```

Run: `python3 extract.py "<survey.docx>" survey_raw.txt`

---

## Step 2 — Understand Survey Structure Before Parsing

Every Seurat Group quant survey follows this architecture:

- **Messages (M1, M2…)**: Informational screens shown to respondents, not
  questions. Check their text and show conditions.
- **Screener (S1, S2…)**: Qualification questions. Each can terminate, route,
  or assign variables.
- **Main modules (Q101–Q199, Q201–Q299, Q301–Q399…)**: Core questionnaire.
  Modules are thematically grouped (e.g., Perceptions, Brand Deep-dive,
  Purchase Behavior).
- **Demographics (D1, D2…)**: Final standard demo questions.

Read the raw text in chunks using `Read` with offset/limit. Work section by
section. Don't try to hold the whole thing in context.

---

## Step 3 — Build the Survey Map File

As you read each section, write its entry into the Survey Map file immediately.
Don't save everything for the end — write incrementally so nothing is lost.

Save to: `[ProjectName]_Survey_Map.md` in the project folder.

Use this exact structure:

```markdown
# Survey Map: [Project Name]
Source file: [filename]
Date: [today]

---

## Variable Registry

Every `<variable>` used anywhere in the survey, with where it's set and what
values it can take. This table is critical — the path generator uses it to
initialize path state.

| Variable | Set At | Trigger Condition | Value Assigned |
|----------|--------|-------------------|----------------|
| <Kids in HH> | S4 | R2, R3, or R4 selected (non-zero kids) | Yes |
| <No kids in HH> | S4 | "No children under 18" selected | Yes |
| <category quota> | S8 | Least-fill logic | Category name string |
| <brand> | S10 | C3 (most recent brand) selected | Brand name string |

---

## Messages

### M1
Shown: Always (survey start)
Text: "[exact message text]"

### M2
Shown: [condition, e.g., "Always" or "Only when <low income> is assigned"]
Text: "[exact message text]"

---

## Screener Questions

### S1 — Age
Type: Dropdown / Single select
Shown: Always
Question text: "[full question text]"
Response options:
  - Dropdown of ages
Programming notes: [any notes]
Variable assignments:
  - Any age selected → <generation> = [value based on age range]
Routing:
  - TERMINATE IMMEDIATELY if: age < 18 or age > [max]
  - TERMINATE END OF SCREENER if: age > [soft cap]

### S4 — Children in Household
Type: Multi-select with dropdowns
Shown: Always
Question text: "[full text]"
Response options:
  - R1: "No children under 18 living in my household" — ANCHORED, NOT a dropdown, MUTUALLY EXCLUSIVE
  - R2: Children under 5 — dropdown for count
  - R3: Children 6–12 — dropdown for count
  - R4: Children 13–17 — dropdown for count
Programming notes: [any]
Variable assignments:
  - R2, R3, or R4 selected with non-zero count → <Kids in HH> = Yes
  - R1 selected → <No kids in HH> = Yes
Routing: none

[Continue for all S-questions...]

---

## Module 1: [Module Name] (Q101–Q1NN)

### Q101 — [Topic]
Type: [10-point scale / single select / multi select / open-end / drag-and-drop / carousel / grid]
Shown: [Always / condition]
Question text: "[full text, noting any bolded/underlined/piped elements]"
Columns: C1=[label, multi-select], C2=[label, single select] (if applicable)
Response options:
  - R1: [text]
  - R2: [text] — ANCHORED TOP, MUTUALLY EXCLUSIVE
  - "Other; please specify" — ANCHORED BOTTOM, open-end
  - "None of the above" — ANCHORED BOTTOM, MUTUALLY EXCLUSIVE
Piping: <brand> piped through in question text; <category> piped in R9 and R17
Response option visibility:
  - R3 "Kid(s) in my household" — shown ONLY when <Kids in HH> is assigned
  - R11–R14 shown ONLY when <category> = "gummy candy"
  - R15–R16 shown ONLY when <category> = "packaged cookies"
Groupings: R2 and R3 are together; R5 and R6 are together
Programming notes: [any special logic, randomization notes, looping logic]
Variable assignments:
  - C3 selection → <brand> = [selected brand name]
Routing: [any skips]
Loop note: This question block loops up to 2 times for each assigned <brand>

[Continue for all Q-questions...]

---

## Demographics

### D1 — Race/Ethnicity
Type: Multi-select
Shown: Always
Response options:
  - "Other; please specify" — ANCHORED BOTTOM, open-end
  - "Prefer not to answer" — ANCHORED BOTTOM, MUTUALLY EXCLUSIVE
[etc.]
```

---

## Step 4 — What to Extract and Why

Every piece of information in the map serves a specific purpose when generating
test paths. Here's how they connect:

**Question type** → determines "Ensure single select" vs "Ensure multi select
in C1 and C2" vs "Ensure question is a 10-point scale"

**Anchored/mutually exclusive options** → every anchored option gets its own
"Ensure '[text]' is anchored at [top/bottom] and mutually exclusive" line in
every path

**Grouped response options** (e.g., "R2 and R3 are together") → generates
"Ensure R2 and R3 are together" in paths

**Piped content** → wherever `<variable>` appears in question text or response
options, generates "Ensure `<variable>` is piped through in question text"

**Per-option visibility conditions** → generates "Ensure you see R3" or
"Ensure you do not see R11, R15, and R16" depending on path's variable state

**Variable assignments** → tells the path generator what state changes after
each selection, which cascades through downstream question visibility

**Loop logic** → generates "Ensure all possible questions in Q201–Q229 are
looped up to [N] times for all assigned <brand>"

**Message text** → generates "Ensure message reads: '[text]'"

---

## Step 5 — Flag Ambiguities

When survey logic is unclear, incomplete, or requires interpretation, add a
flag directly in the map entry:

```
⚠️ AMBIGUOUS: [What is unclear and what assumption was made for now]
```

Common ambiguity sources: contradictory programming notes, conditions that
depend on multiple variables in combination, response option visibility that
isn't explicitly stated in the survey document, complex loop interactions.

Collect all flags in a summary section at the end of the map:

```markdown
---
## Ambiguity Log
1. ⚠️ Q217 — Not clear whether this shows for both <brand type>=BFY and
   <brand type>=Mainstream, or only BFY. Assumed: only BFY based on context.
2. ⚠️ S14 — Response option R22 text is cut off in the survey doc. Captured
   as "R22: [incomplete text — verify in survey]"
```

These flags are essential review points before any test paths are sent to QA.

---

## Step 6 — Completeness Check Before Finishing

Before saving the final map, verify:

1. Every question number referenced in the survey has an entry (no unexplained
   gaps in numbering)
2. Every `<variable>` referenced in any condition or piping note appears in
   the Variable Registry with a definition
3. Every "Shown when [condition]" references a known variable
4. Message texts are copied verbatim — they get checked character-by-character
   in test paths
5. All grouped response options, anchored options, and mutual-exclusivity rules
   are captured

If you find gaps on the pass, go back to the relevant survey section and fill
them in before finishing.

---

## Step 7 — Save and Report

Save the completed Survey Map with a clear filename:
`[ProjectName]_Survey_Map.md`

Then report to the user:
- Total question count by type (S, Q, D, M)
- Total variables in the Variable Registry
- Any ambiguities (list them from the Ambiguity Log)
- Estimated survey complexity (number of conditional branches, loop structures)
- Confirmation that it's ready for test-path-generator

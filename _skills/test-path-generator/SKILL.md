---
name: test-path-generator
description: >
  Generates a single complete survey test path in Seurat Group's exact format,
  given a Survey Map (from the survey-mapper skill) and one row from the test
  path matrix. The path is a question-by-question walkthrough of the survey with
  every check, piping verification, response visibility rule, variable assignment
  confirmation, and selection instruction written out precisely.
  Use this skill when the user says "generate path [N]," "write test path [N],"
  "do path [N]," or similar. Requires a completed Survey Map file as input.
  Run survey-mapper first if no map exists yet.
---

# Test Path Generator

> **Before generating any path, read:** `references/check_format_patterns.md`
> This contains real examples of every check type in the exact wording and format
> that Seurat Group uses. When in doubt about how to phrase anything, look it up there.

Your job is to simulate one specific test path through a survey and write out
every single check, instruction, and verification in Seurat Group's exact format.
This requires reading the Survey Map carefully, initializing the path's variable
state from the test matrix, and then walking through every question in order —
reasoning at each step about what's visible, what needs to be checked, and what
to select.

---

## Step 1 — Gather Inputs

You need two things before writing anything:

1. **The Survey Map** (`[ProjectName]_Survey_Map.md`) — produced by survey-mapper.
   If it doesn't exist yet, stop and run survey-mapper first.
2. **The test matrix row for this path** — usually in the existing test plan
   draft or provided by the user. It defines the key variable assignments that
   make this path unique (e.g., which category, which brand, whether kids in HH,
   UNREAL buyer/aware status, etc.).

Read the full Survey Map before generating anything. You need to hold the entire
logic structure in mind as you walk through the path.

---

## Step 2 — Initialize the Path's Variable State

Before writing a single check, extract all variable assignments from the matrix
row and write them out explicitly as a "state register." This is your working
memory for the path.

Example state register for Path 1 of the Unreal Category Expansion:
```
<Kids in HH> = Yes
<priority category> = "gummy candy," "packaged cookies," "packaged brownies,"
                      "protein bars / bites," "sweet cereal," "cereal bars,"
                      "non-chocolate non-gummy candy"
<category quota> = "gummy candy"
<chocolate buyer> = Yes
<non-buyer category 1> = NOT assigned
<non-buyer category 2> = NOT assigned
<brand> = "Nerds Gummy Clusters," "Better Sour"
<category> = "gummy candy"
<UNREAL buyer> = Yes
<UNREAL aware> = Yes
<brand type for Nerds Gummy Clusters> = Mainstream
<brand type for Better Sour> = BFY
```

This register is what you update after each selection and what you consult to
determine visibility and checks at every downstream question.

---

## Step 3 — Walk Through Every Question in Order

Go question by question through the Survey Map. At each question, before writing
any output, reason through four things:

**A. Is this question visible for this path?**
Check the question's "Shown" condition against the current state register. If
the question is hidden, write only:
```
Q[N]:
Ensure you do not see the question
```
If a question has NO condition, it always shows — don't skip it.

**B. What format and structure checks apply?**
These apply regardless of path-specific state:
- Question type: "Ensure question is a 10-point scale for each category"
- Column types: "Ensure multi select in C1 and C2 and single select in C3"
- Anchored/mutually exclusive options: one line per anchored option, e.g.,
  "Ensure 'None of the above' is anchored at the bottom and mutually exclusive"
- Grouped options: "Ensure R2 and R3 are together"
- Bolded/underlined text in question: "Ensure '[text]' is bolded/underlined"
- Open-end fields: "Ensure 'Other; please specify' is anchored to the bottom
  and open-end"

**C. What path-specific checks apply?**
These depend on the current state register:
- Piping: "Ensure `<brand>` is piped through in question text" — write this
  whenever the Survey Map shows `<variable>` in the question text or response
  options, substituting actual variable values where relevant
- Response option visibility: "Ensure you see R3, 'Kid(s) in my household'"
  (because <Kids in HH> = Yes) or "Ensure you do not see R3" (because
  <No kids in HH> = Yes)
- Variable assignment verification: "Ensure assigned `<category quota>` =
  'gummy candy'" — write this the first time a variable is assigned in this path
- Specific items to confirm are visible/not visible based on state:
  "Ensure you see message text for `<UNREAL buyer>`"

**D. What should be selected?**
- If the matrix row specifies the selection: use it exactly
- If the question is a format/piping check with no specific selection needed:
  "Select any"
- If certain response options must be avoided (based on the path setup): "Select
  any except R5" or "Select any except 'I wouldn't be interested in any of these'"
- For scale questions without a specified value: "Select any"
- For specific screener setups: "Select [exact response text]" or
  "Select any response 18-55"

---

## Step 4 — Write the Output in Exact Format

The output format is precise and non-negotiable. Every path must follow this
structure exactly, because testers read these instructions line by line and
any deviation creates confusion.

### Path header
```
Path [N]
```
Just the path number. No colon, no extra text. One blank line after.

### Message blocks
```
M1: ensure message appears
```
or when there's specific text to verify:
```
M1: Ensure message reads: "[exact message text from Survey Map]"
```
Note: M1 conventionally uses lowercase "ensure." All other checks use "Ensure"
(capital E).

### Question blocks
```
Q[N]:
[Check line 1]
[Check line 2]
[Check line 3]
[Select instruction]
```

The question number is on its own line with a colon. Then checks follow,
one per line, no blank lines between them. One blank line between question blocks.

### Section headers (when the survey has named modules)
If the survey organizes questions into named sections (e.g., "Screener,"
"Planning," "Shopping," "Buying"), include those as section labels above the
first question in that section:
```
Screener
S1:
Select any age 21-74
```

### Example of a fully written question block:
```
Q205:
Ensure <brand><category> is piped through in question text
Ensure "No one else was there" is anchored to the top and mutually exclusive
Ensure you see R3, "Kid(s) in my household"
Ensure "Other; please specify" is anchored to the bottom and open-end
Select any
```

And for a question that this path should NOT see:
```
Q217:
Ensure you do not see the question
```

And for a loop:
```
Ensure all possible questions in Q201 – Q229 are looped up to two times for all
assigned <brand>
```
(This line goes AFTER the last question in the loop, before the next section.)

---

## Step 5 — Check Order Within Each Question Block

Within a single question block, write checks in this order to match firm style:

1. Visibility of the question itself (if conditional): "Ensure you see the
   question" (only needed when the question is conditionally shown and IS showing)
2. Message text verification (for M questions): "Ensure message reads: '...'"
3. Question text checks — piping: "Ensure `<variable>` is piped through in
   question text"
4. Question format: "Ensure question is a [N]-point scale" / "Ensure multi
   select in C1 and single select in C2"
5. Anchored-top options (mutually exclusive): "Ensure 'X' is anchored to the
   top and mutually exclusive"
6. Response option visibility: "Ensure you see R[N]" / "Ensure you do not see
   R[N], R[M], and R[P]"
7. Response groupings: "Ensure R[N] and R[M] are together"
8. Piping into specific response options: "Ensure `<brand>` is piped through
   in R14 response option text"
9. Anchored-bottom options: "Ensure 'None of the above' is anchored to the
   bottom and mutually exclusive" / "Ensure 'Other; please specify' is anchored
   to the bottom and open-end"
10. Variable assignment verifications: "Ensure assigned `<variable>` = 'value'"
11. Selection instruction: "Select any" / "Select R1" / "Select any R1-R3"

When multiple checks of the same type exist (e.g., multiple anchored-bottom
options), list them together.

---

## Step 6 — Update State After Each Selection

After writing the selection instruction for a question that triggers variable
assignments, mentally update your state register. This matters for downstream
questions. For example:

- After S4 where "No children under 18" is selected → update state:
  `<No kids in HH> = Yes`, `<Kids in HH> = NOT assigned`
- After S8 where specific categories are selected → update `<priority category>`,
  `<category quota>`, `<non-buyer categories>`, `<other categories>`
- After S10 where specific brand is selected in C3 → update `<brand>`,
  `<category>`, `<brand type>`

The most common errors in test paths come from not tracking state updates
correctly through complex screener questions. Take extra care at S8, S10, and
any other questions that do heavy variable assignment.

---

## Step 7 — Coverage Verification Pass

After writing all questions through to the final demographic, do a coverage pass:

1. Check that every question in the Survey Map's question list has an entry in
   your generated path (either a set of checks or "Ensure you do not see the
   question").
2. Check that every variable in the path's state register was verified at least
   once with an "Ensure assigned `<variable>`" statement.
3. Check that every anchored/mutually exclusive option in every visible question
   has its own "Ensure '[text]' is anchored..." check.
4. Check that messages M1 through M[last] all appear in the path.
5. Check that any loop logic in the survey has a corresponding loop verification
   statement.

If you find a gap, go back and insert the missing check in the right place.

---

## Step 8 — Flag and Note Uncertainties

If you're uncertain about any check — because the Survey Map had an ambiguity
flag, because the logic was complex, or because a check depends on variable
state that's hard to trace — add an inline flag:

```
Q308:
[checks...]
Select any
⚠️ REVIEW: Not certain whether R12 should be shown for this path — depends on
whether <category> = "packaged brownies" triggers the brownie-specific response
cluster. Verify against survey doc before using in QA.
```

Surface all such flags to the user at the end of the path with a numbered list:

```
--- Path [N] Complete ---
⚠️ Items to review before QA:
1. Q308 — R12 visibility uncertain (see note above)
2. Q217 — Verify this question is truly hidden for <brand type>=Mainstream paths
```

---

## Output File

Save the generated path to:
`Path_[N]_[ProjectName].txt`

This file will be used as input for the test-plan-assembler skill, which
combines all paths into the final formatted .docx test plan.

---
name: test-plan-assembler
description: >
  Takes all generated test path files (from test-path-generator) and assembles
  them into a complete, properly formatted Seurat Group Survey Test Plan .docx
  document. Adds the standard General Checks boilerplate, Screener Termination
  Checks, Survey Test Matrix table, and all numbered paths in firm style.
  Use this skill when all paths for a project have been generated and the user
  says "assemble the test plan," "put together the test plan doc," "format the
  test plan," or "make the final .docx." This is always the last step in the
  test plan workflow, after survey-mapper and test-path-generator.
---

# Test Plan Assembler

Your job is to build the final `.docx` test plan in **Seurat Group's exact visual
style**. Every color, font, size, and bullet level is specified here — do not
deviate. The formatting is just as important as the content.

---

## Exact Visual Specification

### Fonts
- **Primary font throughout**: Franklin Gothic Book
- **Fallback**: Calibri (only if Franklin Gothic Book unavailable)

### Colors
- **Navy blue**: `RGBColor(0x0F, 0x47, 0x61)` — used for title and matrix label
- **Orange**: `RGBColor(0xE9, 0x71, 0x32)` — used for date only

### Title Block
```
[Project Name] Survey Test Plan    ← Franklin Gothic Book, 18pt, Bold, navy blue
[Date]                             ← Franklin Gothic Book, 14pt, NOT bold, orange
[empty line]
```
Title may be split across two paragraphs (e.g., "Bellring GLP-1 Survey" on one
line, "Test Plan" on the next) — both in the same style. Follow however the
project name naturally fits.

### Section Headings
- **"General Checks (all)"** → Word style: `Heading 1`
- **"Screener Termination Checks"** → Word style: `Heading 1`
- **"Test Path N:"** → Word style: `Heading 3`
- **"Screener", "Consumer Journey", "Module X"** (subsections within a path) →
  Word style: `Heading 4`

### Bullet Levels
Use `List Paragraph` style with explicit numPr XML. Two main bullet levels:
- **ilvl=0** (top-level bullet): used for question-group labels in Screener
  Termination Checks (e.g., "S1", "S4")
- **ilvl=1** (indented bullet): used for all path check lines

### "Test Paths Matrix:" label
- Style: Normal, Franklin Gothic Book, 14pt, navy blue (`#0F4761`), NOT bold

---

## Python Implementation

Build the document using this exact Python structure. Read the path files, the
survey map (for screener terminations), and the matrix data, then construct
the document section by section.

```python
from docx import Document
from docx.shared import RGBColor, Pt, Inches
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.text import WD_ALIGN_PARAGRAPH
import copy

NAVY  = RGBColor(0x0F, 0x47, 0x61)
ORANGE = RGBColor(0xE9, 0x71, 0x32)
FONT  = 'Franklin Gothic Book'

doc = Document()

# ── Helpers ────────────────────────────────────────────────────────────────

def set_font(run, size=None, bold=None, color=None, name=FONT):
    run.font.name = name
    if size:  run.font.size = Pt(size)
    if bold is not None: run.bold = bold
    if color: run.font.color.rgb = color

def add_paragraph(text, style='Normal', size=None, bold=None, color=None):
    p = doc.add_paragraph(style=style)
    run = p.add_run(text)
    set_font(run, size=size, bold=bold, color=color)
    return p

def add_bullet(text, level=0, bold_prefix=None):
    """
    Add a bulleted paragraph at the given level (0 or 1).
    level=0 → top-level bullet (used for S1/S4 labels in screener term section)
    level=1 → indented bullet (used for all path check lines)
    bold_prefix: if provided, this text is bolded, rest is normal
    """
    p = doc.add_paragraph(style='List Paragraph')

    # Set numPr for bullet level
    pPr = p._element.get_or_add_pPr()
    numPr = OxmlElement('w:numPr')
    ilvl = OxmlElement('w:ilvl')
    ilvl.set(qn('w:val'), str(level))
    numId = OxmlElement('w:numId')
    numId.set(qn('w:val'), '1')   # use list 1; Word will assign actual numId
    numPr.append(ilvl)
    numPr.append(numId)
    pPr.append(numPr)

    if bold_prefix:
        run1 = p.add_run(bold_prefix)
        run1.bold = True
        run1.font.name = FONT
        run2 = p.add_run(text)
        run2.font.name = FONT
    else:
        run = p.add_run(text)
        run.font.name = FONT
    return p

def add_question_label(label_text):
    """
    Question number label inside a path, e.g. 'S1.' or 'Q201.'
    Style: Normal, plain text, Franklin Gothic Book.
    """
    p = doc.add_paragraph(style='Normal')
    run = p.add_run(label_text)
    run.font.name = FONT
    return p
```

> **Important**: The exact `numId` value for bullets may vary. The safest
> approach is to use python-docx's built-in `List Bullet` and `List Bullet 2`
> paragraph styles instead of manual XML, then Word handles the numId correctly:
> - `doc.add_paragraph(text, style='List Bullet')` → ilvl=0
> - `doc.add_paragraph(text, style='List Bullet 2')` → ilvl=1
>
> Set font on each run after adding. This is cleaner and more reliable.

---

## Step-by-Step Assembly

### 1. Title Block

```python
# Title line(s) — navy blue, 18pt, bold, Franklin Gothic Book
p = add_paragraph('[Project Name] Survey Test Plan',
                  bold=True, size=18, color=NAVY)

# Date — orange, 14pt, not bold
p = add_paragraph('[Month Year]', size=14, color=ORANGE)

doc.add_paragraph()  # empty spacer
```

If the project name is long, split across two paragraphs (same style):
```python
add_paragraph('Bellring GLP-1 Survey', bold=True, size=18, color=NAVY)
add_paragraph('Test Plan',             bold=True, size=18, color=NAVY)
add_paragraph('June/July 2024',        size=14,   color=ORANGE)
doc.add_paragraph()
```

---

### 2. General Checks Section

```python
doc.add_heading('General Checks (all)', level=1)

gc_items = [
    ("top", "Ensure that instructions and question types are easy to understand and intuitive to use"),
    ("top", "Test that single selects, multi selects, and \"select up to specified number\" questions are working properly"),
    ("top", "Check to make sure each question specifies 'select all that apply, select one', or other relevant instructions"),
    ("top", "Check that responses are randomized or not randomized, as indicated in the programming notes"),
    ("top", "Make sure that a space is provided for all questions with an \"Other. Please specify.\" response option and can enter text or numbers there (whichever makes sense for that specific question)"),
    ("top", "Make sure response options are anchored/mutually exclusive (for example: \"none of the above\" responses), as indicated in the programming notes"),
    ("top", "Make sure text responses demand text, and numerical responses demand numbers."),
    ("top", "Make sure you must select a response for each question and that you can't skip pages"),
    ("top", "Make sure all questions and corresponding answer options have been programmed"),
    ("top", "Make sure new screens are shown where dictated"),
    ("top", "Put yourself in respondent's shoes and think about:"),
    ("sub", "Overall, do question formats clearly reflect how to answer the questions?"),
    ("sub", "Is it difficult to scroll through all answer options for any of the questions?"),
    ("sub", "Is a particular question frustrating to answer? Why?"),
    ("sub", "Is survey easy to take and intuitive to use?"),
]

for level, text in gc_items:
    style = 'List Bullet' if level == 'top' else 'List Bullet 2'
    p = doc.add_paragraph(text, style=style)
    for run in p.runs:
        run.font.name = FONT
        run.font.size = Pt(12)

# Images check — Normal (not bulleted)
p = doc.add_paragraph(
    'Make sure that all pictures/logos are shown in an easy to see way')
for run in p.runs:
    run.font.name = FONT
    run.font.size = Pt(12)

doc.add_paragraph()  # spacer
```

---

### 3. Screener Termination Checks Section

**No preamble text.** Go directly from the heading into the bulleted list.
Question label at ilvl=0 (List Bullet), conditions at ilvl=1 (List Bullet 2).

```python
doc.add_heading('Screener Termination Checks', level=1)

# Format: question label at top level, conditions as sub-bullets
# Example:
screener_terms = [
    ("S1", [
        "Terminate if respondents do not select between the ages of 18-65",
        "Ensure respondents who do not select an age between 18-65 are terminated immediately",
    ]),
    ("S4", [
        "Terminate if respondent selects [sensitive industry options]",
        "Ensure respondents are terminated at end of screener",
    ]),
    # ... add all termination points from Survey Map
]

for q_label, conditions in screener_terms:
    # Question label: ilvl=0 bullet
    p = doc.add_paragraph(q_label, style='List Bullet')
    for run in p.runs:
        run.font.name = FONT

    # Conditions: ilvl=1 sub-bullets
    for cond in conditions:
        p = doc.add_paragraph(cond, style='List Bullet 2')
        for run in p.runs:
            run.font.name = FONT

doc.add_paragraph()  # spacer
doc.add_paragraph()  # extra spacer (matches answer key spacing)
```

---

### 4. Survey Test Matrix

```python
# "Test Paths Matrix:" label — navy blue, 14pt, not bold
p = doc.add_paragraph()
run = p.add_run('Test Paths Matrix:')
run.font.name = FONT
run.font.size = Pt(14)
run.font.color.rgb = NAVY

doc.add_paragraph()  # spacer

# Build table
headers = ['', 'Path 1', 'Path 2', 'Path 3', 'Path 4', 'Path 5']
rows_data = [
    ['Tester', 'Zoe', 'Clara', 'Zoe', 'Clara', 'Clara'],
    ['Brand (S9)', 'Ozempic', 'Wegovy', 'Trulicity', 'Zepbound', 'Mounjaro'],
    # ... all matrix rows
]

table = doc.add_table(rows=1 + len(rows_data), cols=len(headers))
table.style = 'Table Grid'

# Header row
hdr_cells = table.rows[0].cells
for i, h in enumerate(headers):
    hdr_cells[i].text = h
    for para in hdr_cells[i].paragraphs:
        for run in para.runs:
            run.font.name = FONT
            run.bold = True

# Data rows
for ri, row_data in enumerate(rows_data):
    cells = table.rows[ri + 1].cells
    for ci, val in enumerate(row_data):
        cells[ci].text = val
        for para in cells[ci].paragraphs:
            for run in para.runs:
                run.font.name = FONT
```

---

### 5. Path Content

Each path follows this exact structure:

```
[Heading 3] "Test Path N:"
[Heading 4] "Screener"          ← or whatever section label applies
[empty line]
[Normal]    "S1."               ← question label: question number + period
[List Bullet 2] "Select 19"    ← check bullet (ilvl=1)
[List Bullet 2] "Ensure <Age Group> = Gen Z"
[empty line]                    ← blank line between questions
[Normal]    "S2."
[List Bullet 2] "Select any response"
[empty line]
...
[Heading 4] "Consumer Journey"  ← next section
[empty line]
[Normal]    "Q201."
[List Bullet 2] "Ensure <brand> is piped through as Ozempic"
[List Bullet 2] "Select any response"
...
```

**Parsing the path text files:**

Each path text file contains blocks like:
```
S1:
Ensure <Age Group> = Gen Z
Select 19
```

Convert each block to:
1. A `Normal` paragraph with the question number + period (e.g., `S1.`)
2. Each subsequent line as a `List Bullet 2` paragraph (ilvl=1 bullet)
3. An empty paragraph after each block

```python
def add_path(path_number, path_text, section_label_map=None):
    """
    path_text: raw content from Path_N_Project.txt
    section_label_map: dict mapping first question of each section to section name
                       e.g., {'S1': 'Screener', 'Q101': 'Attitudes and Motivations'}
    """
    # Path header
    doc.add_heading(f'Test Path {path_number}:', level=3)

    # Parse the path text into question blocks
    blocks = parse_path_blocks(path_text)

    current_section = None
    for q_label, checks in blocks:
        # Check if this question starts a new section
        if section_label_map and q_label in section_label_map:
            doc.add_heading(section_label_map[q_label], level=4)
            doc.add_paragraph()  # spacer after section header

        # Question label as Normal paragraph
        p = doc.add_paragraph(style='Normal')
        run = p.add_run(f'{q_label}.')
        run.font.name = FONT

        # Each check as a List Bullet 2 (ilvl=1 bullet)
        for check_line in checks:
            if check_line.strip():
                p = doc.add_paragraph(check_line.strip(), style='List Bullet 2')
                for run in p.runs:
                    run.font.name = FONT

        # Empty line between question blocks
        doc.add_paragraph()


def parse_path_blocks(path_text):
    """
    Parse path text into list of (question_label, [check_lines]).
    Input format:
        S1:
        Check line 1
        Check line 2

        S2:
        Check line 1
    """
    blocks = []
    lines = path_text.strip().split('\n')

    current_label = None
    current_checks = []

    for line in lines:
        line = line.rstrip()

        # Skip state register sections and internal notes
        if line.startswith('PATH') and 'STATE' in line.upper():
            continue
        if line.startswith('⚠️'):
            continue
        if line.startswith('---'):
            continue

        # Detect question label line (e.g., "S1:", "Q201:", "M1:", "D1:")
        import re
        if re.match(r'^[MSQD]\d+[A-Z]?\s*:', line):
            if current_label:
                blocks.append((current_label, current_checks))
            current_label = line.rstrip(':').strip()
            current_checks = []
        elif line.strip() == '' and current_label:
            # Empty line within block — skip (separator handled between blocks)
            pass
        elif current_label and line.strip():
            current_checks.append(line)

    if current_label and current_checks:
        blocks.append((current_label, current_checks))

    return blocks
```

---

## What NOT to Include

- **No preamble text** before the Screener Termination Checks bullets
- **No ⚠️ flags** anywhere in the document (collect them separately)
- **No state register sections** from the path files
- **No plain-text check lines** — every check must be a bullet (List Bullet 2)
- **No double bullets** — only one bullet style per section, don't nest incorrectly

---

## Step 6 — Final Quality Check

Before saving, verify by scrolling through the document:

1. Title is navy blue, date is orange
2. General Checks heading is styled (larger, formatted), bullets are properly indented
3. Screener Termination Checks: no preamble paragraph, question labels at top bullet
   level, conditions indented below each label
4. Matrix label is navy blue
5. Each path header renders as Heading 3 (larger)
6. Section headers (Screener, Consumer Journey, etc.) render as Heading 4
7. Every question has a label line ("S1.", "Q201.") followed by indented bullets
8. Empty lines separate question blocks within paths
9. No plain text check lines anywhere in path sections — all checks are bullets

---

## Step 7 — Save

```python
output_path = '/path/to/[ProjectName]_Survey_Test_Plan_v0.1.docx'
doc.save(output_path)
```

Filename format: `[ProjectName] Survey Test Plan v0.1.docx`

Report to user: paths assembled, any ⚠️ flags removed (list them).

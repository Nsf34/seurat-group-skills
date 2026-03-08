# Current Merck Wireframe Format Spec

Source of truth: `Merck LATAM Consumer Journey and PDH Wireframe DRAFT 03.06.26.docx`

This file describes the current target layout the skill must reproduce.

## Non-Negotiable Output Shape

The client-facing body is a 3-column layout:
- `Q #`
- `Survey Question`
- `Question Objective`

There is a small hidden extra grid artifact in the Word XML of the reference doc. Ignore it.
Build the visible layout as 3 logical columns.

## Page Setup

- Orientation: portrait
- Margins: 1 inch on all sides
- Cover and overview stay in the same document flow
- Do not force a page break after the cover
- Do not force page breaks between sections unless the user asks for them

## Cover

### Title
- Center aligned
- Font: Franklin Gothic Demi
- Size: 14 pt
- Color: `#1B2E59`

### Subtitle
- Text: `Survey Wireframe`
- Center aligned
- Font treatment should match the Merck title feel
- Size: 14 pt
- Color: `#F15B2A`

### Date
- Center aligned
- Size: 12 pt
- Color: `#758B97`

## Overview

### Main heading
- Text: `Survey Overview`
- Dark blue
- Bold
- 18 pt

### Subheadings
- Blue: `#28A8E0`
- Use for:
  - `Quant Research Objectives`
  - `Quotas`
  - `Survey Flow`

### Body content
- Franklin Gothic Book body text
- Use real Word list formatting, not just indented paragraphs
- `Quant Research Objectives`: real bullet list
- `Quotas`: real bullets with nested bullets where quota groups have sub-points
- `Survey Flow`: numbered main sections with nested bullet details

## Section Table Structure

Each `start_section()` call should create one visible section table.

Row order:
1. Section header row
2. Column header row
3. Section objectives row
4. Message rows and question rows

`add_subsection()` should append the same row pattern within the current table rather than
opening a new table.

## Column Widths

Use these visible DXA widths:
- `Q #`: `1379`
- `Survey Question`: `4871`
- `Question Objective`: `2662`

Keep the table layout fixed.

## Table Style

- Style name: `Table Grid`
- Keep the layout stable and non-autofit

## Header Rows

### Section header row
- Merge all 3 visible columns into one cell
- Center aligned
- White text
- Bold
- Default fill: `#002060`

Some sections in the Merck reference use a darker alternate fill:
- `#1B2E59`

The builder should allow the fill color to be overridden per section.

### Column header row
- 3 separate visible cells
- White text
- Fill: `#4970C8`
- Labels:
  - `Q #`
  - `Survey Question`
  - `Question Objective`

## Section Objectives Row

- Merge all 3 visible columns into one cell
- First paragraph label: `Section Objectives`
- Subsequent paragraphs: bullet list of section objectives
- Do not duplicate the same content into each column

## Message Rows

Message rows are not normal question rows.

Layout:
- Column 1: message label
- Columns 2 and 3: merged into one message cell

Typical labels:
- `Message`
- `Qualification Message`
- `Termination Message`

Rules:
- Keep the label in the `Q #` column
- Merge the question and objective columns together
- Put the respondent-facing message only once in the merged cell
- Allow red piped variables inside the message text

## Question Rows

### Q # column
- Populate by default
- In the reference, numbering is section-aware rather than a single flat sequence
- At minimum, the generated output must always show question numbers

### Survey Question column

The first paragraph usually contains:
- bold topic label followed by colon
- respondent-facing question copy
- red piped variables where relevant
- italic instruction at the end when needed

Typical pattern:

```text
Age: What is your age? Select one.
```

Formatting behavior:
- topic label: bold
- question body: regular
- piped variables: red
- instruction: italic

### Sub-questions inside the same question cell

Use additional paragraphs in the same cell for:
- second grid column prompts
- follow-up prompts
- multi-part questions

Do not create a new table row for those sub-questions unless they are a separate survey item.

### Response options

Render as bullet paragraphs under the prompt.

Use for:
- select-one lists
- select-all lists
- grid row labels
- bipolar statement labels
- category/brand lists

### Notes in the question cell

Use italic note lines when the client needs to review or confirm something, for example:
- brand list needs review
- list customized by category
- images/vignettes to be supplied by client

Red variables may appear inside notes.

## Objective Column

The objective column should contain:
1. Plain-English objective
2. Red programming notes when needed

Programming notes:
- color: red
- size: 10 pt
- one note per paragraph
- no extra blank paragraph after every note

Use programming notes for:
- grid structure
- assignments
- terminations
- qualifications
- randomization
- loops/carousels
- routing
- sample monitoring

## Variable Convention

Render piped variables in red using angle brackets:
- `<brand>`
- `<category>`
- `<segment>`
- `<retailer>`
- `<channel>`
- `<price>`
- `<Qualified Dog>`

Keep names consistent across the full wireframe.

## Interpretation Rules

When converting a loose outline into this format:
- preserve the study's real section structure
- aggressively draft missing questions
- convert analyst notes into internal logic
- choose the most plausible survey mechanic when the outline is vague
- keep the final document client-facing and polished

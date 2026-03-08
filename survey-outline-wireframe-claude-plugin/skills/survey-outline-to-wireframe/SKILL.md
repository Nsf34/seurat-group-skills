---
name: survey-outline-to-wireframe
description: Convert a survey outline .docx, quant outline, wireframe shell, assignments doc, or rough survey plan into a finished client-facing survey wireframe .docx in the Merck three-column format. Use whenever the user wants a polished wireframe built from outline materials, especially in Claude Code or Cowork.
version: 1.0.0
disable-model-invocation: true
argument-hint: <outline.docx> [output.docx]
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash]
---

# Survey Outline To Wireframe

This skill is user-invoked because it writes files.

The user invoked it with:

`$ARGUMENTS`

## Output rule

Create exactly one final `.docx` wireframe per run.

- If the user provides an output path, write only that file.
- If the user provides only an outline path, save one file in the same folder as the input using:
  `[Study Name] Survey Wireframe v0.1.docx`
- If that default path already exists, increment the version.
- Never create duplicate review copies such as `- Codex Version`.
- Do not leave extra `.docx` variants in the working folder.

Temporary text or JSON files are acceptable only if they are stored outside the user's deliverable
folder or removed after the build succeeds.

## Read only what you need

Read these first:

- `references/merck-format-spec.md`
- `references/transformation-patterns.md`
- `scripts/render_from_plan.py`

Use these when needed:

- `scripts/extract_docx_structure.py` to inspect the source `.docx` or verify the output structure
- `scripts/wireframe_builder.py` only if you need lower-level rendering behavior
- `scripts/check_environment.py` to verify that the local Python environment can build `.docx` files

If a local `seurat-brain` repo exists and is accessible, use it as supplemental context for brand
lists, category language, and prior question families. Do not block on Seurat context.

## Required environment check

Before drafting the output, run:

```powershell
python scripts/check_environment.py
```

If the environment check fails, stop and report the missing dependency clearly.

## Workflow

### 1. Resolve paths

Treat the first argument as the input outline path and the second argument, if present, as the
output path.

If the user did not provide an output path:

1. Inspect the outline title or use the input filename stem.
2. Build the default output name as `[Study Name] Survey Wireframe v0.1.docx`.
3. Save it in the same folder as the source outline.
4. If the filename already exists, increment the version number.

### 2. Inspect the source document

Extract the source document into a readable summary before drafting. Prefer:

```powershell
python scripts/extract_docx_structure.py "<outline.docx>" -o "<temp-summary.txt>"
```

From the source, identify:

- study title
- overall objectives
- respondent criteria and quotas
- section architecture
- rough question/topic bullets
- assignments, routing, and variable threading clues
- notes that should become programming guidance

### 3. Build the transformation map

Preserve the real study structure. Do not force a generic template when the outline uses a custom
architecture.

Draft aggressively:

- expand shorthand bullets into finished respondent-facing questions
- infer response options
- convert routing, assignments, and terminations into programming notes
- add transition messages when the flow needs them

### 4. Draft a render plan

Write a temporary JSON plan that matches `scripts/render_from_plan.py`.

Keep the plan client-ready:

- use the Merck three-column structure
- separate respondent copy from internal logic
- keep piped variables consistent
- include section headers, section objectives, messages, and questions

### 5. Render the wireframe

Use the deterministic renderer:

```powershell
python scripts/render_from_plan.py "<plan.json>" "<output.docx>"
```

### 6. Validate the result

Confirm the generated file:

- opens successfully
- has the expected section rows and column headers
- uses real Word list formatting in the overview
- includes visible question numbers
- reflects the source study structure

Use `scripts/extract_docx_structure.py` if needed for validation.

## Rendering principles

Always target the current client-facing Merck structure:

- `Q #`
- `Survey Question`
- `Question Objective`

Match the formatting rules in `references/merck-format-spec.md`.

When the source is sparse, prefer the usable wireframe over a literal but incomplete conversion.

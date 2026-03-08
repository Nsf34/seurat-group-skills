# Survey Outline Wireframe Plugin

Claude Code plugin for converting survey outlines and rough quant planning documents into a
client-facing survey wireframe `.docx` using the Merck three-column format.

## What this repo contains

- `.claude-plugin/plugin.json` - Claude plugin manifest
- `skills/survey-outline-to-wireframe/SKILL.md` - manual-invoked Claude skill
- `skills/survey-outline-to-wireframe/references/` - formatting and transformation rules
- `skills/survey-outline-to-wireframe/scripts/` - deterministic DOCX rendering helpers

## Requirements

- Claude Code with plugin support
- Python 3
- `python-docx`

Install Python dependency:

```powershell
pip install -r requirements.txt
```

## Local test

Run Claude Code with the plugin directory:

```powershell
claude --plugin-dir .
```

Then invoke the skill:

```text
/survey-outline-to-wireframe "C:\path\to\outline.docx"
```

Optional explicit output path:

```text
/survey-outline-to-wireframe "C:\path\to\outline.docx" "C:\path\to\output.docx"
```

## Output behavior

- Produces exactly one final `.docx` per run
- Uses the current Merck three-column client-facing structure
- Preserves study-specific section architecture
- Drafts missing questions aggressively when the outline is sparse

## Notes

- The plugin package is separate from any local Codex-only development copies.
- The renderer depends on a structured plan plus `python-docx`.
- The current version is designed for Claude Code / Cowork style environments with filesystem and
  Python access.

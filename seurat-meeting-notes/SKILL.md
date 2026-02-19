---
name: seurat-meeting-notes
description: Transform meeting transcripts into polished Seurat Group meeting notes documents. Use when asked to create meeting notes, process call transcripts, or generate notes from a meeting. Inputs include transcript, presentation deck content, and personal jotted notes. Outputs a properly formatted .docx with Next Steps, Key Takeaways, and Full Notes sections following Seurat Group standards.
---

# Seurat Meeting Notes

Transform raw meeting materials into polished, client-ready notes documents.

## Inputs Required

1. **Transcript** - Raw call transcript (required)
2. **Deck/Presentation** - Content being presented (if applicable)
3. **Personal Notes** - User's jotted notes highlighting important points (if available)

## Workflow

### Step 1: Gather Context

Before processing, ensure you have:
- Meeting title/type (e.g., "WSI Demand Spaces & Drivers", "Pre-WSII Alignment")
- Date of meeting
- Attendee names (Seurat team and client team)
- Client company name

If missing, ask the user.

### Step 2: Process Materials

Read all provided materials. Identify:
- **Who said what** - Distinguish Seurat team vs client comments
- **Key decisions/alignments** - What did they agree on?
- **Open questions** - What needs follow-up?
- **Action items** - Who committed to do what?

### Step 3: Extract Content (NOT repeat deck/presentation content)

Critical: Notes capture **what the client said and what emerged from discussion**, not what the Seurat team presented or explained.

**Read `references/content-quality.md` for detailed guidance on what makes content useful.**

**If `references/learned-preferences.md` has any entries, read it.** These are preferences extracted from user-refined notes and represent what the user actually wants. Where they conflict with the base rules, follow the learned preferences.

Extract:
- Client reactions to presented material
- Questions raised and how addressed (with underlying concerns)
- Agreements reached and rationale
- Concerns or pushback with specific examples
- Follow-up items with concrete deliverables

Apply the "So What" test: Every point should have clear implications for next steps or decisions.

**Content Quality Essentials:**
- **Synthesize** long discussions into consolidated actionable points
- **Capture underlying concerns**, not just surface questions
- **Preserve specific examples** (brand names, benefit language debated)
- **Quote key phrases** that resonated ("center of gravity", "band-aid approach")
- **Include rationale**, not just positions

Do NOT include:
- What the Seurat team presented or explained (definitions, methodology, data walkthrough)
- Facts already in the deck
- Background information or context from the presentation
- Descriptions of what spaces/concepts mean — this is known; capture reactions to them
- Raw data without interpretation
- "We discussed X" without the outcome
- "Team walked through X" or "Team explained X" — instead capture the client response

### Step 4: Generate Document

Use the docx skill to create a Word document. Read `references/format-guide.md` for detailed formatting rules.

#### Document Structure

```
**[Client] [Meeting Type] Notes [Date]**

Seurat Team: [names]
[Client] Team: [names]

**[Next Steps]{.underline}**
- **Team to** [action]
  - [sub-action details]
- **[Client] to** [action]

**[Key Takeaways]{.underline}**
- [Typically 5-8 bullets - adjust to meeting substance; selective bolding, full sentences]

**[Full Notes]{.underline}**
***[Topic 1]***
- [Discussion points with sub-bullets for responses]

***[Topic 2]***
- [Continue chronologically]
```

## Formatting Quick Reference

| Element | Format |
|---------|--------|
| Font | Franklin Gothic Book, 11pt throughout |
| Bullet spacing | Tight — no extra space between bullets |
| Section headers | Bold + underline |
| Topic headers (Full Notes) | Bold + italic |
| Action items | `**Name to** action...` |
| Key concepts | Selective bold within bullets |

## Key Principles

1. **Client-centric** - Notes are about what THEY said, asked, decided — not what Seurat presented
2. **Net new only** - Don't repeat deck content or explain what concepts/spaces mean
3. **Concise** - Sub-bullets max 3 lines; Key Takeaway main bullets max ~2 lines
4. **Actionable** - Clear owners for all next steps with specific deliverables
5. **Decisions over details** - Focus on what was AGREED/CHANGED/DECIDED
6. **Group related points** - Key Takeaways use sub-bullets for related facets under one theme
7. **Broader topic sections** - Full Notes use fewer, broader headers
8. **Chronological** - Full Notes follow meeting flow
9. **Don't assume formats** - Don't say "one-pager" or "slide" unless certain; use neutral language ("description", "language")

## Section-Specific Rules

### Next Steps

- Use **"Team to"** for Seurat actions (not "Seurat to")
- Use **"[Client] to"** for client actions (not "[Client] core team to")
- Do NOT list individual names in "[Client] to" bullets unless a specific person owns a distinct action
- Do NOT include specific meeting times
- Sub-bullets max 3 lines; aim for 1-2
- Cut sub-bullets that are purely informational with no action
- Each distinct workstream gets its own "Team to" bullet

### Key Takeaways

- Main bullets should be **short** — aim for ~1-2 lines
- Focus on: client reactions, decisions, tensions, strategic implications
- Do NOT recap what Seurat presented or explained
- Do NOT explain what concepts/spaces mean (that is presentation content, not a takeaway)
- Do NOT include methodological notes (e.g., "no statistical changes were made")
- Sub-bullets allowed for grouping related facets, but keep them tight

### Full Notes

- Capture what the **client** said, asked, reacted to — this is the core purpose
- Minimize or omit descriptions of what the Seurat team presented or walked through
- Client questions/comments get main bullets; Team responses get sub-bullets only when the response matters
- Broader topic headers that match discussion themes, not individual sub-topics

## Resources

- **Content Quality Guide**: `references/content-quality.md` - What makes content useful vs. filler (READ FIRST)
- **Format Guide**: `references/format-guide.md` - Detailed formatting rules and examples
- **Example Notes**: `references/example-notes.md` - Complete example document

## Output

Generate a .docx file with filename format:
`[Client Name] [Meeting Type] [External/Internal] [Date].docx`

Example: `Henkel WSI Demand Spaces & Drivers External 1.28.26.docx`

## Learning from Refined Notes

When the user uploads a refined/edited version of notes — or says they've adjusted the output and want the skill to learn — read `learning/LEARN.md` and follow the learning workflow.

**Trigger phrases:** "learn from these notes", "I edited the notes", "here's the final version", "train on this", "refine the skill", "I made some changes to the notes"

The learning workflow extracts preferences from the user's refinements and saves them to `references/learned-preferences.md`, which this skill reads during future note generation (see Step 3). This creates a feedback loop where each set of refined notes makes future outputs better.

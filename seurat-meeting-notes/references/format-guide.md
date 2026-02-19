# Seurat Group Meeting Notes Format Guide

## Typography & Spacing

- **Font**: Franklin Gothic Book, 11pt throughout the entire document
- **Bullet spacing**: Tight — no extra whitespace between bullets. Avoid large gaps. In docx-js, use `spacing: { after: 40 }` on bullets and `spacing: { after: 80 }` max for spacers between bullet groups. Do NOT use `spacing: { after: 200 }` or similar large values on bullets.

## Document Structure

### Title Line
Bold, format: `**[Client Name] [Meeting Type] Notes [Date]**`
- Example: `**Henkel WSI Demand Spaces & Drivers Notes 1.28**`
- Example: `**UNREAL Category Expansion Pre-WSII Alignment External 12.5.25**`

### Attendees
Immediately after title, list teams:
```
Seurat Team: [Names comma-separated]
[Client Name] Team: [Names comma-separated]
```
Use italic for the entire line if desired.

---

## Section 1: Next Steps

### Header
`**[Next Steps:]{.underline}**` or `**[Next Steps]{.underline}**`

### Format Rules
- Each responsible party gets a main bullet starting with **bolded name + "to"**
- Sub-bullets contain specific action items
- Order: Seurat/Team first, then client
- Use **"Team to"** for Seurat actions (never "Seurat to")
- Use **"[Client] to"** for client actions (never "[Client] core team to")
- Do NOT list individual names in "[Client] to" bullets unless a specific person owns a distinct action
- Do NOT include specific meeting times
- **Sub-bullets max 3 lines; aim for 1-2 lines**
- Cut sub-bullets that are purely informational with no action
- Each distinct workstream gets its own "Team to" bullet
- Don't assume document formats — use neutral language ("description", "language") not "one-pager" or "slide" unless certain

### Examples
```markdown
-   **Team to** update "Bring the Salon Home" description language
    -   Pull from key tensions and differentiators to sharpen distinctiveness
    -   Circulate updated deck ahead of Feb. 17 meeting

-   **Team to** begin working toward the next workshop on category vision

-   **Henkel to** regroup on Feb. 17 with Linda to align on current-state deliverables
```

---

## Section 2: Key Takeaways

### Header
`**[Key Takeaways:]{.underline}**` or `**[Key Takeaways]{.underline}**`

### Format Rules
- Typically 5-8 bullets (guideline, not rigid - adjust based on meeting substance)
- Each main bullet should be **short — aim for ~1-2 lines, max ~2.5 lines**
- Each bullet is a **complete sentence** (concise but full)
- **Selective bolding** of key concepts/phrases within bullets
- Sub-bullets allowed for additional depth or multiple related points, but keep tight
- Focus on AGREEMENTS, ALIGNMENTS, and KEY DECISIONS (not just what was said)
- Do NOT recap what Seurat presented or explained
- Do NOT explain what concepts/spaces mean (that is presentation content, not a takeaway)
- Do NOT include methodological notes (e.g., "no statistical changes were made")

### Bolding Patterns
Bold phrases that represent:
- Agreements: "**aligned that...**", "**directionally stronger**"
- Key concepts being discussed: "**brand permission**", "**trend-driven nature**"
- Contrasts or tensions: "**both a risk and a lever**"
- Named elements from the work: "**Let Curls Lead**", "**Fix What's Off**"

### Examples
```markdown
-   Henkel aligned that the **updated demand space names are directionally stronger** and reflect prior feedback well

-   Brand analysis reveals **Got2b has strongest positioning in Fix & Flourish, Elevated Expression, and Wear it Natural**; low equity in Hair Health Haven and Me Moment

-   **Cookies feel on-equity but emotionally and competitively trickier,** with Sophie probing how emotional challenges differ from chocolate

-   **Protein is seen as misaligned with Unreal's core of clean ingredients**, and the team is comfortable deprioritizing
```

---

## Section 3: Full Notes

### Header
`**[Full Notes:]{.underline}**` or `**[Full Notes]{.underline}**`

### Organization
- Chronological order following the meeting flow
- Organize by **topic headers** (italic+bold): `***Topic Name***`
- Topic headers should match deck sections or natural discussion breaks

### Format Rules
- **Capture what the CLIENT said, asked, reacted to** — this is the core purpose
- Minimize or omit descriptions of what the Seurat team presented or walked through
- Client questions/comments get main bullets
- Team responses get sub-bullets only when the response matters for the record
- Use broader topic headers that match discussion themes, not individual sub-topics
- Use "Client asked...", "Client noted...", "Mark flagged..." phrasing

### Example Structure
```markdown
***Demand Map Reactions***

-   Carlos noted Elevated Expression "works really well" and sees it as a strong fit for Got2b's equity

-   Carlos asked for clarity on the distinction between Hair Health Haven and Healthy Habits, stressing this will be critical for the broader team

-   Carlos noted the positioning of both health spaces makes sense with the health & wellness orientation

***Brand Mapping***

-   Carlos confirmed the center-of-gravity framing "really reinforces" the approach

-   Mark asked whether Henkel had coverage across all demand spaces; three spaces currently have no Henkel brands
    -   Mark noted this could generate "rich conversation" with the broader team
```

---

## Content Guidelines

### What to Include
- **Net new information** from the conversation
- Decisions made and rationale
- Questions raised and how they were addressed
- Action items with owners
- Key client reactions and concerns
- Agreements and alignments reached

### What to EXCLUDE
- Information already in the deck/presentation (don't repeat known facts)
- Small talk or off-topic conversation
- Redundant points (consolidate similar comments)
- Your own opinions or interpretations not from the meeting
- Raw data/index numbers unless directly actionable (e.g., don't include "381 index" unless it drives a decision)
- Process/timeline details in Key Takeaways (keep those in Full Notes)

### Key Principles for Quality Notes

**1. Client-centric content**
- Notes are about what the CLIENT said, asked, decided — not what Seurat presented
- Never recap presentation content, methodology, or definitions
- If a detail is about what we explained (not what they reacted to), omit it

**2. Key Takeaways: Short and grouped**
- Main bullets should be ~1-2 lines, max ~2.5
- If a topic has multiple facets, use ONE main bullet with sub-bullets
- Each main takeaway should represent a distinct theme or decision area

```markdown
-   Bring the Salon Home remains the **growth driver with the most internal tension;** Mark wants "evangelical fervor" from Linda
    -   Mindy surfaced that **Linda has negative connotations around "salon quality"**, possibly tied to caution around the pro business
```

**3. Full Notes: Prefer broader topic sections, client voice**
- Use fewer topic headers that match major discussion themes
- Main bullets = what the client said/asked; sub-bullets = team response (only when it matters)
- Only create a new topic header when discussion clearly shifts to a new subject

**4. Conciseness rules**
- Sub-bullets max 3 lines; aim for 1-2
- If a detail doesn't lead to a decision or action, omit it
- Don't assume document formats — use neutral language

### Capturing Client vs Team Attribution
- "Client" = the external company (Henkel, Unreal, etc.)
- "Team" = Seurat Group
- Use specific names when attribution matters: "**Sophie** is interested in..."

---

## File Naming Convention

Format: `[Client Name] [Meeting Type] [External/Internal] [Date].docx`

Examples:
- `Henkel WSI Demand Spaces & Drivers External 1.28.26.docx`
- `UNREAL Category Expansion Pre-WSII Alignment External 12.5.25.docx`

---

## Quick Reference: Formatting Markers

| Element | Format |
|---------|--------|
| Font | Franklin Gothic Book, 11pt throughout |
| Bullet spacing | Tight — no extra whitespace between bullets |
| Section headers | `**[Header:]{.underline}**` |
| Topic subheaders (Full Notes) | `***Topic Name***` |
| Seurat action items | `**Team to** action...` (never "Seurat to") |
| Client action items | `**[Client] to** action...` (never "[Client] core team to") |
| Key concepts in takeaways | `**bolded phrase**` |
| Quoted space/driver names | `"**Name**"` or just `"Name"` |
| Response/clarification | Indented sub-bullet |

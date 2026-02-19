# Learning from Refined Notes

When the user uploads a refined/edited version of meeting notes, follow this workflow to extract preferences and improve future outputs.

## Determine Mode

**Mode 1 — Diff-Based (preferred):** Use when both the AI-generated output AND the user's refined version are available. The AI output may be in the conversation history or provided as a separate file.

**Mode 2 — Style Analysis (fallback):** Use when only the user's refined version is available and the original AI output is not accessible.

Ask the user: "Do you have the original AI-generated version as well? Comparing both versions lets me learn more precisely."

---

## Mode 1: Diff-Based Learning

### Step 1: Extract the Diff

Compare the AI output with the user's refined version at the **semantic level** (not character-by-character). Identify:

- **Deletions** — Content the user removed entirely
- **Additions** — Content the user added that wasn't in the original
- **Rephrased content** — Same idea, different wording
- **Restructured sections** — Content moved or reorganized
- **Formatting changes** — Bolding, bullet structure, header changes

### Step 2: Categorize Each Change

For each meaningful change, classify it as one of:

| Category | Examples |
|----------|----------|
| Content inclusion | User added context the AI missed |
| Content exclusion | User removed presentation recap, methodology notes |
| Synthesis/phrasing | User condensed or reworded for clarity |
| Formatting/structure | User changed bullet nesting, bolding pattern |
| Tone/voice | User softened or sharpened language |
| Section-specific | Change applies only to Next Steps, Key Takeaways, or Full Notes |

### Step 3: Extract the Underlying Preference

For each change, ask: **What is the general rule this change implies?**

Do NOT extract surface-level observations. Go one level deeper:
- Surface: "User deleted the sentence about brand mapping methodology"
- Underlying: "User removes descriptions of what the team presented, preferring only client reactions and decisions"

Look for **patterns across multiple changes** in the same document. Three deletions of team-presentation content are one preference, not three.

### Step 4: Generate Before/After/Lesson Snippets

For the **2-4 most instructive changes**, create a snippet:

```
**Before (AI):** [exact text from AI output]
**After (User):** [exact text from refined version]
**Lesson:** [the distilled rule — one sentence]
```

Choose changes that best illustrate the preference. Skip trivial fixes (typos, minor word swaps).

### Step 5: Present to User for Confirmation

Show the user what you extracted:

> "I identified [N] meaningful changes. Here are the preferences I extracted:
>
> 1. **[Category]:** [preference description]
> 2. **[Category]:** [preference description]
> ...
>
> Should I save all of these? Any to adjust or remove?"

**Do NOT save anything until the user confirms.** This is critical — extracted preferences are interpretations of intent, and the user may have a different reason for a change than what was inferred.

### Step 6: Save

After confirmation:
1. Update `references/learned-preferences.md` — merge new preferences with existing ones (see Merge Rules below)
2. Append a session entry to `learning/changelog.md`
3. If a change warrants a longer example, save a snippet file in `learning/examples/`

---

## Mode 2: Style Analysis

### Step 1: Analyze the Refined Notes

Read the refined notes document thoroughly. Note:
- Document structure and section balance
- Bullet length and nesting depth
- Bolding patterns
- Vocabulary and tone
- What content is included vs. omitted
- How discussions are synthesized

### Step 2: Compare Against Skill Rules

Read `references/content-quality.md`, `references/format-guide.md`, and `references/learned-preferences.md` (if it exists). Identify where the refined document **deviates from or goes beyond** what these rules would produce.

Focus on:
- Things the document does that the rules don't mention
- Things the rules say to do but the document doesn't
- Patterns in the document that are more specific than the rules

### Step 3: Extract Preferences

Apply the same categorization as Mode 1 (content, formatting, tone, section-specific). Mark these as **lower confidence** since without the diff, you cannot distinguish what the user changed from what the AI already got right.

### Step 4: Present and Confirm

Same confirmation flow as Mode 1, but note the lower confidence:

> "Since I don't have the original AI version, these are my best interpretation of your preferences based on analyzing the document. Please review carefully:"

### Step 5: Save

Same as Mode 1 Step 6, but mark preferences with "(inferred — no diff available)" in the changelog.

---

## Merge Rules for `learned-preferences.md`

When updating the preferences file, follow these rules:

### Adding New Preferences
- Add to the appropriate category section
- Mark with confidence: "(seen in 1 session)" for first occurrence
- Include the client/meeting context if the preference might be situational

### Reinforcing Existing Preferences
- When a new preference matches an existing one, increment the session count
- If seen in 3+ sessions, remove the count marker — it is now established
- If the new instance adds nuance, update the preference description

### Handling Contradictions
- If a new preference contradicts an existing one, **do NOT silently overwrite**
- Flag it for the user: "This conflicts with an existing preference: [existing]. Which should I keep, or should both be kept with context about when each applies?"
- Client-specific preferences may appear contradictory but be correct for different contexts

### Managing File Size
- **Target: under 150 lines** for the preferences file
- When approaching 150 lines during a save, review for consolidation opportunities:
  - Merge preferences that express the same underlying rule
  - Graduate well-established preferences (5+ sessions) — propose moving them into `content-quality.md` or `format-guide.md` directly
  - Keep only the most illustrative Before/After snippet for each preference
  - Remove snippets whose lesson is already fully captured by the preference text
- When graduating a preference, note it in the changelog: "Graduated to [target file]: [preference]"

### Managing Examples Directory
- Soft cap of **5-7 files** in `learning/examples/`
- Each file should be 10-30 lines: a focused snippet demonstrating a specific pattern
- When adding a new example and the directory has 7+ files, remove the oldest or least-referenced one
- Reference example files by name in `learned-preferences.md` where appropriate

---

## Handling Multiple Documents at Once

When the user provides several refined documents in one session:

1. Process each document individually (using the appropriate mode)
2. After processing all, do a **cross-document consolidation pass**:
   - "Across these [N] documents, I see these consistent patterns: [list]"
   - "These changes appear situational (seen in only one document): [list]"
3. Let the user decide which situational changes to keep vs. skip
4. Save all confirmed preferences in a single update to `learned-preferences.md`
5. Log as one session in `changelog.md` with all source files noted

---

## Edge Cases

**Few changes detected:** If the diff is small (1-2 minor changes), acknowledge it: "Only [N] minor changes detected. The skill appears to be performing well for this type of meeting." Still extract preferences from those changes if they represent meaningful patterns.

**Client-specific preferences:** If the learning workflow detects that preferences differ by client, organize them with client context in `learned-preferences.md`: "For [Client] meetings: [preference]." The skill already tracks client name in Step 1, so it can apply client-specific preferences during generation.

**Ambiguous changes:** If a change could be interpreted multiple ways, ask the user rather than guessing: "You changed [X] to [Y] — was this because [interpretation A] or [interpretation B]?"

# Transformation Patterns

This reference captures how the example source documents become finished wireframes.

## Core Mechanism

The workflow is not a literal copy-edit. It is a structured expansion:

1. Read the source for study intent, sections, quotas, routing clues, and rough question ideas.
2. Infer the real survey flow.
3. Convert rough bullets into respondent-facing questions plus internal programming logic.
4. Preserve the study's section architecture.
5. Render the final output in the current Merck 3-column format.

## Source Types Seen In The Examples

### 1. Loose outline

Examples:
- Ocean Spray outline
- CCC outline

Typical characteristics:
- section names plus bullets
- respondent criteria and quotas
- "Thoughts" or analyst notes
- references to older studies or decks
- incomplete question wording
- response options missing or partial

Expected behavior:
- aggressively draft full questions
- infer realistic response options
- elevate routing/assignment logic into programming notes

### 2. Shell wireframe

Example:
- UNREAL shell

Typical characteristics:
- many sections already named
- some table structure already present
- rows may be sparse or empty
- objectives are often explicit
- question ideas may exist without finished wording

Expected behavior:
- preserve the section structure
- keep the intended logic
- rewrite into the current Merck client-facing format
- fill missing question text, options, and programming notes

## Example Pattern: Ocean Spray

Observed source behavior:
- bullets outline the full study arc
- section names resemble a path-to-purchase flow
- notes reference other studies for inspiration
- there are clues about assignments, segmentation, and barriers

Observed output behavior:
- screener becomes a formal qualification flow
- juice category bullets become multi-part purchase/usage questions
- rough brand/product bullets become assignment questions using `<brand>` and `<product>`
- light vs. super users become monitoring or assignment logic
- non-buyer barriers appear before termination

Mechanics to copy:
- turn category bullets into full grids when multiple timeframes are implied
- convert "assign brand" style bullets into explicit programming notes
- use follow-up questions when a bullet clearly implies a second stage

## Example Pattern: CCC

Observed source behavior:
- explicit objectives and respondent criteria
- named sections, but many question ideas are shorthand
- outlines advanced constructs: home barista typing, retailer assignment, Gabor-Granger

Observed output behavior:
- screener expands into a full qualification and assignment block
- product/segment bullets become 2-column or 3-column grid questions
- rough "attitudes" bullets become batteries and paired-statement questions
- retailer/shop bullets become grounded questions using `<retailer>`
- brand/pricing bullets become a staged Gabor-Granger flow

Mechanics to copy:
- when the outline implies assignment, define a variable and keep threading it
- when the outline names a construct like Gabor-Granger, build the actual survey sequence
- when bullets imply monitoring quotas, surface them in programming notes
- when a section is marked "light," keep it focused but still complete

## Example Pattern: UNREAL

Observed source behavior:
- more complete shell with objectives and thoughts
- non-standard section names tied to the project type
- category tailoring is central to the study

Observed output behavior:
- custom section names are preserved
- category assignment and tailoring are made explicit
- "Thoughts" bullets become finished questions about barriers, discovery, role of brand, and fit
- respondent paths bifurcate by category where needed

Mechanics to copy:
- preserve custom study architecture instead of flattening it into a generic template
- convert category-tailoring clues into programming notes or piped variables
- when the source says answer options differ by category, write that explicitly

## How To Treat Common Outline Signals

### "Thoughts:"

Treat these as high-value analyst intent.

Do:
- turn them into concrete questions
- decide whether each belongs in question copy, response options, or programming notes

Do not:
- copy "Thoughts:" text directly into respondent-facing copy

### "Look at prior survey / deck"

Treat this as a hint about:
- likely question families
- response frameworks
- wording direction

Do not:
- leave the output dependent on that missing external file

### Short bullets like "Brands they bought"

Expand into the most likely finished mechanic, for example:
- awareness + purchase + most recent grid
- single-select brand assignment
- retailer follow-up using assigned brand

### Quotas and sample notes

Move them into:
- overview quota bullets
- section objectives where relevant
- programming notes when they affect screening or monitoring

### Routing clues

Examples:
- "before termination"
- "show to non-buyers"
- "assign to parent or kid"
- "tailor by category"

These should become explicit programming notes. Do not leave routing implied.

## Drafting Heuristics

When the outline is sparse, prefer these decisions:
- make the question concrete
- make the response list realistic
- state the internal logic clearly
- preserve the original study structure

If a choice must be made between staying literal and producing a usable wireframe, choose the
usable wireframe.

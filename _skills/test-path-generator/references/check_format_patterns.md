# Test Path Check Format Patterns

Real examples from Seurat Group test plans. When in doubt about how to phrase a
check, find the closest matching pattern here and follow it exactly.

---

## Path Header
```
Path 1
```
(No colon. No extra descriptors. Just "Path N")

---

## Messages
```
M1: ensure message appears
M2: Ensure you see the message
M3: Ensure you see the message
M4: Ensure you see the message
Ensure <brand> <category> is piped through in message text
M5: Ensure you see the message text for <UNREAL buyer>
```

---

## Selection Instructions

**Select any:**
```
Select any
```

**Select any within a range:**
```
Select any response 18-55
Select any R5-R9
Select any R1-R2
```

**Select a specific response:**
```
Select R1 "Yes"
Select "No children under 18 living in my household"
Select R4: Challenging – breathing harder, noticeable sweat
```

**Select specific responses in a grid:**
```
Select C1, C2, and C3 for "Nerds Gummy Clusters," and "Better Sour"
Select C1 & C2 for all priority categories and any others
Select C1 & C2 for chocolate buyer
```

**Select any EXCEPT something:**
```
Select any except R5
Select any except R2
Select any except "I wouldn't be interested in any of these"
```

**Select a specific scale value for each statement:**
```
Select the following for each statement:
I find exercise enjoyable, not a chore - 3
I have a structured approach to managing my health and wellness - 2
I believe a healthy lifestyle can include occasional indulgences - 2
```

---

## Visibility Checks — Questions

**Question is conditionally shown and IS visible:**
```
Ensure you see the question
Ensure you see question text for <UNREAL buyer>
```

**Question is NOT visible for this path:**
```
Ensure you do not see the question
Ensure you don't see the question
```
(Both forms are acceptable — be consistent within a path)

---

## Visibility Checks — Response Options

**See specific response options:**
```
Ensure you see R3, "Kid(s) in my household"
Ensure you see R5 and R6
Ensure you see R12
Ensure you do see R11, R15, and R16
```

**Do NOT see specific response options:**
```
Ensure you do not see R5 and R6
Ensure you do not see R2, R4, R5, R6, R7, R9, R10, R11, and R13
Ensure you do not see R3, "Kid(s) in my household"
Ensure you don't see the question
```

---

## Piping Checks

**Piped through in question text:**
```
Ensure <brand><category> is piped through in question text
Ensure <category> is piped through in question text
Ensure "gummy candy" is piped through in question text
Ensure "gummy candy," "packaged cookies," "packaged brownies," "protein bars /
bites," "sweet cereal," "cereal bars," "non-chocolate non-gummy candy" are piped
through
```

**Piped through in response options:**
```
Ensure <brand> is piped through in R14 response option text
Ensure <category> is piped through in R9, R11, and R17 response text
Ensure response options selected in Q211 are piped through
```

**Piped through in columns:**
```
Ensure <brand><category> is piped through in question text and columns
```

**Category piped as bolded headers:**
```
Ensure question pipes through "gummy candy," "packaged cookies," "packaged brownies,"
"protein bars / bites," "sweet cereal," "cereal bars," "non-chocolate non-gummy
candy" as bolded headers
```

---

## Format / Question Type Checks

**Scale questions:**
```
Ensure question is a 10 point scale for each category
Ensure question is a 5 point agreement scale
Ensure question is a 4 point scale with one statement all the way to the left /
other all the way to the right
```

**Multi-select / single-select:**
```
Ensure multi select in C1 and C2
Ensure multi select in C1 and C2 and single select in C3
Ensure single select in C1 and C2
Ensure multi select in C1 and single select in C2
```

**Bolded/underlined text:**
```
Ensure "equally high-quality and clean ingredients" is underlined
Ensure "delicious," "real / simple ingredients," and "less sugar than conventional
alternatives," is bolded
Ensure "health and wellness?" is bolded
```

**Dropdown:**
```
Ensure "No children under 18 living in my household" is not a dropdown and
mutually exclusive
```

---

## Anchoring Checks

**Anchored at bottom, mutually exclusive:**
```
Ensure "None of the above" is anchored at the bottom and mutually exclusive
Ensure "I wouldn't be interested in any of these" is anchored to the bottom and
mutually exclusive
Ensure "Brand does not matter to me" is anchored to the top and mutually exclusive
Ensure "Prefer not to answer" is anchored at bottom and mutually exclusive
Ensure "No one else was there" is anchored to the top and mutually exclusive
Ensure "Emotions were not important" is anchored to the top and mutually exclusive
```

**Anchored at bottom, open-end:**
```
Ensure "Other; please specify" is anchored to the bottom and open-end
Ensure "Other, please specify" is anchored at bottom
```

---

## Grouping Checks
```
Ensure R2 and R3 are together
Ensure R4 and R5 are together
Ensure R5 and R6 are together
Ensure R8 and R9 are together
Ensure R11 and R12 are together
```

---

## Variable Assignment Checks
```
Ensure assigned <Kids in HH>
Ensure assigned <No kids in HH> is assigned
Ensure assigned <category quota> = "gummy candy"
Ensure assigned <brand> = "Nerds Gummy Clusters," and "Better Sour"
Ensure assigned <category> = "gummy candy"
Ensure <nerds gummy clusters> is assigned <brand type> = Mainstream
Ensure assigned <priority category> = "gummy candy," "packaged cookies,"
"packaged brownies," "protein bars / bites," "sweet cereal," "cereal bars,"
"non-chocolate non-gummy candy"
Ensure not assigned <non-buyer category 1> or <non-buyer category 2>
Ensure assigned <other category> for all other response options selected
Ensure assigned <Unreal aware>
Ensure assigned <Unreal buyer>
Ensure assigned <high interest category> based on up to 3 responses
```

---

## Loop Checks
```
Ensure all possible questions in Q201 – Q229 are looped up to two times for all
assigned <brand>
Ensure Q301 - Q302 is looped up to two times for all assigned <brand>
```

---

## Non-Buyer Question Checks
```
Ensure you see the question
Ensure <non-buyer category 1> and <non-buyer category 2> is piped through in
question text and the question cycles through twice
Ensure you see R20 and R21
```

---

## Key Formatting Rules

1. Question number on its own line with colon: `Q205:`
2. Each check on its own line — no blank lines between checks within one question
3. Blank line between question blocks
4. Selection instruction always LAST within a block
5. Variable names always in angle brackets: `<brand>`, `<category>`
6. Response options in double quotes when referenced: `"None of the above"`
7. Response numbers as R1, R2, R3... and column numbers as C1, C2, C3...
8. "Ensure" capitalized in all checks except the M1 message line
9. Scale descriptions use numbers separated by dashes: `3`, `5 point`
10. Never bullet-point the check lines — plain text only

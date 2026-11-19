# Packaging: titles, thumbnails, podcast episodes

Packaging (title + thumbnail) decides most outcomes. **Angle first, then the brief.**

## 1. Research the angle (never skip)

- Pull outliers for the topic: vidIQ `vidiq_outliers` (see `references/vidiq-playbook.md`), or `scripts/yt_snapshot.py` on 3-5 competitor channels, or a web search of YouTube results.
- Note what the top performers promise, and the angle **nobody** is taking. Zero results for an angle with a big audience is a virgin-territory signal, not a reason to drop it.
- Check `references/saturated-angles.md`.
- Kill test: *could anyone with AI write this angle?* If yes, dig deeper.

## 2. Podcast episodes: guest name or idea first?

| Guest | Lead with | Why |
|---|---|---|
| Big, widely known name | **The name**, plus a fresh spin on what they're known for | Podcasts are about 50% the guest. A famous name carries the click. |
| Not well known | **The idea**: a number, a confession, a conflict | Nobody clicks a name they don't know. Never lead with "Ft. [unknown guest]". |

Good packaging still lifts a big-name episode. Never rely on the name alone if there's a stronger idea in the conversation. Quote-style titles only after reading the transcript.

**No transcript yet?** Ask for it. Meanwhile, give angle-level titles with clear placeholders, e.g. `Ankur Warikoo: The [₹ figure from episode] Mistake Most 25-Year-Olds Make`, and list the moments to look for (a specific number, a regret, a disagreement with common advice). Never fill a placeholder with an invented number.

## 3. Write titles

- Write 5-8 options across different angles, then cut to the best 3.
- **Front-load the searchable keyword** when the video has search demand.
- **Match the brand register.** Premium or institutional brands use authoritative, lecture-style titles. Personality-led or founder-led channels can go louder. Clickbait the video doesn't deliver is banned (rule 10).
- **Number-led formula**, for money and business topics: a specific figure with full precision (₹4,73,000, not "lakhs"), an age or time period as a second hook, and bold high-contrast type on the thumbnail. It's different from a money-promise thumbnail ("₹10 Cr in 1 year"), which is saturated: the number has to be a fact from the video, not a promise to the viewer.
- Don't fact-check the hook into mush: keep the emotional and comparative logic.
- **Score:** with vidIQ, run `vidiq_score_title` on all variants in parallel. Compare only within one language: Hinglish scores lower than English by default. Scores are a signal, not a verdict. Never pick a higher score that bait-switches the content.

## 4. Grade the thumbnail: the 4Cs

| C | Question |
|---|---|
| **Clarity** | Readable in one second at phone size? |
| **Curiosity** | Opens a loop the title alone can't close? |
| **Controversy** | Takes a position? |
| **Conflict** | Visible tension in the image, not just information? |

A thumbnail doesn't need all four. **2 is the floor, 3-4 is the target. More Cs, better odds.** Clarity is the one to never trade away.

**Utility beats novelty:** the viewer should instantly see what's in it for them.

**Critique checklist:** face too small? No visual antagonist? No text overlay? Flat, centred composition? Background figures stealing focus (blur them, keep the story)? Text repeating the title instead of adding to it?

## 5. Designer brief (never generate the image)

```
Concept:     <one line: the story the thumbnail tells>
Subject:     <face/person, expression, size in frame>
Antagonist:  <the opposing element creating conflict, if any>
Text:        <2-4 words max, not repeating the title>
Layout:      <placement, contrast, background blur>
4Cs:         Clarity ✓ / Curiosity ✓ / Controversy ✗ / Conflict ✓  (3/4)
```

## Output

| # | Title | Angle | Language | Score (if any) | Pairs with |
|---|---|---|---|---|---|

Then: **Recommended pick + why**, and one designer brief per shortlisted concept.

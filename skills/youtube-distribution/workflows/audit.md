# Channel and video audit

Goal: one clear answer to "what do we do next week?", not a report to explore. **A windshield, not a rearview mirror.**

## 1. Get honest numbers

`python3 scripts/yt_snapshot.py @handle @competitor1 @competitor2`, or with vidIQ, `vidiq_channel_videos` with separate `long` and `short` calls and `popular: true`. Without either, ask for the last 20 videos' views and dates.

Read the output for:
- **Honest baseline**, per format: the median after stripping the top 10% and anything under 7 days old.
- **Likely-paid videos**: big views with under 0.2% likes. Exclude them from every judgement and say so. A brand whose "best" videos are all ads has no proven organic content.
- **Outliers (3x+) vs flops (0.3x or less)**: what's different about them? Look at topic, format, who's on screen, the title pattern and the language.
- **Cadence**: regular or random?

## 2. Diagnose in this order

| Symptom | Likely cause | Check |
|---|---|---|
| Most videos are about the company | The #1 founder mistake (SKILL.md) | Topic list of the last 20 videos |
| Low impressions | Topic has no audience, or no search or browse demand | Outliers for the topic, keyword data |
| Impressions fine, low CTR | Packaging | 4Cs, title vs outliers (`packaging.md`) |
| CTR fine, low retention | The video doesn't deliver the title, or the intro is slow | First 30 seconds against the promise |
| Shorts flat | Draw, standalone claim, topic fit | Pre-Upload Gate on the last 10 (`shorts.md`) |
| Spiky, then nothing | No IP or series to come back for | Is there a recurring format? |

CTR and retention come from YouTube Studio, which only the owner can see. Ask for screenshots instead of guessing.

## 3. Give the HOW

For every problem: **what to change, where, and to what.** "Fix the hook" fails. "Replace the 25-second logo intro with the ₹4.7L number at second 0" passes.

## 4. Compare with a peer

Run the snapshot on 1-2 brands in the same category, and put the winners and flops from every channel side by side. The pattern that wins across several channels is the category's truth, not one channel's luck. Use `references/examples.md` for Indian brand benchmarks.

Only call out the #1 founder mistake if the evidence shows it. Many channels have a different problem.

## Output

```
Verdict:        <one line>
Evidence:       baseline <x> (long) / <y> (Shorts); outliers: <titles + x>; flops: <titles + x>; paid excluded: <n>
Top 3 fixes:    1. <what → where → to what>  2. ...  3. ...
Next week:      <the one recommendation to approve or reject>
```

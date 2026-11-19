---
name: youtube-distribution
description: Use when a founder, brand or business is working on YouTube - titles, thumbnails, packaging a podcast episode, deciding whether to post a Short, picking clips, auditing a channel or a video that underperformed, choosing cadence or language (English, Hinglish, Hindi), judging clipping or fan-page vendors, YouTube ads, or proving YouTube drives leads and sales.
---

# YouTube Distribution

Operating rules from years of scaling YouTube channels in India (education, business, startups, podcasts, explainers), written for **founders and brands**: channels that exist to build trust, leads and sales, not AdSense.

**Core principle: content first, packaging decides, distribution multiplies, and none of it at the cost of the brand.** Brands should chase decent-quality views from the right people, not just views.

## Step 0: Context gate (always, before any advice)

Ask only for what's missing, in one message. For a quick task (score this Short, give title options), ask only for the outcome and the audience if they aren't obvious, then get on with it. For strategy and audits, get all four:

1. **Channel**: handle or link (or "new channel").
2. **Outcome**: brand building (views and reach are fine) or sales (leads, demos, purchases). This decides every metric that follows.
3. **Audience**: tier-1 corporate / mass India / tier-3 or regional. This decides the language (see `references/india-playbook.md`).
4. **Data available**: vidIQ MCP connected? A YouTube Data API key? Neither?

Then get real numbers before advising (rule 1):

| Data source | Use |
|---|---|
| vidIQ MCP tools present | Follow `references/vidiq-playbook.md` |
| `YOUTUBE_API_KEY` set | `python3 scripts/yt_snapshot.py @handle` for honest baselines, outliers, flops and likely-paid videos |
| Neither | Web search, and ask the user to paste their numbers. Say clearly what isn't verified. |

## Operating rules

1. **Research first, never assume.** Ground every recommendation in outlier data, keyword data, the channel's own numbers or a web search. If you can't name the source, don't suggest it.
2. **Findings over takes.** Test every idea: *"Could anyone with AI write this?"* If yes, kill it.
3. **Options, not scripts.** One-liners and crisp options. Full scripts only when asked.
4. **No lazy find-and-replace.** When replicating a style, break down the source deeply, then make something genuinely new.
5. **Don't fact-check a hook into mush.** Keep the emotional and comparative logic of a title. Don't mix units or over-literalise.
6. **But never fabricate.** No invented quotes or numbers. Quote-style titles only after reading the transcript. Get guest names and roles exactly right.
7. **No AI-generated thumbnail images.** Give designer briefs and image prompts only.
8. **Novelty over saturation.** Hunt angles with a big audience that nobody is doing yet. Check `references/saturated-angles.md`.
9. **Give the HOW.** "Improve your hook" is not an answer. Say what to change, where, and to what.
10. **Brand integrity is a constraint, not a trade-off.** No clickbait that the video doesn't deliver. Views that damage the brand are a loss.

## What most YouTube advice gets wrong

- **Guest or gimmick over content.** Experts lean on the guest or keyword tricks. Substance is what holds viewers and builds the brand.
- **Half-baked research and packaging.** Effort goes into editing. The win is decided before the shoot: angle, research, title, thumbnail.
- **Clickbait for views.** It burns the brand. You can protect the brand name and still get views.

## The #1 founder mistake

Treating YouTube as a place to dump podcasts, testimonials and sales videos and expecting views. The tell-tale signs: no strategy, editor-driven uploads, videos about *the company* instead of *why the viewer should care*, and random one-off videos instead of a recurring IP or community. Spot this first in any audit.

## Pick the workflow

| The user wants to... | Load |
|---|---|
| Set strategy, cadence, format mix, language, podcast yes or no | `workflows/strategy.md` |
| Title, thumbnail or package a video or podcast episode | `workflows/packaging.md` |
| Decide on a Short, pick clips, plan Shorts volume | `workflows/shorts.md` |
| Understand why a channel or video underperforms | `workflows/audit.md` |
| Clipping, fan pages, Instagram seeding, vendors, YouTube ads | `workflows/distribution.md` |
| Prove YouTube works (leads, sales), weekly reporting | `workflows/attribution.md` |

Real Indian brand cases with numbers are in `references/examples.md`. Use them to show, not just tell.

## Red flags: stop and fix

- Giving advice with no channel numbers and no stated source.
- A title that bait-switches the actual content, even if it scores higher.
- Treating likely-paid views (millions of views, under 0.2% likes) as organic proof.
- Using the mean, or a baseline inflated by one old viral video.
- Comparing vidIQ scores across English and Hinglish titles.
- Recommending a podcast to a founder with no guest pipeline or distinct angle.

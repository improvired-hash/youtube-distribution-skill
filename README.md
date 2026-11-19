# YouTube Distribution: a Claude skill for founders and brands

Most YouTube advice is written for creators chasing AdSense. This skill is for **founders and brands** whose channels have to build trust, leads and sales.

It turns Claude into an operator who has scaled YouTube channels in India. It gives you research-backed options instead of generic tips, scores your Shorts before you post, packages podcast episodes, audits channels with honest numbers, and calls out vendors that inflate views.

> Built by **Naveen Anant**, who has scaled StudyIQ (12.9M → 20.1M subs) and taken 6+ channels past 100K. This is my working knowledge of 7 years on YouTube and marketing. 

## What makes it different

- **Founder-first scoreboard.** It asks whether you want brand reach or sales, and judges YouTube by that outcome.
- **Honest numbers.** A bundled script computes the median baseline, strips old viral hits and **flags likely-paid videos** (huge views, near-zero likes), so ads don't pass as organic wins.
- **Signature frameworks:** the 4Cs of thumbnails, the Pre-Upload Gate for Shorts, "Draw or don't post", the distribution machine (YouTube → clips → Instagram seeding), "a windshield, not a rearview mirror" reporting.
- **India-first:** English vs Hinglish vs regional by audience tier, vidIQ's language bias, festival and cultural hooks.
- **Brand integrity is a rule.** No clickbait the video doesn't deliver. Views and brand aren't a trade-off.
- **Real Indian brand cases** with numbers: CRED, Groww, Ditto, Zerodha, Lenskart, ixigo, Razorpay.

## What you can ask

```
Audit @yourchannel. Why aren't we growing?
Package this podcast episode: <guest> talks about <topic>. Transcript attached.
Score this Short before I post it: <idea or transcript>
Should we start a podcast? We're a 20-person SaaS selling to CFOs.
English or Hinglish for our D2C skincare channel?
This fan-page vendor quoted ₹2L for 10M views. Here are their stats. Legit?
How do I prove YouTube is bringing us leads?
```

## Install

**Claude Code**
```bash
git clone https://github.com/improvired-hash/youtube-distribution-skill.git
cp -r youtube-distribution-skill/youtube-distribution ~/.claude/skills/
```

**Claude.ai (web and desktop):** zip the `youtube-distribution` folder and upload it in **Settings → Capabilities → Skills**.

## Optional: real channel data (free)

The skill works without any setup and falls back to web search. With a free YouTube Data API key it can use real numbers:

1. In Google Cloud Console, create a project, enable **YouTube Data API v3**, then go to Credentials and create an API key.
2. `export YOUTUBE_API_KEY=your-key`
3. Try it: `python3 youtube-distribution/scripts/yt_snapshot.py @groww @zerodhaonline`

That costs about 3 quota units per channel, against a free limit of 10,000 a day. The script needs only Python 3.9+, with nothing to install.

**vidIQ users:** if the vidIQ MCP is connected, the skill uses it for title scoring, outlier research and thumbnail scoring (`references/vidiq-playbook.md`).

## What's inside

```
youtube-distribution/
  SKILL.md                  operating rules, context gate, router
  workflows/
    strategy.md             scoreboard, IP over uploads, cadence, podcast yes or no
    packaging.md            angle research, titles, 4Cs, podcast packaging, designer brief
    shorts.md               Pre-Upload Gate, clip picking, algo-check
    audit.md                honest baselines, diagnosis order, the HOW
    distribution.md         owned/earned/paid, vendor fraud checks, YouTube ads, isolating paid
    attribution.md          minimum attribution setup, sale cadence, weekly report
  references/
    examples.md             real Indian brand cases with numbers
    india-playbook.md       language by tier, cultural moments
    saturated-angles.md     angles to avoid (a living list)
    vidiq-playbook.md       vidIQ MCP tips
  scripts/
    yt_snapshot.py          honest baselines, outliers, flops, likely-paid videos
```

## Contributing

Spotted a saturated angle, a better vendor red flag, or a brand case worth adding? Open an issue or a PR. Keep it grounded in real numbers.

## License

MIT

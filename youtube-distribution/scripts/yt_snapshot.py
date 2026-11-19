#!/usr/bin/env python3
"""Channel snapshot with honest baselines. Free YouTube Data API key, no installs.

    YOUTUBE_API_KEY=... python3 yt_snapshot.py @zerodhaonline [@another ...]
    python3 yt_snapshot.py @handle --json        # machine-readable

For each channel: subscribers, upload cadence, honest median baselines
(long-form and Shorts kept separate), outliers (3x+), underperformers
(0.3x or less), like rates, and likely-paid videos (big views, near-zero likes),
which are kept out of baselines so ads don't fake the channel's real reach. About 3 quota units per channel; the free
quota is 10,000 a day.

Honest baseline = median views of videos at least 7 days old, with the
top 10% stripped, so one old viral hit doesn't set the bar.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from statistics import median

API = "https://www.googleapis.com/youtube/v3/"
SHORT_MAX_SECONDS = 180
OUTLIER_X = 3.0
UNDER_X = 0.3
MIN_AGE_DAYS = 7
PAID_LIKE_RATE = 0.2      # % likes per view; ads get huge views and almost no likes
PAID_MIN_VIEWS = 10_000


def key():
    k = os.environ.get("YOUTUBE_API_KEY") or os.environ.get("YT_API_KEY")
    if not k:
        sys.exit("Set YOUTUBE_API_KEY (free: Google Cloud Console > enable YouTube Data API v3 > Credentials > API key).")
    return k


def call(endpoint, **params):
    params["key"] = key()
    url = API + endpoint + "?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "yt-snapshot"}), timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:300]
        if e.code == 403 and "quota" in body.lower():
            sys.exit("Daily YouTube API quota used up. It resets at midnight Pacific time.")
        raise ValueError(f"YouTube API error {e.code} on {endpoint}")


def seconds(iso):
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m:
        return 0
    d, h, mi, s = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + s


def channel(ref):
    if ref.startswith("UC") and len(ref) == 24:
        res = call("channels", part="snippet,statistics,contentDetails", id=ref)
    else:
        res = call("channels", part="snippet,statistics,contentDetails", forHandle="@" + ref.lstrip("@"))
    if not res.get("items"):
        raise ValueError(f"Channel not found: {ref}")
    return res["items"][0]


def honest_baseline(views):
    if len(views) < 5:
        return None
    views = sorted(views)
    keep = views[: max(5, int(len(views) * 0.9))]   # strip the top 10%
    return int(median(keep))


def snapshot(ref):
    ch = channel(ref)
    uploads = ch["contentDetails"]["relatedPlaylists"]["uploads"]
    ids = [i["contentDetails"]["videoId"] for i in
           call("playlistItems", part="contentDetails", playlistId=uploads, maxResults=50).get("items", [])]
    vids = call("videos", part="snippet,statistics,contentDetails", id=",".join(ids)).get("items", []) if ids else []
    now = datetime.now(timezone.utc)
    rows = []
    for v in vids:
        sn, st = v["snippet"], v.get("statistics", {})
        if sn.get("liveBroadcastContent") in ("live", "upcoming"):
            continue
        secs = seconds(v["contentDetails"].get("duration"))
        views = int(st.get("viewCount", 0))
        likes = int(st["likeCount"]) if "likeCount" in st else None
        pub = datetime.fromisoformat(sn["publishedAt"].replace("Z", "+00:00"))
        rows.append({"id": v["id"], "title": sn["title"], "published": pub.date().isoformat(),
                     "age_days": (now - pub).days, "format": "short" if 0 < secs <= SHORT_MAX_SECONDS else "long",
                     "duration": secs, "views": views, "likes": likes,
                     "like_rate": round(likes / views * 100, 2) if likes is not None and views else None})
        r = rows[-1]
        r["likely_paid"] = bool(views >= PAID_MIN_VIEWS and r["like_rate"] is not None and r["like_rate"] < PAID_LIKE_RATE)
    out = {"channel": ch["snippet"]["title"], "handle": ch["snippet"].get("customUrl", ref),
           "subscribers": int(ch["statistics"].get("subscriberCount", 0)) if not ch["statistics"].get("hiddenSubscriberCount") else None,
           "total_videos": int(ch["statistics"].get("videoCount", 0)), "formats": {}}
    for fmt in ("long", "short"):
        paid = [r for r in rows if r["format"] == fmt and r["likely_paid"]]
        fr = [r for r in rows if r["format"] == fmt and not r["likely_paid"]]
        if not fr and not paid:
            continue
        base = honest_baseline([r["views"] for r in fr if r["age_days"] >= MIN_AGE_DAYS])
        allf = fr + paid
        span_days = max((max(r["age_days"] for r in allf) - min(r["age_days"] for r in allf)), 1)
        for r in fr:
            r["x"] = round(r["views"] / base, 2) if base else None
        rates = [r["like_rate"] for r in fr if r["like_rate"] is not None]
        out["formats"][fmt] = {
            "videos_in_sample": len(allf),
            "per_week": round(len(allf) / span_days * 7, 1),
            "likely_paid": sorted(paid, key=lambda r: -r["views"]),
            "honest_baseline_views": base,
            "median_like_rate_pct": round(median(rates), 2) if rates else None,
            "outliers": sorted([r for r in fr if r["x"] and r["x"] >= OUTLIER_X], key=lambda r: -r["x"]),
            "underperformers": sorted([r for r in fr if r["x"] is not None and r["x"] <= UNDER_X
                                       and r["age_days"] >= MIN_AGE_DAYS], key=lambda r: r["x"]),
            "videos": fr,
        }
    return out


def num(n):
    if n is None:
        return "-"
    return f"{n / 1e6:.1f}M" if n >= 1e6 else f"{n / 1e3:.1f}K" if n >= 1e3 else str(n)


def print_md(s):
    print(f"## {s['channel']} ({s['handle']}): {num(s['subscribers'])} subs\n")
    for fmt, f in s["formats"].items():
        label = "Long-form" if fmt == "long" else "Shorts"
        print(f"**{label}**: {f['videos_in_sample']} recent uploads, {f['per_week']}/week, "
              f"honest baseline {num(f['honest_baseline_views'])} views (organic), median like rate {str(f['median_like_rate_pct']) + '%' if f['median_like_rate_pct'] is not None else 'hidden'}"
              + (f", {len(f['likely_paid'])} likely-paid videos excluded" if f["likely_paid"] else "") + "\n")
        for name, key_ in (("Outliers (3x+)", "outliers"), ("Underperformers (0.3x or less)", "underperformers"),
                           ("Likely paid (excluded from baseline)", "likely_paid")):
            rows = f[key_][:8]
            if rows:
                print(f"{name}:\n\n| x | views | like % | date | title |\n|---|---|---|---|---|")
                for r in rows:
                    print(f"| {r.get('x', '-')} | {num(r['views'])} | {r['like_rate'] if r['like_rate'] is not None else 'hidden'} | {r['published']} | {r['title'][:90]} |")
                print()


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    snaps = []
    for a in args:
        try:
            snaps.append(snapshot(a))
        except ValueError as e:
            print(f"> skipped {a}: {e}\n", file=sys.stderr)
    if "--json" in sys.argv:
        print(json.dumps(snaps, indent=1, ensure_ascii=False))
    else:
        for s in snaps:
            print_md(s)

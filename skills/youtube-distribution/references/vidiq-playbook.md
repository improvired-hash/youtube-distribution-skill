# vidIQ MCP playbook

Load only when vidIQ MCP tools are available in the session.

| Tool | How to use it well |
|---|---|
| `vidiq_score_title` | Set `type: "long"` for long-form. Pass a channel handle or `videoId` for context. Run variants in parallel. Scores above ~95 cluster, so break ties on brand fit and accuracy. |
| `vidiq_outliers` | Add a `userGoal` describing the **angle**, not just a keyword. Use a `minViews` floor of 50K-100K depending on how saturated the topic is. **Zero results = virgin-territory signal.** |
| `vidiq_channel_videos` | Separate calls for `long` and `short`, with `popular: true`. Some tools need the `UC…` channel ID instead of the @handle: get stats by handle first, grab the ID, then reuse it. |
| `vidiq_score_thumbnail` | Needs an HTTPS image URL. Local files fail. |
| `vidiq_get_images` | With `resolution: full`, read competitor thumbnail text and layout. |
| `vidiq_instagram_tiktok_outlier_search` | Write a natural-language scenario as `query`, plus a structured `audienceQuery` (`Culture/Region: X; Global: true/false; Demographics: Y`). Use `excludeCreatorHandles` to strip affiliate spam. Run region and global searches in parallel. Trust the outlier multiple over raw views. |

## Language bias

vidIQ scores English titles above Hinglish for India content. **Compare scores only within one language, never across.** A Hinglish title scoring 78 can beat an English one scoring 90 for a mass-India audience.

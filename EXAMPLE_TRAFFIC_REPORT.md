# Example Traffic Report

This is an example of what the traffic report looks like when you run `check_traffic.py`.

## Sample Output

```
===========================================================================
Repository Traffic for christophergaughan/antibody-glycosylation-penetrance
===========================================================================

⚠️  Warning: No GITHUB_TOKEN found in environment.
   Some data may not be available without authentication.
   Set token with: export GITHUB_TOKEN='your_token'

📊 VIEWS (Last 14 days)
   Total views: 342
   Unique visitors: 47

   Daily breakdown:
   2026-01-30: 28 views (6 unique)
   2026-01-29: 41 views (12 unique)
   2026-01-28: 35 views (9 unique)
   2026-01-27: 19 views (4 unique)
   2026-01-26: 52 views (8 unique)
   2026-01-25: 31 views (5 unique)
   2026-01-24: 24 views (3 unique)

📦 CLONES (Last 14 days)
   Total clones: 18
   Unique cloners: 9

   Daily breakdown:
   2026-01-30:  3 clones (2 unique)
   2026-01-29:  2 clones (1 unique)
   2026-01-28:  1 clones (1 unique)
   2026-01-27:  4 clones (2 unique)
   2026-01-26:  1 clones (1 unique)
   2026-01-25:  5 clones (1 unique)
   2026-01-24:  2 clones (1 unique)

🔗 TOP REFERRING SITES
   1. google.com (87 views, 23 unique)
   2. reddit.com/r/bioinformatics (45 views, 12 unique)
   3. twitter.com (28 views, 8 unique)
   4. github.com (19 views, 6 unique)
   5. linkedin.com (14 views, 4 unique)

📁 POPULAR CONTENT
   1. /README.md (156 views, 34 unique)
   2. /ALL_Data_penetrance_itr2_2_GitHub.ipynb (89 views, 21 unique)
   3. /x_residue_penetrance_20260127.png (67 views, 18 unique)
   4. /melo_braga_vs_validation_20260127.png (45 views, 15 unique)
   5. /LICENSE (23 views, 8 unique)

===========================================================================
SUMMARY
===========================================================================
Approximately 46 people (other than you) have viewed
this repository in the last 14 days.

Note: GitHub only retains traffic data for 14 days.
      Run this script regularly to track long-term trends.

```

## Interpreting the Results

Based on this example report:
- **47 unique visitors** in the last 14 days
- **Subtracting yourself** = ~46 other people have viewed your repository
- Most traffic came from **Google** (87 views from 23 unique visitors)
- The **README.md** is the most popular page (156 views)
- **18 people cloned** your repository (actually downloaded it)

## Real-Time Check

To get your actual numbers right now:
1. Go to: https://github.com/christophergaughan/antibody-glycosylation-penetrance/graphs/traffic
2. Or run: `python check_traffic.py` (requires GITHUB_TOKEN)

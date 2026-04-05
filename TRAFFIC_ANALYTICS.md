# Repository Traffic Analytics

This guide shows you how to check how many people have viewed your GitHub repository.

## Quick Answer via GitHub Web UI

The easiest way to see repository traffic is through GitHub's web interface:

1. Go to your repository: https://github.com/christophergaughan/antibody-glycosylation-penetrance
2. Click on **Insights** (top navigation bar)
3. Click on **Traffic** in the left sidebar

You'll see:
- **Views**: Total number of views and unique visitors (last 14 days)
- **Clones**: Number of times the repository was cloned (last 14 days)
- **Referring sites**: Where your traffic is coming from
- **Popular content**: Which files/paths are most viewed

## Using the GitHub API

For programmatic access, use the included `check_traffic.py` script:

```bash
python check_traffic.py
```

### Setup

1. Create a GitHub Personal Access Token:
   - Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Click "Generate new token (classic)"
   - Give it a name like "repo-traffic"
   - Select the `repo` scope (grants read/write access to code, commit statuses, pull requests, and repository traffic)
   - Click "Generate token"
   - Copy the token (you won't see it again!)

2. Set your token as an environment variable:
   ```bash
   export GITHUB_TOKEN="your_token_here"
   ```

3. Run the script:
   ```bash
   python check_traffic.py
   ```

### What Data is Available?

GitHub's Traffic API provides:
- **Views**: Last 14 days of traffic data
  - Total views
  - Unique visitors
  - Daily breakdown
- **Clones**: Last 14 days of clone data
  - Total clones
  - Unique cloners
  - Daily breakdown
- **Popular paths**: Most visited pages/files
- **Referring sites**: Top referrers

### Limitations

⚠️ **Important**: GitHub only retains traffic data for the past 14 days. If you want historical data, you'll need to:
- Run the script regularly (daily/weekly) and save the results
- Use a third-party service (like Google Analytics for GitHub Pages)
- Check the Insights tab regularly and take screenshots

## Manual Check (No Script Needed)

If you don't want to use the API or script:

1. Navigate to: https://github.com/christophergaughan/antibody-glycosylation-penetrance/graphs/traffic
2. You'll see graphs showing:
   - Views per day
   - Unique visitors per day
   - Top referrers
   - Popular content

This is only available to repository owners/collaborators, so others won't be able to see this data.

## Understanding the Metrics

- **Views**: Every time someone loads a page in your repository (including you!)
- **Unique Visitors**: Count of distinct users who viewed your repository
- **Clones**: Number of times someone used `git clone` on your repository
- **Unique Cloners**: Count of distinct users who cloned your repository

To answer "how many people other than me have looked at this repository?":
- Take the "Unique Visitors" count
- Subtract 1 (yourself)
- Note: This only covers the last 14 days

## Example Output

When you run `check_traffic.py`, you'll see something like:

```
Repository Traffic for christophergaughan/antibody-glycosylation-penetrance
===========================================================================

📊 VIEWS (Last 14 days)
   Total views: 127
   Unique visitors: 23
   
   Daily breakdown:
   2026-01-30: 15 views (5 unique)
   2026-01-29: 22 views (8 unique)
   ...

📦 CLONES (Last 14 days)
   Total clones: 12
   Unique cloners: 7
   
🔗 TOP REFERRING SITES
   1. google.com (45 views)
   2. reddit.com (12 views)
   ...

📁 POPULAR CONTENT
   1. /README.md (78 views)
   2. /ALL_Data_penetrance_itr2_2_GitHub.ipynb (34 views)
   ...
```

Based on this, approximately **22 people other than you** have viewed your repository in the last 14 days (23 unique visitors - 1 for yourself).

#!/usr/bin/env python3
"""
GitHub Repository Traffic Checker

This script retrieves traffic statistics for the antibody-glycosylation-penetrance repository.
It shows views, clones, referrers, and popular content from the last 14 days.

Usage:
    export GITHUB_TOKEN="your_github_token"
    python check_traffic.py

Requirements:
    - requests library (install with: pip install requests)
    - A GitHub Personal Access Token with 'repo' scope
"""

import os
import sys
from datetime import datetime
import json

try:
    import requests
except ImportError:
    print("Error: 'requests' library not found.")
    print("Install it with: pip install requests")
    sys.exit(1)


class GitHubTrafficChecker:
    """Check GitHub repository traffic statistics."""
    
    def __init__(self, owner, repo, token=None):
        self.owner = owner
        self.repo = repo
        self.token = token or os.environ.get('GITHUB_TOKEN')
        self.base_url = f"https://api.github.com/repos/{owner}/{repo}"
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
        }
        if self.token:
            self.headers['Authorization'] = f'token {self.token}'
    
    def _get(self, endpoint):
        """Make a GET request to the GitHub API."""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                print("❌ Authentication failed. Please check your GITHUB_TOKEN.")
                print("   Create a token at: https://github.com/settings/tokens")
                print("   Make sure to select 'repo' scope.")
            elif e.response.status_code == 403:
                print("❌ Access forbidden. The token might not have the 'repo' scope.")
            elif e.response.status_code == 404:
                print("❌ Repository not found or you don't have access to view traffic.")
            else:
                print(f"❌ HTTP Error: {e}")
            return None
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    def get_views(self):
        """Get view statistics for the last 14 days."""
        return self._get("traffic/views")
    
    def get_clones(self):
        """Get clone statistics for the last 14 days."""
        return self._get("traffic/clones")
    
    def get_referrers(self):
        """Get top referrers."""
        return self._get("traffic/popular/referrers")
    
    def get_popular_paths(self):
        """Get popular content paths."""
        return self._get("traffic/popular/paths")
    
    def print_report(self):
        """Print a comprehensive traffic report."""
        print("=" * 75)
        print(f"Repository Traffic for {self.owner}/{self.repo}")
        print("=" * 75)
        print()
        
        if not self.token:
            print("⚠️  Warning: No GITHUB_TOKEN found in environment.")
            print("   Some data may not be available without authentication.")
            print("   Set token with: export GITHUB_TOKEN='your_token'")
            print()
        
        # Views
        print("📊 VIEWS (Last 14 days)")
        views_data = self.get_views()
        if views_data:
            print(f"   Total views: {views_data.get('count', 0)}")
            print(f"   Unique visitors: {views_data.get('uniques', 0)}")
            print()
            
            if views_data.get('views'):
                print("   Daily breakdown:")
                for view in views_data['views'][-7:]:  # Last 7 days
                    date = view['timestamp'][:10]
                    count = view['count']
                    uniques = view['uniques']
                    print(f"   {date}: {count:3d} views ({uniques} unique)")
                print()
        else:
            print("   Unable to retrieve views data.")
            print()
        
        # Clones
        print("📦 CLONES (Last 14 days)")
        clones_data = self.get_clones()
        if clones_data:
            print(f"   Total clones: {clones_data.get('count', 0)}")
            print(f"   Unique cloners: {clones_data.get('uniques', 0)}")
            print()
            
            if clones_data.get('clones'):
                print("   Daily breakdown:")
                for clone in clones_data['clones'][-7:]:  # Last 7 days
                    date = clone['timestamp'][:10]
                    count = clone['count']
                    uniques = clone['uniques']
                    print(f"   {date}: {count:3d} clones ({uniques} unique)")
                print()
        else:
            print("   Unable to retrieve clones data.")
            print()
        
        # Referrers
        print("🔗 TOP REFERRING SITES")
        referrers = self.get_referrers()
        if referrers and len(referrers) > 0:
            for i, ref in enumerate(referrers[:10], 1):
                print(f"   {i}. {ref['referrer']} ({ref['count']} views, {ref['uniques']} unique)")
            print()
        else:
            print("   No referrer data available or no external referrers.")
            print()
        
        # Popular paths
        print("📁 POPULAR CONTENT")
        paths = self.get_popular_paths()
        if paths and len(paths) > 0:
            for i, path in enumerate(paths[:10], 1):
                print(f"   {i}. {path['path']} ({path['count']} views, {path['uniques']} unique)")
            print()
        else:
            print("   No popular path data available.")
            print()
        
        # Summary
        print("=" * 75)
        print("SUMMARY")
        print("=" * 75)
        if views_data:
            unique_visitors = views_data.get('uniques', 0)
            others = max(0, unique_visitors - 1)  # Subtract yourself
            print(f"Approximately {others} people (other than you) have viewed")
            print(f"this repository in the last 14 days.")
            print()
            print("Note: GitHub only retains traffic data for 14 days.")
            print("      Run this script regularly to track long-term trends.")
        print()


def main():
    """Main entry point."""
    # Repository details
    OWNER = "christophergaughan"
    REPO = "antibody-glycosylation-penetrance"
    
    # Check for token
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print("⚠️  No GITHUB_TOKEN found in environment variables.")
        print()
        print("To get full traffic data, you need a GitHub Personal Access Token:")
        print("1. Go to: https://github.com/settings/tokens")
        print("2. Click 'Generate new token (classic)'")
        print("3. Select 'repo' scope")
        print("4. Generate and copy the token")
        print("5. Run: export GITHUB_TOKEN='your_token_here'")
        print()
        response = input("Continue without token? (y/n): ")
        if response.lower() != 'y':
            sys.exit(0)
        print()
    
    # Create checker and print report
    checker = GitHubTrafficChecker(OWNER, REPO, token)
    checker.print_report()


if __name__ == "__main__":
    main()

import requests
from urllib.parse import urlparse

GITHUB_API = "https://api.github.com"

def parse_pr_url(pr_url: str):
    parts = urlparse(pr_url).path.strip("/").split("/")
    owner, repo, _, pr_number = parts
    return owner, repo, pr_number

def fetch_pr(owner, repo, pr_number):
    pr_api = f"{GITHUB_API}/repos/{owner}/{repo}/pulls/{pr_number}"
    diff_url = pr_api + ".diff"

    pr_data = requests.get(pr_api).json()
    diff_text = requests.get(diff_url).text

    return {
        "title": pr_data["title"],
        "body": pr_data.get("body", ""),
        "base_repo": pr_data["base"]["repo"]["clone_url"],
        "base_branch": pr_data["base"]["ref"],
        "diff": diff_text
    }
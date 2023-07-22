import datetime
import time

import requests
from dateutil.parser import parse


def list_github_issues(org: str, repo: str, per_page=100, page=1):
    url = f"https://api.github.com/repos/{org}/{repo}/issues?page={page}&per_page={per_page}&state=closed"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "Bearer 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",
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        # An error occured
        raise Exception(f"GET {url} {response.status_code}")

    return response.json()


def get_lifetime(issue):
    if issue["closed_at"] is None:
        return datetime.datetime.now().replace(tzinfo=None) - parse(issue["created_at"]).replace(tzinfo=None)

    return parse(issue["closed_at"]) - parse(issue["created_at"])


def main():
    lifetime_array = []
    page = 1
    repo = "pytype"
    org = "google"

    issues = list_github_issues(org, repo, page=page)
    while issues:
        for issue in issues:
            lifetime_array.append(get_lifetime(issue).total_seconds())

        page += 1
        print(page)
        issues = list_github_issues(org, repo, page=page)

    mean_seconds = round(sum(lifetime_array) / len(lifetime_array))

    print("Seconds", mean_seconds)
    minutes = mean_seconds // 60
    print("Minutes", minutes)
    hours = minutes // 60
    print("Hours", hours)
    days = hours // 24
    print("Days", days)
    weeks = days // 7
    print("Weeks", weeks)
    years = weeks // 52
    print("Years", years)


if __name__ == "__main__":
    main()

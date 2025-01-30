import requests
import os

# Use GitHub Secrets for repo details
OWNER = os.getenv("REPO_OWNER")
REPO = os.getenv("REPO_NAME")

def get_contributors(owner, repo):
    """Fetch contributors from GitHub API."""
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        contributors = response.json()
        leaderboard = [
            {
                "username": contributor["login"],
                "contributions": contributor["contributions"],
                "avatar_url": contributor["avatar_url"]
            }
            for contributor in contributors
        ]
        return sorted(leaderboard, key=lambda x: x["contributions"], reverse=True)
    else:
        print(f"Failed to fetch contributors: {response.status_code}")
        return []

def generate_html(leaderboard):
    """Generate leaderboard.html for GitHub Pages."""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Leaderboard</title>
        <style>
            body {{
                background: linear-gradient(0deg, #1b2838, #1e3a4c, #1f4c60, #16202b);
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 20px;
            }}
            table {{
                width: 80%;
                margin: 20px auto;
                border-collapse: collapse;
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
            }}
            th, td {{
                padding: 10px;
                border: 1px solid white;
            }}
            .avatar {{
                width: 40px;
                height: 40px;
                border-radius: 50%;
                margin-right: 10px;
                vertical-align: middle;
            }}
        </style>
    </head>
    <body>
        <h1>Leaderboard for {}</h1>
        <table>
            <thead>
                <tr>
                    <th>Rank</th>
                    <th>Contributor</th>
                    <th>Contributions</th>
                </tr>
            </thead>
            <tbody>
    """.format(REPO)

    for rank, contributor in enumerate(leaderboard, start=1):
        html += """
                <tr>
                    <td>{}</td>
                    <td><img src="{}" class="avatar"> {}</td>
                    <td>{}</td>
                </tr>
        """.format(rank, contributor["avatar_url"], contributor["username"], contributor["contributions"])

    html += """
            </tbody>
        </table>
    </body>
    </html>
    """
    return html

def save_html_to_file(html, filename="leaderboard.html"):
    """Save HTML to file."""
    with open(filename, "w") as file:
        file.write(html)

def update_readme(leaderboard):
    """Update README.md with the Top 5 contributors."""
    top_5 = leaderboard[:5]
    markdown = f"# {REPO} Top 5 Contributors\n\n"
    markdown += "| Rank | Contributor | Contributions |\n"
    markdown += "|------|-------------|----------------|\n"
    for rank, contributor in enumerate(top_5, start=1):
        markdown += (
            f"| {rank} | <img src='{contributor['avatar_url']}' width='20' height='20'> {contributor['username']} | {contributor['contributions']} |\n"
        )

    with open("README.md", "w") as file:
        file.write(markdown)

if __name__ == "__main__":
    print(f"Generating leaderboard for {OWNER}/{REPO}...")
    leaderboard = get_contributors(OWNER, REPO)
    if leaderboard:
        save_html_to_file(generate_html(leaderboard))
        update_readme(leaderboard)
        print("✅ Leaderboard updated successfully.")
    else:
        print("❌ No contributors found or failed to retrieve data.")

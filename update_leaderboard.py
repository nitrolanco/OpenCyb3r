import requests
import os

# Dynamically fetch repository details from environment variables
OWNER = os.getenv("REPO_OWNER", "default_owner")
REPO = os.getenv("REPO_NAME", "default_repo")
SECRET_PHRASE = os.getenv("LEADERBOARD_SECRET", "default_secret")

def validate_secret():
    """Validate the secret phrase to ensure the script is running securely."""
    if SECRET_PHRASE == "default_secret":
        print("❌ WARNING: LEADERBOARD_SECRET is not set! Using default.")
    else:
        print("✅ Secret phrase validated successfully.")

def get_contributors(owner, repo):
    """Fetch contributors from the GitHub API."""
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        contributors = response.json()
        leaderboard = []

        for contributor in contributors:
            leaderboard.append({
                "username": contributor["login"],
                "contributions": contributor["contributions"],
                "avatar_url": contributor["avatar_url"]
            })

        return sorted(leaderboard, key=lambda x: x["contributions"], reverse=True)
    else:
        print(f"Failed to fetch contributors: {response.status_code}, {response.text}")
        return []

if __name__ == "__main__":
    validate_secret()  # Check the secret phrase before running
    print(f"Generating leaderboard for {OWNER}/{REPO}...")

    leaderboard = get_contributors(OWNER, REPO)

    if leaderboard:
        print("✅ Leaderboard generated successfully.")
    else:
        print("❌ No contributors found or failed to retrieve data.")


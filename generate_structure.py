import requests
import os
import shutil

USERNAME = "your-github-username"

def fetch_repos():
    url = f"https://api.github.com/users/{USERNAME}/repos"
    response = requests.get(url)
    return response.json()

def clean_old_folders(repos):
    existing_dirs = [d for d in os.listdir() if os.path.isdir(d)]

    repo_names = [repo["name"] for repo in repos]

    for d in existing_dirs:
        if d not in repo_names and d != ".github":
            shutil.rmtree(d)

def create_repo_folder(repo):
    name = repo["name"]
    desc = repo["description"] or "No description"
    stars = repo["stargazers_count"]
    url = repo["html_url"]
    language = repo["language"]

    os.makedirs(name, exist_ok=True)

    content = f"# {name}\n\n"
    content += f"{desc}\n\n"
    content += f"🔗 Repo: {url}\n\n"
    content += f"⭐ Stars: {stars}\n\n"
    content += f"🛠 Language: {language}\n"

    with open(f"{name}/README.md", "w", encoding="utf-8") as f:
        f.write(content)

def generate_main_readme(repos):
    content = "# 🚀 My Projects\n\n"
    content += "Auto-generated project directory:\n\n"

    for repo in repos:
        if repo["fork"]:
            continue

        name = repo["name"]
        desc = repo["description"] or "No description"

        content += f"## 📁 {name}\n"
        content += f"{desc}\n\n"
        content += f"👉 [Open Folder](./{name})\n\n---\n\n"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

def main():
    repos = fetch_repos()

    # optional: remove forks
    repos = [r for r in repos if not r["fork"]]

    clean_old_folders(repos)

    for repo in repos:
        create_repo_folder(repo)

    generate_main_readme(repos)

if __name__ == "__main__":
    main()

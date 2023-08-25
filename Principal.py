import os
import subprocess

def create_project_structure():
    project_structure = [
        "data/cleaned",
        "data/raw",
        "docs",
        "models",
        "notebooks",
        "reports",
        "src"
    ]

    for directory in project_structure:
        os.makedirs(directory, exist_ok=True)

    with open("LICENSE", "w") as f:
        pass

    with open("Makefile", "w") as f:
        pass

    with open("notebooks/main.ipynb", "w") as f:
        pass

    with open("README.md", "w") as f:
        pass

    with open("requirements.txt", "w") as f:
        pass

    with open("src/utils.py", "w") as f:
        pass

def initialize_git_repo():
    subprocess.run(["git", "init"])

def add_and_commit_files():
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Initial commit"])

def create_remote_repo():
    # Replace 'your_username', 'your_token', and 'your_repo_name' with actual values
    subprocess.run([
        "curl",
        "-u",
        "your_username:your_token",
        "https://api.github.com/user/repos",
        "-d",
        '{"name":"your_repo_name"}'
    ])

def push_to_remote():
    subprocess.run(["git", "remote", "add", "origin", "https://github.com/your_username/your_repo_name.git"])
    subprocess.run(["git", "push", "-u", "origin", "master"])

if __name__ == "__main__":
    create_project_structure()
    initialize_git_repo()
    add_and_commit_files()
    create_remote_repo()
    push_to_remote()

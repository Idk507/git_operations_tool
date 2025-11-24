# Git Operations Tool

[![PyPI version](https://badge.fury.io/py/git-operations-tool.svg)](https://test.pypi.org/project/git-operations-tool/)
[![Python versions](https://img.shields.io/pypi/pyversions/git-operations-tool.svg)](https://pypi.org/project/git-operations-tool/)
[![License](https://img.shields.io/pypi/l/git-operations-tool.svg)](https://opensource.org/licenses/MIT)
[![CI/CD](https://github.com/Idk507/git-operations-tool/actions/workflows/test.yml/badge.svg)](https://github.com/Idk507/git-operations-tool/actions) 

A comprehensive, interactive command-line interface (CLI) for managing Git repositories. This tool simplifies common Git workflows, making it easier to manage branches, commits, tags, remotes, and pull requests without memorizing complex Git commands.

## Features

### 🚀 Core Operations
- **Auto Commit & Push**: Automatically stage, commit, and push all changes with a single command. Supports bulk commits or individual file commits.
- **Interactive Add & Push**: Select specific files to stage and commit from a list of changed files. Perfect for granular commits.
- **Safe Pushing**: Built-in retry logic and safety checks to handle network interruptions or non-fast-forward updates gracefully.

### 🌿 Branch Management
- **Create & Checkout**: Easily create new branches and switch between them.
- **List Branches**: View all local and remote branches.
- **Merge & Delete**: Merge branches into the current branch or delete old branches.

### 🏷️ Tag & Release Management
- **Manage Tags**: Create lightweight or annotated tags for releases (e.g., `v1.0.0`).
- **Push Tags**: Push tags to the remote repository.
- **Delete Tags**: Remove tags locally and from the remote.

### 🌐 Remote Management
- **Manage Remotes**: Add, list, and remove remote repositories (e.g., `origin`, `upstream`) directly from the tool.

### 🤝 Collaboration
- **Pull Requests**: Create GitHub pull requests directly from the CLI (requires GitHub Personal Access Token).

### 📊 Insights & Logs
- **Status Dashboard**: View the current status of your repository (modified, staged, untracked files).
- **Commit Logs**: View the commit history.
- **Visual Graph**: Visualize the commit history tree with a graph view (`git log --graph`).

## Installation

You can install the tool directly from PyPI:

```bash
pip install git-operations-tool
```

## Usage

After installation, simply run the tool from your terminal within a Git repository (or it will prompt you to clone/init one):

```bash
git-ops
```

### Main Menu Options

1.  **Auto commit and push all files**: Quickest way to save everything.
2.  **Interactive Add & Push**: Select specific files to commit.
3.  **Create branch**: Create a new branch from the current HEAD.
4.  **List branches**: See all local and remote branches.
5.  **Checkout branch**: Switch to another branch.
6.  **Delete branch**: Remove a branch.
7.  **Merge branch**: Merge another branch into your current one.
8.  **Pull changes**: Update your local branch from the remote.
9.  **Push changes**: Push your local commits to the remote.
10. **Show status**: See what's changed in your working directory.
11. **Show commit log**: View recent commit history.
12. **Show graph log**: View a visual graph of the commit tree.
13. **Create pull request**: Open a PR on GitHub.
14. **Stash changes**: Temporarily save changes.
15. **Apply stash**: Restore stashed changes.
16. **Manage Tags**: Submenu for creating, listing, and deleting tags.
17. **Manage Remotes**: Submenu for adding or removing remotes.
18. **Exit**: Close the tool.

## Development

To contribute or run from source:

1. Clone the repository:
   ```bash
   git clone https://github.com/Idk507/git_operations_tool.git
   cd git-operations-tool
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the tool:
   ```bash
   python main.py
   ```

4. Run tests:
   ```bash
   python -m unittest discover tests
   ```

## License

MIT License - See [LICENSE](LICENSE) for details.

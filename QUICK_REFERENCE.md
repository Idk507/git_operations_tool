# Git Operations Tool - Quick Reference Guide

## All 18 Features at a Glance

### 🚀 Quick Start
```bash
cd git_operation_tool/git_operations_tool
python main.py
```

---

## Feature Reference

### 1️⃣ Auto Commit and Push All Files
**What it does**: Automatically commits and pushes all changes  
**Options**: 
- Bulk commit (all in one)
- Single file commits (separate commits for each file)
**Use when**: You have many files to commit

---

### 2️⃣ Create Branch
**What it does**: Creates a new Git branch  
**Prompts**: Branch name  
**Use when**: Starting new feature or fix

---

### 3️⃣ List Branches
**What it does**: Shows all local and remote branches  
**Output**: 
- Local branches (current marked with *)
- Remote branches
**Use when**: Need to see available branches

---

### 4️⃣ Checkout Branch
**What it does**: Switches to a different branch  
**Prompts**: Branch name  
**Smart features**:
- Checks out existing local branch
- Creates from remote if exists
- Creates new if doesn't exist
**Use when**: Switching between branches

---

### 5️⃣ Delete Branch
**What it does**: Deletes a branch  
**Prompts**: Branch name  
**Safety**: Cannot delete current branch  
**Use when**: Cleaning up old branches

---

### 6️⃣ Merge Branch
**What it does**: Merges another branch into current  
**Prompts**: Branch name to merge  
**Use when**: Integrating changes from another branch

---

### 7️⃣ Pull Changes
**What it does**: Downloads changes from remote  
**Prompts**: Branch name (default: main)  
**Use when**: Getting latest updates from remote

---

### 8️⃣ Push Changes
**What it does**: Uploads your commits to remote  
**Prompts**: Branch name (default: current)  
**Use when**: Sharing your changes with team

---

### 9️⃣ Show Status
**What it does**: Shows current repository state  
**Output**:
- Current branch
- Modified files
- Staged files
- Untracked files
**Use when**: Checking what's changed

---

### 🔟 Show Commit Log
**What it does**: Displays commit history  
**Prompts**: Number of commits (default: 10)  
**Output**: Hash, author, date, message  
**Use when**: Reviewing recent changes

---

### 1️⃣1️⃣ Create Pull Request
**What it does**: Creates a GitHub pull request  
**Prompts**:
- PR title
- PR description
- Head branch (your changes)
- Base branch (default: main)
- GitHub token
**Requirements**: GitHub repository  
**Use when**: Ready to merge changes on GitHub

---

### 1️⃣2️⃣ Stash Changes
**What it does**: Temporarily saves uncommitted changes  
**Use when**: Need to switch branches but not ready to commit

---

### 1️⃣3️⃣ Apply Stash
**What it does**: Restores previously stashed changes  
**Use when**: Ready to continue work on stashed changes

---

### 1️⃣4️⃣ Create Tag ⭐ NEW
**What it does**: Creates a Git tag  
**Prompts**:
- Tag name
- Tag message (optional)
**Use when**: Marking releases or important commits

---

### 1️⃣5️⃣ List Tags ⭐ NEW
**What it does**: Shows all repository tags  
**Output**: List of all tags  
**Use when**: Viewing available versions/releases

---

### 1️⃣6️⃣ Push Tags ⭐ NEW
**What it does**: Uploads all tags to remote  
**Use when**: Sharing tags with team/publishing releases

---

### 1️⃣7️⃣ Delete Tag ⭐ NEW
**What it does**: Removes a tag locally and remotely  
**Prompts**: Tag name  
**Use when**: Removing incorrect or old tags

---

### 1️⃣8️⃣ Exit
**What it does**: Closes the application  
**Use when**: Done with Git operations

---

## Common Workflows

### 🔄 Starting New Feature
1. **Create branch** (option 2)
2. Make your changes
3. **Show status** (option 9) to verify
4. **Auto commit and push** (option 1)

### 🔀 Merging Feature
1. **Checkout branch** (option 4) to main
2. **Pull changes** (option 7) to get latest
3. **Merge branch** (option 6) your feature
4. **Push changes** (option 8)

### 🏷️ Creating Release
1. **Show commit log** (option 10) to verify
2. **Create tag** (option 14) with version
3. **Push tags** (option 16) to publish

### 🚨 Emergency Branch Switch
1. **Stash changes** (option 12)
2. **Checkout branch** (option 4) to other branch
3. Do urgent work
4. **Checkout branch** (option 4) back
5. **Apply stash** (option 13)

### 📊 Checking Status
1. **Show status** (option 9) - current state
2. **List branches** (option 3) - available branches
3. **Show commit log** (option 10) - recent history
4. **List tags** (option 15) - versions

---

## Tips & Tricks

### 💡 Best Practices
- Always **pull** before starting work
- Use **status** frequently to track changes
- Create **tags** for releases
- Use **stash** instead of committing incomplete work
- **List branches** to avoid duplicates

### ⚠️ Common Mistakes to Avoid
- Don't delete the current branch
- Don't forget to push tags after creating them
- Don't merge without pulling first
- Don't create PR without pushing branch first

### 🎯 Power User Tips
- Use **auto commit** with single-file mode for detailed history
- Create **tags** with messages for better documentation
- Use **stash** when switching contexts quickly
- Check **status** before and after operations

---

## Keyboard Shortcuts (Menu Navigation)

Just type the number and press Enter:
- `1` - Auto commit
- `2` - Create branch
- `3` - List branches
- ... and so on
- `18` - Exit

---

## Error Messages

### Common Errors & Solutions

**"Cannot delete current branch"**
→ Checkout to different branch first

**"Pull requests are only supported for GitHub"**
→ Only works with GitHub repositories

**"GitHub token is required"**
→ Need Personal Access Token for PR creation

**"No tags found"**
→ Repository has no tags yet, create one!

---

## Version Information

**Current Version**: 0.4.1  
**New in 0.4.1**:
- ⭐ Tag management (create, list, push, delete)
- 🎯 18 total features (was 14)
- 🧹 Clean codebase structure

---

## Need Help?

- Check **STATUS_REPORT.md** for current status
- Check **IMPLEMENTATION_VERIFICATION.md** for technical details
- Check **README.md** for installation and setup

---

**Happy Git Operations! 🚀**

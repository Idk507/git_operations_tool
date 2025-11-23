from datetime import datetime
import time

class GitOperations:
    def __init__(self, repo):
        self.repo = repo
        
    def pull_changes(self, branch='main'):
        """Pull changes from remote repository"""
        try:
            origin = self.repo.remote('origin')
            origin.pull(branch)
            print(f"Pulled changes from remote/{branch}")
            return True
        except Exception as e:
            print(f"✗ Error pulling changes: {str(e)}")
            return False

    def push_changes(self, branch=None):
        """Push changes to remote repository"""
        try:
            if branch is None:
                branch = self.repo.active_branch.name
            
            origin = self.repo.remote('origin')
            origin.push(refspec=f'{branch}:{branch}')
            print(f"Pushed changes to remote/{branch}")
            return True
        except Exception as e:
            print(f"✗ Error pushing changes: {str(e)}")
            return False

    def show_status(self):
        """Show repository status"""
        try:
            print(f"\nRepository Status:")
            print(f"Current branch: {self.repo.active_branch.name}")
            
            # Show modified files
            modified_files = [item.a_path for item in self.repo.index.diff(None)]
            if modified_files:
                print(f"Modified files: {', '.join(modified_files)}")
            
            # Show staged files
            staged_files = [item.a_path for item in self.repo.index.diff("HEAD")]
            if staged_files:
                print(f"Staged files: {', '.join(staged_files)}")
            
            # Show untracked files
            untracked_files = self.repo.untracked_files
            if untracked_files:
                print(f"Untracked files: {', '.join(untracked_files)}")
            
            if not modified_files and not staged_files and not untracked_files:
                print("Working directory clean")
            
            return True
        except Exception as e:
            print(f"✗ Error showing status: {str(e)}")
            return False

    def show_log(self, limit=10):
        """Show commit log"""
        try:
            print(f"\nCommit Log (last {limit} commits):")
            commits = list(self.repo.iter_commits(max_count=limit))
            
            for commit in commits:
                print(f"Commit: {commit.hexsha[:8]}")
                print(f"Author: {commit.author.name} <{commit.author.email}>")
                print(f"Date: {datetime.fromtimestamp(commit.committed_date)}")
                print(f"Message: {commit.message.strip()}")
                print("-" * 50)
            
            return True
        except Exception as e:
            print(f"✗ Error showing log: {str(e)}")
            return False

    def stash_changes(self):
        """Stash current changes"""
        try:
            self.repo.git.stash('push', '-m', f'Stash created at {datetime.now()}')
            print("Changes stashed")
            return True
        except Exception as e:
            print(f"✗ Error stashing changes: {str(e)}")
            return False

    def apply_stash(self):
        """Apply latest stash"""
        try:
            self.repo.git.stash('pop')
            print("Stash applied")
            return True
        except Exception as e:
            print(f"✗ Error applying stash: {str(e)}")
            return False
import sys
import os
import time

# Add the parent directory to sys.path to allow running as a script
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from git import Repo, InvalidGitRepositoryError
from git_operations_tool.core.repository import RepositoryManager
from git_operations_tool.core.branches import BranchManager
from git_operations_tool.core.operations import GitOperations
from git_operations_tool.core.pull_requests import PullRequestManager
from git_operations_tool.core.tags import TagManager
from git_operations_tool.core.remotes import RemoteManager
from git_operations_tool.interface.prompts import get_repo_url
from git_operations_tool.interface.menu import MenuSystem

class GitOperationsTool:
    def __init__(self):
        self.repo_manager = RepositoryManager()
        self.branch_manager = None
        self.operations = None
        self.pr_manager = None
        self.tag_manager = None
        self.remote_manager = None
        self.menu = None
        
    def auto_commit_and_push(self):
        """Auto commit and push with options for bulk or individual commits"""
        print("\nAnalyzing repository status...")
        
        try:
            if not self.repo_manager.repo.is_dirty() and not self.repo_manager.repo.untracked_files:
                print("✓ Repository is already clean - no changes to commit.")
                return
        except Exception as e:
            print(f"Warning: Could not check repository status: {str(e)}")
        
        print("Discovering files and folders...")
        items = self.repo_manager.get_all_files_and_folders()

        if not items:
            print("No files or folders found to commit.")
            return

        print(f"Found {len(items)} items to process:")
        for i, (item_type, item_path) in enumerate(items[:10]):
            print(f"  - {item_type}: {item_path}")
        if len(items) > 10:
            print(f"  ... and {len(items) - 10} more items")

        print("\nCommit Mode Options:")
        print("1. Bulk commit (all changes in one commit)")
        print("2. Single file commits (each file separately)")

        while True:
            mode_choice = input("\nSelect commit mode (1-2): ").strip()
            if mode_choice in ['1', '2']:
                break
            print("Invalid choice. Please enter 1 or 2.")

        if mode_choice == '1':
            print("\nBulk Commit Mode: All changes will be committed together.")
            confirm = input("Do you want to proceed? (y/N): ").strip().lower()
            if confirm != 'y':
                print("Operation cancelled.")
                return
            if self.repo_manager.commit_all_changes("Bulk commit: Add all files"):
                if self.repo_manager.push_to_remote_with_retry():
                    print("✓ Successfully committed and pushed all changes.")
                else:
                    print("✗ Failed to push changes to remote.")
            else:
                print("✗ Failed to commit changes.")
        else:
            print(f"\nSingle File Commit Mode: This will create {len(items)} separate commits.")
            delay = 1.5
            try:
                delay_input = input("Enter delay between commits in seconds (default: 1.5): ").strip()
                if delay_input:
                    delay = float(delay_input)
                    if delay < 0:
                        delay = 0
            except ValueError:
                print("Invalid delay value. Using default delay of 1.5 seconds.")

            confirm = input(
                f"Do you want to proceed with {delay} seconds delay between commits? (y/N): ").strip().lower()
            if confirm != 'y':
                print("Operation cancelled.")
                return

            print(f"\nProcessing {len(items)} items...")
            success_count = 0
            failed_items = []
            for i, (item_type, item_path) in enumerate(items, 1):
                print(f"\n[{i}/{len(items)}] Processing {item_type}: {item_path}")
                if self.repo_manager.commit_and_push_item_with_retry(item_type, item_path):
                    success_count += 1
                else:
                    failed_items.append((item_type, item_path))
                if i < len(items) and delay > 0:
                    print(f"Waiting {delay} seconds before next commit...")
                    time.sleep(delay)

            print(f"\nSummary:")
            print(f"  - Successfully processed: {success_count}/{len(items)} items")
            print(f"  - Failed: {len(failed_items)}/{len(items)} items")

    def run(self):
        """Main application loop"""
        print("Git Operations Tool")
        print("=" * 50)
        
        # Get repository URL and initialize
        repo_url = get_repo_url()
        
        try:
            self.repo_manager.initialize_or_clone_repo(repo_url)
            self.branch_manager = BranchManager(self.repo_manager.repo)
            self.operations = GitOperations(self.repo_manager.repo)
            self.pr_manager = PullRequestManager(self.repo_manager.repo, repo_url)
            self.tag_manager = TagManager(self.repo_manager.repo)
            self.remote_manager = RemoteManager(self.repo_manager.repo)
            self.menu = MenuSystem(self)
        except Exception as e:
            print(f"✗ Error initializing repository: {str(e)}")
            sys.exit(1)
        
        # Main menu loop
        while True:
            self.menu.show_menu()
            
            try:
                choice = input("\nEnter your choice (1-18): ").strip()
                if not self.menu.handle_choice(choice):
                    break
                    
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user.")
                break
            except Exception as e:
                print(f"✗ Error: {str(e)}")

def run_tool():
    """Entry point for the console script"""
    tool = GitOperationsTool()
    tool.run()
    
if __name__ == "__main__":
    tool = GitOperationsTool()
    tool.run()

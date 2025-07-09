import sys
from git import Repo, InvalidGitRepositoryError
from git_operations_tool.core.repository import RepositoryManager
from git_operations_tool.core.branches import BranchManager
from git_operations_tool.core.operations import GitOperations
from git_operations_tool.core.pull_requests import PullRequestManager
from git_operations_tool.interface.prompts import get_repo_url
from git_operations_tool.interface.menu import MenuSystem
import time 

class GitOperationsTool:
    def __init__(self):
        self.repo_manager = RepositoryManager()
        self.branch_manager = None
        self.operations = None
        self.pr_manager = None
        self.menu = None
        
    def auto_commit_and_push(self):
        """Auto commit and push all files individually"""
        print("\nDiscovering files and folders...")
        items = self.repo_manager.get_all_files_and_folders()
        
        if not items:
            print("No files or folders found to commit.")
            return
        
        print(f"Found {len(items)} items to process:")
        for item_type, item_path in items:
            print(f"  - {item_type}: {item_path}")
        
        # Confirm before proceeding
        print(f"\nThis will create {len(items)} separate commits and push them one by one.")
        confirm = input("Do you want to proceed? (y/N): ").strip().lower()
        
        if confirm != 'y':
            print("Operation cancelled.")
            return
        
        # Process each item
        print(f"\nProcessing {len(items)} items...")
        success_count = 0
        
        for i, (item_type, item_path) in enumerate(items, 1):
            print(f"\n[{i}/{len(items)}] Processing {item_type}: {item_path}")
            
            if self.repo_manager.commit_and_push_item(item_type, item_path):
                success_count += 1
            
            # Small delay between operations
            if i < len(items):
                time.sleep(0.5)
        
        # Summary
        print(f"\nSummary:")
        print(f"  - Successfully processed: {success_count}/{len(items)} items")
        print(f"  - Failed: {len(items) - success_count}/{len(items)} items")

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
            self.menu = MenuSystem(self)
        except Exception as e:
            print(f"✗ Error initializing repository: {str(e)}")
            sys.exit(1)
        
        # Main menu loop
        while True:
            self.menu.show_menu()
            
            try:
                choice = input("\nEnter your choice (1-14): ").strip()
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


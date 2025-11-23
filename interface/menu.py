class MenuSystem:
    def __init__(self, git_tool):
        self.git_tool = git_tool
        
    def show_menu(self):
        """Show main menu"""
        print("\nGit Operations Tool")
        print("=" * 50)
        print("1.  Auto commit and push all files")
        print("2.  Create branch")
        print("3.  List branches")
        print("4.  Checkout branch")
        print("5.  Delete branch")
        print("6.  Merge branch")
        print("7.  Pull changes")
        print("8.  Push changes")
        print("9.  Show status")
        print("10. Show commit log")
        print("11. Create pull request")
        print("12. Stash changes")
        print("13. Apply stash")
        print("14. Exit")
        print("=" * 50)

    def handle_choice(self, choice):
        """Handle user menu choice"""
        if choice == '1':
            self.git_tool.auto_commit_and_push()
        elif choice == '2':
            branch_name = input("Enter branch name: ").strip()
            self.git_tool.branch_manager.create_branch(branch_name)
        elif choice == '3':
            self.git_tool.branch_manager.list_branches()
        elif choice == '4':
            branch_name = input("Enter branch name to checkout: ").strip()
            self.git_tool.branch_manager.checkout_branch(branch_name)
        elif choice == '5':
            branch_name = input("Enter branch name to delete: ").strip()
            self.git_tool.branch_manager.delete_branch(branch_name)
        elif choice == '6':
            branch_name = input("Enter branch name to merge: ").strip()
            self.git_tool.branch_manager.merge_branch(branch_name)
        elif choice == '7':
            branch = input("Enter branch name (default: main): ").strip() or 'main'
            self.git_tool.operations.pull_changes(branch)
        elif choice == '8':
            branch = input("Enter branch name (current branch): ").strip() or None
            self.git_tool.operations.push_changes(branch)
        elif choice == '9':
            self.git_tool.operations.show_status()
        elif choice == '10':
            limit = input("Enter number of commits to show (default: 10): ").strip()
            limit = int(limit) if limit.isdigit() else 10
            self.git_tool.operations.show_log(limit)
        elif choice == '11':
            title = input("Enter PR title: ").strip()
            body = input("Enter PR description: ").strip()
            head_branch = input("Enter head branch: ").strip()
            base_branch = input("Enter base branch (default: main): ").strip() or 'main'
            self.git_tool.pr_manager.create_pull_request(title, body, head_branch, base_branch)
        elif choice == '12':
            self.git_tool.operations.stash_changes()
        elif choice == '13':
            self.git_tool.operations.apply_stash()
        elif choice == '14':
            print("Goodbye!")
            return False
        else:
            print("Invalid choice. Please try again.")
        return True
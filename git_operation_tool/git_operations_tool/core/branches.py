class BranchManager:
    def __init__(self, repo):
        self.repo = repo
        
    def create_branch(self, branch_name):
        """Create a new branch"""
        try:
            # Create new branch
            new_branch = self.repo.create_head(branch_name)
            new_branch.checkout()
            print(f"✓ Created and switched to branch: {branch_name}")
            return True
        except Exception as e:
            print(f"✗ Error creating branch {branch_name}: {str(e)}")
            return False

    def list_branches(self):
        """List all branches"""
        try:
            print("\nLocal Branches:")
            for branch in self.repo.branches:
                current = "* " if branch == self.repo.active_branch else "  "
                print(f"{current}{branch.name}")
            
            print("\nRemote Branches:")
            for ref in self.repo.remote().refs:
                print(f"  {ref.name}")
            return True
        except Exception as e:
            print(f"✗ Error listing branches: {str(e)}")
            return False

    def checkout_branch(self, branch_name):
        """Checkout to a specific branch"""
        try:
            # Check if branch exists locally
            if branch_name in [b.name for b in self.repo.branches]:
                self.repo.git.checkout(branch_name)
                print(f"✓ Switched to existing branch: {branch_name}")
            else:
                # Try to checkout from remote
                try:
                    self.repo.git.checkout('-b', branch_name, f'origin/{branch_name}')
                    print(f"✓ Created and switched to branch: {branch_name} (from remote)")
                except:
                    # Create new branch
                    self.repo.git.checkout('-b', branch_name)
                    print(f"✓ Created and switched to new branch: {branch_name}")
            return True
        except Exception as e:
            print(f"✗ Error checking out branch {branch_name}: {str(e)}")
            return False

    def delete_branch(self, branch_name):
        """Delete a branch"""
        try:
            if branch_name == self.repo.active_branch.name:
                print(f"✗ Cannot delete current branch {branch_name}")
                return False
            
            self.repo.delete_head(branch_name, force=True)
            print(f"Deleted branch: {branch_name}")
            return True
        except Exception as e:
            print(f"✗ Error deleting branch {branch_name}: {str(e)}")
            return False

    def merge_branch(self, branch_name):
        """Merge a branch into current branch"""
        try:
            current_branch = self.repo.active_branch.name
            merge_branch = self.repo.heads[branch_name]
            
            # Perform merge
            self.repo.git.merge(branch_name)
            print(f"Merged {branch_name} into {current_branch}")
            return True
        except Exception as e:
            print(f"✗ Error merging branch {branch_name}: {str(e)}")
            return False
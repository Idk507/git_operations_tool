from git.exc import GitCommandError

class TagManager:
    def __init__(self, repo):
        self.repo = repo

    def create_tag(self, tag_name, message=None):
        """Create a new tag"""
        try:
            if message:
                self.repo.create_tag(tag_name, message=message)
            else:
                self.repo.create_tag(tag_name)
            print(f"✓ Created tag: {tag_name}")
            return True
        except GitCommandError as e:
            print(f"✗ Error creating tag {tag_name}: {str(e)}")
            return False
        except Exception as e:
            print(f"✗ Unexpected error creating tag: {str(e)}")
            return False

    def list_tags(self):
        """List all tags"""
        try:
            print("\nTags:")
            if not self.repo.tags:
                print("  No tags found.")
            for tag in self.repo.tags:
                print(f"  - {tag.name}")
            return True
        except Exception as e:
            print(f"✗ Error listing tags: {str(e)}")
            return False

    def push_tags(self):
        """Push all tags to remote"""
        try:
            origin = self.repo.remote('origin')
            origin.push(tags=True)
            print("✓ Pushed all tags to remote")
            return True
        except GitCommandError as e:
            print(f"✗ Error pushing tags: {str(e)}")
            return False
        except Exception as e:
            print(f"✗ Unexpected error pushing tags: {str(e)}")
            return False

    def delete_tag(self, tag_name):
        """Delete a tag locally and from remote"""
        try:
            # Delete local
            self.repo.delete_tag(tag_name)
            print(f"✓ Deleted local tag: {tag_name}")
            
            # Try to delete remote
            try:
                origin = self.repo.remote('origin')
                origin.push(refspec=f':refs/tags/{tag_name}')
                print(f"✓ Deleted remote tag: {tag_name}")
            except (ValueError, GitCommandError):
                print(f"⚠ Could not delete remote tag {tag_name} (might not exist on remote or no remote configured)")
            except Exception as e:
                print(f"⚠ Unexpected error deleting remote tag: {str(e)}")
            
            return True
        except GitCommandError as e:
            print(f"✗ Error deleting tag {tag_name}: {str(e)}")
            return False
        except Exception as e:
            print(f"✗ Unexpected error deleting tag: {str(e)}")
            return False

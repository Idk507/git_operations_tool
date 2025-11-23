from git.exc import GitCommandError

class RemoteManager:
    def __init__(self, repo):
        self.repo = repo

    def list_remotes(self):
        """List all remotes"""
        try:
            print("\nRemotes:")
            for remote in self.repo.remotes:
                print(f"  - {remote.name}: {remote.url}")
            return True
        except Exception as e:
            print(f"✗ Error listing remotes: {str(e)}")
            return False

    def add_remote(self, name, url):
        """Add a new remote"""
        try:
            self.repo.create_remote(name, url)
            print(f"✓ Added remote {name}: {url}")
            return True
        except GitCommandError as e:
            print(f"✗ Error adding remote: {str(e)}")
            return False
        except Exception as e:
            print(f"✗ Unexpected error adding remote: {str(e)}")
            return False

    def remove_remote(self, name):
        """Remove a remote"""
        try:
            self.repo.delete_remote(name)
            print(f"✓ Removed remote: {name}")
            return True
        except GitCommandError as e:
            print(f"✗ Error removing remote: {str(e)}")
            return False
        except ValueError:
             print(f"✗ Remote '{name}' not found.")
             return False
        except Exception as e:
            print(f"✗ Unexpected error removing remote: {str(e)}")
            return False

import os
from git import Repo, InvalidGitRepositoryError
from pathlib import Path
import fnmatch

class RepositoryManager:
    def __init__(self):
        self.repo = None
        self.repo_url = None
        
    def initialize_or_clone_repo(self, repo_url, local_path="."):
        """Initialize or clone the repository"""
        try:
            # Try to open existing repo
            self.repo = Repo(local_path)
            print(f"✓ Found existing Git repository at {local_path}")
            
            # Add remote if it doesn't exist
            try:
                origin = self.repo.remote('origin')
                if origin.url != repo_url:
                    print(f"Warning: Remote origin URL differs from provided URL")
                    print(f"Existing: {origin.url}")
                    print(f"Provided: {repo_url}")
            except:
                self.repo.create_remote('origin', repo_url)
                print(f"✓ Added remote origin: {repo_url}")
                
            return self.repo
            
        except InvalidGitRepositoryError:
            # Initialize new repo
            print(f"Initializing new Git repository at {local_path}")
            self.repo = Repo.init(local_path)
            self.repo.create_remote('origin', repo_url)
            print(f"✓ Created new repository with remote: {repo_url}")
            return self.repo

    def _load_gitignore_patterns(self):
        """Load gitignore patterns from .gitignore file"""
        gitignore_path = Path(self.repo.working_dir) / '.gitignore'
        patterns = []
        
        if gitignore_path.exists():
            with open(gitignore_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        patterns.append(line)
        
        # Add default patterns for common unwanted files
        default_patterns = [
            '__pycache__/',
            '*.pyc',
            '*.pyo',
            '*.pyd',
            '.DS_Store',
            'Thumbs.db',
            '*.egg-info/',
            'dist/',
            'build/',
            '.pytest_cache/',
            '.coverage'
        ]
        
        return patterns + default_patterns

    def _is_ignored(self, file_path, patterns):
        """Check if a file matches any gitignore pattern"""
        for pattern in patterns:
            # Handle directory patterns
            if pattern.endswith('/'):
                if file_path.startswith(pattern) or f"/{pattern}" in file_path:
                    return True
            # Handle file patterns
            elif fnmatch.fnmatch(file_path, pattern) or fnmatch.fnmatch(os.path.basename(file_path), pattern):
                return True
            # Handle patterns with path separators
            elif '/' in pattern and fnmatch.fnmatch(file_path, pattern):
                return True
                
        return False

    def get_all_files_and_folders(self, path="."):
        """Get all files and folders that should be tracked by git"""
        items = []
        patterns = self._load_gitignore_patterns()
        
        # Walk through directory tree
        for root, dirs, files in os.walk(path):
            # Skip .git directory
            if '.git' in root:
                continue
                
            # Add files
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, path).replace('\\', '/')
                
                # Skip files that match gitignore patterns
                if not self._is_ignored(relative_path, patterns):
                    # Skip hidden files except .gitignore
                    if not relative_path.startswith('.') or relative_path == '.gitignore':
                        items.append(('file', relative_path))
        
        return items

    def commit_all_changes(self, commit_message="Auto commit: Add all files"):
        """Commit all changes at once instead of individual files"""
        try:
            # Check if there are any changes
            if self.repo.is_dirty() or self.repo.untracked_files:
                # Add all files
                self.repo.git.add('.')
                
                # Check if there are staged changes after adding
                # For new repos without any commits, we need to handle the case where HEAD doesn't exist
                try:
                    if self.repo.head.is_valid():
                        # Repository has commits, compare with HEAD
                        has_staged_changes = bool(self.repo.index.diff("HEAD"))
                    else:
                        # New repository, check if index has any files
                        has_staged_changes = bool(list(self.repo.index.entries.keys()))
                except:
                    # Fallback: check if index has any files
                    has_staged_changes = bool(list(self.repo.index.entries.keys()))
                
                if has_staged_changes:
                    # Create commit
                    commit = self.repo.index.commit(commit_message)
                    print(f"✓ Committed all changes (commit: {commit.hexsha[:8]})")
                    return True
                else:
                    print("⚠ No changes to commit")
                    return False
            else:
                print("⚠ No changes to commit")
                return False
                
        except Exception as e:
            print(f"✗ Error committing changes: {str(e)}")
            return False

    def push_to_remote(self, branch='main'):
        """Push changes to remote repository"""
        try:
            # Ensure we're on the correct branch
            try:
                current_branch = self.repo.active_branch.name
                if current_branch != branch:
                    try:
                        self.repo.git.checkout(branch)
                    except:
                        # Create branch if it doesn't exist
                        self.repo.git.checkout('-b', branch)
            except:
                # For new repos, create the main branch
                self.repo.git.checkout('-b', branch)
            
            # Push to remote
            origin = self.repo.remote('origin')
            origin.push(refspec=f'{branch}:{branch}')
            print(f"✓ Pushed changes to remote/{branch}")
            return True
            
        except Exception as e:
            print(f"✗ Error pushing to remote: {str(e)}")
            return False

    def commit_and_push_item(self, item_type, item_path, branch='main'):
        """Commit and push a single item"""
        try:
            # Check if item still exists
            full_path = Path(self.repo.working_dir) / item_path
            if not full_path.exists():
                print(f"⚠ Skipping {item_path} - file/folder no longer exists")
                return False
            
            # Add the item to staging
            self.repo.index.add([item_path])
            
            # Check if there are any staged changes for this specific file
            try:
                if self.repo.head.is_valid():
                    # Repository has commits, compare with HEAD
                    staged_files = self.repo.index.diff("HEAD")
                    has_changes = any(item.a_path == item_path for item in staged_files)
                else:
                    # New repository, check if file is in index
                    has_changes = any(item_path in str(key) for key in self.repo.index.entries.keys())
            except:
                # Fallback: assume there are changes if file exists
                has_changes = True
            
            if not has_changes:
                print(f"⚠ No changes to commit for {item_path}")
                return False
            
            # Create commit message
            commit_msg = f"Add {item_type}: {item_path}"
            
            # Commit
            commit = self.repo.index.commit(commit_msg)
            print(f"✓ Committed {item_type}: {item_path} (commit: {commit.hexsha[:8]})")
            
            # Ensure we're on the correct branch
            try:
                current_branch = self.repo.active_branch.name
                if current_branch != branch:
                    try:
                        self.repo.git.checkout(branch)
                    except:
                        # Create branch if it doesn't exist
                        self.repo.git.checkout('-b', branch)
            except:
                # For new repos, create the main branch
                self.repo.git.checkout('-b', branch)
            
            # Push to remote
            origin = self.repo.remote('origin')
            origin.push(refspec=f'{branch}:{branch}')
            print(f"✓ Pushed {item_type}: {item_path} to remote/{branch}")
            
            return True
            
        except Exception as e:
            print(f"✗ Error processing {item_path}: {str(e)}")
            return False

    def auto_commit_and_push_all(self, branch='main'):
        """Improved auto commit and push functionality"""
        print("\nAnalyzing repository status...")
        
        # Check repository status
        has_untracked = bool(self.repo.untracked_files)
        has_modified = self.repo.is_dirty()
        
        if not has_untracked and not has_modified:
            print("✓ Repository is clean - no changes to commit")
            return True
        
        # Show what will be committed
        if has_untracked:
            print(f"Untracked files ({len(self.repo.untracked_files)}):")
            for file in self.repo.untracked_files[:10]:  # Show first 10
                print(f"  + {file}")
            if len(self.repo.untracked_files) > 10:
                print(f"  ... and {len(self.repo.untracked_files) - 10} more files")
        
        if has_modified:
            print("Modified files:")
            try:
                if self.repo.head.is_valid():
                    for item in self.repo.index.diff(None):
                        print(f"  M {item.a_path}")
                else:
                    print("  (New repository - all files will be added)")
            except:
                print("  (New repository - all files will be added)")
        
        # Check if this is the first commit
        is_first_commit = False
        try:
            is_first_commit = not self.repo.head.is_valid()
        except:
            is_first_commit = True
        
        if is_first_commit:
            print("\n🎉 This appears to be the first commit to this repository!")
        
        # Confirm before proceeding
        print(f"\nThis will commit and push all changes to the '{branch}' branch.")
        confirm = input("Do you want to proceed? (y/N): ").strip().lower()
        
        if confirm != 'y':
            print("Operation cancelled.")
            return False
        
        # Commit and push all changes
        if self.commit_all_changes("Initial commit" if is_first_commit else "Auto commit: Add all files"):
            return self.push_to_remote(branch)
        else:
            return False
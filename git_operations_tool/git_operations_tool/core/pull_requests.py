import requests
from datetime import datetime

class PullRequestManager:
    def __init__(self, repo, repo_url):
        self.repo = repo
        self.repo_url = repo_url
        
    def create_pull_request(self, title, body, head_branch, base_branch='main'):
        """Create a pull request (GitHub only)"""
        try:
            # Extract GitHub info from repo URL
            if 'github.com' not in self.repo_url:
                print("✗ Pull requests are only supported for GitHub repositories")
                return False
            
            # Parse GitHub URL
            repo_path = self.repo_url.replace('https://github.com/', '').replace('.git', '')
            owner, repo_name = repo_path.split('/')
            
            # GitHub API token (user should set this)
            token = input("Enter your GitHub Personal Access Token: ").strip()
            if not token:
                print("✗ GitHub token is required for pull requests")
                return False
            
            # Create PR via GitHub API
            api_url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls"
            headers = {
                'Authorization': f'token {token}',
                'Accept': 'application/vnd.github.v3+json'
            }
            
            data = {
                'title': title,
                'body': body,
                'head': head_branch,
                'base': base_branch
            }
            
            response = requests.post(api_url, headers=headers, json=data)
            
            if response.status_code == 201:
                pr_data = response.json()
                print(f"✓ Pull request created: {pr_data['html_url']}")
                return True
            else:
                print(f"✗ Error creating pull request: {response.json()}")
                return False
                
        except Exception as e:
            print(f"✗ Error creating pull request: {str(e)}")
            return False
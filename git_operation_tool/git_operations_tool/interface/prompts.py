def get_repo_url():
    """Get repository URL from user input"""
    while True:
        repo_url = input("Enter the Git repository URL (SSH or HTTPS): ").strip()
        if repo_url:
            return repo_url
        print("Please enter a valid repository URL.")

def confirm_operation(message):
    """Confirm an operation with the user"""
    confirm = input(f"{message} (y/N): ").strip().lower()
    return confirm == 'y'
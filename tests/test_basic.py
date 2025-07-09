import pytest
from git_operations_tool.core.repository import RepositoryManager

def test_repository_manager_initialization():
    """Test that RepositoryManager initializes correctly"""
    manager = RepositoryManager()
    assert manager.repo is None
    assert manager.repo_url is None
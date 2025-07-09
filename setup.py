from setuptools import setup, find_packages

setup(
    name="git-operations-tool",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "gitpython>=3.1.30",
        "requests>=2.28.1",
    ],
    entry_points={
        "console_scripts": [
            "git-ops=git_operations_tool.main:run_tool",
        ],
    },
)
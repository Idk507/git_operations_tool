# Publishing Guide for git-operations-tool

## Package Built Successfully! ✓

Your package has been built and is ready to publish. The distribution files are in the `dist/` directory.

## Publishing to PyPI

### Option 1: Test PyPI (Recommended First)

Test your package on Test PyPI before publishing to the real PyPI:

```bash
# Upload to Test PyPI
python -m twine upload --repository testpypi dist/*

# You'll be prompted for:
# Username: __token__
# Password: <your-test-pypi-token>
```

To get a Test PyPI token:
1. Go to https://test.pypi.org/
2. Register/Login
3. Go to Account Settings → API tokens
4. Create a new token with scope for this project

Test installation:
```bash
pip install --index-url https://test.pypi.org/simple/ git-operations-tool
```

### Option 2: Real PyPI

Once tested, publish to the real PyPI:

```bash
# Upload to PyPI
python -m twine upload dist/*

# You'll be prompted for:
# Username: __token__
# Password: <your-pypi-token>
```

To get a PyPI token:
1. Go to https://pypi.org/
2. Register/Login
3. Go to Account Settings → API tokens
4. Create a new token

### Using .pypirc (Optional)

To avoid entering credentials each time, create `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = <your-pypi-token>

[testpypi]
username = __token__
password = <your-test-pypi-token>
```

Then upload with:
```bash
python -m twine upload --repository testpypi dist/*  # Test PyPI
python -m twine upload dist/*                         # Real PyPI
```

## Version 0.4.0 Features

This release includes:
- ✅ Interactive file selection for commits
- ✅ Tag management (create, list, push, delete)
- ✅ Remote management (add, list, remove)
- ✅ Visual commit graph
- ✅ Bulk or single-file commit modes
- ✅ Safe push with retry logic
- ✅ Bug fixes and improved error handling

## After Publishing

1. Verify on PyPI: https://pypi.org/project/git-operations-tool/
2. Test installation: `pip install git-operations-tool`
3. Update GitHub releases with the new version tag
4. Consider creating a CHANGELOG.md for future releases

## Troubleshooting

- **"File already exists"**: You're trying to upload a version that already exists. Bump the version number in `pyproject.toml` and `setup.py`, then rebuild.
- **Authentication failed**: Double-check your API token and ensure you're using `__token__` as the username.
- **Invalid distribution**: Make sure all required files are included in MANIFEST.in

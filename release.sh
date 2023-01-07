# release a new version of the project to PyPI
# Usage: ./release.sh

# check that we are on the main branch
branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$branch" != "main" ]; then
    echo "You must be on the main branch to release a new version."
    exit 1
fi

# check that we have no uncommitted changes
if ! git diff --quiet; then
    echo "You have uncommitted changes."
    exit 1
fi

# check that we are up to date
git fetch
if ! git diff --quiet origin/main; then
    echo "You are not up to date with origin/main."
    exit 1
fi

# get the version number
version=$(python setup.py --version)

# build the source and wheel distributions
python setup.py sdist bdist_wheel

# upload to PyPI
twine upload dist/*

# clean up
rm -rf build dist .egg *.egg-info
from setuptools import setup

# Read the requirements from the requirements.txt file
with open("requirements.txt", "r") as f:
    requirements = f.readlines()

# Strip leading and trailing whitespace from each requirement
requirements = [req.strip() for req in requirements]

# Read the contents of the README.md file
with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="aidoc",
    version="0.1.2",
    author="Saikat Kumar Dey",
    author_email="deysaikatkumar@gmail.com",
    description="A simple CLI tool to generate documentation for your Python projects automatically.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saikatkumardey/aidoc",
    py_modules=["aidoc"],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "aidoc=aidoc:main",
        ],
    },
)

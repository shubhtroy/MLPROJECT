from setuptools import find_packages, setup
from pathlib import Path

def get_requirements(path: str):
    lines = Path(path).read_text().splitlines()
    reqs = [l.strip() for l in lines if l.strip() and not l.startswith("#") and l.strip() != "-e ."]
    return reqs

setup(
    name="mlproject",
    version="0.0.1",
    author="shubh",
    author_email="shubhbajpai7@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements("requirements.txt"),
)

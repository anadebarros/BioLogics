from setuptools import setup, find_packages

setup(
    name="biologics",
    version="0.1.0",
    author="Your Name",
    description="Bio-inspired programming language based on genetic sequences",
    packages=find_packages(),
    install_requires=[
        "biopython>=1.80"
    ],
    python_requires=">=3.10",
)

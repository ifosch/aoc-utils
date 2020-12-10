from setuptools import setup, find_packages

setup(
    name="aoc-utils",
    version="0.1.0",
    description="Utilities to setup/test/run https://adventofcode.com challenges",
    url="https://github.com/ifosch/aoc-utils",
    author="Ignasi Fosch",
    author_email="natx@y10k.ws",
    install_requires=[
        "advent-of-code-data >= 0.9.0",
    ],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "setup=aoc_utils.setup:main",
            "run_tests=aoc_utils.run_tests:main",
            "check=aoc_utils.check:main",
        ],
    },
)

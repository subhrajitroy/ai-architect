"""
Setup script for the Architecture Advisor package.
"""

from setuptools import setup, find_packages

setup(
    name="architecture_advisor",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "architecture_advisor": ["data/*.md"],
    },
    install_requires=[
        "langchain",
        "langchain-community",
        "langchain-openai",
        "pydantic",
        "openai",
    ],
    entry_points={
        "console_scripts": [
            "architecture-advisor=architecture_advisor.main:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for analyzing architecture decisions",
    keywords="architecture, decision, analysis",
    python_requires=">=3.7",
) 
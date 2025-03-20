"""
Main module for the Architecture Advisor package.
"""
import os
from architecture_advisor.core.architect import Architect
from architecture_advisor.core.agent import Agent
from architecture_advisor.core.adr import ADR
from architecture_advisor.utils.file_utils import get_data_path
from architecture_advisor.extract.file_source import load_file

def main():
    """
    Main function that demonstrates the analysis of an ADR using architecture principles.
    """
    cwd = os.getcwd();
    arch_principles_text = load_file(file_path=f"{cwd}/architecture_principles.md")
    adr_text = load_file(file_path=f"{cwd}/sample_adr.md")
    architect = Architect(architecture_principles=arch_principles_text)
    response = architect.analyze_adr(adr_content=adr_text)
    print(response)


if __name__ == "__main__":
    main() 
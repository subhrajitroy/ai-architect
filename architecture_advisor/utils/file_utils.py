"""
File utility functions for the Architecture Advisor package.
"""

import os
import pathlib

def get_project_root():
    """
    Get the absolute path to the project root directory.
    
    Returns:
        pathlib.Path: Path to the project root directory.
    """
    return pathlib.Path(__file__).parent.parent.parent.absolute()

def get_data_path(filename):
    """
    Get the absolute path to a file in the data directory.
    
    Args:
        filename (str): Name of the file in the data directory.
        
    Returns:
        str: Absolute path to the file.
    """
    data_dir = os.path.join(get_project_root(), "architecture_advisor", "data")
    return os.path.join(data_dir, filename) 
"""
ADR module for working with Architecture Decision Records.
"""

class ADR:
    """
    A simple class to load and provide Architecture Decision Record (ADR) content.
    """
    
    def __init__(self, text:str):
        self.text = text

    def __str__(self):
        return self.text
    
    
"""
Architect module for managing architecture principles.
"""

from architecture_advisor.core.agent import Agent
from architecture_advisor.core.prompts import Prompt

class Architect(Agent):
    """
    A class that represents an architect who follows architecture principles
    loaded from a text file.
    """
    
    def __init__(self, architecture_principles,model_name="gpt-3.5-turbo", temperature=0.7, provider="openai"):
        super().__init__(model_name,temperature,provider)
        self.principles = architecture_principles
        
    
    
    
    def analyze_adr(self, adr_content):
        """
        Analyze an Architecture Decision Record and provide feedback.
        
        Args:
            adr_content (str): The content of the ADR to analyze.
            architect (Architect, optional): An Architect instance containing principles
                                           to consider during analysis.
            
        Returns:
            AnalysisResult: A structured analysis result with status and summary.
        """
        
        prompt = f"""
        Please analyze the following Architecture Decision Record:
        
        {adr_content}
        
        Include in your analysis:
        1. Completeness of context and decision rationale
        2. Clarity of the options considered
        3. Soundness of the decision based on the context
        4. Appropriateness of the technology choices
        5. Any missing information or considerations
        6. Alignment with architecture principles (if applicable)
        
        {Prompt.FORMAT_INSTRUCTIONS}
        
        
        """
        
        system_message = f"T{Prompt.SYSTEM_MESSAGE}\n The architecture principles to be follwed in every ADR are as follows: \n {self.principles}"

        # Get the raw response
        raw_response = super().invoke(query=prompt, system_message=system_message)
        return raw_response
    
    
    def __str__(self):
        """
        Return a string representation of the Architect.
        
        Returns:
            str: A string representation of the Architect.
        """
        if not self.principles:
            return "Architect with no principles defined."
        
        principles_str = "\n".join([f"- {p}" for p in self.principles])
        return f"Architect with the following principles:\n{principles_str}" 
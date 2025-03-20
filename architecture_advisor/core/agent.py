"""
Agent module for interacting with language models.
"""

from langchain.chat_models import init_chat_model
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal


class AnalysisResult(BaseModel):
    """
    Pydantic model for the analysis result.
    """
    status: Literal["accepted", "needs change"] = Field(
        description="Whether the ADR is accepted or needs changes"
    )
    summary: str = Field(
        description="A summary of the analysis result"
    )

class Agent:
    """
    A class that represents an agent capable of invoking a language model
    to answer queries using the LangChain library.
    """
    
    def __init__(self, model_name="gpt-3.5-turbo", temperature=0.7, provider="openai", system_message=""):
        """
        Initialize the Agent with a specific language model.
        
        Args:
            model_name (str, optional): The name of the language model to use.
                                       Defaults to "gpt-3.5-turbo".
            temperature (float, optional): Controls randomness in the model's responses.
                                          Lower values make responses more deterministic.
                                          Defaults to 0.7.
            api_key (str, optional): The API key for the language model service.
                                    If not provided, it will look for OPENAI_API_KEY
                                    environment variable.
        """
        self.llm = init_chat_model(model=model_name, temperature=temperature,model_provider=provider)
        
        # Initialize the Pydantic output parser
        # self.parser = PydanticOutputParser(pydantic_object=AnalysisResult)
    
    def invoke(self, query,system_message):
        """
        Invoke the language model with a query.
        
        Args:
            query (str): The query or prompt to send to the language model.
            system_message (str, optional): A custom system message to use for this query.
                                           Defaults to None, which uses the default system message.
            use_chat (bool, optional): Whether to use the chat model or the standard LLM.
                                      Defaults to True.
            
        Returns:
            str: The response from the language model.
        """

        # print("*"*20)
        # print(system_message)
        # print("*"*20)
            # Use the chat model with system and human messages
        messages = [
                SystemMessage(content=system_message),
                HumanMessage(content=query)
            ]
        response = self.llm.invoke(messages)
        return response.content
        
    
    
    def generate_architecture_advice(self, problem_description):
        """
        Generate architecture advice for a given problem.
        
        Args:
            problem_description (str): Description of the architectural problem.
            
        Returns:
            str: Architecture advice from the language model.
        """
        
        prompt = f"""
        I need architecture advice on the following problem:
        
        {problem_description}
        
        Please provide:
        1. A high-level architectural approach
        2. Key components and their interactions
        3. Potential challenges and how to address them
        4. Technology recommendations
        """
        
        return self.invoke(prompt, system_message=self.system_message)
    
    
       
        
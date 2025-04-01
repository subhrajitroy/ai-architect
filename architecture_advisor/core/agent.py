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
        self.llm = init_chat_model(model=model_name, temperature=temperature,model_provider=provider)
        self.parser = PydanticOutputParser(pydantic_object=AnalysisResult)
    
    def invoke(self, query,system_message):
        messages = [
                SystemMessage(content=system_message),
                HumanMessage(content=query)
            ]
        response = self.llm.invoke(messages)
        return response.content
    
    
       
        
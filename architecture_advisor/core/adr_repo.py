from abc import ABC, abstractmethod
from adr import ADR
import os
from architecture_advisor.db.in_memory_db import InMemoryDb
from architecture_advisor.utils.adr_parser import AdrParser

class AdrRepo(ABC):

    @abstractmethod
    def get_similar_adrs(self, adr:ADR):
        pass


class LocalFileSystemAdrRepo(AdrRepo):
    
    def __init__(self, adr_dir:str):
        self.adr_dir = adr_dir
        self.db = InMemoryDb()
        self.load_adrs()
        

    def load_adrs(self):
        # Load all ADRs from the directory
        adr_parser = AdrParser()
        adrs = []
        for filename in os.listdir(self.adr_dir):
            with open(os.path.join(self.adr_dir, filename), 'r') as file:
                adr_text_as_lines = file.readlines()
                adr = adr_parser.parse(adr_text_as_lines)
                adrs.append(adr)
        adr_contexts = [adr['context'] for adr in adrs]
        adr_decisions = [adr['decision'] for adr in adrs]
        documents = []
        for context, decision in zip(adr_contexts, adr_decisions):
            summary = self.__combine(context, decision)
            documents.append(summary)
        self.db.save(documents=documents)
    
    def get_similar_adrs(self, adr:ADR):
        adr_as_text = self.__combine(adr=adr)
        similar_adrs = self.db.search(adr_as_text)
        return similar_adrs

    def __combine(self, adr):
        return f"Context: {adr['context']}\nDecision: {adr['decision']}"              

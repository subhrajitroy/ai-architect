import os
from dotenv import load_dotenv

load_dotenv()


class Session:
    def __init__(self):
        pass

    @staticmethod
    def start(self):
        if not os.environ["OPENAI_API_KEY"]:
            raise ValueError("OPENAI_API_KEY is not set")
        return Session()
       
        

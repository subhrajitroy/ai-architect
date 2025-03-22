from pymongo.mongo_client import MongoClient
from architecture_advisor.utils.embeddings import Embeddings
from architecture_advisor.utils.text_source import TextSource

class Database:
    def __init__(self,connection_string):
        self.client = MongoClient(connection_string)
        self.db = self.client["ai"]
        self.collection = self.db["embedded_architecture_documents"]
    

    def save(self,documents):
        for document in documents:
            self.collection.insert_one(document=document)

    def search(self,query):
        q = query if isinstance(query,list) else [query]
        chunks = TextSource(q).create_chunks()
        _ , embeddings = Embeddings().encode(chunks)
        print(embeddings[0][:4])
        pipeline = [
                        {
                            "$vectorSearch": {
                                    "index": "vector_index2",
                                    "queryVector": embeddings[0],
                                    "path": "embedding",
                                    "exact": True,
                                    "limit": 5
                            }
                        }, 
                        {
                            "$project": {
                                "_id": 0, 
                                "text": 1,
                                "score": {
                                    "$meta": "vectorSearchScore"
                                }
                            }
                        }
                    ]
        results = self.collection.aggregate(pipeline)
        return results
        

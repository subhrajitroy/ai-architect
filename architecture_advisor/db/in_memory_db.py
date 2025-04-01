import chromadb

class InMemoryDb:

    def __init__(self):
        self.client = chromadb.Client()
    
    def save(self, documents, collection_name):
        collection = self.client.get_or_create_collection(name=collection_name)
        ids =  [ f"id{i}" for i in range(len(documents))]
        collection.add(documents,ids=ids)

    def search(self, query, collection_name):
        collection = self.client.get_collection(name=collection_name)
        results = collection.query(query_texts=[query],n_results=2)
        return results

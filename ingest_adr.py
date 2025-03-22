from architecture_advisor.utils.embeddings import Embeddings
from architecture_advisor.db.databse import Database
from architecture_advisor.utils.text_source import TextSource
import os

def extract_content(file_name):
    lines = None
    with open(file_name,"r") as f:
        lines = f.readlines()
    return lines




def create_embeddings():
    root = os.getcwd()
    chunks = TextSource(extract_content(f"{root}/data/adr/sample_adr.md")).create_chunks()
    return Embeddings().encode(chunks)


db = Database("mongodb://localhost:27017/?directConnection=true")

def ingest_document_embeddings():
    lines, embeddings = create_embeddings()
    documents = []
    for i, (line,emb) in enumerate(zip(lines,embeddings)):
        document = {
            "_id" : i,
            "text" : line,
            "embedding" : emb,
        }
        documents.append(document)
    db.save(documents=documents)

    
# ingest_document_embeddings()
def search(query):
    results = db.search(query)
    for result in results:
        print(result)

search("Approaches for designing a microservices architecture")




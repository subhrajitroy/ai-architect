from pymongo.mongo_client import MongoClient
from pymongo.operations import SearchIndexModel
import time

CONNECTTION_STRING="mongodb://localhost:27017/?directConnection=true"

db_client = MongoClient(CONNECTTION_STRING)
database = db_client["ai"]
collection = database["embedded_architecture_documents"]

search_index_model = SearchIndexModel(
  definition={
    "fields": [
      {
        "type": "vector",
        "path": "embedding",
        "numDimensions": 768,
        "similarity": "dotProduct",
        "quantization": "scalar"
      }
    ]
  },
  name="vector_index2",
  type="vectorSearch"
)

result = collection.create_search_index(model=search_index_model)
print("New search index named " + result + " is building.")
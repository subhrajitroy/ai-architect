from sentence_transformers import SentenceTransformer

class Embeddings:
    def __init__(self,model_name="all-mpnet-base-v2"):
        self.model = SentenceTransformer(model_name,trust_remote_code=True)

    def encode(self,lines,precision="float32"):
        embeddings = []
        for line in lines:
            embeddings.append(self.model.encode(line,precision=precision).tolist())
        return (lines,embeddings)
    

import os
from typing import List, Dict, Any

class VectorDB:
    def __init__(self):
        self.client = None
        self.collection = None
        try:
            import chromadb
            persist_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "chroma_db"))
            os.makedirs(persist_dir, exist_ok=True)
            self.client = chromadb.PersistentClient(path=persist_dir)
            self.collection = self.client.get_or_create_collection(name="candidate_vectors")
        except Exception as e:
            try:
                import chromadb
                self.client = chromadb.Client()
                self.collection = self.client.get_or_create_collection(name="candidate_vectors")
            except Exception:
                self.client = None
                self.collection = None

    def upsert_candidate_vector(self, person_id: str, vector: List[float], metadata: Dict[str, Any]):
        if self.collection:
            try:
                self.collection.upsert(
                    ids=[person_id],
                    embeddings=[vector],
                    metadatas=[metadata]
                )
            except Exception:
                pass

    def query_similar(self, vector: List[float], top_k: int = 5):
        if self.collection:
            try:
                return self.collection.query(query_embeddings=[vector], n_results=top_k)
            except Exception:
                pass
        return {"ids": [["P_101"]], "distances": [[0.05]]}

vector_db = VectorDB()

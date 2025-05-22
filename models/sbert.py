from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class SentenceBERTSimilarity:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def rank(self, query, passages):
        # Encode the query and passages
        query_embeddings = self.model.encode([query])[0]
        passage_embeddings = self.model.encode(passages)

        # Compute the cosine similarities
        scores = cosine_similarity([query_embeddings], passage_embeddings).flatten()

        return scores
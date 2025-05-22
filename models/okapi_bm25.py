from rank_bm25 import BM25Okapi
import spacy

class BM25Similarity:
    # Use SpaCy module for better preprocessing
    def __init__(self, spacy_model='en_core_web_sm', use_preprocessing=True):
        self.nlp = spacy.load(spacy_model)
        self.use_preprocessing = use_preprocessing

    def preprocess(self, text):
        doc = self.nlp(text.lower())
        return [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    
    def rank(self, query, passages):
        if self.use_preprocessing:
            tokenized_passages = [self.preprocess(p) for p in passages]
            tokenized_query  = self.preprocess(query)
        else:
            tokenized_passages = [p.split() for p in passages]
            tokenized_query = query.split()

        bm25 = BM25Okapi(tokenized_passages)
        scores = bm25.get_scores(tokenized_query)

        return scores
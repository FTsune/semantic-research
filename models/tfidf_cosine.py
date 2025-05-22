from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy

class TFIDFCosineSimilarity:
    def __init__(self, spacy_model='en_core_web_sm', use_preprocessing=True):
        self.nlp = spacy.load(spacy_model)
        self.vectorizer = TfidfVectorizer()
        self.use_preprocessing = use_preprocessing

    def preprocess(self, text):
        doc = self.nlp(text)
        tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
        return " ".join(tokens)

    def rank(self, query, passages):
        if self.use_preprocessing:
            query = self.preprocess(query)
            passages = [self.preprocess(p) for p in passages]

        corpus = [query] + passages


        tfidf_matrix = self.vectorizer.fit_transform(corpus)
        query_vec = tfidf_matrix[0:1]
        passage_vecs = tfidf_matrix[1:]

        scores = cosine_similarity(query_vec, passage_vecs).flatten()
        return scores
        
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
import spacy

class TFIDFCosineSimilarity:
    def __init__(self, spacy_model='en_core_web_sm', use_preprocessing=True, use_dimensionality_reduction=False, n_components=100):
        self.nlp = spacy.load(spacy_model)
        self.vectorizer = TfidfVectorizer()
        self.use_preprocessing = use_preprocessing
        self.use_dimensionality_reduction = use_dimensionality_reduction
        self.n_components = n_components
        self.reducer = None  # Will initialize after fitting

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
        
        if self.use_dimensionality_reduction:
            max_components = min(self.n_components, tfidf_matrix.shape[1] - 1)
            self.reducer = TruncatedSVD(n_components=max_components)
            tfidf_matrix = self.reducer.fit_transform(tfidf_matrix)

        query_vec = tfidf_matrix[0:1]
        passage_vecs = tfidf_matrix[1:]

        scores = cosine_similarity(query_vec, passage_vecs).flatten()
        return scores
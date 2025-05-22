import spacy

class JaccardSimilarity:
    def __init__(self, spacy_model='en_core_web_sm', use_preprocessing=True):
        self.nlp = spacy.load(spacy_model)
        self.use_preprocessing = use_preprocessing

    def preprocess(self, text):
        doc = self.nlp(text.lower())
        return {token.lemma_ for token in doc if not token.is_stop and not token.is_punct}

    def jaccard_score(self, set1, set2):
        intersection = set1 & set2
        union = set1 | set2
        return len(intersection) / len(union) if union else 0.0
    
    def rank(self, query, passages):
        if self.use_preprocessing:
            query_tokens = set(self.preprocess(query))
            passage_tokens_list = [set(self.preprocess(p)) for p in passages]
        else:
            query_tokens = set(query.lower().split())
            passage_tokens_list = [set(p.lower().split()) for p in passages]

        scores = [
            self.jaccard_score(query_tokens, passage_tokens)
            for passage_tokens in passage_tokens_list
        ]
        return scores
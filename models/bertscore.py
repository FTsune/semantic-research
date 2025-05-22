from bert_score import score
import numpy as np

class BERTScoreSimilarity:
    def __init__(self, model_type='microsoft/deberta-xlarge-mnli', lang='en'):
        self.model_type = model_type
        self.lang = lang
    
    def rank(self, query, passages):
        # Score returns (P, R, F1)
        __, __, f1 = score(passages, [query] * len(passages), model_type=self.model_type, lang=self.lang, verbose=False)
        return f1.numpy()
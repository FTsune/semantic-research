import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from models.tfidf_cosine import TFIDFCosineSimilarity

class TestTFIDFModel(unittest.TestCase):
    def setUp(self):
        self.model = TFIDFCosineSimilarity()

    def test_ranking_length(self):
        query = "legal contract"
        passages = ["A legal contract", "Banana is yellow"]
        scores = self.model.rank(query, passages)
        self.assertEqual(len(scores), len(passages))
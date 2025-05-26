import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from models.okapi_bm25 import BM25Similarity

class TestBM25Model(unittest.TestCase):
    def setUp(self):
        self.model = BM25Similarity()

    def test_ranking(self):
        query = "tax law"
        passages = ["tax regulation and law", "weather is sunny"]
        scores = self.model.rank(query, passages)
        self.assertEqual(len(scores), len(passages))
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from models.sbert import SentenceBERTSimilarity

class TestSBERTModel(unittest.TestCase):
    def setUp(self):
        self.model = SentenceBERTSimilarity()

    def test_basic_functionality(self):
        query = "law and order"
        passages = ["public law and criminal code", "beach resort"]
        scores = self.model.rank(query, passages)
        self.assertEqual(len(scores), len(passages))
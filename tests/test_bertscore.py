import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from models.bertscore import BERTScoreSimilarity

class TestBERTScoreModel(unittest.TestCase):
    def setUp(self):
        self.model = BERTScoreSimilarity()

    def test_basic_functionality(self):
        query = "environmental law"
        passages = [
            "The principles of environmental legislation are established in the constitution.",
            "The weather today is sunny with some clouds."
        ]
        scores = self.model.rank(query, passages)
        self.assertEqual(len(scores), len(passages))
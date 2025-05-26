import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from models.tfidf_cosine import TFIDFCosineSimilarity

class TestTFIDFModel(unittest.TestCase):

    def setUp(self):
        self.model = TFIDFCosineSimilarity()

    def test_basic_ranking(self):
        query = "legal contract agreement"
        passages = [
            "This document is a legal contract.",
            "Apple is a fruit.",
            "Agreement between two parties"
        ]
        scores = self.model.rank(query, passages)
        self.assertEqual(len(scores), len(passages))
        self.assertGreater(scores[0], scores[1]) 
        self.assertGreater(scores[0], 0)

if __name__ == '__main__':
    unittest.main()
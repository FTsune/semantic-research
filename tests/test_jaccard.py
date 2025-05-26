import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from models.jaccard import JaccardSimilarity

class TestJaccardModel(unittest.TestCase):
    def setUp(self):
        self.model = JaccardSimilarity()

    def test_ranking(self):
        query = "intellectual property"
        passages = ["property rights", "apple and banana"]
        scores = self.model.rank(query, passages)
        self.assertEqual(len(scores), len(passages))
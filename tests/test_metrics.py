import unittest
from evaluation.metrics import precision_at_k, recall_at_k, mean_reciprocal_rank

class TestMetrics(unittest.TestCase):
    def test_precision_at_k(self):
        scores = [0.9, 0.2, 0.8, 0.1]
        labels = [1, 0, 1, 0]
        self.assertAlmostEqual(precision_at_k(scores, labels, k=1), 1.0)
        self.assertAlmostEqual(precision_at_k(scores, labels, k=3), 2 / 3)

    def test_recall_at_k(self):
        scores = [0.9, 0.2, 0.8, 0.1]
        labels = [1, 0, 1, 0]
        self.assertAlmostEqual(recall_at_k(scores, labels, k=3), 1.0)
        self.assertAlmostEqual(recall_at_k(scores, labels, k=1), 0.5)

    def test_mrr(self):
        ranks = [1, 2, 3]
        self.assertAlmostEqual(mean_reciprocal_rank(ranks), (1 + 1/2 + 1/3) / 3)
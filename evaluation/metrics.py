import numpy as np
import time
import tracemalloc

def precision_at_k(scores, labels, k):
    k = min(k, len(labels))
    top_k = np.argsort(scores)[::-1][:k]
    relevant = sum(labels[i] for i in top_k)
    return relevant / k

def recall_at_k(scores, labels, k):
    total_relevant = sum(labels)
    if total_relevant == 0:
        return 0.0
    k = min(k, len(labels))
    top_k = np.argsort(scores)[::-1][:k]
    retrieved_relevant = sum(labels[i] for i in top_k)
    return retrieved_relevant / total_relevant

def mean_reciprocal_rank(all_ranks):
    reciprocals = [1.0 / rank for rank in all_ranks]
    return np.mean(reciprocals)

def evaluate_model(model, dataset):
    precision_at_1_scores = []
    precision_at_3_scores = []
    recall_at_3_scores = []
    ranks = []

    # Track time and memory
    start_time = time.time()
    tracemalloc.start()

    for group in dataset:
        query = group['query']
        passages = [p['text'] for p in group['passages']]
        labels = [p['relevant'] for p in group['passages']]

        scores = model.rank(query, passages)
        sorted_indices = np.argsort(scores)[::-1]

        # Precision@1
        p1 = precision_at_k(scores, labels, k=1)
        precision_at_1_scores.append(p1)

        # Precision@3
        p3 = precision_at_k(scores, labels, k=3)
        precision_at_3_scores.append(p3)

        # Recall@3
        r3 = recall_at_k(scores, labels, k=3)
        recall_at_3_scores.append(r3)

        # Find MRR rank (first relevant)
        rank = None
        for idx_rank, idx in enumerate(sorted_indices, start=1):
            if labels[idx]:
                rank = idx_rank
                break
        if rank is None:
            rank = len(labels) + 1
        ranks.append(rank)
    
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "Precision@1": np.mean(precision_at_1_scores),
        "Precision@3": np.mean(precision_at_3_scores),
        "Recall@3": np.mean(recall_at_3_scores),
        "MRR": mean_reciprocal_rank(ranks),
        "Runtime (in seconds)": end_time - start_time,
        "Peak Memory (in KB)": peak / 1024
    }
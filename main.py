import json
from models.tfidf_cosine import TFIDFCosineSimilarity
from models.okapi_bm25 import BM25Similarity
from models.jaccard import JaccardSimilarity
from models.sbert import SentenceBERTSimilarity
from models.bertscore import BERTScoreSimilarity
from evaluation.metrics import evaluate_model
import warnings

warnings.filterwarnings('ignore')

def load_dataset(path):
    with open(path, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    return dataset

def main():
    dataset_path = "dataset/philippine-legal-dataset.json"
    dataset = load_dataset(dataset_path)

    print("Initializing models...")
    tfidf_model = TFIDFCosineSimilarity()
    bm25_model = BM25Similarity()
    jaccard_model = JaccardSimilarity()
    sbert_model = SentenceBERTSimilarity()
    bertscore_model =  BERTScoreSimilarity()

    print("Evaluating TF-IDF Cosine Similarity...")
    tfidf_results = evaluate_model(tfidf_model, dataset)

    print("Evaluating BM25 Similarity...")
    bm25_results = evaluate_model(bm25_model, dataset)

    print("Evaluating Jaccard Similarity...")
    jaccard_results = evaluate_model(jaccard_model, dataset)

    # print("Evaluating SBERT Similarity...")
    # sbert_results = evaluate_model(sbert_model, dataset)

    # print("Evaluating BERTScore Similarity...")
    # bertscore_results = evaluate_model(bertscore_model, dataset)

    print("\n=== Evaluation Results ===")
    print("TF-IDF Cosine:")
    for metric, val in tfidf_results.items():
        print(f"  {metric}: {val:.4f}")

    print("\nBM25:")
    for metric, val in bm25_results.items():
        print(f"  {metric}: {val:.4f}")

    print("\nJaccard:")
    for metric, val in jaccard_results.items():
        print(f"  {metric}: {val:.4f}")

    # print("\nSentence BERT:")
    # for metric, val in sbert_results.items():
    #     print(f"  {metric}: {val:.4f}")

    # print("\nBERTScore:")
    # for metric, val in bertscore_results.items():
    #     print(f"  {metric}: {val:.4f}")

if __name__ == "__main__":
    main()

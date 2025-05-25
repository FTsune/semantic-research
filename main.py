import json
from models.tfidf_cosine import TFIDFCosineSimilarity
from models.okapi_bm25 import BM25Similarity
from models.jaccard import JaccardSimilarity
from models.sbert import SentenceBERTSimilarity
from models.bertscore import BERTScoreSimilarity
from evaluation.metrics import evaluate_model
from evaluation.analyzer import generate_analysis_log
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
    tfidf_model = TFIDFCosineSimilarity(use_dimensionality_reduction=True, n_components=50)
    bm25_model = BM25Similarity()
    jaccard_model = JaccardSimilarity()
    sbert_model = SentenceBERTSimilarity(model_name='all-mpnet-base-v2')
    bertscore_model = BERTScoreSimilarity(model_type='distilbert-base-uncased')
    
    print("Evaluating TF-IDF Cosine Similarity...")
    tfidf_results = evaluate_model(tfidf_model, dataset)

    print("Evaluating BM25 Similarity...")
    bm25_results = evaluate_model(bm25_model, dataset)

    print("Evaluating Jaccard Similarity...")
    jaccard_results = evaluate_model(jaccard_model, dataset)

    print("Evaluating SBERT Similarity...")
    sbert_results = evaluate_model(sbert_model, dataset)

    print("Evaluating BERTScore Similarity...")
    bertscore_results = evaluate_model(bertscore_model, dataset)

    print("\n=== Evaluation Results ===")
    for name, results in [
        ("TF-IDF Cosine", tfidf_results),
        ("BM25", bm25_results),
        ("Jaccard", jaccard_results),
        ("Sentence BERT", sbert_results),
        ("BERTScore", bertscore_results),
    ]:
        print(f"\n{name}:")
        for metric, val in results.items():
            print(f"  {metric}: {val:.4f}")

    print("\nGenerating report logs...")
    generate_analysis_log("tfidf", dataset, tfidf_model, metrics=tfidf_results)
    generate_analysis_log("bm25", dataset, bm25_model, metrics=bm25_results)
    generate_analysis_log("jaccard", dataset, jaccard_model, metrics=jaccard_results)
    generate_analysis_log("sbert", dataset, sbert_model, metrics=sbert_results)
    generate_analysis_log("bertscore", dataset, bertscore_model, metrics=bertscore_results)

if __name__ == "__main__":
    main()
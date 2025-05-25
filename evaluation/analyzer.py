import os
import numpy as np

def generate_analysis_log(model_name, dataset, model, metrics=None, output_dir="reports", clean_previous=True):
    os.makedirs(output_dir, exist_ok=True)
    log_path = os.path.join(output_dir, f"{model_name}_performance.md")

    # Optional cleanup step
    if clean_previous and os.path.exists(log_path):
        os.remove(log_path)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(f"# Performance Analysis Report: {model_name}\n\n")

        # Quantitative Metrics Section
        if metrics:
            f.write("## Quantitative Metrics\n\n")
            for metric, value in metrics.items():
                f.write(f"- **{metric}**: {value:.4f}\n")
            f.write("\n---\n\n")

        # Qualitative Analysis Section
        f.write("## Qualitative Analysis\n\n")

        for i, group in enumerate(dataset):
            query = group["query"]
            passages = [p["text"] for p in group["passages"]]
            labels = [p["relevant"] for p in group["passages"]]
            tags = [p["label"] for p in group["passages"]]

            scores = model.rank(query, passages)
            sorted_indices = np.argsort(scores)[::-1]

            top1_idx = sorted_indices[0]
            top3_idx = sorted_indices[:3]

            correct_top1 = labels[top1_idx]

            f.write(f"### Example {i + 1}\n")
            f.write(f"**Query:** {query}\n\n")
            f.write(f"**Top-1 Match:**\n> {passages[top1_idx]}\n\n")
            f.write(f"**Top-1 Label:** `{tags[top1_idx]}` | **Relevant:** `{labels[top1_idx]}` | **Score:** `{scores[top1_idx]:.4f}`\n\n")

            if not correct_top1:
                f.write("❌ **Top-1 retrieval failed (irrelevant passage).**\n\n")
            else:
                f.write("✅ **Top-1 retrieval correct.**\n\n")

            f.write("**Top-3 Retrieved Passages:**\n")
            for rank, idx in enumerate(top3_idx, 1):
                rel = "✅" if labels[idx] else "❌"
                snippet = passages[idx][:100].strip().replace("\n", " ")
                f.write(f"{rank}. {rel} `{tags[idx]}` | Score: `{scores[idx]:.4f}` - {snippet}...\n")

            f.write("\n")

            # Edge Cases
            if all(label == 0 for label in labels):
                f.write("⚠️ **Edge Case:** All passages are irrelevant.\n\n")

            if all(label == 1 for label in labels):
                f.write("⚠️ **Edge Case:** All passages are relevant.\n\n")

            if sum(labels[idx] for idx in top3_idx) > 1 and not correct_top1:
                f.write("⚠️ **Edge Case:** Multiple relevant passages in top-3 but top-1 is incorrect.\n\n")

            f.write("\n---\n\n")
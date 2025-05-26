# Performance Analysis Report: tf-idf_cosine

## Quantitative Metrics

- **Precision@1**: 0.9800
- **Precision@3**: 0.7467
- **Recall@3**: 0.7467
- **MRR**: 0.9867
- **Runtime (in seconds)**: 6.4904
- **Peak Memory (in KB)**: 896.2490

---

## Qualitative Analysis

### Example 18
**Query:** What is 'legal education' requirement for lawyers in the Philippines?

**Top-1 Match:**
> Continuing legal education is mandatory for practicing lawyers to stay updated with developments in the law.

**Top-1 Label:** `irrelevant` | **Relevant:** `False` | **Score:** `0.2933`

❌ **Top-1 retrieval failed (irrelevant passage).**

**Top-3 Retrieved Passages:**
1. ❌ `irrelevant` | Score: `0.2933` - Continuing legal education is mandatory for practicing lawyers to stay updated with developments in...
2. ❌ `irrelevant` | Score: `0.2210` - The Integrated Bar of the Philippines is the national organization of lawyers....
3. ✅ `exact` | Score: `0.2133` - Legal education in the Philippines requires completion of a four-year Bachelor of Laws degree after...


---


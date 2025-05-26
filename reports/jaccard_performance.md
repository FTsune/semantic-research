# Performance Analysis Report: jaccard

## Quantitative Metrics

- **Precision@1**: 0.9600
- **Precision@3**: 0.6867
- **Recall@3**: 0.6867
- **MRR**: 0.9767
- **Runtime (in seconds)**: 6.1181
- **Peak Memory (in KB)**: 31746.8447

---

## Qualitative Analysis

### Example 11
**Query:** What is the concept of 'intellectual property rights' under Philippine law?

**Top-1 Match:**
> The Intellectual Property Office of the Philippines processes applications for IP registration.

**Top-1 Label:** `irrelevant` | **Relevant:** `False` | **Score:** `0.2727`

❌ **Top-1 retrieval failed (irrelevant passage).**

**Top-3 Retrieved Passages:**
1. ❌ `irrelevant` | Score: `0.2727` - The Intellectual Property Office of the Philippines processes applications for IP registration....
2. ✅ `exact` | Score: `0.1667` - Intellectual property rights are legal protections granted to creators and inventors for their creat...
3. ✅ `conceptual` | Score: `0.1429` - Legal systems incentivize innovation by providing creators with exclusive rights to their intellectu...

⚠️ **Edge Case:** Multiple relevant passages in top-3 but top-1 is incorrect.


---

### Example 18
**Query:** What is 'legal education' requirement for lawyers in the Philippines?

**Top-1 Match:**
> Continuing legal education is mandatory for practicing lawyers to stay updated with developments in the law.

**Top-1 Label:** `irrelevant` | **Relevant:** `False` | **Score:** `0.2500`

❌ **Top-1 retrieval failed (irrelevant passage).**

**Top-3 Retrieved Passages:**
1. ❌ `irrelevant` | Score: `0.2500` - Continuing legal education is mandatory for practicing lawyers to stay updated with developments in...
2. ❌ `irrelevant` | Score: `0.2222` - The Integrated Bar of the Philippines is the national organization of lawyers....
3. ✅ `exact` | Score: `0.1765` - Legal education in the Philippines requires completion of a four-year Bachelor of Laws degree after...


---


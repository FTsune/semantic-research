# Performance Analysis Report: bm25

## Quantitative Metrics

- **Precision@1**: 0.9400
- **Precision@3**: 0.6867
- **Recall@3**: 0.6867
- **MRR**: 0.9700
- **Runtime (in seconds)**: 6.0761
- **Peak Memory (in KB)**: 31821.6387

---

## Qualitative Analysis

### Example 18
**Query:** What is 'legal education' requirement for lawyers in the Philippines?

**Top-1 Match:**
> Continuing legal education is mandatory for practicing lawyers to stay updated with developments in the law.

**Top-1 Label:** `irrelevant` | **Relevant:** `False` | **Score:** `1.1576`

❌ **Top-1 retrieval failed (irrelevant passage).**

**Top-3 Retrieved Passages:**
1. ❌ `irrelevant` | Score: `1.1576` - Continuing legal education is mandatory for practicing lawyers to stay updated with developments in...
2. ✅ `exact` | Score: `0.9079` - Legal education in the Philippines requires completion of a four-year Bachelor of Laws degree after...
3. ❌ `irrelevant` | Score: `0.0000` - Notarial services require a commission from the court....


---

### Example 23
**Query:** What is the 'writ of kalikasan' in Philippine environmental law?

**Top-1 Match:**
> The Securities Regulation Code governs the registration and sale of securities in the Philippines.

**Top-1 Label:** `irrelevant` | **Relevant:** `False` | **Score:** `1.4552`

❌ **Top-1 retrieval failed (irrelevant passage).**

**Top-3 Retrieved Passages:**
1. ❌ `irrelevant` | Score: `1.4552` - The Securities Regulation Code governs the registration and sale of securities in the Philippines....
2. ✅ `paraphrase` | Score: `1.3358` - The writ of kalikasan allows citizens to seek court protection against large-scale environmental har...
3. ✅ `exact` | Score: `1.0840` - The writ of kalikasan is a legal remedy available to persons whose constitutional right to a balance...

⚠️ **Edge Case:** Multiple relevant passages in top-3 but top-1 is incorrect.


---

### Example 39
**Query:** What does 'double jeopardy' mean in the context of criminal law?

**Top-1 Match:**
> Criminal cases involve the state prosecuting a person for an alleged offense.

**Top-1 Label:** `irrelevant` | **Relevant:** `False` | **Score:** `1.2614`

❌ **Top-1 retrieval failed (irrelevant passage).**

**Top-3 Retrieved Passages:**
1. ❌ `irrelevant` | Score: `1.2614` - Criminal cases involve the state prosecuting a person for an alleged offense....
2. ✅ `paraphrase` | Score: `1.1413` - A person cannot be tried again for a crime for which they were already acquitted or convicted, which...
3. ✅ `exact` | Score: `1.0785` - Double jeopardy protects a person from being prosecuted twice for the same offense after acquittal o...

⚠️ **Edge Case:** Multiple relevant passages in top-3 but top-1 is incorrect.


---


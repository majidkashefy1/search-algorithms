# ✍️ String Search Algorithms Explained

This guide introduces key **string search (pattern matching) algorithms**, used to find occurrences of one string (pattern) inside another (text). These algorithms are essential in text editors, search engines, DNA analysis, and data cleaning.

---

## 1️⃣ Naive (Brute Force) Search

### 💡 Concept

The simplest approach: check the pattern at every possible position in the text.

**Analogy:** Like scanning each page of a book line by line to find a specific word.

### ⚙️ Step-by-Step

1. Start from the first character of the text.
2. Compare the pattern with the substring of the same length.
3. If all characters match, record the index.
4. If not, move one character forward and repeat.

### 🧩 Pseudocode

```
NaiveSearch(text, pattern):
    for i in range(0, len(text) - len(pattern) + 1):
        match = True
        for j in range(0, len(pattern)):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            print("Pattern found at index", i)
```

### ⏱️ Complexity

* **Time:** O(n × m) (n = text length, m = pattern length)
* **Space:** O(1)

### ✅ When to Use

* For small texts or single search queries.

### ⚖️ Comparison

* Naive search is **simple** but inefficient for long texts.
* Advanced algorithms like **KMP** and **Rabin–Karp** reduce redundant comparisons.

---

## 2️⃣ Knuth–Morris–Pratt (KMP) Algorithm

### 💡 Concept

KMP avoids re-checking previously matched characters by precomputing a **Longest Prefix Suffix (LPS)** table.

**Analogy:** If you’re reading a sentence and spot a mismatch, you remember how much of the pattern already matched and jump forward intelligently.

### ⚙️ Step-by-Step

1. Preprocess the pattern to create an LPS array:

    * LPS[i] = length of longest prefix which is also a suffix for substring[0..i].
2. While matching text:

    * On mismatch, use LPS to skip unnecessary comparisons.

### 🧩 Pseudocode

```
KMP(text, pattern):
    lps = computeLPS(pattern)
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1; j += 1
        if j == len(pattern):
            print("Pattern found at index", i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
```

### ⏱️ Complexity

* **Time:** O(n + m)
* **Space:** O(m)

### ✅ When to Use

* Large texts with repetitive patterns.
* Searching inside logs, DNA sequences, or codebases.

### ⚖️ Comparison

* Much faster than Naive search on repeated substrings.
* Unlike Rabin–Karp, no hashing involved (no false positives).

---

## 3️⃣ Rabin–Karp Algorithm

### 💡 Concept

Uses a **hash function** to compare pattern and substring hashes instead of direct character-by-character comparison.

**Analogy:** Like comparing fingerprints — if two fingerprints (hashes) match, then check them closely (verify characters).

### ⚙️ Step-by-Step

1. Compute hash of pattern and first substring of text.
2. Slide window by one character and update hash efficiently.
3. If hashes match, compare actual substring to confirm.

### 🧩 Pseudocode

```
RabinKarp(text, pattern, base=256, prime=101):
    m = len(pattern); n = len(text)
    pattern_hash = hash(pattern)
    text_hash = hash(text[0:m])

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i+m] == pattern:
                print("Pattern found at index", i)
        if i < n - m:
            text_hash = rehash(text, i, i+m, base, prime)
```

### ⏱️ Complexity

* **Time:** O(n + m) average, O(nm) worst (if many hash collisions)
* **Space:** O(1)

### ✅ When to Use

* Searching multiple patterns efficiently.
* Ideal for plagiarism detection or string fingerprinting.

### ⚖️ Comparison

* Faster on average than Naive search.
* KMP guarantees linear time; Rabin–Karp depends on good hash function.

---

## 🧭 Summary Table

| Algorithm  | Key Idea                        | Average Time | Best For                  | Uses Extra Memory |
| ---------- | ------------------------------- | ------------ | ------------------------- | ----------------- |
| Naive      | Compare all positions           | O(n × m)     | Small texts               | ❌                 |
| KMP        | Skip repeats using prefix table | O(n + m)     | Large repetitive data     | ✅ (LPS array)     |
| Rabin–Karp | Hash-based matching             | O(n + m) avg | Multiple pattern matching | ✅ (hash values)   |

---
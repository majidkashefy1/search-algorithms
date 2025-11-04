# 🧠 Search Algorithms API (Dockerized)

This project is a **learning-friendly API** that demonstrates multiple **search algorithms** implemented in Python and exposed through a **Flask REST API**. You can easily build and run it using **Docker** or **Docker Compose**.

---

## 📚 Overview
This API allows you to experiment with different search algorithms and see how they behave under various conditions (sorted/unsorted arrays, uniform/non-uniform distributions, etc.). Each algorithm has its own endpoint, and all return the index of the target value (or `-1` if not found).

### Supported Algorithms
1. **Linear Search**
2. **Binary Search**
3. **Jump Search**
4. **Interpolation Search**
5. **Exponential Search**
6. **Fibonacci Search**

---

## ⚙️ How to Run

### 🐳 Using Docker
```bash
docker build -t search-algorithms:latest .
docker run -p 5000:5000 --rm search-algorithms:latest
```

### 🧩 Using Docker Compose
```bash
docker-compose up --build
```

### 🧪 Test Example
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"array": [2,5,8,12,16,23,38,56,72,91], "target": 23}' \
http://localhost:5000/binary-search
```

Expected Response:
```json
{
  "algorithm": "binary_search",
  "sorted_array": [2,5,8,12,16,23,38,56,72,91],
  "index": 5
}
```

---

## 🧮 Algorithm Explanations

### 1️⃣ Linear Search
**Concept:** Checks every element one by one until it finds the target or reaches the end.

**Works On:** Sorted or Unsorted Arrays

**Time Complexity:** O(n)

**Example:**
```
List: [10, 20, 30, 40, 50]
Target: 40 → Found at index 3
```

**Pros:** Simple, no sorting needed.  
**Cons:** Slow for large lists.

#### 🔍 Detailed Explanation
**Real-life analogy:** Imagine you’re searching for a name in an unsorted list of papers. You check each one until you find the right name — that’s linear search.

**Steps:**
1. Start from the first element.
2. Compare each element with the target.
3. If you find a match, return the index.
4. If you reach the end, return -1.

**Pseudocode:**
```
for i from 0 to length(array) - 1:
    if array[i] == target:
        return i
return -1
```

**When to use:** When the dataset is small or unsorted.  
**Comparison:** Slower than all others for large datasets.

---

### 2️⃣ Binary Search
**Concept:** Divides a sorted list in half repeatedly, checking the middle value each time.

**Works On:** Sorted Arrays Only

**Time Complexity:** O(log n)

**Example:**
```
List: [10, 20, 30, 40, 50]
Target: 40
→ Check mid (30), 40 > 30, move right.
→ Found at index 3.
```

**Pros:** Extremely fast for large sorted data.  
**Cons:** Requires sorted array.

#### 🔍 Detailed Explanation
**Real-life analogy:** Searching for a word in a dictionary — you open the middle, see if your word is before or after, and keep narrowing down.

**Steps:**
1. Sort the array (if not already sorted).
2. Find the middle element.
3. If it’s equal to the target → done.
4. If target < middle → search left half.
5. If target > middle → search right half.
6. Repeat until found or range is empty.

**Pseudocode:**
```
low = 0
high = length(array) - 1
while low <= high:
    mid = (low + high) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
return -1
```

**When to use:** Large, sorted datasets.  
**Comparison:** Much faster than linear search but needs sorting.

---

### 3️⃣ Jump Search
**Concept:** Jumps ahead by √n steps until it finds a block containing the target, then performs a linear search within that block.

**Works On:** Sorted Arrays

**Time Complexity:** O(√n)

**Example:**
```
List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Target: 8
→ Jump by 3 (√9 = 3) → Stops near 7 → Linear search block → Found.
```

**Pros:** Faster than linear search for large sorted lists.  
**Cons:** Still slower than binary search.

#### 🔍 Detailed Explanation
**Real-life analogy:** Looking for a page in a book by flipping several pages at once, then checking carefully once near the right spot.

**Steps:**
1. Jump ahead by fixed steps (√n).
2. If target > current element, keep jumping.
3. When target ≤ current element, stop.
4. Perform linear search in the last jump block.

**Pseudocode:**
```
step = √n
prev = 0
while array[min(step, n)-1] < target:
    prev = step
    step += √n
    if prev >= n:
        return -1
for i from prev to step:
    if array[i] == target:
        return i
return -1
```

**When to use:** Sorted lists where binary search isn’t suitable.  
**Comparison:** Trade-off between simplicity and performance.

---

### 4️⃣ Interpolation Search
**Concept:** Like binary search but estimates where the target might be based on value distribution.

**Works On:** Uniformly Distributed Sorted Data

**Time Complexity:** O(log log n) (best case), O(n) (worst case)

**Example:**
```
List: [10, 20, 30, 40, 50]
Target: 40 → Predicted position ≈ index 3 → Found.
```

**Pros:** Faster on uniformly distributed data.  
**Cons:** Unstable on non-uniform data.

#### 🔍 Detailed Explanation
**Real-life analogy:** If you’re guessing someone’s age in a class where ages range evenly, you can estimate where to start.

**Steps:**
1. Use interpolation formula to predict the likely position:
   `pos = low + ((target - array[low]) * (high - low)) / (array[high] - array[low])`
2. Compare target with array[pos].
3. Adjust low/high accordingly until found.

**Pseudocode:**
```
while low <= high and target >= array[low] and target <= array[high]:
    pos = low + ((target - array[low]) * (high - low)) // (array[high] - array[low])
    if array[pos] == target:
        return pos
    if array[pos] < target:
        low = pos + 1
    else:
        high = pos - 1
return -1
```

**When to use:** Data is evenly distributed.  
**Comparison:** Smarter than binary search on uniform data.

---

### 5️⃣ Exponential Search
**Concept:** Doubles the range (1, 2, 4, 8, ...) until it finds a block containing the target, then performs binary search inside that block.

**Works On:** Sorted Arrays

**Time Complexity:** O(log n)

**Example:**
```
List: [1, 3, 5, 7, 9, 11, 13]
Target: 9 → Range 1, 2, 4, 8 → Found range → Binary search → Found.
```

**Pros:** Ideal for unbounded/infinite data sets.  
**Cons:** Requires sorted array.

#### 🔍 Detailed Explanation
**Real-life analogy:** Searching through an unending bookshelf — you look at every 1st, 2nd, 4th, 8th book until you pass the target, then search back.

**Steps:**
1. Start at index 1.
2. Double the index until array[i] > target.
3. Perform binary search between last two indexes.

**Pseudocode:**
```
if array[0] == target:
    return 0
index = 1
while index < n and array[index] <= target:
    index *= 2
return binary_search(array, index//2, min(index, n-1), target)
```

**When to use:** When list size is unknown or infinite.  
**Comparison:** Combination of binary and dynamic range detection.

---

### 6️⃣ Fibonacci Search
**Concept:** Similar to binary search but divides the list based on Fibonacci numbers.

**Works On:** Sorted Arrays

**Time Complexity:** O(log n)

**Example:**
```
List: [10, 22, 35, 40, 45, 50, 80]
Target: 45 → Uses Fibonacci numbers (1, 2, 3, 5, 8, ...)
→ Determines partition → Found.
```

**Pros:** Works well on slower memory (like disk-based systems).  
**Cons:** More complex implementation.

#### 🔍 Detailed Explanation
**Real-life analogy:** You have a ruler marked by Fibonacci steps — each step helps you divide the search range efficiently.

**Steps:**
1. Generate Fibonacci numbers until one exceeds array length.
2. Use them to partition the search space.
3. Move index using smaller Fibonacci offsets until found.

**Pseudocode:**
```
while (fibM > 1):
    i = min(offset + fibMM2, n-1)
    if array[i] < target:
        fibM = fibMM1
        fibMM1 = fibMM2
        fibMM2 = fibM - fibMM1
        offset = i
    elif array[i] > target:
        fibM = fibMM2
        fibMM1 = fibMM1 - fibMM2
        fibMM2 = fibM - fibMM1
    else:
        return i
return -1
```

**When to use:** Sequential access environments.  
**Comparison:** Similar to binary search but can be more efficient in specific systems.

---

## 🔍 API Endpoints

| Endpoint | Algorithm | Sorted Required | Typical Time Complexity |
|-----------|------------|-----------------|--------------------------|
| `/linear-search` | Linear Search | ❌ No | O(n) |
| `/binary-search` | Binary Search | ✅ Yes | O(log n) |
| `/jump-search` | Jump Search | ✅ Yes | O(√n) |
| `/interpolation-search` | Interpolation Search | ✅ Yes | O(log log n) |
| `/exponential-search` | Exponential Search | ✅ Yes | O(log n) |
| `/fibonacci-search` | Fibonacci Search | ✅ Yes | O(log n) |

---

## 📘 Example JSON Payload
```json
{
  "array": [2, 5, 8, 12, 16, 23, 38, 56, 72, 91],
  "target": 23
}
```

---

## 🧑‍💻 Developer Notes
- Each algorithm is implemented independently under `/algorithms`.
- For Binary, Jump, Interpolation, Exponential, and Fibonacci — ensure the input array is **sorted**.
- Flask handles API routing, and Gunicorn runs the production server inside Docker.

---

## 🧩 Running Tests (Developers)
If you run tests locally, ensure the Python path includes the project root:

```bash
pytest -q
```

(Pytest will automatically detect paths if you use the provided `conftest.py`.)

---
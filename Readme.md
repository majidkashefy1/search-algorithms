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

## 💡 Learning Tip
Try modifying the array size and order to see how each algorithm performs differently.

If you want to **document your learning or generate algorithm reports automatically**, you can use [**Jenni AI**](https://jenni.ai/?via=lekys) — it helps you write, organize, and research efficiently.

---

## 🧩 Credits
Created as a practical learning project for understanding **search algorithms**, **Flask APIs**, and **Docker deployment**.

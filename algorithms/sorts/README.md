# 🔢 Sorting Algorithms (Beginner Friendly Guide)

Sorting algorithms are methods for **arranging data in a specific order**, such as ascending or descending. They’re fundamental in computer science and appear everywhere — from organizing your contact list to optimizing database queries.

---

## 📘 Overview

Sorting makes searching and analyzing data faster and easier. There are many sorting algorithms, each with trade-offs in **speed, memory use, and complexity**.

This guide covers five foundational algorithms:

1. **Bubble Sort** 🫧
2. **Insertion Sort** 🧩
3. **Selection Sort** 🎯
4. **Merge Sort** 🧵
5. **Quick Sort** ⚡

---

## 1️⃣ Bubble Sort

**Concept:**
Compares adjacent elements and swaps them if they’re in the wrong order — repeatedly — until the list is sorted.

**Real-Life Analogy:**
Imagine you’re arranging books on a shelf by height. You keep comparing pairs and swapping them if one is taller than the other. Eventually, the biggest book “bubbles” to the rightmost position.

**Steps:**

1. Compare the first two elements.
2. If they’re in the wrong order, swap them.
3. Move to the next pair.
4. Repeat until the list is sorted.

**Pseudocode:**

```
for i from 0 to n-1:
    for j from 0 to n-i-2:
        if array[j] > array[j+1]:
            swap(array[j], array[j+1])
```

**Time Complexity:** O(n²)
**Space Complexity:** O(1)
**Pros:** Simple to implement.
**Cons:** Very slow for large datasets.
**When to Use:** For educational purposes or very small lists.

---

## 2️⃣ Insertion Sort

**Concept:**
Builds the final sorted array one element at a time by inserting each new element into its proper position.

**Real-Life Analogy:**
Like sorting playing cards in your hand — you pick up a new card and place it where it belongs among the cards you already sorted.

**Steps:**

1. Assume the first element is sorted.
2. Take the next element and compare backward.
3. Insert it in the correct position.
4. Repeat for all elements.

**Pseudocode:**

```
for i from 1 to n-1:
    key = array[i]
    j = i - 1
    while j >= 0 and array[j] > key:
        array[j+1] = array[j]
        j = j - 1
    array[j+1] = key
```

**Time Complexity:** O(n²)
**Space Complexity:** O(1)
**Pros:** Efficient for small or nearly sorted data.
**Cons:** Inefficient for large lists.
**When to Use:** When you expect small, mostly sorted data (like adding new entries to a sorted list).

---

## 3️⃣ Selection Sort

**Concept:**
Selects the smallest (or largest) element from the unsorted part and places it at the correct position.

**Real-Life Analogy:**
Suppose you’re arranging marbles from smallest to largest. You repeatedly find the smallest one and move it to the beginning.

**Steps:**

1. Find the smallest element.
2. Swap it with the first element.
3. Move the boundary between sorted and unsorted.
4. Repeat until fully sorted.

**Pseudocode:**

```
for i from 0 to n-1:
    min_index = i
    for j from i+1 to n:
        if array[j] < array[min_index]:
            min_index = j
    swap(array[i], array[min_index])
```

**Time Complexity:** O(n²)
**Space Complexity:** O(1)
**Pros:** Simple and performs fewer swaps.
**Cons:** Still inefficient on large data.
**When to Use:** When memory writes are costly and you want fewer swaps.

---

## 4️⃣ Merge Sort

**Concept:**
Divides the array into halves, sorts each half, then merges them back together in order.

**Real-Life Analogy:**
Think of organizing two stacks of sorted papers — you merge them by picking the smallest top paper from either stack.

**Steps:**

1. Divide the array into halves recursively.
2. Sort each half.
3. Merge the two sorted halves.

**Pseudocode:**

```
function merge_sort(array):
    if length(array) > 1:
        mid = length(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, array)
```

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)
**Pros:** Very efficient and stable.
**Cons:** Uses more memory.
**When to Use:** For large datasets when stability matters (e.g., sorting records by multiple fields).

---

## 5️⃣ Quick Sort

**Concept:**
Selects a pivot element and partitions the array into two halves — smaller and larger — then recursively sorts each half.

**Real-Life Analogy:**
Imagine dividing books into two piles — those shorter and those taller than a chosen one. Then repeat the process for each pile.

**Steps:**

1. Choose a pivot.
2. Rearrange elements: smaller on left, larger on right.
3. Recursively sort the subarrays.

**Pseudocode:**

```
function quick_sort(array):
    if length(array) <= 1:
        return array
    pivot = array[last]
    left = [x for x in array if x < pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
```

**Time Complexity:** O(n log n) (average), O(n²) (worst)
**Space Complexity:** O(log n)
**Pros:** Very fast on average.
**Cons:** Performance drops with poor pivot choices.
**When to Use:** Great general-purpose sorter for large in-memory datasets.

---

## ⚖️ Comparison Table

| Algorithm      | Best Case  | Average Case | Worst Case | Space    | Stable | Notes                 |
| -------------- | ---------- | ------------ | ---------- | -------- | ------ | --------------------- |
| Bubble Sort    | O(n)       | O(n²)        | O(n²)      | O(1)     | ✅      | Good for learning     |
| Insertion Sort | O(n)       | O(n²)        | O(n²)      | O(1)     | ✅      | Best for small lists  |
| Selection Sort | O(n²)      | O(n²)        | O(n²)      | O(1)     | ❌      | Few swaps             |
| Merge Sort     | O(n log n) | O(n log n)   | O(n log n) | O(n)     | ✅      | Stable & efficient    |
| Quick Sort     | O(n log n) | O(n log n)   | O(n²)      | O(log n) | ❌      | Very fast in practice |

---

## 🧩 Next Step

Continue learning with:

* 🔍 [Search Algorithms](../searches/README_searches.md)
* 🌐 [Graph Algorithms](../graphs/README.md)
* ✍️ [String Algorithms](../strings/README_strings.md)

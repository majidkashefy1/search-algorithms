# 🌐 Graph Algorithms Explained

This guide introduces key **graph traversal and pathfinding algorithms** that help you navigate networks of connected nodes (like social networks, maps, or dependency trees). It’s designed for beginners, with analogies, step-by-step logic, pseudocode, and comparisons.

---

## 1️⃣ Breadth-First Search (BFS)

### 💡 Concept

BFS explores a graph **level by level**, visiting all neighbors of a node before moving deeper.

**Analogy:** Imagine spreading a rumor — everyone who hears it passes it to all their friends at the same time, level by level.

### ⚙️ Step-by-Step

1. Start from a chosen node (source).
2. Visit it and mark as visited.
3. Add all unvisited neighbors to a queue.
4. Take the next node from the queue and repeat until the queue is empty.

### 🧩 Pseudocode

```
BFS(graph, start):
    create a queue Q
    mark start as visited
    enqueue(start)
    while Q is not empty:
        node = dequeue(Q)
        for each neighbor of node:
            if neighbor not visited:
                mark visited
                enqueue(neighbor)
```

### ⏱️ Complexity

* **Time:** O(V + E) (V = vertices, E = edges)
* **Space:** O(V)

### ✅ When to Use

* Finding shortest path in **unweighted graphs**
* Level order traversal (like in trees)

### ⚖️ Comparison

* BFS uses a **queue**, exploring layer by layer.
* DFS (below) uses a **stack**, diving deep first.

---

## 2️⃣ Depth-First Search (DFS)

### 💡 Concept

DFS explores as far as possible along a branch before backtracking.

**Analogy:** Imagine exploring a maze — you follow one path until a dead end, then go back and try another.

### ⚙️ Step-by-Step

1. Start from a source node.
2. Visit and mark it.
3. For each unvisited neighbor, recursively apply DFS.
4. Backtrack when no unvisited neighbors remain.

### 🧩 Pseudocode

```
DFS(graph, start, visited):
    mark start as visited
    for each neighbor in graph[start]:
        if neighbor not visited:
            DFS(graph, neighbor, visited)
```

### ⏱️ Complexity

* **Time:** O(V + E)
* **Space:** O(V) (recursive stack)

### ✅ When to Use

* Detecting **cycles** in a graph
* Topological sorting
* Solving **mazes** and puzzles

### ⚖️ Comparison

* DFS is **memory-efficient** for sparse graphs.
* BFS is better for shortest path problems.

---

## 3️⃣ Dijkstra’s Algorithm

### 💡 Concept

Finds the **shortest path** between nodes in a weighted graph (non-negative weights).

**Analogy:** Think of navigating a city map — each road has a travel time, and Dijkstra finds the fastest route.

### ⚙️ Step-by-Step

1. Assign a tentative distance value: 0 for start, infinity for all others.
2. Mark all nodes unvisited. Set the start node as current.
3. For current node, check all unvisited neighbors and calculate new distances.
4. If new distance < old, update it.
5. Mark the current node as visited and move to the unvisited node with smallest tentative distance.
6. Repeat until all nodes are visited or destination is reached.

### 🧩 Pseudocode

```
Dijkstra(graph, start):
    dist[start] = 0
    for each node != start:
        dist[node] = infinity
    priority_queue = [start]

    while priority_queue not empty:
        node = extract_min(priority_queue)
        for each neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                update priority_queue
```

### ⏱️ Complexity

* **Time:** O((V + E) log V) using a priority queue
* **Space:** O(V)

### ✅ When to Use

* Finding shortest routes in **maps**, **networks**, **routing systems**.

### ⚖️ Comparison

* Works only with **non-negative edge weights**.
* For graphs with negative edges, use **Bellman-Ford**.

---

## 4️⃣ A* (A-Star) Search

### 💡 Concept

A* improves Dijkstra’s by using a **heuristic** to guide the search toward the goal faster.

**Analogy:** Like Dijkstra’s GPS but with intuition — it “guesses” which paths look closer to the destination.

### ⚙️ Step-by-Step

1. Each node has: `f(n) = g(n) + h(n)`

    * `g(n)` = cost from start to current node
    * `h(n)` = estimated cost from current to goal (heuristic)
2. Use a priority queue sorted by lowest `f(n)`.
3. Expand nodes until the goal is reached.

### 🧩 Pseudocode

```
A*(start, goal, graph, heuristic):
    open_set = priority_queue([start])
    g[start] = 0
    f[start] = heuristic(start, goal)

    while open_set not empty:
        node = extract_min(open_set)
        if node == goal:
            return reconstruct_path()

        for neighbor, cost in graph[node]:
            tentative_g = g[node] + cost
            if tentative_g < g.get(neighbor, infinity):
                g[neighbor] = tentative_g
                f[neighbor] = g[neighbor] + heuristic(neighbor, goal)
                add neighbor to open_set
```

### ⏱️ Complexity

* **Time:** Depends on heuristic; typically O(E)
* **Space:** O(V)

### ✅ When to Use

* Pathfinding in **games**, **robots**, **maps**, and **AI navigation**.

### ⚖️ Comparison

* A* is **faster than Dijkstra** if the heuristic is good.
* With heuristic = 0, A* behaves exactly like Dijkstra.

---

## 🧭 Summary Table

| Algorithm | Use Case                                  | Weighted | Finds Shortest Path | Key Structure              |
| --------- | ----------------------------------------- | -------- | ------------------- | -------------------------- |
| BFS       | Unweighted shortest path, level traversal | ❌        | ✅                   | Queue                      |
| DFS       | Exploring paths, cycle detection          | ❌        | ❌                   | Stack / Recursion          |
| Dijkstra  | Shortest path (non-negative weights)      | ✅        | ✅                   | Priority Queue             |
| A*        | Optimized shortest path with heuristic    | ✅        | ✅                   | Priority Queue + Heuristic |

---
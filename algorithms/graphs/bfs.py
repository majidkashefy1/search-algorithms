from collections import deque
from typing import Dict, List, Any

def bfs(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Breadth-first search on adjacency-list graph.
    graph: dict[node] = list_of_neighbors
    Returns list of visited nodes in BFS order.
    """
    visited = []
    queue = deque([start])
    seen = set([start])

    while queue:
        v = queue.popleft()
        visited.append(v)
        for neighbor in graph.get(v, []):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return visited

import heapq
from typing import Dict, Any

def dijkstra(graph: Dict[Any, Dict[Any, float]], start: Any) -> Dict[Any, float]:
    """
    Dijkstra's shortest paths from start.
    graph: node -> {neighbor: weight, ...}
    Returns dict of distances.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        dist_u, u = heapq.heappop(pq)
        if dist_u > distances[u]:
            continue
        for v, w in graph[u].items():
            alt = dist_u + w
            if alt < distances.get(v, float('inf')):
                distances[v] = alt
                heapq.heappush(pq, (alt, v))
    return distances

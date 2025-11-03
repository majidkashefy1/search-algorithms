import heapq
from typing import Dict, Tuple, Callable, Any, List

def a_star(start: Any, goal: Any,
           neighbors_fn: Callable[[Any], List[Tuple[Any, float]]],
           heuristic_fn: Callable[[Any, Any], float]) -> List[Any]:
    """
    A* search that returns path from start to goal (list of nodes) or empty list if none.
    neighbors_fn(node) -> list of (neighbor, cost)
    heuristic_fn(a, b) -> estimated cost from a to b
    """
    open_set = []
    heapq.heappush(open_set, (0 + heuristic_fn(start, goal), 0, start, None))
    came_from = {}
    g_score = {start: 0}
    closed = set()

    while open_set:
        _, current_g, current, parent = heapq.heappop(open_set)

        if current in closed:
            continue

        came_from[current] = parent

        if current == goal:
            # reconstruct path
            path = []
            node = current
            while node is not None:
                path.append(node)
                node = came_from.get(node)
            return list(reversed(path))

        closed.add(current)

        for neighbor, cost in neighbors_fn(current):
            tentative_g = current_g + cost
            if neighbor in closed and tentative_g >= g_score.get(neighbor, float('inf')):
                continue
            if tentative_g < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic_fn(neighbor, goal)
                heapq.heappush(open_set, (f, tentative_g, neighbor, current))

    return []

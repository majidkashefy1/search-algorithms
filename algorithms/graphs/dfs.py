from typing import Dict, List, Any

def dfs(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Depth-first search (iterative) returning visitation order.
    """
    visited = []
    stack = [start]
    seen = set()

    while stack:
        v = stack.pop()
        if v in seen:
            continue
        seen.add(v)
        visited.append(v)
        # push neighbors in reverse to have natural order
        for neighbor in reversed(graph.get(v, [])):
            if neighbor not in seen:
                stack.append(neighbor)
    return visited

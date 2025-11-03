from typing import List, Any
import heapq

def heap_sort(arr: List[Any]) -> List[Any]:
    """
    Heap sort using Python's heapq module.
    Returns a new sorted list.
    """
    a = list(arr)
    heapq.heapify(a)
    return [heapq.heappop(a) for _ in range(len(a))]

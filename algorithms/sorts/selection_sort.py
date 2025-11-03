from typing import List, Any

def selection_sort(arr: List[Any]) -> List[Any]:
    """
    Selection sort: repeatedly select min and place at front.
    Returns a new sorted list.
    """
    a = list(arr)
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

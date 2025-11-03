from typing import List, Any

def quick_sort(arr: List[Any]) -> List[Any]:
    """
    Quick sort (simple functional implementation).
    Returns a new sorted list.
    """
    if len(arr) <= 1:
        return list(arr)
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

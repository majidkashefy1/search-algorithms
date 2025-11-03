from typing import List, Any

def insertion_sort(arr: List[Any]) -> List[Any]:
    """
    Insertion sort: good for small or nearly-sorted data.
    Returns a new sorted list.
    """
    a = list(arr)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

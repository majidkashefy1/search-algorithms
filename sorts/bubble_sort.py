from typing import List, Any

def bubble_sort(arr: List[Any]) -> List[Any]:
    """
    Bubble sort: in-place kind-of, returns new list sorted ascending.
    Not efficient for large arrays.
    """
    a = list(arr)
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

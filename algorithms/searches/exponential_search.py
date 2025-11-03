from algorithms.searches.binary_search import binary_search

def exponential_search(arr, target):
    """Exponential Search - finds the range, then uses binary search."""
    if len(arr) == 0:
        return -1
    if arr[0] == target:
        return 0

    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2

    return binary_search(arr[:min(i, len(arr))], target)

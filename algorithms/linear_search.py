def linear_search(arr, target):
    """Simple linear search algorithm."""
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

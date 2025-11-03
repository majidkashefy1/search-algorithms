def interpolation_search(arr, target):
    """Interpolation Search (works best with uniformly distributed sorted data)."""
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            return low if arr[low] == target else -1

        pos = low + int(
            (float(high - low) / (arr[high] - arr[low]) * (target - arr[low]))
        )

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

def naive_search(text: str, pattern: str) -> int:
    """
    Naive substring search: returns starting index of first occurrence or -1.
    """
    n = len(text); m = len(pattern)
    if m == 0:
        return 0
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            return i
    return -1

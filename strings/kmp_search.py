from typing import List

def _compute_lps(pattern: str) -> List[int]:
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text: str, pattern: str) -> int:
    """
    Knuth-Morris-Pratt pattern search. Returns index of first match or -1.
    """
    n = len(text); m = len(pattern)
    if m == 0:
        return 0
    lps = _compute_lps(pattern)
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1; j += 1
            if j == m:
                return i - j
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return -1

def rabin_karp(text: str, pattern: str, base=256, mod=101) -> int:
    """
    Rabin-Karp string search using rolling hash.
    Returns index of first occurrence or -1.
    Default mod is a small prime for demonstration; in production pick a large prime.
    """
    n = len(text); m = len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1

    hpattern = 0
    htext = 0
    h = 1  # base^(m-1) % mod

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        hpattern = (base * hpattern + ord(pattern[i])) % mod
        htext = (base * htext + ord(text[i])) % mod

    for i in range(n - m + 1):
        if hpattern == htext:
            # possible match, verify
            if text[i:i+m] == pattern:
                return i
        if i < n - m:
            htext = (base * (htext - ord(text[i]) * h) + ord(text[i+m])) % mod
            if htext < 0:
                htext += mod
    return -1

# tests/test_strings.py
from algorithms.strings.naive_search import naive_search
from algorithms.strings.kmp_search import kmp_search
from algorithms.strings.rabin_karp import rabin_karp

TEXT = "the quick brown fox jumps over the lazy dog"
PAT = "jumps"

def test_naive():
    assert naive_search(TEXT, PAT) == TEXT.index(PAT)

def test_kmp():
    assert kmp_search(TEXT, PAT) == TEXT.index(PAT)

def test_rabin():
    assert rabin_karp(TEXT, PAT) == TEXT.index(PAT)

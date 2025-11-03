# tests/test_searches.py
import pytest
from algorithms.searches.linear_search import linear_search
from algorithms.searches.binary_search import binary_search
from algorithms.searches.jump_search import jump_search
from algorithms.searches.interpolation_search import interpolation_search
from algorithms.searches.exponential_search import exponential_search
from algorithms.searches.fibonacci_search import fibonacci_search

S = [2,5,8,12,16,23,38,56,72,91]

def test_linear_search_found():
    assert linear_search(S, 23) == 5

def test_linear_search_not_found():
    assert linear_search(S, 7) == -1

def test_binary_search_found():
    assert binary_search(S, 38) == 6

def test_jump_search_found():
    assert jump_search(S, 56) == 7

def test_interpolation_search_found():
    assert interpolation_search(S, 72) == 8

def test_exponential_search_found():
    assert exponential_search(S, 16) == 4

def test_fibonacci_search_found():
    assert fibonacci_search(S, 91) == 9

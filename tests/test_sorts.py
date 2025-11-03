# tests/test_sorts.py
from algorithms.sorts.bubble_sort import bubble_sort
from algorithms.sorts.selection_sort import selection_sort
from algorithms.sorts.insertion_sort import insertion_sort
from algorithms.sorts.merge_sort import merge_sort
from algorithms.sorts.quick_sort import quick_sort
from algorithms.sorts.heap_sort import heap_sort

A = [5,2,9,1,5,6]
SORTED = [1,2,5,5,6,9]

def test_bubble():
    assert bubble_sort(A) == SORTED

def test_selection():
    assert selection_sort(A) == SORTED

def test_insertion():
    assert insertion_sort(A) == SORTED

def test_merge():
    assert merge_sort(A) == SORTED

def test_quick():
    assert quick_sort(A) == SORTED

def test_heap():
    assert heap_sort(A) == SORTED

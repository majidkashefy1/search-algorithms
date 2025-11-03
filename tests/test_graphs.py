# tests/test_graphs.py
from algorithms.graphs.bfs import bfs
from algorithms.graphs.dfs import dfs
from algorithms.graphs.dijkstra import dijkstra

GRAPH = {
    "A": ["B","C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

def test_bfs():
    order = bfs(GRAPH, "A")
    assert "A" in order and "B" in order

def test_dfs():
    order = dfs(GRAPH, "A")
    assert order[0] == "A"

def test_dijkstra_simple():
    g = {
        "A": {"B": 1, "C": 4},
        "B": {"C": 2, "D": 5},
        "C": {"D": 1},
        "D": {}
    }
    dist = dijkstra(g, "A")
    assert dist["D"] == 4  # A->B->C->D cost 1+2+1 = 4

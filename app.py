# app.py
from flask import Flask, request, jsonify
from typing import Any, Dict

# --- IMPORT SEARCH ALGORITHMS ---
from algorithms.searches.linear_search import linear_search
from algorithms.searches.binary_search import binary_search
from algorithms.searches.jump_search import jump_search
from algorithms.searches.interpolation_search import interpolation_search
from algorithms.searches.exponential_search import exponential_search
from algorithms.searches.fibonacci_search import fibonacci_search

# --- IMPORT SORT ALGORITHMS ---
from algorithms.sorts.bubble_sort import bubble_sort
from algorithms.sorts.selection_sort import selection_sort
from algorithms.sorts.insertion_sort import insertion_sort
from algorithms.sorts.merge_sort import merge_sort
from algorithms.sorts.quick_sort import quick_sort
from algorithms.sorts.heap_sort import heap_sort

# --- IMPORT GRAPH ALGORITHMS ---
from algorithms.graphs.bfs import bfs
from algorithms.graphs.dfs import dfs
from algorithms.graphs.dijkstra import dijkstra
from algorithms.graphs.astar import a_star

# --- IMPORT STRING ALGORITHMS ---
from algorithms.strings.naive_search import naive_search
from algorithms.strings.kmp_search import kmp_search
from algorithms.strings.rabin_karp import rabin_karp

app = Flask(__name__)

# Helper: validate json
def json_req():
    data = request.get_json(force=True)
    if data is None:
        return None, ({"error": "Invalid JSON body"}, 400)
    return data, None

# --- SEARCH ENDPOINTS ---
# We support `/search/<algo>` where algo is one of: linear,binary,jump,interpolation,exponential,fibonacci
@app.route("/search/<algo>", methods=["POST"])
def search_route(algo: str):
    data, err = json_req()
    if err:
        return err
    arr = data.get("array")
    target = data.get("target")
    if arr is None or target is None:
        return jsonify({"error": "Please provide 'array' and 'target' fields"}), 400

    # mapping
    algo_map = {
        "linear": (linear_search, False),
        "binary": (binary_search, True),
        "jump": (jump_search, True),
        "interpolation": (interpolation_search, True),
        "exponential": (exponential_search, True),
        "fibonacci": (fibonacci_search, True)
    }

    if algo not in algo_map:
        return jsonify({"error": f"Unknown search algorithm '{algo}'"}), 404

    func, requires_sorted = algo_map[algo]

    arr_input = list(arr)
    arr_used = sorted(arr_input) if requires_sorted else arr_input

    index = func(arr_used, target)
    response = {
        "algorithm": algo,
        "sorted_used": requires_sorted,
        "array_used": arr_used if requires_sorted else None,
        "index": index,
        "found": index != -1
    }
    return jsonify(response), 200

# --- SORT ENDPOINTS ---
@app.route("/sort/<algo>", methods=["POST"])
def sort_route(algo: str):
    data, err = json_req()
    if err:
        return err
    arr = data.get("array")
    if arr is None:
        return jsonify({"error": "Please provide 'array' field"}), 400

    algo_map = {
        "bubble": bubble_sort,
        "selection": selection_sort,
        "insertion": insertion_sort,
        "merge": merge_sort,
        "quick": quick_sort,
        "heap": heap_sort
    }

    if algo not in algo_map:
        return jsonify({"error": f"Unknown sort algorithm '{algo}'"}), 404

    func = algo_map[algo]
    sorted_arr = func(list(arr))
    return jsonify({"algorithm": algo, "sorted": sorted_arr}), 200

# --- GRAPH ENDPOINTS ---
@app.route("/graph/<algo>", methods=["POST"])
def graph_route(algo: str):
    data, err = json_req()
    if err:
        return err

    algo_map = {
        "bfs": bfs,
        "dfs": dfs,
        "dijkstra": dijkstra,
        "astar": a_star
    }

    if algo not in algo_map:
        return jsonify({"error": f"Unknown graph algorithm '{algo}'"}), 404

    func = algo_map[algo]

    if algo in ("bfs", "dfs"):
        graph = data.get("graph")
        start = data.get("start")
        if graph is None or start is None:
            return jsonify({"error": "Please provide 'graph' and 'start' fields"}), 400
        result = func(graph, start)
        return jsonify({"algorithm": algo, "result": result}), 200

    if algo == "dijkstra":
        graph = data.get("graph")
        start = data.get("start")
        if graph is None or start is None:
            return jsonify({"error": "Please provide 'graph' and 'start' fields"}), 400
        distances = func(graph, start)
        return jsonify({"algorithm": algo, "distances": distances}), 200

    if algo == "astar":
        # expect a grid-like graph or adjacency + heuristic indicator
        start = data.get("start")
        goal = data.get("goal")
        neighbors = data.get("neighbors")  # optional adjacency dict: node -> [(neighbor,cost),...]
        heuristic = data.get("heuristic")  # optional: a simple heuristic name like "manhattan"

        if start is None or goal is None or neighbors is None:
            return jsonify({"error": "Please provide 'start','goal','neighbors'"}), 400

        # neighbors is expected as dict[node] -> list of [neighbor, cost]
        def neighbors_fn(node):
            # convert the posted structure into list of tuples
            return [(n, c) for n, c in neighbors.get(node, [])]

        # support two heuristics for demonstration
        def heuristic_fn(a, b):
            # if heuristic provided as 'zero' -> behaves like Dijkstra
            if heuristic == "zero" or heuristic is None:
                return 0
            # for grid-like nodes that are tuples (x,y)
            try:
                ax, ay = a
                bx, by = b
                return abs(ax - bx) + abs(ay - by)
            except Exception:
                return 0

        path = func(start, goal, neighbors_fn, heuristic_fn)
        return jsonify({"algorithm": algo, "path": path}), 200

# --- STRING ENDPOINTS ---
@app.route("/string/<algo>", methods=["POST"])
def string_route(algo: str):
    data, err = json_req()
    if err:
        return err

    algo_map = {
        "naive": naive_search,
        "kmp": kmp_search,
        "rabin": rabin_karp
    }

    if algo not in algo_map:
        return jsonify({"error": f"Unknown string algorithm '{algo}'"}), 404

    func = algo_map[algo]
    text = data.get("text")
    pattern = data.get("pattern")
    if text is None or pattern is None:
        return jsonify({"error": "Please provide 'text' and 'pattern' fields"}), 400

    index = func(text, pattern)
    return jsonify({"algorithm": algo, "index": index, "found": index != -1}), 200

# Root index
@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "service": "search-algorithms-api",
        "endpoints": {
            "search": ["/search/linear", "/search/binary", "/search/jump", "/search/interpolation", "/search/exponential", "/search/fibonacci"],
            "sort": ["/sort/bubble", "/sort/quick", "/sort/merge", "/sort/heap"],
            "graph": ["/graph/bfs", "/graph/dijkstra", "/graph/astar"],
            "string": ["/string/naive", "/string/kmp", "/string/rabin"]
        }
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

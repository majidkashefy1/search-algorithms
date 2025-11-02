from flask import Flask, request, jsonify
from algorithms.linear_search import linear_search
from algorithms.binary_search import binary_search
from algorithms.jump_search import jump_search
from algorithms.interpolation_search import interpolation_search
from algorithms.exponential_search import exponential_search
from algorithms.fibonacci_search import fibonacci_search

app = Flask(__name__)

def get_data():
    data = request.get_json(force=True)
    arr = data.get("array")
    target = data.get("target")
    if not arr or target is None:
        return None, None, jsonify({"error": "Please provide 'array' and 'target'"}), 400
    return arr, target, None, None

@app.route('/')
def index():
    return jsonify({
        "algorithms": [
            "linear_search", "binary_search", "jump_search",
            "interpolation_search", "exponential_search", "fibonacci_search"
        ]
    })

@app.route('/linear-search', methods=['POST'])
def linear():
    arr, target, err, code = get_data()
    if err: return err, code
    return jsonify({"algorithm": "linear_search", "index": linear_search(arr, target)})

@app.route('/binary-search', methods=['POST'])
def binary():
    arr, target, err, code = get_data()
    if err: return err, code
    arr_sorted = sorted(arr)
    return jsonify({
        "algorithm": "binary_search",
        "sorted_array": arr_sorted,
        "index": binary_search(arr_sorted, target)
    })

@app.route('/jump-search', methods=['POST'])
def jump():
    arr, target, err, code = get_data()
    if err: return err, code
    arr_sorted = sorted(arr)
    return jsonify({
        "algorithm": "jump_search",
        "index": jump_search(arr_sorted, target)
    })

@app.route('/interpolation-search', methods=['POST'])
def interpolation():
    arr, target, err, code = get_data()
    if err: return err, code
    arr_sorted = sorted(arr)
    return jsonify({
        "algorithm": "interpolation_search",
        "index": interpolation_search(arr_sorted, target)
    })

@app.route('/exponential-search', methods=['POST'])
def exponential():
    arr, target, err, code = get_data()
    if err: return err, code
    arr_sorted = sorted(arr)
    return jsonify({
        "algorithm": "exponential_search",
        "index": exponential_search(arr_sorted, target)
    })

@app.route('/fibonacci-search', methods=['POST'])
def fibonacci():
    arr, target, err, code = get_data()
    if err: return err, code
    arr_sorted = sorted(arr)
    return jsonify({
        "algorithm": "fibonacci_search",
        "index": fibonacci_search(arr_sorted, target)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """
    Home route that returns a welcome message.
    """
    return "Welcome to the Data Processing API!"

@app.route('/api/data/mean', methods=['POST'])
def calculate_mean():
    """
    Calculate the mean of the data provided in the POST request.

    Request JSON format:
    {
        "data": [list of numbers]
    }

    Returns:
    JSON object with the mean value.
    """
    data = request.json.get('data', [])
    if not data:
        return jsonify({"error": "No data provided"}), 400
    mean_value = sum(data) / len(data)
    return jsonify({"mean": mean_value})

@app.route('/api/data/sum', methods=['POST'])
def calculate_sum():
    """
    Calculate the sum of the data provided in the POST request.

    Request JSON format:
    {
        "data": [list of numbers]
    }

    Returns:
    JSON object with the sum value.
    """
    data = request.json.get('data', [])
    if not data:
        return jsonify({"error": "No data provided"}), 400
    sum_value = sum(data)
    return jsonify({"sum": sum_value})

@app.route('/api/data/max', methods=['POST'])
def calculate_max():
    """
    Calculate the maximum value of the data provided in the POST request.

    Request JSON format:
    {
        "data": [list of numbers]
    }

    Returns:
    JSON object with the maximum value.
    """
    data = request.json.get('data', [])
    if not data:
        return jsonify({"error": "No data provided"}), 400
    max_value = max(data)
    return jsonify({"max": max_value})

@app.route('/api/data/min', methods=['POST'])
def calculate_min():
    """
    Calculate the minimum value of the data provided in the POST request.

    Request JSON format:
    {
        "data": [list of numbers]
    }

    Returns:
    JSON object with the minimum value.
    """
    data = request.json.get('data', [])
    if not data:
        return jsonify({"error": "No data provided"}), 400
    min_value = min(data)
    return jsonify({"min": min_value})

if __name__ == '__main__':
    app.run(debug=True)

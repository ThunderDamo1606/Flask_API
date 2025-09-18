from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask server is running "

@app.route('/calculator', methods=['POST'])
def calculator():
    data = request.get_json()

    # Validate request
    if not data or 'num1' not in data or 'num2' not in data or 'operation' not in data:
        return jsonify({"error": "Invalid request. Please send num1, num2, and operation"}), 400

    num1 = data['num1']
    num2 = data['num2']
    operation = data['operation']

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({"error": "num1 and num2 must be numbers"}), 400

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return jsonify({"error": "Cannot divide by zero"}), 400
        result = num1 / num2
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({
        "num1": num1,
        "num2": num2,
        "operation": operation,
        "result": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

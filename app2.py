from flask import Flask, render_template, request
import math

app2 = Flask(__name__)

@app2.route('/', methods=["GET", "POST"])
def home_page():
    return render_template('index.html')

@app2.route('/math', methods=["POST"])
def math():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    operation = request.form.get('operation')

    # Validate numeric input
    try:
        num1 = float(num1)
        num2 = float(num2)
    except (ValueError, TypeError):
        return render_template('results.html', result="Invalid input. Please enter valid numbers.")

    # Define operations
    operations = {
        "add": lambda a, b: f"{a} + {b} = {a + b}",
        "subtract": lambda a, b: f"{a} - {b} = {a - b}",
        "multiply": lambda a, b: f"{a} × {b} = {a * b}",
        "divide": lambda a, b: "Cannot divide by zero" if b == 0 else f"{a} ÷ {b} = {a / b}",
        "modulus": lambda a, b: "Cannot take modulus by zero" if b == 0 else f"{a} % {b} = {a % b}",
        "power": lambda a, b: f"{a} ^ {b} = {a ** b}",
        "sqrt": lambda a, b: f"√{a} = {math.sqrt(a)} , √{b} = {math.sqrt(b)}" if a >= 0 and b >= 0 else "Cannot take square root of negative numbers"
    }

    # Perform selected operation
    if operation in operations:
        result = operations[operation](num1, num2)
    else:
        result = "❌ Invalid operation selected"

    return render_template('results.html', result=result)

if __name__ == "__main__":
    app2.run(host="0.0.0.0", port=5000, debug=True)

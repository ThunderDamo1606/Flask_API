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
    except (ValueError, TypeError):
        return render_template('results.html', result="Invalid input for first number")

    # num2 is optional for some operations
    if num2:
        try:
            num2 = float(num2)
        except (ValueError, TypeError):
            return render_template('results.html', result="Invalid input for second number")
    else:
        num2 = None

    result = ""

    try:
        if operation == "add":
            if num2 is None:
                result = "Second number required for addition"
            else:
                result = f"{num1} + {num2} = {num1 + num2}"

        elif operation == "subtract":
            if num2 is None:
                result = "Second number required for subtraction"
            else:
                result = f"{num1} - {num2} = {num1 - num2}"

        elif operation == "multiply":
            if num2 is None:
                result = "Second number required for multiplication"
            else:
                result = f"{num1} × {num2} = {num1 * num2}"

        elif operation == "divide":
            if num2 is None:
                result = "Second number required for division"
            elif num2 == 0:
                result = "Cannot divide by zero"
            else:
                result = f"{num1} ÷ {num2} = {num1 / num2}"

        elif operation == "modulus":
            if num2 is None:
                result = "Second number required for modulus"
            elif num2 == 0:
                result = "Cannot take modulus by zero"
            else:
                result = f"{num1} % {num2} = {num1 % num2}"

        elif operation == "power":
            if num2 is None:
                result = "Second number required for power"
            else:
                result = f"{num1} ^ {num2} = {num1 ** num2}"

        elif operation == "square":
            result = f"{num1}² = {num1 ** 2}"

        elif operation == "sqrt":
            if num1 < 0:
                result = "Cannot take square root of negative number"
            else:
                result = f"√{num1} = {math.sqrt(num1)}"

        elif operation == "factorial":
            if num1 < 0 or not num1.is_integer():
                result = "Factorial requires a non-negative integer"
            else:
                result = f"{int(num1)}! = {math.factorial(int(num1))}"

        elif operation == "percentage":
            if num2 is None or num2 == 0:
                result = "Total marks (second number) required and cannot be zero"
            else:
                percent = (num1 / num2) * 100
                result = f"{num1} / {num2} × 100 = {percent:.2f}%"

        else:
            result = "Invalid operation selected"

    except Exception as e:
        result = f"Error: {str(e)}"

    return render_template('results.html', result=result)


if __name__ == "__main__":
    app2.run(host="0.0.0.0", port=5000, debug=True)

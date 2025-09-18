from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home_page():
    return render_template('index.html')

@app.route('/math', methods=["POST"])
def math():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    operation = request.form.get('operation')

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return render_template('results.html', result="Invalid input. Please enter numbers only.")

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            result = "Cannot divide by zero"
        else:
            result = num1 / num2
    else:
        result = "Invalid operation"

    return render_template('results.html', result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

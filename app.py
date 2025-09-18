from flask import Flask, request

app = Flask(__name__)  # Flask Object

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/hello1")
def hello_world1():
    return "<h1>Hello, World! 1</h1>"

@app.route("/hello2")
def hello_world2():
    return "<h1>Hello, World! 2</h1>"

@app.route("/hello3")
def hello_world3():
    return "<h1>Hello, World! 3</h1>"

@app.route("/test")
def test():
    a = 8 + 9
    return "This is my function to run app {}".format(a)

# input function for url input
@app.route("/test2")
def test2():
    a = request.args.get("x")   # take value of x from url
    return "This is a data input from my url {}".format(a)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

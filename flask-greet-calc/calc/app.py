# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)


# @app.route('/add')
# def add(a, b):
#     x = a + b
#     return f"the result of {a} + {b} is {x}"


# @app.route('/sub')
# def add(a, b):
#     x = a - b
#     return f"the result of {a} - {b} is {x}"


# @app.route('/mult')
# def add(a, b):
#     x = a * b
#     return f"the result of {a} x {b} is {x}"


# @app.route('/div')
# def add(a, b):
#     x = a / b
#     return f"the result of {a} / {b} is {x}"

@app.route('/add')
def do_add():
    'add a and b parameters'
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)
    return str(result)


@app.route('/sub')
def do_sub():
    'subtract a and b parameters'
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)
    return str(result)


@app.route('/mult')
def do_mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)
    return str(result)


@app.route('/div')
def do_div():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)
    return str(result)


operators = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}


@app.route('/math/<oper>')
def do_math(oper):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operators[oper](a, b)
    return str(result)

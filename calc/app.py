"""Put your app in here."""
from flask import Flask,request
from operations import add,sub,mult,div
app = Flask(__name__)

@app.route("/add", methods=['GET'])
def do_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)
    return str(result)

@app.route("/sub", methods=['GET'])
def do_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    return str(result)

@app.route("/mult", methods=['GET'])
def do_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)
    return str(result)

@app.route("/div", methods=['GET'])
def do_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    return str(result)





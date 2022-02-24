import json

from flask import Flask, jsonify

TODOS = []

with open("todos.json") as fp:
    datas = json.load(fp)
    for d in datas:
        TODOS.append(d)

app = Flask(__name__)

@app.route('/todos')
def todos_list():
    return jsonify(TODOS)
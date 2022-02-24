from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/v1/ip')
def ip_list():
    return jsonify([
        "1.1.1.1",
        "192.168.1.2"
    ])

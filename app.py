from flask import Flask, request, jsonify
import json

app = Flask(__name__)

latest_signal = {}

@app.route('/signal', methods=['POST'])
def receive_signal():
    global latest_signal
    data = request.get_json()
    if data:
        latest_signal = data
        print(f"Signal received: {data}")
        return jsonify({"status": "ok"}), 200
    return jsonify({"status": "error"}), 400

@app.route('/signal', methods=['GET'])
def get_signal():
    return jsonify(latest_signal), 200

@app.route('/', methods=['GET'])
def home():
    return "TV Flask Bridge Running", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

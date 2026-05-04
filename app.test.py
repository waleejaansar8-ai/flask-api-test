from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from API"})

@app.route('/data')
def data():
    data = []
    for i in range(1000):
        data.append({"id": i, "name": "User " + str(i)})
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
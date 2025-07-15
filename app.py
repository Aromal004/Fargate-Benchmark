import os
import time
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

startup_start_flask = time.time()

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Flask App",
        "endpoints": ["/ping", "/fib", "/health", "/startup"]
    })

@app.route('/ping')
def ping():
    start = time.time()
    duration = round(time.time() - start, 4)
    return jsonify({"delay": duration, "status": "ok"})

@app.route('/fib')
def cpu_task():
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    start = time.time()
    result = fib(30)
    duration = round(time.time() - start, 4)
    return jsonify({
        "n": 30,
        "result": result,
        "duration": duration,
        "status": "completed"
    })

@app.route("/health")
def health_check():
    return jsonify({"status": "healthy"}), 200

duration = round(time.time() - startup_start_flask, 10)
@app.route("/startup")
def startup_time():   
    return jsonify({"startup_time": duration})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

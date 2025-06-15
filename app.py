from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ping')
def ping():
    start = time.time()
    duration = round(time.time() - start, 4)
    return render_template('ping.html', delay=duration)

@app.route('/cpu')
def cpu_task():
    def fib(n):
        return fib(n - 1) + fib(n - 2) if n > 1 else n
    start = time.time()
    result = fib(30)
    duration = round(time.time() - start, 4)
    return render_template('cpu.html', result=result, duration=duration)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True, port=5000)
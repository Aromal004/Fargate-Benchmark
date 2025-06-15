from flask import Flask, render_template
import time

app = Flask(__name__)

INPUT_PATH = "image.jpg"
OUTPUT_PATH = "output.jpg"

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


@app.route("/convert", methods=["GET"])
def convert_image():
    if not os.path.exists(INPUT_PATH):
        return {"error": "image.jpg not found"}, 404

    if os.path.exists(OUTPUT_PATH):
        os.remove(OUTPUT_PATH)

    image = Image.open(INPUT_PATH).convert("L")
    image.save(OUTPUT_PATH)

    return send_file(OUTPUT_PATH, mimetype="image/jpeg")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True, port=5000)

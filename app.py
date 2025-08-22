from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    # ⚠️ In real app: run ML model here
    # For demo, generate random severity
    score = random.randint(10, 100)
    if score < 40:
        severity = "LOW"
    elif score < 70:
        severity = "MEDIUM"
    else:
        severity = "CRITICAL"

    return jsonify({"severity": severity, "score": score})

if __name__ == "__main__":
    app.run(debug=True)

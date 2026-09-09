import os

from flask import Flask, jsonify

app = Flask(__name__)

ITEMS = ["pomme", "banane", "orange"]


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


@app.route("/api/items")
def get_items():
    return jsonify(items=ITEMS), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
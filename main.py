from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ GBOB Auto System Running by Rana Liaqat"

@app.route("/webhook", methods=['POST'])
def webhook():
    data = request.json
    print("📩 Incoming Request:", data)
    return jsonify({"status": "OK"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

client = MongoClient(os.environ.get("MONGO_URI", "mongodb://localhost:27017"))
db = client["blogapp"]

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Blog App API you all!"})
 
 
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})
 
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



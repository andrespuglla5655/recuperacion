from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({"message": "CI/CD funcionando correctamente Puglla v1.0.5"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

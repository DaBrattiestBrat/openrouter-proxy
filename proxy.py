from flask import Flask, request
import requests, os

app = Flask(__name__)

OPENROUTER_KEY = os.environ.get("OPENROUTER_KEY")

@app.route("/v1/chat/completions", methods=["POST"])
def proxy():
    r = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_KEY}",
            "Content-Type": "application/json"
        },
        json=request.json
    )
    return (r.text, r.status_code, {"Content-Type": "application/json"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

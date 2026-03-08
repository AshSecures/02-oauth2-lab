from flask import Flask, redirect, request
import requests

app = Flask(__name__)

AUTH_SERVER = "http://127.0.0.1:5000"

@app.route("/")
def login():
    return redirect(
        f"{AUTH_SERVER}/authorize?"
        "client_id=client123&"
        "redirect_uri=http://127.0.0.1:5001/callback"
    )

@app.route("/callback")
def callback():
    code = request.args.get("code")

    token_response = requests.post(
        f"{AUTH_SERVER}/token",
        data={"code": code}
    )

    return token_response.json()

app.run(port=5001, debug=True)

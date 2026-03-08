from flask import Flask, redirect, request, session
import requests, secrets
import hashlib
import base64

app = Flask(__name__)
app.secret_key = "super_secret_key"

AUTH_SERVER = "http://127.0.0.1:5000"

@app.route("/")
def login():
    state = secrets.token_urlsafe(16)
    session["oauth_state"] = state

    code_verifier = secrets.token_urlsafe(32)
    session["code_verifier"] = code_verifier

    code_challenge = base64.urlsafe_b64encode(
    hashlib.sha256(code_verifier.encode()).digest()
    ).rstrip(b"=").decode()

    return redirect(
        f"{AUTH_SERVER}/authorize?"
        f"client_id=client123&"
        f"redirect_uri=http://127.0.0.1:5001/callback&"
        f"state={state}&"
        f"code_challenge={code_challenge}&"
        f"code_challenge_method=S256"
    )

#    return redirect(auth_url)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    state = request.args.get("state")

    if state != session.get("oauth_state"):
        return "Invalid state parameter!", 400

    code_verifier = session.get("code_verifier")

    data = {
        "code": code,
        "code_verifier": code_verifier
    }

    token_response = requests.post(
        f"{AUTH_SERVER}/token",
        data=data
    )

    return token_response.text

app.run(port=5001, debug=True)


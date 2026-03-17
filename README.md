# 02-oauth2-lab

🔐 OAuth Security Lab

A hands-on lab demonstrating common vulnerabilities in OAuth 2.0 and how to secure them using modern best practices like state validation and OAuth 2.0 PKCE.

📌 Overview

This project was built to explore how real-world OAuth implementations fail—not at the protocol level, but due to insecure or incomplete implementations.

The lab includes:

A deliberately vulnerable OAuth flow

A simulated attacker capturing authorization codes

A hardened implementation with proper security controls

The goal is to move beyond theory and understand OAuth from both an attacker’s and defender’s perspective.

🧱 Architecture
User → Client Application → Authorization Server
                ↓
        Authorization Code
                ↓
           Access Token
⚠️ Vulnerable Implementation

The initial version intentionally omits critical protections:

❌ No state parameter → susceptible to Login CSRF

❌ No PKCE → vulnerable to authorization code interception

❌ Minimal validation of OAuth parameters

Impact

These gaps allow attackers to:

Intercept authorization codes

Attempt unauthorized token exchanges

Manipulate authentication flows

🧪 Attack Simulation

An attacker server is included to simulate code interception:

attacker/attacker_server.py

Example behavior:

@app.route("/steal")
def steal():
    code = request.args.get("code")
    print(f"[ATTACKER] Captured authorization code: {code}")

This demonstrates how OAuth codes can be exposed if redirect handling is insecure.

🛡️ Hardened Implementation

The secure version introduces key protections recommended by OWASP.

✅ State Parameter

Generated per request

Stored in session

Validated during callback

Prevents:

Login CSRF attacks
✅ PKCE (Proof Key for Code Exchange)

Implements:

code_verifier
code_challenge (S256)

Flow:

Client sends code_challenge during authorization

Server stores challenge

Client sends code_verifier during token exchange

Server verifies hash before issuing token

Prevents:
Authorization code interception attacks

📁 Project Structure
oauth-security-lab
│
├── vulnerable
│   ├── auth_server.py
│   └── client_app.py
│
├── hardened
│   ├── auth_server.py
│   └── client_app.py
│
├── attacker
│   └── attacker_server.py
│
├── attacks
│   └── code_interception.py
│
├── diagrams
│   └── oauth-flow.png
│
└── README.md
🚀 Running the Lab
1️⃣ Start Authorization Server
cd vulnerable
python auth_server.py

2️⃣ Start Client Application
cd vulnerable
python client_app.py

(or use hardened/ for secure flow)

3️⃣ Start Attacker Server
cd attacker
python attacker_server.py

4️⃣ Trigger Flow
http://127.0.0.1:5001/

Observe:

Authorization code issuance

Redirection behavior

Token exchange

🧠 Key Learnings

OAuth vulnerabilities are often implementation issues, not protocol flaws

Missing controls like state and PKCE introduce real attack surfaces

Simulating attacks provides deeper understanding than reading specs

Secure authentication requires defensive design, not just functional correctness

📄 Blog

Detailed write-up:
👉 (https://medium.com/@ashutoshshinde1112/understanding-oauth-security-by-building-a-vulnerable-lab-and-fixing-it-with-pkce-4dd32a3e0960)

🤝 Contributions

This is a learning-focused project. Suggestions, improvements, or additional attack scenarios are welcome.

⭐ Final Note

This lab is part of a broader effort to build practical expertise in:

Application Security
Authentication Protocols
Offensive + Defensive Security Engineering

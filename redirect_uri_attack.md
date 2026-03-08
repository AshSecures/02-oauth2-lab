OAuth Redirect URI Manipulation

Description:
If the authorization server does not validate redirect_uri against a
pre-registered value, an attacker can provide their own redirect
endpoint and capture the authorization code.

Attack Flow:
1. Victim starts OAuth login
2. Attacker modifies redirect_uri
3. Authorization server redirects to attacker
4. Attacker receives authorization code
5. Attacker exchanges code for access token

Impact:
Authorization code theft leading to account takeover.

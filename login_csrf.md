OAuth Login CSRF (Missing State Parameter)

Description:
If the OAuth client does not use the state parameter, an attacker can
force a victim to complete an OAuth flow initiated by the attacker.

Attack Flow:
1. Attacker logs into OAuth provider
2. Attacker receives authorization code
3. Attacker sends victim a crafted callback URL
4. Victim visits URL
5. Victim logs into attacker account

Impact:
Session confusion and account linking vulnerabilities.

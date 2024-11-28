import time
import jwt
from jose import jwt as jose_jwt

# Load private key from file
private_key = open('.github/private/prreviewajin2024.2024-11-28.private-key.pem', 'r').read()
print(private_key)
# GitHub App ID
app_id = '1072194'  # Replace with your actual GitHub App ID

# JWT payload
jwt_payload = {
    "iat": int(time.time()),  # Issued at time
    "exp": int(time.time()) + 600,  # Expiration time (10 minutes)
    "iss": app_id  # GitHub App ID
}

# Generate JWT token
jwt_token = jwt.encode(jwt_payload, private_key, algorithm="RS256")

# Save JWT token to a file
with open(".github/secrets/jwt_token.txt", "w") as file:
    file.write(jwt_token)

# Print JWT token to the workflow logs
print(f"JWT Token: {jwt_token}")

print("JWT token generated and saved.")

import sys
import time
import jwt

# Load private key from file
with open('.github/private/prreviewajin2024.2024-11-28.private-key.pem', 'rb') as pem_file:
    private_key = pem_file.read()

# GitHub App ID and Client ID
app_id = '1072194'  # Replace with your actual GitHub App ID
client_id = 'Iv23liIBLbPfqF3jlZX3'  # Replace with your actual GitHub App client ID

# JWT payload
jwt_payload = {
    # Issued at time
    'iat': int(time.time()),
    # JWT expiration time (10 minutes maximum)
    'exp': int(time.time()) + 600,
    
    # GitHub App's client ID
    'iss': client_id
}

# Encode JWT using private key
encoded_jwt = jwt.encode(jwt_payload, private_key, algorithm='RS256')

print(f"JWT: {encoded_jwt}")

# Save JWT token to a file
with open(".github/secrets/jwt_token.txt", "w") as file:
    file.write(encoded_jwt)

print("JWT token generated and saved.")

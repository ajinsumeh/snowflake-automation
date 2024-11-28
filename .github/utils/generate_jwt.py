import jwt
import time
from datetime import datetime, timedelta
from jose import jwt as jose_jwt

# Load your private key
private_key = open('.github/private/prreviewajin2024.2024-11-28.private-key.pem', 'r').read()

# Define the app id (replace with your GitHub App ID)
app_id = '1072194'  # Replace with your actual GitHub App ID

# Create the JWT payload
jwt_payload = {
    "iat": int(time.time()),
    "exp": int(time.time()) + 600,  # Expires in 10 minutes
    "iss": app_id
}

# Encode the JWT
jwt_token = jwt.encode(jwt_payload, private_key, algorithm="RS256")

# Print the JWT token to the console
print("Generated JWT Token: ", jwt_token)

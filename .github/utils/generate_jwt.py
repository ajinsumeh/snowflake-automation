import jwt
import time

# Load your private key (make sure it's securely stored, and provide the correct path)
private_key_path = '.github/private/prreviewajin2024.2024-11-28.private-key.pem'  # Adjusted to the correct path
with open(private_key_path, 'r') as key_file:
    private_key = key_file.read()

# Define the app ID (replace with your GitHub App ID)
app_id = '1072194'  # Replace with your actual GitHub App ID

# Create the JWT payload
jwt_payload = {
    "iat": int(time.time()),
    "exp": int(time.time()) + 600,  # Expires in 10 minutes
    "iss": app_id  # Issuer is the GitHub App ID

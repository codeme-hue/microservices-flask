# client_with_encryption.py
import requests
from cryptography.fernet import Fernet

# Load the key
with open("secret.key", "rb") as key_file:
    secret_key = key_file.read()

cipher_suite = Fernet(secret_key)

url = 'http://localhost:5001/send'
message = 'Hi, ini adalah pesan dengan enkripsi'

encrypted_message = cipher_suite.encrypt(message.encode()).decode()
response = requests.post(url, json={'message': encrypted_message})

response_data = response.json()
decrypted_feedback = cipher_suite.decrypt(response_data['feedback'].encode()).decode()

print(f"Encrypted feedback: {response_data['feedback']}")
print(f"Decrypted feedback: {decrypted_feedback}")

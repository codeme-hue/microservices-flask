from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

with open("secret.key", "rb") as key_file:
    secret_key = key_file.read()

cipher_suite = Fernet(secret_key)

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    encrypted_message = data.get('message')
    decrypted_message = cipher_suite.decrypt(encrypted_message.encode()).decode()

    response_message = f"Pesan '{decrypted_message}' diterima dengan enkripsi"
    encrypted_response = cipher_suite.encrypt(response_message.encode()).decode()

    response = {
        'received_message': encrypted_message,
        'feedback': encrypted_response
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

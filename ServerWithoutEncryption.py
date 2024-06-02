from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    message = data.get('message')
    response = {
        'received_message': message,
        'feedback': 'Pesan diterima tanpa enkrips'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

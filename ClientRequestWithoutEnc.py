import requests

url = 'http://localhost:5000/send'
message = {'message': 'Hai, ini adalah pesan tanpa enkripsi'}

response = requests.post(url, json=message)
print(response.json())


import requests
import json

print("Hello World")
payloads = { 'method': 2, 'subject': 'in_en', 'fingprint': 'en16504262', 'week': 'week1'}
r = requests.post('http://localhost:3000', json = payloads)

req_text = r.text
data = json.loads(req_text)

print(data['name'])
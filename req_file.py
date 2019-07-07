
import requests
import json

print("Hello World")
payloads = { 'method': 2, 'subject': 'in_en', 'fingprint': 'en16504262', 'week': 'week1'}
r = requests.post('http://localhost:3000', json = payloads)

req_text = r.text
data = json.loads(req_text)

print(data['name'])

lec fingerprint = 3a28ab5c879d24d67ce89f5f51a64f945b5967f0dab48510db4ab727130d6e61
stu = 59ea4846251468183bd6097afff2aa1479868fc71ef19348c8ca1964cccb5349

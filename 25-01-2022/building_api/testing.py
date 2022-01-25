import requests

data = {'search': 'good morning?'}

r = requests.post('http://localhost:5050/', json=data)
print('status:', r.status_code)
print('json:', r.json())
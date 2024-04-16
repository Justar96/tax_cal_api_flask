import requests
import time
import json


url = 'http://127.0.0.1:5000/tax-cal'

header = {'content-type':'application/json'}
form = {'value': 500000}

r = requests.post(url,data=json.dumps(form),headers=header)

print(r.status_code)
print(r.text)
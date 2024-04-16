import requests
import json

url = 'http://127.0.0.1:5000/tax-cal?value=500000'

# header = {'content-type':'application/json'}
# form = {'value':'500000'}

r = requests.get(url)

print(r.status_code)
print(r.text)
import requests
import json 

f = open('spelers.json')  
data = json.load(f)

res = requests.post('http://localhost:5000/test', json = data)

if res.ok:
    print(res.json())
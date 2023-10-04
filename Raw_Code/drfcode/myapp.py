import requests
import json

URL = ""

data = {
    'name':'Saim',
    'rollno':101,
    'city':'Vehari',
}
json_data = json.dump(data)
r = requests.post(url = URL, data = json_data)
data = r,json()
print(data)
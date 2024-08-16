import requests
# this is for basic authentication
from requests.auth import HTTPBasicAuth 



response = requests.get('http://127.0.0.1:8000/drinks', auth = HTTPBasicAuth('admin','Admin@123'))

print(response.json())
for i,j in enumerate(response):
    print(f"{i} : {j}")
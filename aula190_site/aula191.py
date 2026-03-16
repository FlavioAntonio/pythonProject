import requests
URL = "http://localhost:3333/"
response = requests.get(URL)
print(response.status_code)
print(response.text)
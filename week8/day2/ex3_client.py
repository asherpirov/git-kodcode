import requests

url = "http://127.0.0.1:8000/greet"

query = {"name": "asher"}

response = requests.get(url)
query_response = requests.get(url, params=query)
print(response.json())
print(query_response.json())



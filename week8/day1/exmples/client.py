import requests

response = requests.get("http://localhost:8000/items/5")
print(response.status_code) # 200
print(response.json())
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(response.status_code)
print(response.json())

data = response.json()

print(f"Name: {data["name"]}")
print(f"Email: {data["email"]}")
print(f"City: {data["address"]["city"]}")

response2 = requests.get("https://jsonplaceholder.typicode.com/posts")

print(response2.status_code)
data2 = response2.json()
print(len(data2))

response3 = requests.get("https://jsonplaceholder.typicode.com/posts?userId=2")

data3 = response3.json()

for post in data3:
    print(f"{post["title"]}")




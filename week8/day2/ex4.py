import requests

users_response = requests.get("https://jsonplaceholder.typicode.com/users")
posts_response = requests.get("https://jsonplaceholder.typicode.com/posts")

users_data = users_response.json()
posts_data = posts_response.json()

users_dict = {}

for user in users_data:
    users_dict[user["id"]] = user["name"]
print(users_dict)

for post in posts_data:
    post_title = post["title"]
    author_name = users_dict[post["userId"]]
    print( f"{post_title} by {author_name}")


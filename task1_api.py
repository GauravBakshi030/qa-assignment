import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    print("Status code is 200 - OK")
else:
    print("Error")

data = response.json()

for post in data:
    if "userId" in post and "id" in post and "title" in post and "body" in post:
        continue
    else:
        print("Key missing")

first_5 = data[:5]

with open("first_5_posts.json", "w") as file:
    json.dump(first_5, file, indent=4)

print("Done")
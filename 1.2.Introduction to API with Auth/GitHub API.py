import requests
response_fruit = requests.get("https://api.github.com/users/MohamadNematizadeh/followers?per_page=100")
print("api fruit :", response_fruit.json())
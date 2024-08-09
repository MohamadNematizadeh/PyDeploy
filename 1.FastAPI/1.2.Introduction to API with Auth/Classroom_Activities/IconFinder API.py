import requests
import os
import dotenv
dotenv = dotenv.load_dotenv()
url = "https://api.iconfinder.com/v4/icons/search?query=arrow&count=10"

IconFinder_API_KEY = os.getenv("IconFinder_API_KEY")
headers = {
    "accept": "application/json",
    "Authorization": IconFinder_API_KEY
}

response = requests.get(url, headers=headers)
response.status_code
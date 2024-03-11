import requests
import os
import dotenv
dotenv = dotenv.load_dotenv()
url = "https://the-one-api.dev/v2/movie"

One_API_KEY = os.getenv("One_API_KEY")
payload = {}
headers = {
  'Authorization': One_API_KEY
}

response = requests.request("GET", url, headers=headers, data=payload)
response.status_code
response.json()
import requests
import os 
import dotenv

dotenv = dotenv.load_dotenv()
KEY_plantnet = os.getenv("KEY_plantnet")
url = "https://my-api.plantnet.org/v2/identify/all"
headers ={
}
payload = {
"api-key" : KEY_plantnet
}
files = {
"images" : open("local-filename.jpg","rb")
}
responset = requests.post(url,headers=headers,params=payload,files=files)
print(responset.status_code)
response = responset.json()["results"]
import os
import argparse
import requests
import dotenv
from urllib.request import urlretrieve
dotenv = dotenv.load_dotenv()
parser = argparse.ArgumentParser()
parser.add_argument('--image-plant', help='create image plant')
opt = parser.parse_args()
create_image_plant = opt.image_plant

def post_fal(name):
    API_KEY= os.getenv("KEY_llusion_diffusion")
    url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"
    headers ={
        "Authorization":API_KEY,
        "Content_Type":"application/json"}
    payload = {
        "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
        f"prompt": "(masterpiece:1.4), (best quality), (detailed),"+name,
        "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t"}
    
    responset = requests.post(url,headers=headers,json=payload)
    print(responset.status_code)
    response = responset.json()["image"]
    return response
    
def post_plantnet(image):
    API_KEY = os.getenv("KEY_plantnet")
    url = "https://my-api.plantnet.org/v2/identify/all"
    headers ={}
    payload = {
      "api-key" : API_KEY}
    files = {
      "images" : open("local-filename.jpg","rb")}
    responset = requests.post(url,headers=headers,params=payload,files=files)
    print(responset.status_code)
    response = responset.json()["results"]
    response = response.pop(4)
    response = response["species"]
    return  response

images = post_fal(create_image_plant)   
image = images["url"]
url = image
urlretrieve(url, "local-plant.jpg")

name = post_plantnet(image)
name = name["commonNames"][0]
print(name)
import requests
import dotenv
import os 

dotenv = dotenv.load_dotenv()
KEY_llusion_diffusion = os.getenv("KEY_llusion_diffusion")

url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"
headers ={
    "Authorization":KEY_llusion_diffusion,
    "Content_Type":"application/json"
}
payload = {
    "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
    f"prompt": "(masterpiece:1.4), (best quality), (detailed), A beautiful forest full of snow and rain and a fire in a wooden hut",
    "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t"
}
responset = requests.post(url,headers=headers,json=payload)
print(responset.status_code)
response = responset.json()
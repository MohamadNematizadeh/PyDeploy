import requests
import os
import dotenv
dotenv = dotenv.load_dotenv()
KEY_D_ID = os.getenv("KEY_D_ID")
url = "https://api.d-id.com/clips"
payload = {
    "script": {
        "type": "text",
        "provider": {
            "type": "microsoft",
            "voice_id": "en-US-JennyNeural"
        },
        "ssml": "false",
        "input": "Hello there. I am your Smart Assistant. How can I help you?"
    },
    "config": { "result_format": "mp4" },
    "presenter_config": { "crop": { "type": "wide" } },
    "background": { "color": "false" },
    "presenter_id": "anita-6_uTzyZtNR"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": KEY_D_ID
}
response = requests.post(url, json=payload, headers=headers)
response.status_code
response = response.json()
import io
import json
import cv2
from fastapi import FastAPI 
from urllib.request import urlretrieve
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse 


app = FastAPI()
plants = json.load(open("jsons/planet.json"))

   
@app.get("/")
def read_root():
    text =  "Hi, welcome to the solar system api In this api there is about solar system plants"
    return text
            

@app.get("/planet")
def get_plants():
    return plants
    

@app.get("/planet/{name_plants}/")
def test2(name_plants: str):
    return plants[name_plants]


@app.get("/planet/{name_plants}/image")
def create_image(name_plants: str):
    url_images= plants[name_plants]
    url_image = url_images["image"]
    image2 = urlretrieve(url_image, "local-plant.png")
    image = cv2.imread("local-plant.png")
    _, encode_image = cv2.imencode(".png", image)
    return StreamingResponse(content=io.BytesIO(encode_image.tobytes()), media_type = "image/png")

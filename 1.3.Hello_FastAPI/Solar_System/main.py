import json
from fastapi import FastAPI 
from urllib.request import urlretrieve
from fastapi.responses import FileResponse

app = FastAPI()
plants = plants = json.load(open("jsons/planet.json"))

   
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
    image = urlretrieve(url_image, "local-plant.png")
    return FileResponse("local-plant.png")

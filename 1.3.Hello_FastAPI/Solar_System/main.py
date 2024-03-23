import json
from fastapi import FastAPI 
from urllib.request import urlretrieve
from fastapi.responses import FileResponse

app = FastAPI()
planet = json.load(open("jsons/planet.json"))

   
@app.get("/")
def start():
    text =  "Hi, welcome to the solar system api In this api there is about solar system planet"
    return text
            

@app.get("/planet")
def get_planet():
    return planet
    

@app.get("/planet/{name_planet}/")
def get_planet_name(name_planet: str):
    return planet[name_planet]


@app.get("/planet/{name_planet}/image")
def create_planet_image(name_planet: str):
    url_images= planet[name_planet]
    url_image = url_images["image"]
    image = urlretrieve(url_image, "local-plant.png")
    return FileResponse("local-plant.png")

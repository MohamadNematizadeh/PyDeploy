
from fastapi import FastAPI
from urllib.request import urlretrieve
from fastapi.responses import FileResponse

app = FastAPI()
sins = {
    "Avarice (Taknavardi)": {
        "description": "Excessive desire for material wealth or possessions.",
        "image" : "https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQh-AxJRcDz5yLgVfFA_uPIl6gww1aeEmAWM7DGaHTucBrN5JmPYkFGlVjrfQuWd_60",
    },
    "Lying (Kosrat)":{
      "description": "Deception, falsehood, or telling lies."
    },
    "Injustice (Zolm)":{
      "description": "Unfairness, oppression, or treating others unjustly."
    },
    "Envy (Hasad)":{
      "description": "Jealousy and coveting what others have, leading to resentment."
    },
    "Rudeness (Bazgasht)":{
      "description": "Lack of manners, disrespect, or impoliteness."
    },
    "Ignorance (Nadani)":{
      "description": "Lack of knowledge, unawareness, or being uninformed."
    },
    "Oppression (Sarvand)":{
      "description": "Imposing one's will or power on others, often in a cruel or harsh manner."
    }
}



@app.get("/")
def read_root():
    return "Hello, welcome to 7-Sins api. In this api, some information about 7 major sins is said"

@app.get("/sins")
def get_sins():
    return sins
    

@app.get("/sins/{name_sins}/")
def get_name(name_sins: str):
    return sins[name_sins]


@app.get("/sins/{name_sins}/image")
def get_image(name_sins: str):
    url_images= sins[name_sins]
    url_image = url_images["image"]
    image = urlretrieve(url_image, "local-plant.png")
    return FileResponse("local-plant.png")
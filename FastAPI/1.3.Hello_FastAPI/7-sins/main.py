
from fastapi import FastAPI
from urllib.request import urlretrieve
from fastapi.responses import FileResponse

app = FastAPI()
sins = {
    "Sabzeh (سبزه)": {
        "description": "Wheat, barley, mung bean, or lentil sprouts grown in a dish, symbolizing rebirth and renewal.",
        "image" : "https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQh-AxJRcDz5yLgVfFA_uPIl6gww1aeEmAWM7DGaHTucBrN5JmPYkFGlVjrfQuWd_60",
    },
    "Samanu (سمنو)":{
      "description": "Sweet pudding made from germinated wheat, symbolizing power, strength, and fertility.",
      "image" : "https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQh-AxJRcDz5yLgVfFA_uPIl6gww1aeEmAWM7DGaHTucBrN5JmPYkFGlVjrfQuWd_60",

    },
    "Senjed (سنجد)":{
      "description": "Dried oleaster fruit, symbolizing love and compassion.",
      "image" : "https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQh-AxJRcDz5yLgVfFA_uPIl6gww1aeEmAWM7DGaHTucBrN5JmPYkFGlVjrfQuWd_60",

    },
    "Sir (سیر)":{
      "description": "Garlic, symbolizing medicine and health.",
       "image" : "https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQh-AxJRcDz5yLgVfFA_uPIl6gww1aeEmAWM7DGaHTucBrN5JmPYkFGlVjrfQuWd_60",

    },
    "Sib (سیب)":{
      "description": "Apple, symbolizing beauty and health.",
      "image" : "https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQh-AxJRcDz5yLgVfFA_uPIl6gww1aeEmAWM7DGaHTucBrN5JmPYkFGlVjrfQuWd_60",

    },
    "Somaq (سماق)":{
      "description": "Sumac berries, symbolizing the sunrise and the victory of light over darkness.",
              "image" : "https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQh-AxJRcDz5yLgVfFA_uPIl6gww1aeEmAWM7DGaHTucBrN5JmPYkFGlVjrfQuWd_60",

    },
    "Serkeh (سرکه)":{
      "description": "Vinegar, symbolizing patience and wisdom.",
              "image" : "https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQh-AxJRcDz5yLgVfFA_uPIl6gww1aeEmAWM7DGaHTucBrN5JmPYkFGlVjrfQuWd_60",

    }

}



@app.get("/")
def read_root():
    return "Hello, welcome to 7-Sins api. In this api, some information about 7 major sins is said"

@app.get("/7sins")
def get_sins():
    return sins
    

@app.get("/7sins/{name_sins}/")
def get_name(name_sins: str):
    return sins[name_sins]


@app.get("/7sins/{name_sins}/image")
def get_image(name_sins: str):
    url_images= sins[name_sins]
    url_image = url_images["image"]
    image = urlretrieve(url_image, "local-plant.png")
    return FileResponse("local-plant.png")
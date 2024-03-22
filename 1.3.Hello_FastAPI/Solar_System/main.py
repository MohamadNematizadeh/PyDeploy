from operator import and_
from fastapi import FastAPI 
from urllib.request import urlretrieve
from fastapi.responses import FileResponse

app = FastAPI()
plants = {
    "Sun"and("sun"): {
        "distance_from_sun_km": 0,
        "equatorial_radius_km": 696340,
        "moons": [],
        "image" : "https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQh-AxJRcDz5yLgVfFA_uPIl6gww1aeEmAWM7DGaHTucBrN5JmPYkFGlVjrfQuWd_60",
        "fact": "The Sun is the center of our solar system and provides the energy for life on Earth through the process of nuclear fusion."
    },
    "Mercury"and("mercury"): {
        "distance_from_sun_km": 57910000,
        "equatorial_radius_km": 2439.7,
        "moons": [],
        "image" : "https://science.nasa.gov/wp-content/uploads/2023/11/mercury-messenger-globe-pia15162.jpg",
        "fact": "Mercury is the smallest planet in the Solar System and the closest to the Sun."
    },
    "Venus"and("venus"): {
        "distance_from_sun_km": 108200000,
        "equatorial_radius_km": 6051.8,
        "moons": [],
        "image" : "https://t1.gstatic.com/licensed-image?q=tbn:ANd9GcT6b03Qr3tnaBzlbznWySao6lYzR84Qw7kF-5DJ6C-3tWD_HB7yHI1dvHB4OwlWX7q-",
        "fact": "Venus is often called Earth's 'sister planet' because of their similar size and composition."
    },
    "Earth"and("earth"): {
        "distance_from_sun_km": 149600000,
        "equatorial_radius_km": 6371.0,
        "moons": ["Moon"],
        "image" : "https://cdn.mos.cms.futurecdn.net/FaWKMJQnr2PFcYCmEyfiTm-1200-80.jpg",

        "fact": "Earth is the only planet known to support life, with a diverse range of organisms."
    },
    "Moon"and("moon"): {
        "distance_from_sun_km": 384400,
        "equatorial_radius_km": 1737.5,
        "moons": [],
        "image" : "https://t3.gstatic.com/licensed-image?q=tbn:ANd9GcT1g1V8Nalm9FkR2atv7annUXbPvk5g-mWffaNxT_ItIFogl-6mC_lHNifw5Tw9-yiS",
        "fact": "The Moon is Earth's only natural satellite and is responsible for tides on Earth."
    },
    "Mars"and("mars"): {
        "distance_from_sun_km": 227900000,
        "equatorial_radius_km": 3389.5,
        "moons": ["Phobos", "Deimos"],
        "image" : "https://upload.wikimedia.org/wikipedia/commons/0/0c/Mars_-_August_30_2021_-_Flickr_-_Kevin_M._Gill.png",
        "fact": "Mars is often called the 'Red Planet' due to its reddish appearance caused by iron oxide on its surface."
    },
    "Jupiter"and("jupiter"): {
        "distance_from_sun_km": 778500000,
        "equatorial_radius_km": 69911,
        "moons": ["Io", "Europa", "Ganymede", "Callisto"],
        "image" : "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Jupiter.jpg/800px-Jupiter.jpg",

        "fact": "Jupiter is the largest planet in the Solar System and has a strong magnetic field."
    },
    "Saturn"and("saturn"): {
        "distance_from_sun_km": 1433000000,
        "equatorial_radius_km": 58232,
        "moons": ["Mimas", "Enceladus", "Tethys", "Dione", "Rhea", "Titan", "Hyperion", "Iapetus"],
        "image" : "https://planetfacts.org/wp-content/uploads/2023/12/planet_saturn.jpg",

        "fact": "Saturn is known for its spectacular ring system, made up of ice particles and dust."
    },
    "Uranus"and("uranus"): {
        "distance_from_sun_km": 2877000000,
        "equatorial_radius_km": 25362,
        "moons": ["Miranda", "Ariel", "Umbriel", "Titania", "Oberon"],
        "image" : "https://imageio.forbes.com/specials-images/imageserve/5f91806c76fcfa4a1e885d7c/Uranus-will-this-week-be-easy-to-see-for-one-night-only-just-north-of-a-crescent/960x0.jpg?format=jpg&width=960",

        "fact": "Uranus rotates on its side, likely due to a collision with a massive object in the past."
    },
    "Neptune"and("neptune"): {
        "distance_from_sun_km": 4503000000,
        "equatorial_radius_km": 24622,
        "moons": ["Triton", "Nereid"],
        "image" : "https://science.nasa.gov/wp-content/uploads/2023/09/PIA01492-1.jpg",

        "fact": "Neptune is the farthest planet from the Sun and was the first planet discovered through mathematical predictions."
    }
}
@app.get("/")
def read_root():
    return "Hi, welcome to the solar system api In this api there is about solar system plants"
            

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

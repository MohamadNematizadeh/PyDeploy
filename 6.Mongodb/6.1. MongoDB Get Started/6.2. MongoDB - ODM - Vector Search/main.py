import os
import binascii
from uuid import uuid4
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from mongoengine import connect, Document, StringField, FloatField, DictField
from datetime import datetime, timedelta
import jwt
from pyngrok import ngrok
connect(host="mongodb+srv://mohammad:09156006138Mohmmad@home.sk0tg.mongodb.net/")

app = FastAPI()
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="signin")

class TokenGenerator:
    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

class User(BaseModel):
    username: str
    password: str
    confirm_password: str

class House(BaseModel):
    features: dict
    price: float

class Token(BaseModel):
    access_token: str
    token_type: str

class UserModel(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    key = StringField()

class HouseModel(Document):
    features = DictField()
    price = FloatField()

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.get("/")
def hello():
    return {"message": "Hello, World!"}

@app.post("/signup")
def signup(user: User):
    if UserModel.objects(username=user.username):
        raise HTTPException(status_code=400, detail="User already exists")
    if user.password != user.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    
    token_gen = TokenGenerator()
    user_key = token_gen.generate_key()
    
    new_user = UserModel(username=user.username, password=user.password, key=user_key)
    new_user.save()

    return {"message": "User created successfully"}

@app.post("/signin", response_model=Token)
def signin(form_data: OAuth2PasswordRequestForm = Depends()):
    user = UserModel.objects(username=form_data.username).first()
    if not user or user.password != form_data.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": form_data.username})
    user.key = access_token 
    user.save()
    
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/add")
def add_house(features: str, price: str, token: str):
    user = UserModel.objects(key=token).first()  
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    house_model = HouseModel(features=features, price=price)
    house_model.save()
    
    return {"message": "House added successfully"}

@app.post("/predict")
def predict_price(features: dict, token: str = Depends(oauth2_scheme)):
    predicted_price = 500000  
    return {"predicted_price": predicted_price}

@app.get("/train")
def train(token: str = Depends(oauth2_scheme)):
    return {"message": "Training started"}

ngrok.set_auth_token("2mNqxRNRtku1XKb786pwv4aar3b_6C2wmP29319kfUdA6uwDU")
public_url = ngrok.connect(8000)
print(f"Public URL: {public_url}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

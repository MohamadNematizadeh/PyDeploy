from sqlmodel import Field, SQLModel, create_engine, Session, select
import bcrypt
from pydantic import BaseModel

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name: str = Field()
    last_name: str = Field()
    email: str = Field()
    username: str = Field(index=True)
    age: str = Field()
    city: str = Field()
    country: str = Field()
    password_hash: str

class RegisterModel(BaseModel):
    first_name: str 
    last_name: str 
    email: str 
    username: str 
    age: str 
    city: str 
    country: str 
    password: str


class LoginModel(BaseModel):
    username: str
    password: str
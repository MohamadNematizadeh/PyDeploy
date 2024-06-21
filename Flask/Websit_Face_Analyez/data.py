from sqlmodel import Field, SQLModel, create_engine, Session, select
import bcrypt
from model import User,RegisterModel

DATABASE_URL = 'sqlite:///./data.db'
engine = create_engine(DATABASE_URL, echo=True)
SQLModel.metadata.create_all(engine)

class Data:                
    def get_user_by_username(username: str):
        with Session(engine) as db_session:
            statement = select(User).where(User.username == username)
            return db_session.exec(statement).first()
        
    def create_user(user_data: RegisterModel):
        password_bytes = user_data.password.encode('utf-8')
        password_hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        user = User(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            username=user_data.username,
            age=user_data.age,
            city=user_data.city,
            country=user_data.country,
            password_hash=password_hash
        )
        with Session(engine) as db_session:
            db_session.add(user)
            db_session.commit()
            db_session.refresh(user)
        return user


    def verify_password(password: str, password_hash: str) -> bool:
        password_bytes = password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, password_hash)

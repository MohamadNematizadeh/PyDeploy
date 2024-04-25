from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseConfig

BaseConfig.arbitrary_types_allowed = True

# SQLAlchemy setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./beginner_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
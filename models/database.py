# import os
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, Session
from config import settings


# SQLALCHEMY_DATABASE_URI=os.getenv("FASTAPI_DB_URL")
SQLALCHEMY_DATABASE_URI = settings.DATABASE_URL_psycopg


# FASTAPI_DB_URL postgresql+psycopg://postgres:postgres@localhost:5432/natdb путь к базе данных строка подключения
engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# dependency
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db  # отдаём сессию
    finally:
        db.close()  # обязательно закрываем


# вход в  psql -h localhost -p 5432 -U postgres -d natdb

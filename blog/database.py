from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from util.config import get_database_url

SQLALCHEMY_DATABASE_URL = get_database_url()

# print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(str(SQLALCHEMY_DATABASE_URL))


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

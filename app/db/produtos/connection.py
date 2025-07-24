from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from app.config import PRODUTOS_USER, PRODUTOS_NAME, PRODUTOS_PASSWORD, PRODUTOS_HOST

engine = create_engine(f"mysql://{PRODUTOS_USER}:{PRODUTOS_PASSWORD}@{PRODUTOS_HOST}/{PRODUTOS_NAME}")
Base = declarative_base()

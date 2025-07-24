from sqlalchemy import Column, Integer, String, JSON
from app.db.produtos.connection import Base


class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String(45), nullable=False)


class Produtos(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    categoria = Column(String(45), nullable=False)
    tags = Column(JSON, nullable=False)

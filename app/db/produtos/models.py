from sqlalchemy import Column, Integer, String, JSON
from app.db.produtos.connection import Base


class UsuariosTable(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String(45), nullable=False)


class ProdutosTable(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    categoria = Column(String(45), nullable=False)
    tags = Column(JSON, nullable=False)

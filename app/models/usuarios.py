from app.db.produtos.connection import Base
from sqlalchemy import Column, Integer, String

# Modelo base para um usuário
class Usuarios(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)

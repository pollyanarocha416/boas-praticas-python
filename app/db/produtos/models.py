from sqlalchemy import Column, Integer, String
from app.db.produtos.connection import Base



# Definindo o modelo do usuário
class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String(45), nullable=False)

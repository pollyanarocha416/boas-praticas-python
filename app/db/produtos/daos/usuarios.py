from sqlalchemy.orm import sessionmaker
from app.db.produtos.connection import engine
from app.models.usuarios import Usuarios
from typing import List


class UsuariosDaos:
    def all(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            users = session.query(Usuarios).all()
            return [ {"id": u.id, "nome": u.nome} for u in users ]
        finally:
            session.close()

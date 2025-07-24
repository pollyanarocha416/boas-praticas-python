from sqlalchemy.orm import sessionmaker
from app.db.produtos.connection import engine
from app.db.produtos.models import Usuarios  # modelo ORM

class UsuariosDaos:
    def all(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            users = session.query(Usuarios).all()
            return list(users) if users else []
        finally:
            session.close()

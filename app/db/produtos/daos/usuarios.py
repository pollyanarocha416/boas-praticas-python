from sqlalchemy.orm import sessionmaker
from app.db.produtos.connection import engine
from app.db.produtos.models import UsuariosTable  # modelo ORM

class Usuarios:
    def all(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            users = session.query(UsuariosTable).all()
            return list(users) if users else []
        finally:
            session.close()

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

    def add(self, nome: str):
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            novo_usuario = UsuariosTable(nome=nome)
            session.add(novo_usuario)
            session.commit()
            session.refresh(novo_usuario)
            return novo_usuario
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

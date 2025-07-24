from sqlalchemy.orm import sessionmaker
from app.db.produtos.connection import engine
from app.db.produtos.models import Produtos 


class ProdutosDaos:
    def all(self):
        session = sessionmaker(bind=engine)
        session = session()
        try:
            produtos = session.query(Produtos).all()
            return list(produtos) if produtos else []
        finally:
            session.close()

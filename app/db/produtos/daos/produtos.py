from sqlalchemy.orm import sessionmaker
from app.db.produtos.connection import engine
from app.db.produtos.models import ProdutosTable 


class Produtos:
    def all(self):
        session = sessionmaker(bind=engine)
        session = session()
        try:
            produtos = session.query(ProdutosTable).all()
            return list(produtos) if produtos else []
        finally:
            session.close()

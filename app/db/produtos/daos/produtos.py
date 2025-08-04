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

    def add(self, nome: str, categoria: str, tags):
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            novo_produto = ProdutosTable(nome=nome, categoria=categoria, tags=tags)
            session.add(novo_produto)
            session.commit()
            session.refresh(novo_produto)
            return novo_produto
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

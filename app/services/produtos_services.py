from typing import List
from app.schemas.produtos_schemas import ProdutosRequest, Produto
from app.db.produtos.daos.produtos import Produtos


class ProdutosService:

    def get_products(self) -> List[Produto]:
        """
        Retrieve all products from the database.

        Returns:
            List[Usuarios]: A list of product objects.
        """
        produtos_dao = Produtos()
        produtos_db = produtos_dao.all()
        return produtos_db

    def add_product(self, nome: str, categoria: str, tags):
        produto_dao = Produtos()
        novo_produto = produto_dao.add(nome, categoria, tags)
        return ProdutosRequest(
            nome=novo_produto.nome,
            categoria=novo_produto.categoria,
            tags=novo_produto.tags,
        )

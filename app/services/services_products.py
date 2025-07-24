from typing import List
from app.schema.produtos import Produto
from app.db.produtos.daos.produtos import ProdutosDaos


class ProdutosService:

    def get_products(self) -> List[Produto]:
        """
        Retrieve all products from the database.

        Returns:
            List[Usuarios]: A list of product objects.
        """
        produtos_dao = ProdutosDaos()
        produtos = produtos_dao.all()
        return produtos

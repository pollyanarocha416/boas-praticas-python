from typing import List
from app.schemas.produtos_schemas import Produto
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

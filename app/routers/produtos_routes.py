from typing import List, Dict
from fastapi import APIRouter, HTTPException
from app.schemas.produtos_schemas import (
    Produto,
    ProdutosRequest,
    CreateProductRequest,
    HistoricoComprasRequest
)
from app.services.produtos_services import ProdutosService
import pdb

router = APIRouter()


produtos: List[Produto] = []
contador_produto: int = 1
historico_compras: Dict[int, List[int]] = {}


@router.post(
    path="/produtos/",
    summary="Cadastrar produto",
    description="Cadastra um novo produto no sistema.",
    status_code=201,
    response_description="Produto cadastrado com sucesso.",
    response_model=ProdutosRequest,
)
def criar_produto(nome: str, categoria: str, tags: List[str]) -> ProdutosRequest:
    """
    Cria um novo produto.

    Args:
        produto (CriarProduto): O objeto contendo os dados do produto a ser criado.

    Returns:
        Produto: O objeto do produto recém-criado com um ID gerado.
    """
    produto = ProdutosService().add_product(nome=nome, categoria=categoria, tags=tags)
    return produto


@router.get("/produtos/", response_model=List[Produto])
def listar_produtos():
    """
    Lista todos os produtos cadastrados.

    Returns:
        List[Produto]: Uma lista de objetos de produtos cadastrados.
    """

    produtos = ProdutosService().get_products()

    return produtos if produtos else []

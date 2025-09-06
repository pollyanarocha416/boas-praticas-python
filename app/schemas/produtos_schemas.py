from pydantic import BaseModel, Field
from typing import List


# Modelo base para produto
class ProdutosRequest(BaseModel):
    nome: str = Field(..., description = "Nome do produto")
    categoria: str = Field(..., description = "Categoria a qual esse produto faz parte")
    tags: List[str] = Field(..., description="Tags a qual esse produto faz parte")


# Modelo para criar um produto
class CreateProductRequest(ProdutosRequest):
    pass


# Modelo de produto com ID
class Produto(ProdutosRequest):
    id: int
    nome: str
    categoria: str
    tags: List[str]


# Modelo para histórico de compras do usuário
class HistoricoComprasRequest(BaseModel):
    produtos_ids: List[int]


# Modelo para preferências do usuário
class PreferenciasRequest(BaseModel):
    categorias: List[str] | None = None
    tags: List[str] | None = None

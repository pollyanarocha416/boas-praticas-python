from pydantic import BaseModel


# Modelo base para um usuário
class UsuarioSchema(BaseModel):
    id: int
    nome: str


class UsuarioSchemaCreate(BaseModel):
    nome: str

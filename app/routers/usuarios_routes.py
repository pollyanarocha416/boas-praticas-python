from fastapi import APIRouter
from typing import List
from app.schemas.usuarios_schemas import UsuarioSchema as Usuarios, UsuarioSchemaCreate as UsuariosCreate
from app.db.produtos.models import UsuariosTable as UsuariosModel
from app.services.usuarios_services import UsuariosService


router = APIRouter()

# usuarios: List[Usuarios] = []

contador_usuario: int = 1


@router.post(
    path="/usuarios/",
    summary="Cadastrar usuário",
    description="Cadastra um novo usuário no sistema.",
    status_code=201,
    response_description="Usuário cadastrado com sucesso.",
    response_model=Usuarios,
)
def criar_usuario(nome: str) -> Usuarios:
    usuario = UsuariosService().add_user(nome)
    return usuario


@router.get(
    path="/usuarios/",
    summary="Listar usuários",
    description="Retorna uma lista de todos os usuários cadastrados.",
    status_code=200,
    response_model=List[Usuarios],
)
def listar_usuarios() -> List[Usuarios]:
    """
    Lista todos os usuários cadastrados.

    Returns:
        List[Usuario]: Uma lista de objetos de usuários cadastrados.
    """

    usuarios = UsuariosService().get_users()
    if not usuarios:
        return []
    return usuarios

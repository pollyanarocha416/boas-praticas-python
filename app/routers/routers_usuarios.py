from fastapi import APIRouter
from typing import List
from app.models.usuarios import UsuarioSchema as Usuarios
from app.db.produtos.models import Usuarios as UsuariosModel
from app.db.produtos.daos.usuarios import UsuariosDaos
from app.services.services_users import UsuariosService


router = APIRouter()

usuarios: List[Usuarios] = []

contador_usuario: int = 1

@router.post("/usuarios/", response_model=Usuarios)
def criar_usuario(nome: str) -> Usuarios:
    """
    Rota para cadastrar novos usuários.

    Args:
        nome (str): nome do usuário a ser criado.

    Returns:
        Usuario: O objeto do usuário criado com um ID gerado.
    """
    global contador_usuario
    novo_usuario = UsuariosModel(id=contador_usuario, nome=nome)
    usuarios.append(novo_usuario)
    contador_usuario += 1
    return novo_usuario


@router.get(
        path="/usuarios/",
        summary="Listar usuários",
        description="Retorna uma lista de todos os usuários cadastrados.",
        status_code=200, 
        response_model=List[Usuarios]
        )
def listar_usuarios() -> List[Usuarios]:
    """
    Lista todos os usuários cadastrados.

    Returns:
        List[Usuario]: Uma lista de objetos de usuários cadastrados.
    """
    
    # criar funcao que chama os usuarios do bd
    usuarios = UsuariosService().get_users()
    if not usuarios:
        return []
    return usuarios

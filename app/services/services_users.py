from fastapi import APIRouter
from typing import List
from app.models.usuarios import UsuarioSchema as Usuarios
from app.db.produtos.models import Usuarios as UsuariosModel
from app.db.produtos.daos.usuarios import UsuariosDaos


class UsuariosService:

    def get_users(self) -> List[Usuarios]:
        """
        Retrieve all users from the database.

        Returns:
            List[Usuarios]: A list of user objects.
        """
        usuarios_dao = UsuariosDaos()
        usuarios = usuarios_dao.all()
        return [Usuarios(**u) for u in usuarios]

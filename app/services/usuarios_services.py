from typing import List
from app.schemas.usuarios_schemas import UsuarioSchema, UsuarioSchemaCreate
from app.db.produtos.daos.usuarios import Usuarios


class UsuariosService:

    def get_users(self) -> List[UsuarioSchema]:
        """
        Retrieve all users from the database.

        Returns:
            List[Usuarios]: A list of user objects.
        """
        usuarios_dao = Usuarios()
        usuarios_db = usuarios_dao.all()

        return usuarios_db

    def add_user(self, nome: str):
        usuarios_dao = Usuarios()
        novo_usuario = usuarios_dao.add(nome)
        return UsuarioSchema(id=novo_usuario.id, nome=novo_usuario.nome)

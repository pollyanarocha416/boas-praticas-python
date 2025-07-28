import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)


def test_criar_usuario():
    with patch(
        "app.services.usuarios_services.UsuariosService.add_user"
    ) as mock_add_user:
        mock_add_user.return_value = {"id": 1, "nome": "João"}
        response = client.post("/usuarios/", params={"nome": "João"})
        assert response.status_code == 201
        usuario = response.json()
        assert usuario["id"] == 1
        assert usuario["nome"] == "João"

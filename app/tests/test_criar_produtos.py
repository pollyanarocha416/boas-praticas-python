import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_criar_produtos():
    response = client.post(
        "/produtos/",
        json={
            "nome": "Produto Teste",
            "categoria": "categoria 1",
            "tags": ["tag1", "tag2"],
        },
    )
    assert response.status_code == 200

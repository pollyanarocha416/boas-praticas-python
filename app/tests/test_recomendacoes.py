import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_recomendacoes():
    response = client.post(
        "/recomendacoes/1", json={"categorias": ["Categoria 1"], "tags": ["tag1"]}
    )
    assert response.status_code == 200
    assert len(response.json()) == 1

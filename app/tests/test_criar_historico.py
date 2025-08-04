import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_criar_historico():
    response = client.post("/historico_compras/1", json={"produtos_ids": [1]})
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Histórico de compras atualizado"}

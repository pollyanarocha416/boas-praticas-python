import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_listar_produtos():
    response = client.get("/produtos/")
    assert response.status_code == 200

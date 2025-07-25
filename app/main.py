from typing import Dict
from fastapi import FastAPI
from app.routers import produtos_routes, usuarios_routes


MENSAGEM_HOME: str = "Bem-vindo à API de Recomendação de Produtos"


app = FastAPI()
app.include_router(produtos_routes.router)
app.include_router(usuarios_routes.router)


@app.get("/")
def home() -> Dict[str, str]:
    global MENSAGEM_HOME
    return {"mensagem": MENSAGEM_HOME}

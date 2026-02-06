from fastapi import FastAPI
from usuarios.infrastructure.router import router as usuario_router
from pedidos.infrastructure.router import router as pedido_router

app = FastAPI()

app.include_router(usuario_router)
app.include_router(pedido_router)

@app.get("/")
def read_root():
    return {"Mensaje": "¡Hola, Hexagonal + RabbitMQ funcionando! 🐰"}
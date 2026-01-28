from fastapi import FastAPI
# 1. Importamos el router que creamos en la carpeta de infraestructura
from usuarios.infrastructure.router import router as usuario_router

app = FastAPI()

# 2. Esta es la línea mágica: Conectamos las rutas de usuarios a la app principal
app.include_router(usuario_router)

@app.get("/")
def read_root():
    return {"Mensaje": "¡Hola, Hexagonal + RabbitMQ funcionando! 🐰"}
from fastapi import APIRouter, HTTPException
from usuarios.application.servicios import UsuarioService
from usuarios.infrastructure.in_memory_repository import InMemoryUsuarioRepository
from usuarios.infrastructure.rabbitmq_adapter import RabbitMQAdapter

router = APIRouter()

# Inyección de dependencias
repo = InMemoryUsuarioRepository()
notificador = RabbitMQAdapter()
servicio = UsuarioService(repo, notificador)

@router.post("/usuarios/")
def crear_usuario(nombre: str, email: str, password: str):
    try:
        usuario = servicio.registrar_usuario(nombre, email, password)
        return {"mensaje": "Usuario creado y notificado 🐰", "usuario": usuario}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

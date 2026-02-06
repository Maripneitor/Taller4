from fastapi import APIRouter, HTTPException
from usuarios.application.servicios import UsuarioService
from usuarios.infrastructure.in_memory_repository import InMemoryUsuarioRepository
from usuarios.infrastructure.rabbitmq_adapter import RabbitMQAdapter

router = APIRouter()

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

@router.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):
    try:
        usuario = servicio.obtener_usuario_por_id(usuario_id)
        return {
            "mensaje": f"Consultando el usuario {usuario_id}",
            "usuario": usuario,
            "equipo_base": ["sartén de teflón", "cuchillo de chef", "espátula"]
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/usuarios/")
def listar_usuarios():
    try:
        usuarios = servicio.obtener_todos_usuarios()
        return {"usuarios": usuarios, "total": len(usuarios)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

from fastapi import APIRouter, HTTPException, status
from typing import List
from services.usuarios.domain.usuario import Usuario, UsuarioCreate, UsuarioUpdate
from services.usuarios.application.services.usuario_service import UsuarioService
from services.usuarios.infraestructura.adapters.in_memory_repository import InMemoryUsuarioRepository

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

repo = InMemoryUsuarioRepository()
serv = UsuarioService(repo)

@router.post("/", response_model=Usuario, status_code=status.HTTP_201_CREATED)
def crear_usuario(u: UsuarioCreate):
    return serv.registrar_usuario(u)

@router.get("/{idusuario}", response_model=Usuario)
def obtener_usuario(idusuario: int):
    u = serv.obtener_usuario(idusuario)
    if u is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return u

@router.get("/", response_model=List[Usuario])
def listar_usuarios():
    return serv.listar_usuarios()

@router.put("/{idusuario}", response_model=Usuario)
def actualizar_usuario(idusuario: int, u: UsuarioUpdate):
    usr = serv.actualizar_usuario(idusuario, u)
    if usr is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usr

@router.delete("/{idusuario}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(idusuario: int):
    fue_eliminado = serv.eliminar_usuario(idusuario)
    if not fue_eliminado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return

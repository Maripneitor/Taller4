from fastapi import APIRouter, HTTPException, status
from typing import List
from services.usuarios.domain.usuario import Usuario, UsuarioCreate, UsuarioUpdate
from services.usuarios.application.services.usuario_service import UsuarioService
from services.usuarios.infraestructura.adapters.postgres_repository import PostgresUsuarioRepository
from services.usuarios.infraestructura.database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

def get_service():
    db = SessionLocal()
    try:
        repo = PostgresUsuarioRepository(db)
        return UsuarioService(repo)
    finally:
        db.close()

@router.post("/", response_model=Usuario, status_code=status.HTTP_201_CREATED)
def crear_usuario(u: UsuarioCreate):
    serv = get_service()
    return serv.registrar_usuario(u.model_dump())

@router.get("/{idusuario}", response_model=Usuario)
def obtener_usuario(idusuario: int):
    serv = get_service()
    u = serv.obtener_usuario(idusuario)
    if u is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return u

@router.get("/", response_model=List[Usuario])
def listar_usuarios():
    serv = get_service()
    return serv.listar_usuarios()

@router.put("/{idusuario}", response_model=Usuario)
def actualizar_usuario(idusuario: int, u: UsuarioUpdate):
    serv = get_service()
    usr = serv.actualizar_usuario(idusuario, u.model_dump(exclude_unset=True))
    if usr is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usr

@router.delete("/{idusuario}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(idusuario: int):
    serv = get_service()
    fue_eliminado = serv.eliminar_usuario(idusuario)
    if not fue_eliminado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return

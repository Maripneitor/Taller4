from typing import List, Optional
from services.usuarios.domain.usuario import Usuario, UsuarioCreate, UsuarioUpdate
from services.usuarios.application.ports.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def registrar_usuario(self, datos_create: UsuarioCreate) -> Usuario:
        datos = {
            "nombre": datos_create.nombre,
            "email": datos_create.email
        }
        return self.repository.save(datos)

    def obtener_usuario(self, idusuario: int) -> Optional[Usuario]:
        return self.repository.find_by_id(idusuario)

    def listar_usuarios(self) -> List[Usuario]:
        return self.repository.find_all()

    def actualizar_usuario(self, idusuario: int, datos_update: UsuarioUpdate) -> Optional[Usuario]:
        datos = datos_update.model_dump(exclude_unset=True)
        return self.repository.update(idusuario, datos)

    def eliminar_usuario(self, idusuario: int) -> bool:
        return self.repository.delete(idusuario)

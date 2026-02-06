from typing import List, Optional, Dict
from services.usuarios.domain.usuario import Usuario
from services.usuarios.application.ports.usuario_repository import UsuarioRepository

class InMemoryUsuarioRepository(UsuarioRepository):
    def __init__(self):
        self.usuarios: Dict[int, Usuario] = {}
        self.proximo_id = 1

    def save(self, usuario_data: dict) -> Usuario:
        nuevo_usuario = Usuario(
            idusuario=self.proximo_id,
            nombre=usuario_data["nombre"],
            email=usuario_data["email"]
        )
        self.usuarios[self.proximo_id] = nuevo_usuario
        self.proximo_id = self.proximo_id + 1
        return nuevo_usuario

    def find_by_id(self, idusuario: int) -> Optional[Usuario]:
        if idusuario in self.usuarios:
            return self.usuarios[idusuario]
        return None

    def find_all(self) -> List[Usuario]:
        lista = []
        for u in self.usuarios.values():
            lista.append(u)
        return lista

    def update(self, idusuario: int, usuario_data: dict) -> Optional[Usuario]:
        if idusuario not in self.usuarios:
            return None
        
        usuario_actual = self.usuarios[idusuario]
        usuario_actualizado = usuario_actual.model_copy(update=usuario_data)
        self.usuarios[idusuario] = usuario_actualizado
        return usuario_actualizado

    def delete(self, idusuario: int) -> bool:
        if idusuario in self.usuarios:
            del self.usuarios[idusuario]
            return True
        return False

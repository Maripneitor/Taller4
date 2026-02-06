from abc import ABC, abstractmethod
from typing import List, Optional
from services.usuarios.domain.usuario import Usuario

class UsuarioRepository(ABC):
    @abstractmethod
    def save(self, usuario_data: dict) -> Usuario:
        pass

    @abstractmethod
    def find_by_id(self, idusuario: int) -> Optional[Usuario]:
        pass

    @abstractmethod
    def find_all(self) -> List[Usuario]:
        pass

    @abstractmethod
    def update(self, idusuario: int, usuario_data: dict) -> Optional[Usuario]:
        pass

    @abstractmethod
    def delete(self, idusuario: int) -> bool:
        pass

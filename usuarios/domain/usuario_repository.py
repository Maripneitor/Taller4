from abc import ABC, abstractmethod
from .usuario import Usuario

class UsuarioRepository(ABC):
    @abstractmethod
    def guardar(self, usuario: Usuario):
        pass

    @abstractmethod
    def buscar_por_email(self, email: str) -> Usuario | None:
        pass
    
    @abstractmethod
    def obtener_por_id(self, usuario_id: int) -> Usuario | None:
        pass
    
    @abstractmethod
    def obtener_todos(self) -> list[Usuario]:
        pass

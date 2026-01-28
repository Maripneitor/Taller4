from usuarios.domain.usuario import Usuario
from usuarios.domain.usuario_repository import UsuarioRepository

class InMemoryUsuarioRepository(UsuarioRepository):
    def __init__(self):
        self.db = [] 

    def guardar(self, usuario: Usuario):
        self.db.append(usuario)

    def buscar_por_email(self, email: str) -> Usuario | None:
        return next((u for u in self.db if u.email == email), None)

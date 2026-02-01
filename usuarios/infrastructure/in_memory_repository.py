from usuarios.domain.usuario import Usuario
from usuarios.domain.usuario_repository import UsuarioRepository

class InMemoryUsuarioRepository(UsuarioRepository):
    def __init__(self):
        self.db = []
        self.next_id = 1

    def guardar(self, usuario: Usuario):
        usuario_dict = usuario.dict()
        usuario_dict["id"] = self.next_id
        self.db.append(usuario_dict)
        self.next_id += 1
        return usuario_dict

    def buscar_por_email(self, email: str) -> Usuario | None:
        usuario_dict = next((u for u in self.db if u["email"] == email), None)
        return Usuario(**usuario_dict) if usuario_dict else None

    def obtener_por_id(self, usuario_id: int) -> Usuario | None:
        usuario_dict = next((u for u in self.db if u["id"] == usuario_id), None)
        return Usuario(**usuario_dict) if usuario_dict else None

    def obtener_todos(self) -> list[Usuario]:
        return [Usuario(**u) for u in self.db]

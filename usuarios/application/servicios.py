from usuarios.domain.usuario import Usuario
from usuarios.domain.usuario_repository import UsuarioRepository
from usuarios.domain.notificador import Notificador

class UsuarioService:
    def __init__(self, repositorio: UsuarioRepository, notificador: Notificador):
        self.repositorio = repositorio
        self.notificador = notificador

    def registrar_usuario(self, nombre: str, email: str, password: str):
        nuevo_usuario = Usuario(nombre=nombre, email=email, password=password)
        
        usuario_guardado = self.repositorio.guardar(nuevo_usuario)
        
        self.notificador.enviar_mensaje(f"Bienvenido {nombre}, tu cuenta fue creada.")
        
        return usuario_guardado
    
    def obtener_usuario_por_id(self, usuario_id: int):
        usuario = self.repositorio.obtener_por_id(usuario_id)
        if not usuario:
            raise ValueError(f"Usuario con ID {usuario_id} no encontrado")
        return usuario
    
    def obtener_todos_usuarios(self):
        return self.repositorio.obtener_todos()

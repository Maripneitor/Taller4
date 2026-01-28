from usuarios.domain.usuario import Usuario
from usuarios.domain.usuario_repository import UsuarioRepository
from usuarios.domain.notificador import Notificador

class UsuarioService:
    def __init__(self, repositorio: UsuarioRepository, notificador: Notificador):
        self.repositorio = repositorio
        self.notificador = notificador

    def registrar_usuario(self, nombre: str, email: str, password: str):
        nuevo_usuario = Usuario(nombre=nombre, email=email, password=password)
        
        # 1. Guardar en BD
        self.repositorio.guardar(nuevo_usuario)
        
        # 2. Notificar a RabbitMQ
        self.notificador.enviar_mensaje(f"Bienvenido {nombre}, tu cuenta fue creada.")
        
        return nuevo_usuario

from pedidos.domain.pedido import Pedido
from pedidos.domain.pedido_repository import PedidoRepository

class PedidoService:
    def __init__(self, repositorio: PedidoRepository):
        self.repositorio = repositorio

    def crear_pedido(self, id_usuario: int, producto: str, cantidad: int):
        nuevo_pedido = Pedido(id_usuario=id_usuario, producto=producto, cantidad=cantidad)
        return self.repositorio.guardar(nuevo_pedido)
    
    def obtener_pedidos_usuario(self, usuario_id: int):
        return self.repositorio.obtener_por_usuario(usuario_id)

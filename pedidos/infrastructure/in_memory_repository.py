from pedidos.domain.pedido import Pedido
from pedidos.domain.pedido_repository import PedidoRepository

class InMemoryPedidoRepository(PedidoRepository):
    def __init__(self):
        self.db = []
        self.next_id = 1

    def guardar(self, pedido: Pedido):
        pedido_dict = pedido.dict()
        pedido_dict["id"] = self.next_id
        self.db.append(pedido_dict)
        self.next_id += 1
        return pedido_dict

    def obtener_por_usuario(self, usuario_id: int) -> list[Pedido]:
        # Filter logic: if 'id_usuario' matches
        return [Pedido(**p) for p in self.db if p["id_usuario"] == usuario_id]

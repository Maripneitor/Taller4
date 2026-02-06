from typing import List, Optional, Dict
from services.pedidos.domain.pedido import Pedido
from services.pedidos.application.ports.pedido_repository import PedidoRepository

class InMemoryPedidoRepository(PedidoRepository):
    def __init__(self):
        self.pedidos: Dict[int, Pedido] = {}
        self.proximo_id = 1

    def save(self, datos: dict) -> Pedido:
        nuevo_pedido = Pedido(
            id_pedido=self.proximo_id,
            idusuario=datos["idusuario"],
            total=datos["total"]
        )
        self.pedidos[self.proximo_id] = nuevo_pedido
        self.proximo_id = self.proximo_id + 1
        return nuevo_pedido

    def find_by_id(self, id_pedido: int) -> Optional[Pedido]:
        if id_pedido in self.pedidos:
            return self.pedidos[id_pedido]
        return None

    def find_all(self) -> List[Pedido]:
        lista = []
        for p in self.pedidos.values():
            lista.append(p)
        return lista

    def find_by_usuario(self, idusuario: int) -> List[Pedido]:
        lista = []
        for p in self.pedidos.values():
            if p.idusuario == idusuario:
                lista.append(p)
        return lista

    def update(self, id_pedido: int, pedido_data: dict) -> Optional[Pedido]:
        if id_pedido not in self.pedidos:
            return None
        
        actual = self.pedidos[id_pedido]
        nuevo = actual.model_copy(update=pedido_data)
        self.pedidos[id_pedido] = nuevo
        return nuevo

    def delete(self, id_pedido: int) -> bool:
        if id_pedido in self.pedidos:
            del self.pedidos[id_pedido]
            return True
        return False

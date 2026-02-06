from abc import ABC, abstractmethod
from .pedido import Pedido

class PedidoRepository(ABC):
    @abstractmethod
    def guardar(self, pedido: Pedido):
        pass
    
    @abstractmethod
    def obtener_por_usuario(self, usuario_id: int) -> list[Pedido]:
        pass

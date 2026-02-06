from abc import ABC, abstractmethod
from typing import List, Optional
from services.pedidos.domain.pedido import Pedido

class PedidoRepository(ABC):
    @abstractmethod
    def save(self, pedido_data: dict) -> Pedido:
        pass

    @abstractmethod
    def find_by_id(self, id_pedido: int) -> Optional[Pedido]:
        pass

    @abstractmethod
    def find_all(self) -> List[Pedido]:
        pass

    @abstractmethod
    def find_by_usuario(self, idusuario: int) -> List[Pedido]:
        pass

    @abstractmethod
    def update(self, id_pedido: int, pedido_data: dict) -> Optional[Pedido]:
        pass

    @abstractmethod
    def delete(self, id_pedido: int) -> bool:
        pass

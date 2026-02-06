from typing import List, Optional
from services.pedidos.domain.pedido import Pedido, PedidoCreate, PedidoUpdate
from services.pedidos.application.ports.pedido_repository import PedidoRepository

class PedidoService:
    def __init__(self, repository: PedidoRepository):
        self.repository = repository

    def crear_pedido(self, datos_create: PedidoCreate) -> Pedido:
        datos = {
            "idusuario": datos_create.idusuario,
            "total": datos_create.total
        }
        return self.repository.save(datos)

    def obtener_pedido(self, id_pedido: int) -> Optional[Pedido]:
        return self.repository.find_by_id(id_pedido)

    def listar_pedidos(self) -> List[Pedido]:
        return self.repository.find_all()

    def listar_pedidos_por_usuario(self, idusuario: int) -> List[Pedido]:
        return self.repository.find_by_usuario(idusuario)

    def actualizar_pedido(self, id_pedido: int, datos_update: PedidoUpdate) -> Optional[Pedido]:
        datos = datos_update.model_dump(exclude_unset=True)
        return self.repository.update(id_pedido, datos)

    def eliminar_pedido(self, id_pedido: int) -> bool:
        return self.repository.delete(id_pedido)

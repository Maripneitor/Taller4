from pydantic import BaseModel
from typing import Optional

class Pedido(BaseModel):
    id_pedido: int
    idusuario: int
    total: float

class PedidoCreate(BaseModel):
    idusuario: int
    total: float

class PedidoUpdate(BaseModel):
    total: Optional[float] = None

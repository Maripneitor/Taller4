from pydantic import BaseModel
from datetime import datetime

class Pedido(BaseModel):
    id_usuario: int
    producto: str
    cantidad: int
    fecha: datetime = datetime.now()

from fastapi import APIRouter, HTTPException, status
from typing import List
from services.pedidos.domain.pedido import Pedido, PedidoCreate, PedidoUpdate
from services.pedidos.application.services.pedido_service import PedidoService
from services.pedidos.infraestructura.adapters.in_memory_repository import InMemoryPedidoRepository

router = APIRouter(prefix="/pedidos", tags=["pedidos"])

repo = InMemoryPedidoRepository()
serv = PedidoService(repo)

@router.post("/", response_model=Pedido, status_code=status.HTTP_201_CREATED)
def crear_pedido(p: PedidoCreate):
    return serv.crear_pedido(p)

@router.get("/{id_pedido}", response_model=Pedido)
def obtener_pedido(id_pedido: int):
    p = serv.obtener_pedido(id_pedido)
    if p is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return p

@router.get("/", response_model=List[Pedido])
def listar_pedidos():
    return serv.listar_pedidos()

@router.get("/usuario/{idusuario}", response_model=List[Pedido])
def listar_pedidos_por_usuario(idusuario: int):
    return serv.listar_pedidos_por_usuario(idusuario)

@router.put("/{id_pedido}", response_model=Pedido)
def actualizar_pedido(id_pedido: int, p: PedidoUpdate):
    ped = serv.actualizar_pedido(id_pedido, p)
    if ped is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return ped

@router.delete("/{id_pedido}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_pedido(id_pedido: int):
    fue_eliminado = serv.eliminar_pedido(id_pedido)
    if not fue_eliminado:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return

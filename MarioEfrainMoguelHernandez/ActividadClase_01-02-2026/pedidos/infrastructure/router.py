from fastapi import APIRouter, HTTPException
from pedidos.application.servicios import PedidoService
from pedidos.infrastructure.in_memory_repository import InMemoryPedidoRepository

router = APIRouter()

repo = InMemoryPedidoRepository()
servicio = PedidoService(repo)

@router.post("/pedidos/")
def crear_pedido(id_usuario: int, producto: str, cantidad: int):
    try:
        pedido = servicio.crear_pedido(id_usuario, producto, cantidad)
        return {"mensaje": "Pedido creado", "pedido": pedido}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/usuarios/{usuario_id}/pedidos")
def listar_pedidos_usuario(usuario_id: int):
    try:
        pedidos = servicio.obtener_pedidos_usuario(usuario_id)
        return {"usuario_id": usuario_id, "pedidos": pedidos, "total": len(pedidos)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

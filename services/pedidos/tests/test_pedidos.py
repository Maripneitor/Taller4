import pytest
from fastapi.testclient import TestClient
from services.pedidos.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["service"] == "pedidos"

def test_crud_pedido():
    # 1. Crear
    pedido_data = {"idusuario": 10, "total": 99.9}
    response = client.post("/pedidos/", json=pedido_data)
    assert response.status_code == 201
    creado = response.json()
    assert creado["id_pedido"] == 1
    assert creado["idusuario"] == 10

    # 2. Consultar
    response = client.get("/pedidos/1")
    assert response.status_code == 200
    assert response.json()["id_pedido"] == 1

    # 3. Listar por usuario
    response = client.get("/pedidos/usuario/10")
    assert response.status_code == 200
    assert len(response.json()) == 1

    # 4. Actualizar
    response = client.put("/pedidos/1", json={"total": 150.0})
    assert response.status_code == 200
    assert response.json()["total"] == 150.0

    # 5. Eliminar
    response = client.delete("/pedidos/1")
    assert response.status_code == 204
    
    # 6. Verificar 404
    response = client.get("/pedidos/1")
    assert response.status_code == 404

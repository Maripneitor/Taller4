import pytest
from fastapi.testclient import TestClient
from services.usuarios.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_crud_usuario():
    # 1. Crear
    user_data = {"nombre": "Test User", "email": "test@example.com"}
    response = client.post("/usuarios/", json=user_data)
    assert response.status_code == 201
    creado = response.json()
    assert creado["nombre"] == "Test User"
    assert creado["idusuario"] == 1

    # 2. Consultar
    response = client.get("/usuarios/1")
    assert response.status_code == 200
    assert response.json()["idusuario"] == 1

    # 3. Listar
    response = client.get("/usuarios/")
    assert response.status_code == 200
    assert len(response.json()) >= 1

    # 4. Actualizar
    update_data = {"nombre": "Nombre Actualizado"}
    response = client.put("/usuarios/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["nombre"] == "Nombre Actualizado"

    # 5. Eliminar
    response = client.delete("/usuarios/1")
    assert response.status_code == 204
    
    # 6. Verificar 404
    response = client.get("/usuarios/1")
    assert response.status_code == 404

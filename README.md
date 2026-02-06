# Taller 4: Microservicios de Restaurante (Arquitectura Hexagonal)

Sistema de microservicios con IDs numéricos y arquitectura limpia.

## Arquitectura
- **domain**: Entidades simples.
- **application**: Puertos y Servicios (Lógica).
- **infraestructura**: API (FastAPI) y Adapters (Memoria).

## Cómo Correr con Docker
```bash
docker compose up --build
```

## Pruebas con curl (Paso a Paso)

### 1. Servicios Health
```bash
curl http://localhost:8001/health
curl http://localhost:8002/health
```

### 2. Flujo Usuarios (ID numérico)
```bash
# A) Crear usuario
curl -X POST http://localhost:8001/usuarios/ -H "Content-Type: application/json" -d '{"nombre": "Mario", "email": "mario@example.com"}'

# B) Listar todos
curl http://localhost:8001/usuarios/

# C) Consultar por ID 1
curl http://localhost:8001/usuarios/1

# D) Actualizar nombre
curl -X PUT http://localhost:8001/usuarios/1 -H "Content-Type: application/json" -d '{"nombre": "Mario Efrain"}'

# E) Eliminar
curl -X DELETE http://localhost:8001/usuarios/1

# F) Confirmar 404
curl http://localhost:8001/usuarios/1
```

### 3. Flujo Pedidos (ID numérico)
```bash
# A) Crear pedido para usuario 1
curl -X POST http://localhost:8002/pedidos/ -H "Content-Type: application/json" -d '{"idusuario": 1, "total": 100.5}'

# B) Listar todos
curl http://localhost:8002/pedidos/

# C) Listar pedidos del usuario 1
curl http://localhost:8002/pedidos/usuario/1

# D) Actualizar total del pedido 1
curl -X PUT http://localhost:8002/pedidos/1 -H "Content-Type: application/json" -d '{"total": 150.0}'

# E) Eliminar
curl -X DELETE http://localhost:8002/pedidos/1
```

## Pruebas Locales (Pytest)
```bash
export PYTHONPATH=$PYTHONPATH:.
python3 -m pytest services/usuarios/tests services/pedidos/tests -q
```

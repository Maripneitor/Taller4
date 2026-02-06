# Taller 4 - Arquitectura Hexagonal con FastAPI

## 📋 Descripción
Aplicación de usuarios y pedidos implementando arquitectura hexagonal con FastAPI y RabbitMQ.

## 🚀 Instalación y Ejecución

### Con Docker (Recomendado):
```bash
# 1. Clonar repositorio
git clone [TU-REPO-URL]
cd maripneitor-taller4

# 2. Levantar servicios
docker compose up --build

# 3. Acceder a la API
#    http://localhost:8000
#    http://localhost:8000/docs (Swagger UI)
```

## 📡 Endpoints

### Usuarios:
- `GET /` - Mensaje de bienvenida
- `POST /usuarios/?nombre=X&email=Y&password=Z` - Crear usuario
- `GET /usuarios/{id}` - Obtener usuario por ID
- `GET /usuarios/` - Listar todos los usuarios

### Pedidos:
- `POST /pedidos/?id_usuario=X&producto=Y&cantidad=Z` - Crear pedido
- `GET /usuarios/{id}/pedidos` - Listar pedidos de un usuario

## 🐰 RabbitMQ
- Dashboard: http://localhost:15672
- Usuario: `guest`
- Contraseña: `guest`
- Cola: `registro_usuarios`

## 🏗️ Arquitectura
```
usuarios/           pedidos/
├── domain/         ├── domain/
├── application/    ├── application/
└── infrastructure/ └── infrastructure/
```

## 📝 Autor
Mario Erain Moguel Hernandez

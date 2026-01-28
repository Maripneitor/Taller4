# Usamos Python 3.12 oficial (versión ligera)
FROM python:3.12-slim

# Establecemos la carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos primero los requisitos para aprovechar la caché de Docker
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo tu código al contenedor
COPY . .

# Comando para iniciar la app (escuchando en todas las interfaces)
CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0"]
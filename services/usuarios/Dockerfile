FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# OJO AQUÍ: Copiamos el código DENTRO de una carpeta "services/usuarios"
COPY . /app/services/usuarios

ENV PYTHONPATH=/app

# Ejecutamos apuntando a la nueva ruta
CMD ["python", "/app/services/usuarios/main.py"]

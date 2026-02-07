FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos en la estructura anidada
COPY . /app/services/pedidos

ENV PYTHONPATH=/app

CMD ["python", "/app/services/pedidos/main.py"]

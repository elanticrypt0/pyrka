FROM python:3.12-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements.txt primero
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# No necesitamos copiar todo el código aquí porque lo montaremos como volumen
# pero creamos la estructura de directorios necesaria
RUN mkdir -p /app/app

EXPOSE 5000
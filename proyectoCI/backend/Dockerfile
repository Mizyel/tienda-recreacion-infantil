# /backend/Dockerfile
# Usar una imagen base de Python (Contenedor 1)
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código (app.py)
COPY . .

# Exponer el puerto de la aplicación (Flask corre en 5000 por defecto)
EXPOSE 5000

# Comando para correr la aplicación cuando el contenedor inicie
CMD ["python", "app.py"]
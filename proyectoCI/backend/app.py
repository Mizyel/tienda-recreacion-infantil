# /backend/app.py
import os
import time
import psycopg2
from flask import Flask

app = Flask(__name__)

# Configuración de la conexión a la DB (usará el nombre del servicio 'db' definido en docker-compose)
DB_HOST = os.environ.get('DB_HOST', 'db')
DB_NAME = os.environ.get('DB_NAME', 'mydatabase')
DB_USER = os.environ.get('DB_USER', 'myuser')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'mypassword')

@app.route('/')
def index():
    try:
        # Intenta conectar a la Base de Datos
        conn = psycopg2.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD
        )
        conn.close()
        return "¡He conseguido comunicar correctamente el Backend y la Base de Datos! "
    except Exception as e:
        # Devuelve un error si la conexión falla
        return f"Error al conectar con la Base de Datos. Revisa la comunicación de contenedores: {e}", 500

if __name__ == '__main__':
    # Esperar un poco para que la DB inicie antes de conectar
    time.sleep(10)
    app.run(debug=True, host='0.0.0.0')

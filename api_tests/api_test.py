from flask import Flask, jsonify, request
import mysql.connector
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Crear la aplicación Flask
app = Flask(__name__)

# Función para obtener la conexión a la base de datos MySQL
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "2722"),
        database=os.getenv("DB_NAME", "bank")
    )

# Endpoint para obtener los usuarios
@app.route('/api/users', methods=['GET'])
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT id_cliente, nombre FROM clientes")
    users = cursor.fetchall()
    
    connection.close()
    
    # Retornar los usuarios como JSON
    return jsonify({"users": users})

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)

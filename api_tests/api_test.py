from flask import Flask, jsonify, request
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "2722"),
        database=os.getenv("DB_NAME", "bank"),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor  # Esto devolverá diccionarios
    )

@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT id_cliente, nombre FROM clientes")
            users = cursor.fetchall()
        return jsonify({"users": users}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'connection' in locals():
            connection.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
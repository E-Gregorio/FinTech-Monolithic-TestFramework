import mysql.connector

# Configuración de conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",      # Cambia esto si tu base de datos está en otro host
        user="root",           # Tu usuario de MySQL
        password="root",       # Tu contraseña de MySQL
        database="bank"        # Nombre correcto de la base de datos
    )

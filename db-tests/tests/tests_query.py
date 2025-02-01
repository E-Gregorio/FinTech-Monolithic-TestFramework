import os
from dotenv import load_dotenv
import mysql.connector
import pytest
import allure
from allure_commons.types import AttachmentType

load_dotenv()

# Función para obtener la conexión a la base de datos MySQL
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),    # Lee DB_HOST desde el .env
        user=os.getenv("DB_USER", "root"),         # Lee DB_USER desde el .env
        password=os.getenv("DB_PASSWORD", "2722"), # Lee DB_PASSWORD desde el .env
        database=os.getenv("DB_NAME", "bank")      # Lee DB_NAME desde el .env
    )

# Función para obtener los usuarios desde la base de datos
def get_all_users():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Consulta para obtener el listado de clientes
    cursor.execute("SELECT id_cliente, nombre FROM clientes")
    users = cursor.fetchall()
    
    connection.close()  # Cerramos la conexión
    return users

# Test para validar que la consulta devuelve usuarios
@pytest.fixture(scope="module")
def setup_db():
    yield
    # Aquí puedes agregar limpieza o configuración adicional si es necesario

@allure.feature('Cliente')
@allure.story('Listado de Clientes')
@pytest.mark.usefixtures("setup_db")
def test_get_all_users():
    # Obtenemos los usuarios de la base de datos
    users = get_all_users()
    
    # Adjuntamos el listado de clientes al reporte de Allure
    allure.attach(str(users), name="Listado de Clientes", attachment_type=AttachmentType.TEXT)
    
    # Validamos que al menos un usuario fue encontrado
    assert len(users) > 0, "No se encontraron clientes en la base de datos"

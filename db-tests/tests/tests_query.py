import os
from dotenv import load_dotenv
import pymysql
import pytest
import allure
from allure_commons.types import AttachmentType

load_dotenv()

def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD"),  # Quitar valor por defecto
        database=os.getenv("DB_NAME", "bank"),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

def get_all_users():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id_cliente, nombre FROM clientes")
            users = cursor.fetchall()
        return users
    except Exception as e:
        print(f"Error al obtener usuarios: {e}")
        return []
    finally:
        connection.close()

@pytest.fixture(scope="module")
def db_connection():
    conn = get_db_connection()
    yield conn
    conn.close()

@allure.feature('Cliente')
@allure.story('Listado de Clientes')
def test_get_all_users(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("SELECT id_cliente, nombre FROM clientes")
        users = cursor.fetchall()
    
    allure.attach(str(users), name="Listado de Clientes", attachment_type=AttachmentType.TEXT)
    
    assert users is not None, "La consulta retornó None"
    assert len(users) > 0, "No se encontraron clientes en la base de datos"
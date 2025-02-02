import os
from dotenv import load_dotenv
import pymysql
import pytest
import allure
from allure_commons.types import AttachmentType

load_dotenv()

def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "2722"),
        database=os.getenv("DB_NAME", "bank"),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

def get_all_users():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT id_cliente, nombre FROM clientes")
            users = cursor.fetchall()
        return users
    finally:
        if 'connection' in locals():
            connection.close()

@pytest.fixture(scope="module")
def setup_db():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
        conn.close()
    except pymysql.Error as err:
        pytest.fail(f"Error de conexión a la base de datos: {err}")
    yield

@allure.feature('Cliente')
@allure.story('Listado de Clientes')
@pytest.mark.usefixtures("setup_db")
def test_get_all_users():
    users = get_all_users()
    
    allure.attach(str(users), name="Listado de Clientes", attachment_type=AttachmentType.TEXT)
    
    assert users is not None, "La consulta retornó None"
    assert len(users) > 0, "No se encontraron clientes en la base de datos"
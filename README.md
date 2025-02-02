
---

# **FinTech Monolithic Test Framework**

Este repositorio contiene un framework de pruebas para un proyecto de FinTech utilizando tecnologías como y **Pytest** para la validación de datos en una base de datos MySQL. y API

## **Requisitos previos**


- **Python** 3.x instalado para ejecutar las pruebas de Pytest.
- **MySQL** como base de datos para las pruebas de validación de datos.
- **Docker** (opcional) si necesitas levantar la base de datos MySQL en un contenedor.

## **Configuración del entorno**



```bash
# Para instalar las dependencias de Playwright
npm install playwright
```

#### Pytest (Para pruebas en MySQL):

```bash
# Para instalar las dependencias de Pytest
pip install -r requirements.txt
```

Asegúrate de tener el archivo `requirements.txt` con las siguientes dependencias:

```txt
pytest
mysql-connector-python
python-dotenv
allure-pytest
```

### 2. **Configuración de variables de entorno**

Utiliza un archivo `.env` para almacenar las configuraciones de tu base de datos de forma segura:

#### Archivo `.env`

```plaintext
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=2722
DB_NAME=bank
```

### 3. **Crear la base de datos MySQL** (si no está configurada):

Puedes crear la base de datos manualmente o utilizar Docker para levantar un contenedor MySQL.

```bash
# Crear la base de datos en MySQL
CREATE DATABASE bank;
```

### 4. **Agregar datos aleatorios a la base de datos** (usando Python):

Puedes usar un script Python para insertar datos de prueba en la base de datos.

```python
import mysql.connector
from faker import Faker

# Generación de datos de prueba
fake = Faker()
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2722",
    database="bank"
)
cursor = connection.cursor()

# Crear la tabla de clientes
cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id_cliente INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255))")

# Insertar datos aleatorios
for _ in range(20):
    nombre = fake.name()
    cursor.execute("INSERT INTO clientes (nombre) VALUES (%s)", (nombre,))
    connection.commit()

# Cerrar la conexión
connection.close()
```



### 6. **Pruebas de base de datos con Pytest**

#### 6.1 **Comando para ejecutar las pruebas de base de datos**

```bash
# Ejecutar las pruebas de base de datos (validación de datos en MySQL)
pytest --alluredir=allure-results db-tests/tests/tests_query.py
```

#### 6.2 **Comando para generar el reporte Allure**

```bash
# Generar el reporte de Allure
allure serve allure-results
```

#### 6.3 **Ejemplo de prueba de base de datos**

```python
import os
from dotenv import load_dotenv
import mysql.connector
import pytest
import allure
from allure_commons.types import AttachmentType

# Función para obtener la conexión a la base de datos MySQL
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "2722"),
        database=os.getenv("DB_NAME", "bank")
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
```

### 7. **Generación de Reportes con Allure**

Después de ejecutar las pruebas, puedes generar un reporte visual con Allure:

1. Ejecuta las pruebas con `pytest` y guarda los resultados en `allure-results`.
2. Usa el siguiente comando para generar el reporte Allure:

```bash
allure serve allure-results
```


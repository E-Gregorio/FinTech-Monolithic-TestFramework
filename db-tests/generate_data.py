import mysql.connector
from faker import Faker
import random

# Inicializar Faker para generar datos aleatorios
fake = Faker()

# Configuración de conexión a la base de datos
def get_db_connection():
    print("Conectando a la base de datos...")
    return mysql.connector.connect(
        host="localhost",      # Cambia esto si tu base de datos está en otro host
        user="root",           # Tu usuario de MySQL
        password="2722",       # Tu contraseña de MySQL
        database="bank"        # Nombre de la base de datos "bank"
    )

# Función para generar datos aleatorios para los clientes
def generate_fake_client():
    return {
        'nombre': fake.name(),
        'direccion': fake.address(),
        'telefono': fake.phone_number()[:15],
        'email': fake.email()
    }

# Función para generar datos aleatorios para las cuentas
def generate_fake_account(client_id):
    return {
        'id_cliente': client_id,  # Asignamos el id_cliente generado en la tabla clientes
        'saldo': round(fake.random_number(digits=5), 2),  # Generar un saldo aleatorio con dos decimales
        'tipo_cuenta': fake.random_element(['ahorro', 'corriente'])  # Tipo de cuenta
    }

# Función para generar datos aleatorios para las transacciones
def generate_fake_transaction(account_ids):
    cuenta_origen = random.choice(account_ids)
    cuenta_destino = random.choice(account_ids)
    
    # Aseguramos que la cuenta de origen y destino no sean la misma
    while cuenta_origen == cuenta_destino:
        cuenta_destino = random.choice(account_ids)
    
    return {
        'id_cuenta_origen': cuenta_origen,  # ID de la cuenta de origen
        'id_cuenta_destino': cuenta_destino,  # ID de la cuenta de destino
        'monto': round(fake.random_number(digits=4), 2),  # Monto de la transacción con dos decimales
        'fecha': fake.date_this_month()  # Fecha de la transacción
    }

# Función para insertar un cliente en la base de datos
def insert_client(client_data):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = """
        INSERT INTO clientes (nombre, direccion, telefono, email)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (client_data['nombre'], client_data['direccion'], client_data['telefono'], client_data['email']))
    
    connection.commit()
    client_id = cursor.lastrowid  # Obtener el ID del cliente insertado
    cursor.close()
    connection.close()
    
    print(f"Cliente insertado con ID: {client_id}")  # Mensaje de depuración
    return client_id  # Devolver el id del cliente insertado

# Función para insertar una cuenta en la base de datos
def insert_account(account_data):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = """
        INSERT INTO cuentas (id_cliente, saldo, tipo_cuenta)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (account_data['id_cliente'], account_data['saldo'], account_data['tipo_cuenta']))
    
    connection.commit()
    account_id = cursor.lastrowid  # Obtener el ID de la cuenta insertada
    cursor.close()
    connection.close()
    
    print(f"Cuenta insertada con ID: {account_id}")  # Mensaje de depuración
    return account_id  # Devolver el id de la cuenta insertada

# Función para insertar una transacción en la base de datos
def insert_transaction(transaction_data):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = """
        INSERT INTO transacciones (id_cuenta_origen, id_cuenta_destino, monto, fecha)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (transaction_data['id_cuenta_origen'], transaction_data['id_cuenta_destino'], transaction_data['monto'], transaction_data['fecha']))
    
    connection.commit()
    cursor.close()
    connection.close()
    
    print(f"Transacción insertada: {transaction_data}")  # Mensaje de depuración

# Generar y insertar datos de prueba
def generate_and_insert_data():
    account_ids = []  # Lista para almacenar los IDs de las cuentas creadas
    print("Generando datos...")
    for _ in range(10):  # Vamos a insertar 10 registros de cada tipo
        # Insertar cliente
        client_data = generate_fake_client()
        client_id = insert_client(client_data)
        
        # Insertar cuenta para el cliente
        account_data = generate_fake_account(client_id)
        account_id = insert_account(account_data)
        account_ids.append(account_id)  # Guardar el ID de la cuenta creada
        
    # Insertar transacciones, entre cuentas aleatorias
    for _ in range(10):  # Insertar 10 transacciones
        transaction_data = generate_fake_transaction(account_ids)
        insert_transaction(transaction_data)

# Llamar a la función para generar e insertar los datos
generate_and_insert_data()

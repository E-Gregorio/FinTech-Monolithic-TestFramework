-- Crear tabla de clientes
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion TEXT,
    telefono VARCHAR(20),
    email VARCHAR(100) UNIQUE
);

-- Crear tabla de cuentas
CREATE TABLE IF NOT EXISTS cuentas (
    id_cuenta INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    saldo DECIMAL(10,2) DEFAULT 0.00,
    tipo_cuenta ENUM('ahorro', 'corriente') NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- Crear tabla de transacciones
CREATE TABLE IF NOT EXISTS transacciones (
    id_transaccion INT AUTO_INCREMENT PRIMARY KEY,
    id_cuenta_origen INT NOT NULL,
    id_cuenta_destino INT NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    fecha DATE,
    FOREIGN KEY (id_cuenta_origen) REFERENCES cuentas(id_cuenta),
    FOREIGN KEY (id_cuenta_destino) REFERENCES cuentas(id_cuenta)
);
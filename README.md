FinTech Monolithic Test Framework
Framework de pruebas automatizadas para un proyecto FinTech con validación de datos en MySQL y pruebas de API usando Pytest y Allure.
Estructura del Proyecto
FinTech-Monolithic-TestFramework/
│
├── .github/
│   └── workflows/
│       └── database-Api.yml
│
├── api_tests/
│   ├── api_test.py
│   └── test_api.py
│
├── db-tests/
│   ├── generate_data.py
│   ├── schema.sql
│   └── tests/
│       └── tests_query.py
│
├── allure-results/
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
Requisitos previos

## **Descripción de Directorios**

- `.github/workflows/`: Configuración de GitHub Actions para CI/CD
- `api_tests/`: Pruebas y scripts para APIs
- `db-tests/`: Pruebas y scripts para base de datos
- `allure-results/`: Resultados de reportes de pruebas

Python 3.13
MySQL 8
GitHub Actions (para CI/CD)

Configuración del entorno
Instalación de dependencias
bashCopy# Instalar dependencias de Python
pip install pytest==7.4.3
pip install allure-pytest==2.13.2
pip install pymysql
pip install cryptography
pip install flask
pip install requests==2.28.1
pip install python-dotenv
pip install mysql-connector-python
pip install faker
Configuración de variables de entorno
Crea un archivo .env:
plaintextCopyDB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_NAME=bank
Configuración de la base de datos
Crear base de datos
sqlCopyCREATE DATABASE bank;
Generar datos de prueba
bashCopypython db-tests/generate_data.py
Ejecución de pruebas
Pruebas de base de datos
bashCopy# Ejecutar pruebas de base de datos
pytest db-tests/tests/tests_query.py -v

# Generar reporte Allure
allure generate allure-results -o allure-report
Pruebas de API
bashCopy# Ejecutar pruebas de API
pytest api_tests/test_api.py -v
Integración Continua
Configuración de GitHub Actions:

Pruebas automatizadas en cada push o pull request
Generación de reportes Allure
Despliegue en GitHub Pages

Tecnologías

Python
Pytest
Allure
MySQL
GitHub Actions

Contribución

Hacer fork del repositorio
Crear rama de feature
Commit de cambios
Push a la rama
Crear Pull Request
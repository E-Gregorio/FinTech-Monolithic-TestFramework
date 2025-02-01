import pytest
import requests
import allure
import json
import time
from typing import Dict, Any

@allure.epic("API Testing Framework")
@allure.feature("User Management API")
class TestRecurso:
    # URL base de la API
    BASE_URL = "http://127.0.0.1:5000/api"  

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Verificar que el código de estado sea 200 al obtener usuarios")
    @allure.title("Test: Verificar respuesta exitosa con código de estado 200")
    def test_metodo_get(self):
        # Preparación de datos
        with allure.step("Preparar Solicitud GET"):
            endpoint = "/users"  # Endpoint de la API
            url = f"{self.BASE_URL}{endpoint}"
            
            # No se requieren parámetros en este caso
            params = {}

            # Registro de detalles de solicitud
            request_details = {
                "URL": url,
                "Método": "GET",
                "Parámetros": params
            }
            allure.attach(
                json.dumps(request_details, indent=2), 
                name="Detalles de Solicitud", 
                attachment_type=allure.attachment_type.JSON
            )

        # Ejecución de la solicitud
        with allure.step("Enviar Solicitud"):
            start_time = time.time()
            response = requests.get(url, params=params)
            response_time = time.time() - start_time

        # Documentación de la respuesta
        with allure.step("Documentar Respuesta"):
            response_details = {
                "Código de Estado": response.status_code,
                "Tiempo de Respuesta (s)": round(response_time, 2),
                "Cabeceras": dict(response.headers)
            }
            
            # Adjuntar detalles de respuesta
            allure.attach(
                json.dumps(response_details, indent=2), 
                name="Metadatos de Respuesta", 
                attachment_type=allure.attachment_type.JSON
            )
            
            # Adjuntar cuerpo de respuesta
            allure.attach(
                json.dumps(response.json(), indent=2), 
                name="Contenido de Respuesta", 
                attachment_type=allure.attachment_type.JSON
            )

        # Validaciones
        with allure.step("Validar Respuesta"):
            # Validación de código de estado
            assert response.status_code == 200, f"Esperado código 200, pero obtuvimos {response.status_code}"

            # Validación de que la respuesta contiene la lista de usuarios
            data = response.json()
            assert "users" in data, "La clave 'users' no está en la respuesta"

            # Validación de que al menos un usuario está presente en la respuesta
            assert len(data["users"]) > 0, "No se encontraron usuarios en la respuesta"

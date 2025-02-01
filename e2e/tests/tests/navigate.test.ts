import { test, expect } from '@playwright/test';
import { step } from 'allure-js-commons'; // Importar allure-js-commons para los pasos

test('Navegar a la página de Parabank y cerrarla', async ({ page }) => {
  
  // Paso 1: Descripción de la página
  await step('Descripcion de la pagina', async () => {
    console.log('Esta es una prueba automatizada de la página de Parabank');
  });

  // Paso 2: Abrir la página de Parabank
  await step('Abrir la página de Parabank', async () => {
    await page.goto('https://parabank.parasoft.com/parabank/index.htm');
  });

  // Paso 3: Verificar que el título de la página sea el esperado
  await step('Verificar que el título de la página sea el esperado', async () => {
    const pageTitle = await page.locator('img[alt="ParaBank"]');
    await expect(pageTitle).toBeVisible();
  });

  
  // Paso 5: Cerrar la página
  await step('Cerrar la página', async () => {
    await page.close();
  });
});

import { defineConfig } from '@playwright/test';

export default defineConfig({
  reporter: [['allure-playwright']],
  projects: [
    {
      name: 'playwright-tests',
      use: {
        browserName: 'chromium', // O 'firefox' o 'webkit'
      },
    },
  ],
});

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_field = page.locator('//div[@data-testid="login-form-email-input"]//input')
    password_field = page.get_by_test_id('login-form-password-input').locator('input')
    login_button = page.locator('//button[@id = "login-page-login-button"]')
    alert = page.locator("//div[contains(@class, 'MuiAlert-message')]")

    email_field.fill("rugaga@email.ru")
    password_field.fill("password")
    login_button.click()

    expect(alert).to_be_visible()
    expect(alert).to_have_text('Wrong email or password')

    page.wait_for_timeout(3000)

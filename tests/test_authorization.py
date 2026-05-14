from playwright.sync_api import expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password", [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password"),
])
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_field = chromium_page.locator('//div[@data-testid="login-form-email-input"]//input')
    password_field = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    login_button = chromium_page.locator('//button[@id = "login-page-login-button"]')
    alert = chromium_page.locator("//div[contains(@class, 'MuiAlert-message')]")

    email_field.fill(email)
    password_field.fill(password)
    login_button.click()

    expect(alert).to_be_visible()
    expect(alert).to_have_text('Wrong email or password')

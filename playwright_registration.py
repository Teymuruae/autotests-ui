from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id("registration-form-email-input").locator('input')
    username_input = page.get_by_test_id("registration-form-username-input").locator('input')
    password_input = page.get_by_test_id("registration-form-password-input").locator('input')
    registration_button = page.get_by_test_id("registration-page-registration-button")
    dashboard_label = page.get_by_test_id('dashboard-toolbar-title-text')

    email_input.fill("user.name@gmail.com")
    username_input.fill("username")
    password_input.fill("password")
    registration_button.click()

    expect(dashboard_label).to_be_visible()

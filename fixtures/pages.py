import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(chromium_page)


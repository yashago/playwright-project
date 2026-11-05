import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from utilities import config


@pytest.fixture(autouse=True)
def default_timeout(page: Page) -> None:
    page.set_default_timeout(config.DEFAULT_TIMEOUT_MS)

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login = LoginPage(page)
    login.open()
    return login

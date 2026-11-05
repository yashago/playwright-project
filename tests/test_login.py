import pytest
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_sign_in_to_gmail(page: Page):
    signInPage = LoginPage(page)
    signInPage.open()
    page.pause()
    signInPage.clickSignIn()
    signInPage.emailInput.fill("email@test.com")
    pass
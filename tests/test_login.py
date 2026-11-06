import re

import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from utilities.config import GITHUB_EMAIL, GITHUB_PASSWORD, GITHUB_USERNAME


@pytest.mark.smoke
def test_sign_in_to_gmail(page: Page):
    signInPage = LoginPage(page)
    signInPage.open()
    signInPage.clickSignIn()

    assert GITHUB_EMAIL is not None
    assert GITHUB_PASSWORD is not None

    signInPage.emailInput.fill(GITHUB_EMAIL)
    signInPage.passwordInput.fill(GITHUB_PASSWORD)
    signInPage.signInWithCredentials()

    expect(signInPage.greeting).to_be_visible()
    page.pause()
    expect(signInPage.greeting).to_contain_text(GITHUB_USERNAME)
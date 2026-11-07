import re

import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from utilities.config import EMAIL_GITHUB, PASSWORD_GITHUB, GITHUB_USERNAME


@pytest.mark.smoke
def test_sign_in_to_gmail(page: Page):
    signInPage = LoginPage(page)
    signInPage.open()
    signInPage.clickSignIn()

    assert EMAIL_GITHUB is not None
    assert PASSWORD_GITHUB is not None

    signInPage.emailInput.fill(EMAIL_GITHUB)
    signInPage.passwordInput.fill(PASSWORD_GITHUB)
    expect(signInPage.signInButton).to_be_visible()
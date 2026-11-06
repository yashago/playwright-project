from playwright.sync_api import Locator, Page

from pages.base_page import BasePage
from utilities import config
import re


class LoginPage(BasePage):
    PATH = config.GITHUB_URL

    def __init__(self, page: Page):
        super().__init__(page)


    @property
    def signIn(self) -> Locator:
        return self.page.get_by_role("link", name="Sign in")

    @property
    def signInButton(self) -> Locator:
        return self.page.get_by_role("button", name="Sign in", exact=True)


    @property
    def emailInput(self) -> Locator:
        print("Locating email input")
        return self.page.get_by_role("textbox", name="Username or email address")

    @property
    def passwordInput(self) -> Locator:
        print("Locating password input")
        return self.page.get_by_text("Password", exact=True)

    @property
    def greeting(self) -> Locator:
        print("Looking for GitHub greeting...")
        return self.page.get_by_text(re.compile(r"^Good (morning|afternoon|evening)"))

    def clickSignIn(self) -> None:
        print("Clickin on Sign In button")
        self.signIn.click()
        self.page.wait_for_url("**/login")

    def signInWithCredentials(self) -> None:
            print("Signing in...")
            self.signInButton.click()
            self.page.wait_for_load_state('domcontentloaded')
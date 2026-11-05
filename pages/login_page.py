from playwright.sync_api import Locator, Page

from pages.base_page import BasePage
from utilities import config


class LoginPage(BasePage):
    PATH = config.GMAIL_URL

    def __init__(self, page: Page):
        super().__init__(page)


    @property
    def signIn(self) -> Locator:
        return self.page.get_by_role("link", name="Sign into Gmail")

    @property
    def nextToPasswordButton(self) -> Locator:
        return self.page.get_by_role("button", name="Next")

    @property
    def emailInput(self) -> Locator:
        return self.page.get_by_role("textbox", name="Email or phone")

    def nextToPasswordButtonClick(self) -> None:
        with self.page.expect_popup() as popup:
            self.nextToPasswordButton.click(timeout=5000)
        self.page = popup.value

    @property
    def passwordInput(self) -> Locator:
        return self.page.get_by_role("textbox", name="Email or phone")

    def clickSignIn(self) -> None:
        """Click the Sign in link, which opens the form in a new tab, and move to that tab."""
        with self.page.expect_popup() as popup:
            self.signIn.click()
        self.page = popup.value

    # @property
    # def password_next_button(self) -> Locator:
    #     return self.page.locator("#passwordNext")

    # def open(self) -> None:
    #     super().open()
    #     self.click_sign_in_if_present()

    # def click_sign_in_if_present(self) -> None:
    #     """Get to the sign-in form from either page Gmail may show.

    #     A browser with no Google history is usually redirected straight to the form.
    #     Otherwise Gmail shows its marketing page, whose Sign in link opens the form
    #     in a new tab, so self.page moves to that tab.
    #     """
    #     self.sign_in_link.or_(self.email_input).first.wait_for()
    #     if self.sign_in_link.is_visible():
    #         with self.page.expect_popup() as popup:
    #             self.sign_in_link.click()
    #         self.page = popup.value
    #     self.email_input.wait_for()

    # def submit_email(self, email: str) -> None:
    #     self.email_input.fill(email)
    #     self.email_next_button.click()

    # def login(self, email: str, password: str) -> None:
    #     self.submit_email(email)
    #     self.password_input.fill(password)
    #     self.password_next_button.click()

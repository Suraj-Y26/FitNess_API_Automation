from playwright.sync_api import Page
from utils.config import Config

class LoginPage:
    """Page Object Model representing the ICICI styled Banking Login Page."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self._username_input = "input[name='username']"
        self._password_input = "input[name='password']"
        self._login_btn = "button#login-submit, button[type='submit']"

    def load(self) -> None:
        """Navigates to the FitNesse banking portal."""
        self.page.goto("http://localhost:8080/UserTests")

    def login(self, username: str, password: str) -> None:
        """Automates filling credentials and logging in."""
        self.load()
        self.page.fill(self._username_input, username)
        self.page.fill(self._password_input, password)
        self.page.click(self._login_btn)

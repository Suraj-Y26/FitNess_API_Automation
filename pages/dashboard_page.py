from playwright.sync_api import Page

class DashboardPage:
    """Page Object Model representing the post-login ICICI styled Banking Dashboard."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self._welcome_header = ".dashboard-welcome, .navbar-brand"
        self._account_balance = ".account-balance, #balance-value"
        self._logout_link = "a#logout, .logout-btn"

    def is_loaded(self) -> bool:
        """Verifies if the dashboard page welcome header is visible."""
        return self.page.is_visible(self._welcome_header)

    def get_welcome_message(self) -> str:
        """Returns the welcome text from the header."""
        return self.page.inner_text(self._welcome_header)

    def get_account_balance(self) -> str:
        """Returns the account balance value."""
        return self.page.inner_text(self._account_balance)

    def logout(self) -> None:
        """Clicks the logout link to return to login page."""
        self.page.click(self._logout_link)

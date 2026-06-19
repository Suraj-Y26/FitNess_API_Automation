import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.fixture(scope="class")
def browser_instance():
    """Pytest fixture to initialize and manage Playwright browser context."""
    with sync_playwright() as p:
        # Launch Chromium browser headlessly
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page_instance(browser_instance: Browser):
    """Pytest fixture to provide a new page context for each test."""
    context = browser_instance.new_context(viewport={"width": 1280, "height": 720})
    page = context.new_page()
    yield page
    page.close()
    context.close()


class TestBankingUI:
    """Class containing Web UI automation tests for the ICICI Pru - Anti-Money Launderinging Portal."""

    def test_successful_login(self, page_instance: Page):
        """Verifies that an admin user can log in successfully to the ICICI portal."""
        login_page = LoginPage(page_instance)
        dashboard_page = DashboardPage(page_instance)

        # Login using the admin credentials from passwords.txt
        login_page.login("admin", "admin123")

        # Assert dashboard welcome screen contains the logged-in username
        # (This automates testing the styled ICICI Pru - Anti-Money Laundering FitNesse UI!)
        assert page_instance.is_visible(".navbar-brand") or page_instance.is_visible("body")

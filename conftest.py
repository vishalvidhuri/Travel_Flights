import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():

    # Start Playwright
    with sync_playwright() as p:

        # Launch Chromium browser
        browser = p.chromium.launch(headless=False)

        # Create a new browser tab
        page = browser.new_page()

        # Give the page to the test
        yield page

        # Close browser after test finishes
        browser.close()
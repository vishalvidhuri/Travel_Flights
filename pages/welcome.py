from playwright.sync_api import sync_playwright, Page
from utils.config import BASE_URL

class WelcomePage:
    def __init__(self, page: Page): #__init__ is a constructor and automatically called when you create an object of a class
        self.page = page #Playwright page object that you passed into the class.

    def navigate(self):
        self.page.goto(BASE_URL)
        self.page.wait_for_timeout(5000)  # Wait for the page to load

    def select_departure_city(self, city: str):
        self.page.locator("select[name='fromPort']").select_option(city)

    def select_destination_city(self, city: str):
        self.page.locator("select[name='toPort']").select_option(city)

    def click_find_flights(self):
        self.page.get_by_role("button", name="Find Flights").click()
        self.page.wait_for_timeout(5000)  # Wait for the next page to load
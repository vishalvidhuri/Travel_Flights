from playwright.sync_api import expect
from pages.welcome import WelcomePage


def test_search_flight(page):
    # Create WelcomePage object
    welcome_page = WelcomePage(page)

    # Open the BlazeDemo home page
    welcome_page.navigate()

    # Select departure and destination cities
    welcome_page.select_departure_city("Boston")
    welcome_page.select_destination_city("Dublin")

    # Click Find Flights
    welcome_page.click_find_flights()

    # Verify that flight results page is displayed
    expect(page.locator("h3")).to_have_text(
        "Flights from Boston to Dublin:"
    )
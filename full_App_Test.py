from playwright.sync_api import sync_playwright, expect

def test_App():
    with sync_playwright() as p: # p is a variable created to access the browser
        browser = p.chromium.launch(headless=False) # Launching the browser in non-headless mode
        page = browser.new_page() # Creating a new page in the browser.
        #"page" represents the browser tab that we will interact with
        page.goto("https://blazedemo.com/")
        page.wait_for_timeout(5000)             # browser tab title
        print(page.locator("h1").inner_text())
        page.locator("select[name='fromPort']").select_option("Boston") # Selecting Boston as the departure city
        page.locator("select[name='toPort']").select_option("Dublin") # Selecting Dublin as the destination city
        page.wait_for_timeout(5000)
        page.get_by_role("button", name="Find Flights").click() # Clicking the "Find Flights" button
        page.wait_for_timeout(5000)
        page.locator("tr").filter(has_text="234").get_by_role("button", name="Choose This Flight").click()
        page.wait_for_timeout(5000)
        page.get_by_placeholder("First Last").fill("Mamta Rawat")
        page.get_by_role("textbox", name="Address").fill("123 Main Street")
        page.locator("input[name='city']").fill("Boston")
        page.get_by_role("textbox", name="state").fill("Massachusetts")
        page.locator("input[name='zipCode']").fill("12345")
        page.keyboard.press("PageDown")
        page.locator("#cardType").select_option("dinersclub")
        page.get_by_label("Credit Card Number").fill("1234567890123456")
        page.get_by_label("Month").fill("12")
        page.get_by_label("Year").fill("2025")
        page.locator("#nameOnCard").fill("Mamta Rawat")
        page.get_by_role("checkbox", name="Remember me").check()
        page.get_by_role("button", name="Purchase Flight").click()
        page.wait_for_timeout(5000)
        expect(page.locator("h1")).to_have_text("Thank you for your purchase today!")
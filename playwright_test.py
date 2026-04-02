from playwright.sync_api import sync_playwright

def test_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://rahulshettyacademy.com/AutomationPractice/")

        page.fill("#name", "Gaurav")
        page.click("#alertbtn")

        page.on("dialog", lambda dialog: dialog.accept())

        browser.close()
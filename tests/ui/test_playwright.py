from playwright.sync_api import sync_playwright

def test_google_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://google.com")
        assert "Google" in page.title()
        browser.close()

def test_google_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://google.com")
        page.fill("[name='q']", "Playwright Testing")
        page.press("[name='q']", "Enter")
        assert "Playwright" in page.title()
        browser.close()

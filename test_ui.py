from playwright.sync_api import sync_playwright


def test_example_page_title():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com")
        assert "Example Domain" in page.title()
        browser.close()


def test_example_page_heading():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com")
        heading = page.locator("h1").inner_text()
        assert heading == "Example Domain"
        browser.close()

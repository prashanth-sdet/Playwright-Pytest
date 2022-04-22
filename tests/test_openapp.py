from playwright.sync_api import sync_playwright
from playwright.sync_api import Page

# def test_app():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto("http://playwright.dev")
#         print(page.title())
#         browser.close()

def test_example_is_working(page):
        page.goto("http://playwright.dev")
        print(page.title())
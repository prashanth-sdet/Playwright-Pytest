# from playwright.sync_api import sync_playwright
# from playwright.sync_api import Page
# import sys
# sys.path.append("..")

import pytest
from support.utils import load_data

# def test_app():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto("http://playwright.dev")
#         print(page.title())
#         browser.close()

# def test_example_is_working(page):
#         page.goto("http://playwright.dev")
#         print(page.title())

class Test_pytest:

        @pytest.mark.parametrize(*load_data('openapp.json','testcase1'))
        def test_pytest(self, parameter1, parameter2, parameter3):
                print(parameter1, parameter2, parameter3)

        def test_valid_string(self, stringinput):
                print(stringinput)
        
        def test_compute(self, param1):
                print(param1)
        
        def test_case1(self, testdata_case1):
                print(testdata_case1)
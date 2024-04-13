import unittest
from selenium import webdriver

from Elefant.pages.base_page import BasePage
from Elefant.pages.home_page import HomePage


class TestHomePage(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    # Test Home Page Load: Verify that the Elefant home page loads successfully.
    def test_home_page_load(self):
        base_page_instance = BasePage(self.driver)
        home_page_instance = HomePage(self.driver)

        # open home page
        home_page_instance.open_home_page()
        # accept cookies
        base_page_instance.accept_cookies(BasePage.COOKIES_SELECTOR)

        page_title = self.driver.title
        self.assertIn('elefant', page_title.lower(), 'Page title error')

    def tearDown(self) -> None:
        self.driver.quit()

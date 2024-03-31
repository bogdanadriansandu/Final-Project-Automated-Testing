import time
import unittest
from selenium import webdriver

from Elefant.base_page import BasePage
from Elefant.login_page import LoginPage, LoggedInSuccessfully
from Elefant.page_locators import LoginPageData


class TestPositiveLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.my_driver = webdriver.Chrome()
        self.my_driver.maximize_window()
        self.my_driver.implicitly_wait(5)

    def test_valid_login(self):
        base_page_instance = BasePage(self.my_driver)
        login_page_instance = LoginPage(self.my_driver)
        successfully_logged_in_page = LoggedInSuccessfully(self.my_driver)

        # open login page
        login_page_instance.open_login_page()
        # accept cookies
        base_page_instance.accept_cookies(BasePage.COOKIES_SELECTOR)
        # execute login
        login_page_instance.execute_valid_login()

        assert LoginPageData.SUCCESSFULLY_LOGGED_IN_URL == successfully_logged_in_page.get_current_url(), \
            f"Actual URL is not the same as expected: current_url = {successfully_logged_in_page.get_current_url()}"

        assert LoginPageData.SUCCESSFULLY_LOGGED_IN_TEXT == successfully_logged_in_page.get_header_message(), \
            f"Header message not as expected: message = {successfully_logged_in_page.get_header_message()}"

        assert successfully_logged_in_page.is_logout_button_displayed(), "Logout button should be visible"

        time.sleep(2)

    def tearDown(self) -> None:
        self.my_driver.quit()

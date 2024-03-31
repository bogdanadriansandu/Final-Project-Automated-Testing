import time
import unittest
from selenium import webdriver

from Elefant.base_page import BasePage
from Elefant.login_page import LoginPage, LoginFailed
from Elefant.page_locators import LoginPageData, LoginPageLocators


class TestNegativeLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_empty_fields_login(self):
        base_page = BasePage(self.driver)
        login_page = LoginPage(self.driver)
        login_failed = LoginFailed(self.driver)

        # open login page
        login_page.open_login_page()
        # accept cookies
        base_page.accept_cookies(BasePage.COOKIES_SELECTOR)
        # execute empty fields login
        login_page.execute_empty_fields_login()
        time.sleep(3)

        assert LoginPageData.EMPTY_EMAIL_MESSAGE == login_failed.get_error_empty_email(), \
            "Empty email message is not as expected"

        assert LoginPageData.EMPTY_PASSWORD_MESSAGE == login_failed.get_error_empty_password(), \
            "Empty password message is not as expected"

        assert LoginPageData.LOGIN_PAGE_URL == login_failed.get_expected_url(), \
            f"Actual URL is not the same as expected: current_url = {login_failed.get_expected_url()}"

    def test_wrong_format_email(self):
        base_page = BasePage(self.driver)
        login_page = LoginPage(self.driver)
        login_failed = LoginFailed(self.driver)

        # open login page
        login_page.open_login_page()
        # accept cookies
        base_page.accept_cookies(BasePage.COOKIES_SELECTOR)
        # execute wrong format email
        login_page.execute_wrong_format_email()
        time.sleep(3)

        assert LoginPageData.EMAIL_INVALID_EXPECTED_MESSAGE == login_failed.get_error_wrong_format_email(), \
            "Email address wrong format message is not as expected"

    def test_invalid_credentials(self):
        base_page = BasePage(self.driver)
        login_page = LoginPage(self.driver)
        login_failed = LoginFailed(self.driver)

        # open login page
        login_page.open_login_page()
        # accept cookies
        base_page.accept_cookies(BasePage.COOKIES_SELECTOR)
        # execute invalid login
        login_page.execute_invalid_credentials()
        time.sleep(3)

        assert LoginPageData.WRONG_CREDENTIALS_MESSAGE == login_failed.get_error_message(), \
            "Email and Password failed message is not as expected"

        assert LoginPageData.LOGIN_PAGE_FAIL == login_failed.get_expected_url(), \
            f"Actual URL is not the same as expected: current_url = {login_failed.get_expected_url()}"

    def tearDown(self) -> None:
        self.driver.quit()

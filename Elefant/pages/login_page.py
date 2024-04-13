from Elefant.pages.base_page import BasePage
from Elefant.pages.page_locators import LoginPageData, LoginPageLocators


# LoginPage class - execution of all operations that can be done on this page
class LoginPage(BasePage):

    # open login page
    def open_login_page(self):
        super().open_url(LoginPageData.LOGIN_PAGE_URL)

    # execute valid login
    def execute_valid_login(self):
        # enter valid email
        super().type_text(LoginPageLocators.INPUT_EMAIL, LoginPageData.VALID_EMAIL)
        # enter valid password
        super().type_text(LoginPageLocators.INPUT_PASS, LoginPageData.VALID_PASSWORD)
        # click
        super().click(LoginPageLocators.LOGIN_BUTTON)

    # execute empty email && password
    def execute_empty_fields_login(self):
        # click
        super().click(LoginPageLocators.LOGIN_BUTTON)

    # execute wrong email format
    def execute_wrong_format_email(self):
        # enter wrong email format
        super().type_text(LoginPageLocators.INPUT_EMAIL, LoginPageData.WRONG_EMAIL_FORMAT)

    # execute invalid email && password
    def execute_invalid_credentials(self):
        # enter invalid email
        super().type_text(LoginPageLocators.INPUT_EMAIL, LoginPageData.INVALID_EMAIL)
        # enter invalid password
        super().type_text(LoginPageLocators.INPUT_PASS, LoginPageData.INVALID_PASSWORD)
        # click
        super().click(LoginPageLocators.LOGIN_BUTTON)


# class LoggedInSuccessfully - what happens after login if it was successful, or the login page
class LoggedInSuccessfully(BasePage, LoginPageData, LoginPageLocators):
    # get url after successful login
    def get_expected_url(self):
        return super().get_current_url()

    # get text in the login page header
    def get_header_message(self):
        return super().get_text(LoginPageLocators.LOGGED_IN_SUCCESSFULLY_SELECTOR)

    # check if the logout button menu is displayed
    def is_logout_button_displayed(self):
        return super().is_object_displayed(LoginPageLocators.LOGOUT_BUTTON)


# LoginFailed class - what happens after login fail, or the fail page
class LoginFailed(BasePage):
    # get alert error message
    def get_error_message(self):
        return super().get_text(LoginPageLocators.INVALID_CREDENTIALS_SELECTOR)

    # get error message for empty email
    def get_error_empty_email(self):
        return super().get_text(LoginPageLocators.EMAIL_EMPTY_XPATH)

    # get error message for empty password
    def get_error_empty_password(self):
        return super().get_text(LoginPageLocators.PASSWORD_EMPTY_XPATH)

    # get error message for wrong format email address
    def get_error_wrong_format_email(self):
        return super().get_text(LoginPageLocators.EMAIL_INVALID_XPATH)

    # get url after failed login
    def get_expected_url(self):
        return super().get_current_url()

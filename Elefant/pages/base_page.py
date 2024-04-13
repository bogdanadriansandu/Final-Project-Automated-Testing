import time

from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    COOKIES_SELECTOR = (By.CSS_SELECTOR, 'button#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')

    # driver (Chrome, Firefox, etc)
    def __init__(self, driver):
        self.driver = driver

    # open page
    def open_url(self, url: str):
        self.driver.get(url)
        self.driver.implicitly_wait(3)

    # get page title
    def get_page_title(self):
        return self.driver.title

    # get current url
    def get_current_url(self):
        return self.driver.current_url

    # finds an element and returns it
    def find(self, locator: tuple):  # tuple (By.XPATH, By.ID, etc., "//element")
        return self.driver.find_element(*locator)

    # find all the elements
    def find_all_elements(self, locator: tuple):  # tuple (By.XPATH, By.ID, etc., "//element")
        return self.driver.find_elements(*locator)

    # wait for an element to appear on the page
    def wait_for_visible_element(self, locator: tuple, wait_time=10):
        ex_wait = WebDriverWait(self.driver, wait_time)
        ex_wait.until(EC.visibility_of_element_located(locator))

    # wait for an element to appear on the page and to be clickable
    def wait_for_clickable_element(self, locator: tuple):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable(locator))

    # type text in an input label element
    def type_text(self, input_field, text: str):
        self.wait_for_visible_element(input_field, 7)
        self.find(input_field).send_keys(text)

    # get text from an element
    def get_text(self, element: tuple):
        self.wait_for_visible_element(element)
        return self.find(element).text

    # is the object displayed
    def is_object_displayed(self, element):
        try:
            return self.find(element).is_displayed()
        except NoSuchElementException:
            return False

    # click the button
    def click(self, button: tuple):
        self.wait_for_clickable_element(button)
        self.find(button).click()

    # accept cookies
    def accept_cookies(self, locator: tuple):
        try:
            self.wait_for_clickable_element(locator)
            self.find(locator).click()
        except Exception as e:
            print(f"Error clicking the element: {e}")

    # submit a form
    def submit_form(self, locator: tuple):
        self.find(locator).submit()
        time.sleep(1)

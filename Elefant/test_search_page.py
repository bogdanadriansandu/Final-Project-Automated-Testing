import time
import unittest
from selenium import webdriver

from Elefant.page_locators import SearchPageData
from Elefant.search_page import SearchPage


class TestSearchPage(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    # Search Functionality: Test searching for an item works correctly.
    def test_search_functionality(self):
        search_page_instance = SearchPage(self.driver)

        search_page_instance.execute_search()
        self.driver.implicitly_wait(3)

        self.assertIn(SearchPageData.SEARCH_TERM, self.driver.title)

    # check the number of results
    def test_check_results(self):
        search_page_instance = SearchPage(self.driver)

        self.test_search_functionality()
        self.driver.implicitly_wait(5)
        results = [search_page_instance.execute_check_results()]

        self.assertGreaterEqual(len(results), 1, 'No results found')

    # Product Listing: Verify that clicking on a product from the search results navigates to the product detail page.
    def test_product_listing(self):
        search_page_instance = SearchPage(self.driver)

        self.test_search_functionality()
        self.driver.implicitly_wait(3)

        search_page_instance.execute_product_listing()
        self.driver.implicitly_wait(3)

        self.assertIn("elefant.ro", self.driver.title)

    # Add to Cart: Test adding a product to the cart.
    def test_add_to_cart(self):
        search_page_instance = SearchPage(self.driver)

        self.test_product_listing()
        self.driver.implicitly_wait(3)
        result = search_page_instance.execute_add_to_cart()
        self.driver.implicitly_wait(5)

        self.assertNotEqual(result, "0")

    # Remove from Cart: Verify removing an item from the cart.
    def test_remove_from_cart(self):
        search_page_instance = SearchPage(self.driver)

        self.test_add_to_cart()
        self.driver.implicitly_wait(5)

        result = search_page_instance.execute_remove_from_cart()

        self.assertEqual(result, "0")

    def tearDown(self) -> None:
        self.driver.quit()

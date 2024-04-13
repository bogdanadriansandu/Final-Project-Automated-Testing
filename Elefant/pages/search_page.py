import time

from Elefant.pages.base_page import BasePage
from Elefant.pages.page_locators import SearchPageData, SearchPageLocators, HomePageData, CartPageLocators


class SearchPage(BasePage):
    # search for an item
    def execute_search(self):
        # open home page
        super().open_url(HomePageData.HOME_PAGE_URL)
        # accept cookies
        super().accept_cookies(BasePage.COOKIES_SELECTOR)

        # enter search term
        super().type_text(SearchPageLocators.INPUT_SEARCH_SELECTOR, SearchPageData.SEARCH_TERM)
        # submit
        super().submit_form(SearchPageLocators.INPUT_SEARCH_SELECTOR)
        time.sleep(2)

    def execute_check_results(self):
        super().find_all_elements(SearchPageLocators.SEARCH_RESULTS)

    def execute_product_listing(self):
        # super().wait_for_visible_element(SearchPageLocators.PRODUCT_DETAILS)
        # super().find(SearchPageLocators.PRODUCT_DETAILS).click()
        super().click(SearchPageLocators.PRODUCT_DETAILS)
        time.sleep(2)

    def execute_add_to_cart(self):
        super().click(CartPageLocators.ADD_TO_CART_BUTTON)
        time.sleep(2)
        cart = super().find(CartPageLocators.CART_COUNT_ITEMS)
        return cart.text

    def execute_remove_from_cart(self):
        super().click(CartPageLocators.VIEW_CART_BUTTON)
        super().click(CartPageLocators.DELETE_ITEM_BUTTON)
        cart = super().find(CartPageLocators.CART_COUNT_ITEMS)
        return cart.text

from Elefant.pages.base_page import BasePage
from Elefant.pages.page_locators import HomePageData


class HomePage(BasePage):

    # open home page
    def open_home_page(self):
        super().open_url(HomePageData.HOME_PAGE_URL)

from selenium.webdriver.common.by import By


class LoginPageData:
    # save all the data like: links, messages, texts, usernames, passwords, etc.
    LOGIN_PAGE_URL = "https://www.elefant.ro/login"
    SUCCESSFULLY_LOGGED_IN_URL = "https://www.elefant.ro/my-account"
    SUCCESSFULLY_LOGGED_IN_TEXT = "CONTUL MEU"
    EMAIL_INVALID_EXPECTED_MESSAGE = "Te rugăm să introduci o adresă de e-mail validă."
    WRONG_CREDENTIALS_MESSAGE = "Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou."
    EMPTY_EMAIL_MESSAGE = "Vă rugăm să introduceți o adresă de email."
    EMPTY_PASSWORD_MESSAGE = "Vă rugăm să introduceți parola."
    VALID_EMAIL = 'bopad94366@bitofee.com'
    VALID_PASSWORD = 'testare123'
    INVALID_EMAIL = 'eronat@bitofee.com'
    INVALID_PASSWORD = 'gresita'
    WRONG_EMAIL_FORMAT = "email"
    INPUT_EMAIL = (By.ID, 'ShopLoginForm_Login')
    INPUT_PASS = (By.ID, 'ShopLoginForm_Password')
    LOGIN_BUTTON = (By.NAME, 'login')
    LOGIN_PAGE_FAIL = \
        "https://www.elefant.ro/INTERSHOP/web/WFS/elefant-elefantRO-Site/ro_RO/-/RON/ViewUserAccount-ProcessLogin"


class LoginPageLocators:
    # save all the elements on the page using XPATH, or CSS, or ID, or LINK_TEXT, etc.
    INPUT_EMAIL = (By.ID, 'ShopLoginForm_Login')
    INPUT_PASS = (By.ID, 'ShopLoginForm_Password')
    LOGIN_BUTTON = (By.NAME, 'login')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a span.hidden-xs")
    LOGGED_IN_SUCCESSFULLY_SELECTOR = (By.CSS_SELECTOR, "div h2")
    LOGOUT_MENU_BUTTON = (By.CSS_SELECTOR, "span.hidden-xs")
    INVALID_CREDENTIALS_SELECTOR = (By.CSS_SELECTOR, "div.alert")
    EMAIL_EMPTY_XPATH = (By.XPATH, "//div/small[2]")
    EMAIL_INVALID_XPATH = (By.XPATH, "//div[1]/div/small[1]")
    PASSWORD_EMPTY_XPATH = (By.XPATH, "//div[2]/div/small")


class HomePageData:
    HOME_PAGE_URL = "https://www.elefant.ro/"


class HomePageLocators:
    pass


class SearchPageData:
    SEARCH_TERM = "Python"


class SearchPageLocators:
    INPUT_SEARCH_SELECTOR = (By.NAME, 'SearchTerm')
    SEARCH_RESULTS = (By.CSS_SELECTOR, '.product-title')
    PRODUCT_PRICE = (By.CLASS_NAME, 'current-price ')
    PRODUCT_DETAILS = (By.XPATH, "//div[1]/div/div/div[2]/a[3]/h2")


class CartPageData:
    EMPTY_CART_MESSAGE = "NU EXISTĂ NICI UN PRODUS ÎN COȘ."


class CartPageLocators:
    CART_BUTTON = (By.ID, "mini-cart-link")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@name='addProduct']")
    CART_COUNT_ITEMS = (By.CSS_SELECTOR, "span.cart-quantity")
    VIEW_CART_BUTTON = (By.XPATH, "//*[@id='miniCart']/div[3]/a")
    DELETE_ITEM_BUTTON = (By.CSS_SELECTOR, "a.btn-delete")
    EMPTY_CART_SELECTOR = (By.CSS_SELECTOR, "div.empty-cart h2")


class WishlistPageData:
    pass


class WishlistPageLocators:
    WISHLIST_XPATH = (By.XPATH, "//li[2]/a/div/span")
    WISHLIST_COUNT_ITEMS = (By.CSS_SELECTOR, "span.wishlist-count-text")
    WISHLIST_PRODUCT = (By.CSS_SELECTOR, "div.product-detail")

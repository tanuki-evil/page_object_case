from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "p")
    BASKET_HAS_PRODUCT = (By.CSS_SELECTOR, "basket-items")


class LoginPageLocators:
    EMAIL = (By.NAME, 'registration-email')
    PASSWORD1 = (By.NAME, 'registration-password1')
    PASSWORD2 = (By.NAME, 'registration-password2')
    BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators:
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    BASKET_ADD_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    BASKET_STRONG_NAMES = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")

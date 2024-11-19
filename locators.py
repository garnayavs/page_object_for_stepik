from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")

class BasketPageLocators():
    BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY_BASKET_TEXT =  (By.CSS_SELECTOR, '#content_inner p')


class MainPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_TITLE_MAIN = (By.CSS_SELECTOR, "div h1")
    PRODUCT_PRICE_MAIN = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_PRODUCT_SUCCESS_ADDED = (
        By.CSS_SELECTOR, ".alert-safe:nth-of-type(1) strong")
    ALERT_BASKET_PRICE = (By.CSS_SELECTOR, ".alert-safe:nth-of-type(3) strong")
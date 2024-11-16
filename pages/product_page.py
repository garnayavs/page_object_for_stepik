from .base_page import BasePage
from ..locators import ProductPageLocators


class ProductPage(BasePage):
    def shoud_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_BUTTON), "Basket button is not presented"

    def click_add_to_basket_button(self):
        basket_button = self.browser.find_element(
            *ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def shoud_be_alert_product_success_added(self):
        assert self.is_element_present(
            *ProductPageLocators.ALERT_PRODUCT_SUCCESS_ADDED), "Alert with product name is not presented"

    def shoud_be_alert_baket_price(self):
        assert self.is_element_present(
            *ProductPageLocators.ALERT_BASKET_PRICE), "Alert with price is not presented"

    def should_be_product_title_in_alert(self):
        assert self.text(*ProductPageLocators.PRODUCT_TITLE_MAIN) in self.text(
            *ProductPageLocators.ALERT_PRODUCT_SUCCESS_ADDED), f"Product name '{self.text(*ProductPageLocators.PRODUCT_TITLE_MAIN)}' not presented in success alert"

    def should_be_product_price_in_alert(self):
        assert self.text(*ProductPageLocators.PRODUCT_PRICE_MAIN) in self.text(
            *ProductPageLocators.ALERT_BASKET_PRICE), f"Product price '{self.text(*ProductPageLocators.PRODUCT_PRICE_MAIN)}' not presented in alert with basket"

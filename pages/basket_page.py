from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_text_empty_basket(self):
        element_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT)
        assert True == bool(element_text.text), "Text that basket is empty is not presented" 

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), "Basket formset is presented, but should not be"
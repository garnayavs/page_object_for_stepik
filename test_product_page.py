from .pages.product_page import ProductPage
from .locators import ProductPageLocators
import time

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.shoud_be_add_to_basket_button()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.shoud_be_alert_product_success_added()
    page.shoud_be_alert_baket_price()
    page.should_be_product_title_in_alert()
    page.should_be_product_price_in_alert()
    
    

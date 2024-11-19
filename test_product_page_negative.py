from .pages.product_page import ProductPage
import pytest

url= 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = url
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.click_add_to_basket_button()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = url
    page = ProductPage(browser, link,timeout=0)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = url
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.click_add_to_basket_button()
    page.should_be_mesage_dissapear()


    
    

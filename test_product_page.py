from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
import time

base_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}"
promo_links = [base_url.format(i) for i in range(10)]


@pytest.mark.parametrize('promo_link', promo_links)
def test_guest_can_add_product_to_basket(browser, promo_link):
    link = promo_link
    is_expected_failure = "offer7" in link
    if is_expected_failure:
        pytest.xfail(reason="Expected failure for promo offer7")
    page = ProductPage(browser, link)
    page.open()
    page.shoud_be_add_to_basket_button()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.shoud_be_alert_product_success_added()
    page.shoud_be_alert_baket_price()
    page.should_be_product_title_in_alert()
    page.should_be_product_price_in_alert()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url, timeout=0)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_text_empty_basket()
    
    

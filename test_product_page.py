from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
import time

product_url = 'http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/'


@pytest.mark.need_review
# Убрала параметризацию на время p2p-review. Оставила один url, чтобы тест быстрее проходил.
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, product_url)
    page.open()
    page.shoud_be_add_to_basket_button()
    page.click_add_to_basket_button()
    page.shoud_be_alert_product_success_added()
    page.shoud_be_alert_baket_price()
    page.should_be_product_title_in_alert()
    page.should_be_product_price_in_alert()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_url)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_url)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_url)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url, timeout=0)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_text_empty_basket()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_url, timeout=0)
    page.open()
    page.click_add_to_basket_button()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_url, timeout=0)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_url, timeout=0)
    page.open()
    page.click_add_to_basket_button()
    page.should_be_mesage_dissapear()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = MainPage(browser, product_url)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_register_form()
        login_page.register_new_user(f'{str(time.time())}@fakemail.org', "aboba12345")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_url, timeout=0)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_url)
        page.open()
        page.shoud_be_add_to_basket_button()
        page.click_add_to_basket_button()
        page.shoud_be_alert_product_success_added()
        page.shoud_be_alert_baket_price()
        page.should_be_product_title_in_alert()
        page.should_be_product_price_in_alert()
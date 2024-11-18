from .pages.product_page import ProductPage
import pytest

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

    
    

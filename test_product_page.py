from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
import pytest
import time

@pytest.mark.makenow
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "As!"
        page.register_new_user(email, password)
        page.should_be_authorized_user()
    
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link) 
        page.open()
        page.click_on_add_to_basket_button()
        page.solve_quiz_and_get_code()
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        page.should_be_correct_product_name_in_basket(product_name)
        page.should_be_correct_basket_price(product_price)
    
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link) 
        page.open()
        page.click_on_add_to_basket_button()
        page.should_not_be_success_message() 

@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link) 
    page.open()
    page.click_on_add_to_basket_button()
    page.solve_quiz_and_get_code()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.should_be_correct_product_name_in_basket(product_name)
    page.should_be_correct_basket_price(product_price)

@pytest.mark.jhgkjhjhgjhg
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link) 
    page.open()
    page.click_on_add_to_basket_button()
    page.should_not_be_success_message()

@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link) 
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link) 
    page.open()
    page.click_on_add_to_basket_button()
    page.should_be_disappeared_success_message()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser)
    basket_page.should_be_empty_basket_text()
    basket_page.should_not_be_products_in_basket()

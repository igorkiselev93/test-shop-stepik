from pages.base_page import BasePage
from pages.locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def click_on_add_to_basket_button(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
    
    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text
    
    def should_be_correct_product_name_in_basket(self, product_name):
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name == product_name_in_basket, "Product name doesn't match with product name in basket"

    def should_be_correct_basket_price(self, product_price):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, "Product price doesn't match with basket price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
    
    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message did not disappear"
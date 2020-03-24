from pages.base_page import BasePage
from pages.locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasketPage():
    def __init__(self, browser, timeout=10):
        self.browser = browser

    def empty_basket_text_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS),\
        "There are items in basket"
    
    def should_be_empty_basket_text(self):
        assert self.empty_basket_text_present(*BasketPageLocators.BASKET_IS_EMPTY), \
        "There is no empty_basket_text"
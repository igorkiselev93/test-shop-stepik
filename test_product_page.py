from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link) 
    page.open()
    page.click_on_add_to_basket_button()
    page.solve_quiz_and_get_code()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.should_be_correct_product_name_in_basket(product_name)
    page.should_be_correct_basket_price(product_price)

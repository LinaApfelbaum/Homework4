import allure
from framework import get_element


@allure.title("Search for elements on the Product page")
@allure.description("Test checks that 5 elements are presented on the Product page")
def test_product(browser, opencart_base_url, product_page):
    product_page.open(opencart_base_url, 57, 49)
    get_element(browser, product_page.PRODUCT_TITLE)
    get_element(browser, product_page.PRODUCT_CODE)
    get_element(browser, product_page.TAX)
    get_element(browser, product_page.WISH_LIST_BUTTON)
    get_element(browser, product_page.COMPARE_BUTTON)

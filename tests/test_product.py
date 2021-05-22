from framework import wait_element_by
from page_objects.product_page import ProductPage


def test_product(browser, opencart_base_url):
    product_page = ProductPage(browser)
    product_page.open(opencart_base_url, 57, 49)
    wait_element_by(browser, product_page.PRODUCT_TITLE)
    wait_element_by(browser, product_page.PRODUCT_CODE)
    wait_element_by(browser, product_page.TAX)
    wait_element_by(browser, product_page.WISH_LIST_BUTTON)
    wait_element_by(browser, product_page.COMPARE_BUTTON)

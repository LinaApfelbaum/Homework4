from framework import get_element


def test_product(browser, opencart_base_url, product_page):
    product_page.open(opencart_base_url, 57, 42)
    get_element(browser, product_page.PRODUCT_TITLE)
    get_element(browser, product_page.PRODUCT_CODE)
    get_element(browser, product_page.TAX)
    get_element(browser, product_page.WISH_LIST_BUTTON)
    get_element(browser, product_page.COMPARE_BUTTON)

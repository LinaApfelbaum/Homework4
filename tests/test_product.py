from framework import *


def test_product(browser, opencart_base_url):
    browser.get(opencart_base_url +
                "/index.php?route=product/product&path=57&product_id=49")
    wait_element_by_partial_link_text(browser, 'laxy')
    wait_element_by_tag_name(browser, 'footer')
    wait_element_by_xpath(
        browser, "//*[contains(text(),'Tray')]")
    wait_element_by_css_selector(
        browser, 'div.rating .fa-stack:nth-child(3) > i')
    wait_element_by_css_selector(browser, '.btn-group .fa-heart')

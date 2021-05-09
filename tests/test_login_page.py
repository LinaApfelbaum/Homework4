from framework import *


def test_login_page(browser, opencart_base_url):
    browser.get(opencart_base_url +
                "/index.php?route=account/login")
    wait_element_by_link_text(browser, 'Continue')
    wait_element_by_css_selector(browser, 'input[name="email"]')
    wait_element_by_xpath(
        browser, '//*[@id="content"]/div/div[2]/div/form/div[2]/a')
    wait_element_by_css_selector(browser, '#cart .fa-shopping-cart')
    wait_element_by_css_selector(browser, '[title="Checkout"]')

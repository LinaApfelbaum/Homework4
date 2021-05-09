from framework import *


def test_admin_login(browser, opencart_base_url):
    browser.get(opencart_base_url + "/admin")
    wait_elements_by_css_selector(browser, [
                                  '#header-logo', '#input-username', '.text-right', '.btn-primary', '.help-block'])
    wait_elements_by_xpath(browser, ['//div', '//a'])

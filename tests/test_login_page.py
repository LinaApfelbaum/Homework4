from framework import wait_element_by
from page_objects.login_page import LoginPage


def test_login_page(browser, opencart_base_url):
    login_page = LoginPage(browser)
    login_page.open(opencart_base_url)
    wait_element_by(browser, login_page.EMAIL_FIELD)
    wait_element_by(browser, login_page.PASSWORD_FIELD)
    wait_element_by(browser, login_page.FORGOTTEN_PASSWORD_LINK)
    wait_element_by(browser, login_page.NEW_CUSTOMER_BLOCK)
    wait_element_by(browser, login_page.RETURNING_CUSTOMER_BLOCK)

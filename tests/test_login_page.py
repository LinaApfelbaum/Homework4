from framework import get_element


def test_login_page(browser, opencart_base_url, login_page):
    login_page.open(opencart_base_url)
    get_element(browser, login_page.EMAIL_FIELD)
    get_element(browser, login_page.PASSWORD_FIELD)
    get_element(browser, login_page.FORGOTTEN_PASSWORD_LINK)
    get_element(browser, login_page.NEW_CUSTOMER_BLOCK)
    get_element(browser, login_page.RETURNING_CUSTOMER_BLOCK)

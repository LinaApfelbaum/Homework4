from framework import wait_elements_by
from page_objects.admin_page import AdminPage


def test_admin_login(browser, opencart_base_url):
    admin_page = AdminPage(browser)
    admin_page.open(opencart_base_url)
    wait_elements_by(browser, [
        admin_page.FORGOTTEN_PASSWORD_LINK,
        admin_page.LOGIN_BUTTON,
        admin_page.USERNAME_FIELD,
        admin_page.HEADER_LOGO,
        admin_page.HINT_BLOCK,
    ])

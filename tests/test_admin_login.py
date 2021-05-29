from framework import wait_elements_by


def test_admin_login(browser, opencart_base_url, admin_login_page):
    admin_login_page.open(opencart_base_url)
    wait_elements_by(browser, [
        admin_login_page.FORGOTTEN_PASSWORD_LINK,
        admin_login_page.LOGIN_BUTTON,
        admin_login_page.USERNAME_FIELD,
        admin_login_page.HEADER_LOGO,
        admin_login_page.HINT_BLOCK,
    ])

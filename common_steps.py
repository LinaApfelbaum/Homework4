import allure


@allure.step("Admin login")
def step_login(admin_login_page, opencart_base_url, admin_credentials):
    admin_login_page.open(opencart_base_url)
    admin_login_page.login(
        admin_credentials["login"], admin_credentials["password"])


@allure.step("Navigate to products submenu")
def step_navigate_to_products_submenu(admin_page):
    admin_page.open_menu(admin_page.MENU_CATALOG)
    admin_page.open_sub_menu(admin_page.SUBMENU_PRODUCTS)

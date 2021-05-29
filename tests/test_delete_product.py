def test_delete_product(opencart_base_url, admin_credentials, admin_login_page, admin_page, products_page):
    admin_login_page.open(opencart_base_url)
    admin_login_page.login(
        admin_credentials["login"], admin_credentials["password"])

    admin_page.open_menu(admin_page.MENU_CATALOG)
    admin_page.open_sub_menu(admin_page.SUBMENU_PRODUCTS)

    products_page.delete_last_product()

    products_page.assert_success_notification()

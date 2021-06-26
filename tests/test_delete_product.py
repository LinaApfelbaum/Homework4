import allure

from common_steps import step_login, step_navigate_to_products_submenu


@allure.title("Delete product in the Admin panel")
@allure.description("Test checks that product can be deleted in the Admin panel")
def test_delete_product(opencart_base_url, admin_credentials, admin_login_page, admin_page, products_page):
    step_login(admin_login_page, opencart_base_url, admin_credentials)
    step_navigate_to_products_submenu(admin_page)
    step_delete_product(products_page)

    products_page.assert_success_notification()


@allure.step("Delete product")
def step_delete_product(products_page):
    products_page.delete_last_product()

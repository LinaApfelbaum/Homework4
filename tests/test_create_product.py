import allure

from common_steps import step_login, step_navigate_to_products_submenu


@allure.title("Create product in the Admin panel")
@allure.description("Test checks that product can be created in the Admin panel")
def test_create_product(opencart_base_url, admin_credentials, admin_login_page, admin_page, products_page, product_add_page):
    step_login(admin_login_page, opencart_base_url, admin_credentials)
    step_navigate_to_products_submenu(admin_page)
    step_create_product(products_page, product_add_page)

    product_add_page.assert_success_notification()


@allure.step("Create product")
def step_create_product(products_page, product_add_page):
    products_page.add_product()
    product_add_page.fill_form("product_name", "meta_title_tag", "model")
    product_add_page.submit_form()

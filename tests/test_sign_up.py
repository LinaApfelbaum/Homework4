import allure
import time


@allure.title("Sign up into Opencart")
@allure.description("Test checks that user is able to register an account")
def test_sign_up(browser, opencart_base_url, sign_up_page):
    sign_up_page.open(opencart_base_url)
    unique_email = "unique_email{}@example.com".format(time.time())
    sign_up_page.send_form("first_name", "last_name",
                           unique_email, "telephone", "password")

    assert sign_up_page.SUCCESS_URL in browser.current_url

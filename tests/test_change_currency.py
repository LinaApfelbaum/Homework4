import allure


@allure.title("Change currency")
@allure.description("Test check that currency is being switch from default one")
def test_change_currency(opencart_base_url, home_page):
    home_page.open(opencart_base_url)
    home_page.change_currency("GBP")
    assert home_page.get_currency() == "£"

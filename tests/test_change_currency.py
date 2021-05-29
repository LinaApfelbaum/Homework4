def test_change_currency(opencart_base_url, home_page):
    home_page.open(opencart_base_url)
    home_page.change_currency("GBP")
    assert home_page.get_currency() == "£"

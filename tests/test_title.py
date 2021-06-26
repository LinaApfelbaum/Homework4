import allure


@allure.title("Website title")
@allure.description("Test checks that default title is correct")
def test_title(browser, base_url):
    browser.get(base_url)
    assert browser.title == "OpenCart - Open Source Shopping Cart Solution"

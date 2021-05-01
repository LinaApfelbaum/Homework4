

def test_title(browser, base_url):
    browser.get(base_url)
    assert browser.title == "OpenCart - Open Source Shopping Cart Solution"

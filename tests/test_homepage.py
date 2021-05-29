from framework import get_element


def test_homepage(browser, opencart_base_url, home_page):
    home_page.open(opencart_base_url)
    get_element(browser, home_page.MENU)
    get_element(browser, home_page.SLIDER)
    get_element(browser, home_page.SLIDER_PAGINATION)
    get_element(browser, home_page.BRANDS_SLIDER)
    get_element(browser, home_page.FEATURED_HEADER)

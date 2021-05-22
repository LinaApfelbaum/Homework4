from framework import wait_element_by
from page_objects.home_page import HomePage


def test_homepage(browser, opencart_base_url):
    home_page = HomePage(browser)
    home_page.open(opencart_base_url)
    wait_element_by(browser, home_page.MENU)
    wait_element_by(browser, home_page.SLIDER)
    wait_element_by(browser, home_page.SLIDER_PAGINATION)
    wait_element_by(browser, home_page.BRANDS_SLIDER)
    wait_element_by(browser, home_page.FEATURED_HEADER)

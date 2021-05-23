from selenium.webdriver.common.by import By

from framework import get_element


class HomePage:
    FEATURED_HEADER = (By.XPATH, '//*[@id="content"]/h3')
    SLIDER = (By.CSS_SELECTOR, ".swiper-viewport")
    SLIDER_PAGINATION = (By.CSS_SELECTOR, ".swiper-pagination")
    BRANDS_SLIDER = (By.ID, "carousel0")
    MENU = (By.CSS_SELECTOR, ".nav.navbar-nav")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#top button.dropdown-toggle")
    CURRENCY_DROPDOWN_OPTIONS = (
        By.CSS_SELECTOR, "#top .pull-left .dropdown-menu")

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def change_currency(self, code):
        currency_locator = (
            By.CSS_SELECTOR, '#top .pull-left .dropdown-menu button[name="{}"]'.format(code))
        get_element(self.driver, self.CURRENCY_DROPDOWN).click()
        get_element(self.driver, currency_locator).click()

    def get_currency(self):
        return get_element(self.driver, self.CURRENCY_DROPDOWN).text.strip()

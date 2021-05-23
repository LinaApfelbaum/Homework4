from selenium.webdriver.common.by import By

from framework import get_element


class AdminPage:
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    SUBMENU_PRODUCTS = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(2)")

    def __init__(self, driver):
        self.driver = driver

    def open_menu(self, menu_locator):
        get_element(self.driver, menu_locator).click()

    def open_sub_menu(self, submenu_locator):
        get_element(self.driver, submenu_locator).click()

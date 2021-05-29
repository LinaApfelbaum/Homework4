from selenium.webdriver.common.by import By

from framework import get_element


class AdminProductsPage:
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Add New"]')
    LAST_PRODUCT_CHECKBOX = (
        By.CSS_SELECTOR, "#form-product table tbody tr:last-child [type=checkbox]")
    DELETE_BUTTON = (By.CSS_SELECTOR, "[data-original-title=Delete]")
    SUCCESS_NOTIFICATION = (By.CSS_SELECTOR, ".alert-success")

    def __init__(self, driver):
        self.driver = driver

    def add_product(self):
        get_element(self.driver, self.ADD_PRODUCT_BUTTON).click()

    def delete_last_product(self):
        get_element(self.driver, self.LAST_PRODUCT_CHECKBOX).click()
        get_element(self.driver, self.DELETE_BUTTON).click()
        self.driver.switch_to.alert.accept()

    def assert_success_notification(self):
        get_element(self.driver, self.SUCCESS_NOTIFICATION)

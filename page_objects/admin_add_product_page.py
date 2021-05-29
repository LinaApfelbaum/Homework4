from selenium.webdriver.common.by import By

from framework import get_element


class AdminAddProductPage:
    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, "#input-name1")
    META_TITLE_TAG_FIELD = (By.CSS_SELECTOR, "#input-meta-title1")
    MODEL_FIELD = (By.CSS_SELECTOR, "#input-model")
    DATA_TAB = (By.CSS_SELECTOR, 'a[href="#tab-data"]')
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")
    SUCCESS_NOTIFICATION = (By.CSS_SELECTOR, ".alert-success")

    def __init__(self, driver):
        self.driver = driver

    def assert_success_notification(self):
        get_element(self.driver, self.SUCCESS_NOTIFICATION)

    def fill_form(self, product_name, meta_title_tag, model):
        get_element(self.driver, self.PRODUCT_NAME_FIELD).send_keys(
            product_name)
        get_element(self.driver, self.META_TITLE_TAG_FIELD).send_keys(
            meta_title_tag)
        get_element(self.driver, self.DATA_TAB).click()
        get_element(self.driver, self.MODEL_FIELD).send_keys(model)

    def submit_form(self):
        get_element(self.driver, self.SAVE_BUTTON).click()

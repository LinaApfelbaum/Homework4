from selenium.webdriver.common.by import By

from framework import get_element


class SignUpPage:
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#input-email")
    TELEPHONE_FIELD = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    PASSWORD_CONFIRM_FIELD = (By.CSS_SELECTOR, "#input-confirm")
    AGREEMENT_CHECKBOX = (By.CSS_SELECTOR, "[name=agree]")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[type=submit]")

    SUCCESS_URL = "/index.php?route=account/success"

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url + "/index.php?route=account/register")

    def send_form(self, first_name, last_name, email, telephone, password):
        get_element(
            self.driver, self.FIRST_NAME_FIELD).send_keys(first_name)
        get_element(self.driver, self.LAST_NAME_FIELD).send_keys(last_name)
        get_element(self.driver, self.EMAIL_FIELD).send_keys(email)
        get_element(self.driver, self.TELEPHONE_FIELD).send_keys(telephone)
        get_element(self.driver, self.PASSWORD_FIELD).send_keys(password)
        get_element(
            self.driver, self.PASSWORD_CONFIRM_FIELD).send_keys(password)
        get_element(self.driver, self.AGREEMENT_CHECKBOX).click()
        get_element(self.driver, self.CONTINUE_BUTTON).click()

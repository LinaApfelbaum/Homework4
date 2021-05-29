from selenium.webdriver.common.by import By

from framework import get_element


class AdminLoginPage:
    HEADER_LOGO = (By.CSS_SELECTOR, "#header-logo")
    USERNAME_FIELD = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    HINT_BLOCK = (By.CSS_SELECTOR, ".help-block")
    FORGOTTEN_PASSWORD_LINK = (By.CSS_SELECTOR, '.help-block > a')

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url + "/admin")

    def login(self, username, password):
        get_element(self.driver, self.USERNAME_FIELD).send_keys(username)
        get_element(self.driver, self.PASSWORD_FIELD).send_keys(password)
        get_element(self.driver, self.LOGIN_BUTTON).click()

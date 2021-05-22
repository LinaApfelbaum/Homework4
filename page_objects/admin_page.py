from selenium.webdriver.common.by import By


class AdminPage:
    HEADER_LOGO = (By.CSS_SELECTOR, "#header-logo")
    USERNAME_FIELD = (By.CSS_SELECTOR, "#input-username")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    HINT_BLOCK = (By.CSS_SELECTOR, ".help-block")
    FORGOTTEN_PASSWORD_LINK = (By.CSS_SELECTOR, '.help-block > a')

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url + "/admin")

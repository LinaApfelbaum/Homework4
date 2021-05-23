from selenium.webdriver.common.by import By


class LoginPage:
    FORGOTTEN_PASSWORD_LINK = (By.CSS_SELECTOR, "#input-password + a")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#input-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    RETURNING_CUSTOMER_BLOCK = (By.XPATH, '//*[@id="content"]/div/div[2]')
    NEW_CUSTOMER_BLOCK = (By.XPATH, '//*[@id="content"]/div/div[1]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="content"]/div/div[1] ')

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url + "/index.php?route=account/login")

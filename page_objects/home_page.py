from selenium.webdriver.common.by import By


class HomePage:
    FEATURED_HEADER = (By.XPATH, '//*[@id="content"]/h3')
    SLIDER = (By.CSS_SELECTOR, ".swiper-viewport")
    SLIDER_PAGINATION = (By.CSS_SELECTOR, ".swiper-pagination")
    BRANDS_SLIDER = (By.ID, "carousel0")
    MENU = (By.CSS_SELECTOR, ".nav.navbar-nav")

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

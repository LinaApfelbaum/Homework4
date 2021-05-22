from selenium.webdriver.common.by import By


class ProductPage:
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h1")
    WISH_LIST_BUTTON = (By.CSS_SELECTOR, ".btn-group .fa-heart")
    COMPARE_BUTTON = (
        By.CSS_SELECTOR, ".col-sm-4 button[data-original-title='Compare this Product']")
    PRODUCT_CODE = (By.XPATH, '//*[@id="content"]/div/div[2]/ul[1]/li[1]')
    TAX = (By.XPATH, '//*[@id="content"]/div/div[2]/ul[2]/li[2]')

    def __init__(self, driver):
        self.driver = driver

    def open(self, url, category_id, product_id):
        self.driver.get(url + "/index.php?route=product/product&path=" +
                        str(category_id) + "&product_id=" + str(product_id))

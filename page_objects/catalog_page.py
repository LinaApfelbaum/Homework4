from selenium.webdriver.common.by import By


class CatalogPage:
    BREADCRUMBS = (By.CSS_SELECTOR, ".breadcrumb")
    SIDEBAR = (By.CSS_SELECTOR, "#column-left")
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, "#list-view")
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, "#grid-view")
    PAGINATION_INFO = (By.XPATH, '//*[@id="content"]/div[5]/div[2]')

    def __init__(self, driver):
        self.driver = driver

    def open(self, url, category_id):
        self.driver.get(
            url + "/index.php?route=product/category&path=" + str(category_id))

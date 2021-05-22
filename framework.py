from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_element_by_link_text(driver, link_text, timeout=1):
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.LINK_TEXT, link_text)))


def wait_element_by_css_selector(driver, css_selector, timeout=1):
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))


def wait_element_by_xpath(driver, xpath, timeout=1):
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(
        (By.XPATH, xpath)))


def wait_element_by_id(driver, element_id, timeout=1):
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.ID, element_id)))


def wait_element_by_class_name(driver, class_name, timeout=1):
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.CLASS_NAME, class_name)))


def wait_element_by_tag_name(driver, tag_name, timeout=1):
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.TAG_NAME, tag_name)))


def wait_element_by_partial_link_text(driver, partial_link_text, timeout=1):
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, partial_link_text)))


def wait_elements_by_css_selector(browser, css_selectors, timeout=1):
    WebDriverWait(browser, timeout).until(
        visibility_of_elements(By.CSS_SELECTOR, css_selectors))


def wait_elements_by_xpath(driver, xpaths, timeout=1):
    WebDriverWait(driver, timeout).until(
        visibility_of_elements(By.XPATH, xpaths))


class visibility_of_elements(object):
    """
    An expectation for checking that all elements are present on the DOM of a
    page and visible.
    """

    def __init__(self, locator_type, locators):
        self.locators = locators
        self.locator_type = locator_type

    def __call__(self, browser):
        try:
            all_elements_are_visible = True
            for locator in self.locators:
                el = EC._find_element(browser, (self.locator_type, locator))
                is_visible = EC._element_if_visible(el)
                if not is_visible:
                    all_elements_are_visible = False
                    break

            return all_elements_are_visible
        except StaleElementReferenceException:
            return False

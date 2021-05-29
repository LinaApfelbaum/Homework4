import pytest
from selenium import webdriver
from selenium.webdriver.opera.options import Options

from page_objects.admin_add_product_page import AdminAddProductPage
from page_objects.admin_login_page import AdminLoginPage
from page_objects.admin_page import AdminPage
from page_objects.admin_products_page import AdminProductsPage
from page_objects.catalog_page import CatalogPage
from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from page_objects.product_page import ProductPage
from page_objects.sign_up_page import SignUpPage


def pytest_addoption(parser):
    parser.addoption(
        "--drivers_path", action="store", default="/home/lina/otus/drivers", help="Drivers path"
    )
    parser.addoption(
        "--browser", action="store", default="chrome", help="Select browser from chrome, firefox, opera"
    )
    parser.addoption(
        "--url", action="store", default="https://www.opencart.com", help="OpenCart base URL"
    )
    parser.addoption(
        "--opencart_url", action="store", default="https://demo.opencart.com", help="OpenCart base URL"
    )
    parser.addoption("--headless", action="store_true", help="Run headless")


@pytest.fixture()
def browser(request):
    drivers_path = request.config.getoption("--drivers_path")
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = headless
        driver = webdriver.Chrome(
            executable_path=drivers_path + "/chromedriver", options=options)

    elif browser == "opera":
        if headless:
            raise NotImplementedError("This mode is not supported")

        options = Options()
        driver = webdriver.Opera(
            executable_path=drivers_path + "/operadriver", options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = headless
        driver = webdriver.Firefox(
            executable_path=drivers_path + "/geckodriver", options=options)
    else:
        raise ValueError("Browser is not supported")

    request.addfinalizer(driver.quit)
    return driver


@pytest.fixture()
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture()
def opencart_base_url(request):
    return request.config.getoption("--opencart_url")

@pytest.fixture()
def admin_credentials():
    return {"login": "user", "password": "bitnami"}

@pytest.fixture()
def admin_login_page(browser):
    return AdminLoginPage(browser)

@pytest.fixture()
def admin_page(browser):
    return AdminPage(browser)

@pytest.fixture()
def products_page(browser):
    return AdminProductsPage(browser)

@pytest.fixture()
def product_add_page(browser):
    return AdminAddProductPage(browser)

@pytest.fixture()
def catalog_page(browser):
    return CatalogPage(browser)

@pytest.fixture()
def home_page(browser):
    return HomePage(browser)

@pytest.fixture()
def login_page(browser):
    return LoginPage(browser)

@pytest.fixture()
def product_page(browser):
    return ProductPage(browser)

@pytest.fixture()
def sign_up_page(browser):
    return SignUpPage(browser)

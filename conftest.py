import pytest
from selenium import webdriver
from selenium.webdriver.opera.options import Options


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
    parser.addoption("--headless", action="store_true", help="Run headless")


@pytest.fixture()
def browser(request):
    drivers_path = request.config.getoption("drivers_path")
    browser = request.config.getoption("browser")
    headless = request.config.getoption("headless")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = headless
        driver = webdriver.Chrome(
            executable_path=drivers_path + "/chromedriver", options=options)

    elif browser == "opera":
        options = Options()
        options.headless = headless
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
    return request.config.getoption("url")

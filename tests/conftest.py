import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config.config import Config
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome",
        help="Browser to run tests: chrome or firefox"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--disable-notifications")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    elif browser == "firefox":
        options = FirefoxOptions()
        options.set_preference("signon.rememberSignons", False)
        options.set_preference("dom.webnotifications.enabled", False)

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    else:
        pytest.fail(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    login = LoginPage(driver)
    login.login(Config.USERNAME, Config.PASSWORD)

    if "inventory" not in driver.current_url:
        pytest.fail("Login failed — blocking dependent tests")

    return driver

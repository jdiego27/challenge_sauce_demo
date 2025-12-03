import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from config.config import Config
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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
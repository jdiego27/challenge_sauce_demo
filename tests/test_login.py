from pages.login_page import LoginPage
from config.config import Config

def test_login_success(driver):
    login = LoginPage(driver)
    login.login(Config.USERNAME, Config.PASSWORD)
    assert "inventory" in driver.current_url


def test_login_invalid_password(driver):
    login = LoginPage(driver)
    login.login(Config.USERNAME, Config.WRONG_PASSWORD)

    error = login.find((login.ERROR_MESSAGE))
    assert "Epic sadface: Username and password do not match any user in this service" in error.text
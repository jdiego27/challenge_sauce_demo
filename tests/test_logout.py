from pages.logout_page import Logout
from config.config import Config

def test_logout(logged_in_driver):

    logout = Logout(logged_in_driver)
    logout.logout()

    assert logout.is_login_page_displayed()

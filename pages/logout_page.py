from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import LoginPage

class Logout(BasePage):

    BURGER_MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_BTN = (By.ID, "logout_sidebar_link")
    LOGIN_BTN = (By.ID, "login-button")

    def logout(self):
        self.click(self.BURGER_MENU_BTN)
        self.click(self.LOGOUT_BTN)

    def is_login_page_displayed(self):
        return self.find(self.LOGIN_BTN).is_displayed()
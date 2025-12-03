from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutOverview(BasePage):
    
    CHECKOUT_FINISH_BTN = (By.ID, "finish")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "h2.complete-header")

    def checkout_final(self):
        self.click(self.CHECKOUT_FINISH_BTN)
        
    def get_confirmation_message(self) -> str:
        """
        Return the text of the order completion header
        """
        return self.get_text(self.COMPLETE_HEADER)
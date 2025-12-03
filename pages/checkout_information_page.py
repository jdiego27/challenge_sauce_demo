from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutInformation(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CHECKOUT_CONTINUE_BTN = (By.ID, "continue")
    ERROR_INFORMATION_MSG = (By.CSS_SELECTOR, "div.error-message-container.error h3[data-test='error']")

    """
    def checkout_overview(self, firstname, lastname, zipcode):
        self.type(self.FIRST_NAME, firstname)
        self.type(self.LAST_NAME, lastname)
        self.type(self.ZIP_CODE, zipcode)
        self.click(self.CHECKOUT_CONTINUE_BTN)
        """

    def get_error_message(self):
        return self.get_text(self.ERROR_INFORMATION_MSG)
    
    def checkout_overview(self, fname=None, lname=None, zip_code=None):
        if fname is not None:
            self.type(self.FIRST_NAME, fname)
            
        if lname is not None:
            self.type(self.LAST_NAME, lname)
                
        if zip_code is not None:
            self.type(self.ZIP_CODE, zip_code)
                    
        self.click(self.CHECKOUT_CONTINUE_BTN)

    def get_error_message(self) -> str:
        """
        Return the text of the order completion header
        """
        return self.get_text(self.ERROR_INFORMATION_MSG)

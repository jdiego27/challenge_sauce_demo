from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ProductPage(BasePage):
    # Locators
    PRODUCT_BTN_TEMPLATE = "add-to-cart-{}"
    CHECKOUT_LINK = (By.CLASS_NAME, "shopping_cart_link")
    
    # Locators
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")


    def add_product(self, product_id: str):
        product_btn_locator = (By.ID, self.PRODUCT_BTN_TEMPLATE.format(product_id))
        self.click(product_btn_locator)

    def add_products(self, product_ids: list[str]):

        for product_id in product_ids:
            self.add_product(product_id)

    def get_cart_count(self) -> int:
        try:
            badge = self.wait.until(
                EC.visibility_of_element_located(self.CART_BADGE)
            )
            return int(badge.text)
        except:
            return 0
        
    def remove_product(self, product_id: str):
        remove_btn_locator = (By.ID, f"remove-{product_id}")
        self.click(remove_btn_locator)


    def go_to_checkout(self):
        self.click(self.CHECKOUT_LINK)



from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SortPage(BasePage):

    SORT_CONTAINER = (By.CLASS_NAME, "product_sort_container")
    PRICE_INVENTORY = (By.CLASS_NAME, "inventory_item_price")

    def sort_to_low_to_high(self):
        self.select(self.SORT_CONTAINER, "Price (low to high)")

    def get_all_prices(self):
        prices = self.finds(self.PRICE_INVENTORY)
        price_list = []
        
        for p in prices:
            text_price = p.text
            clean_price = text_price.replace("$", "")
            number_price = float(clean_price)
            price_list.append(number_price)
            
        return price_list
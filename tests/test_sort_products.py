from pages.sort_products_page import SortPage

def test_sort_to_low_to_high(logged_in_driver):

    sort_products_page = SortPage(logged_in_driver)
    sort_products_page.sort_to_low_to_high()
    prices = sort_products_page.get_all_prices()
    
    assert prices == sorted(prices)
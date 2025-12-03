from pages.product_page import ProductPage

def test_add_product_to_cart(logged_in_driver):
    driver = logged_in_driver

    product_page = ProductPage(driver)
    # Add the backpack product
    product_page.add_product("sauce-labs-backpack")

    # Assert cart badge shows 1 item
    assert product_page.get_cart_count() == 1

def test_add_multiple_products_to_cart(logged_in_driver):
    product_page = ProductPage(logged_in_driver)

    products = [
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt"
    ]
    product_page.add_products(products)

    assert product_page.get_cart_count() == len(products)
    
def test_remove_product_from_cart(logged_in_driver):
    product_page = ProductPage(logged_in_driver)

    products = [
        "sauce-labs-backpack",
        "sauce-labs-bike-light"
    ]

    # Add two products first
    product_page.add_products(products)
    assert product_page.get_cart_count() == 2

    # Remove one product
    product_page.remove_product("sauce-labs-backpack")

    # Assert cart updates correctly
    assert product_page.get_cart_count() == 1

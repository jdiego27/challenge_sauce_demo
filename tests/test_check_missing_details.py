from pages.product_page import ProductPage
from pages.checkout_information_page import CheckoutInformation
from pages.checkout_page import CheckoutPage

def test_checkout_missing_details(logged_in_driver):

    product_page = ProductPage(logged_in_driver)
    checkout_page = CheckoutPage(logged_in_driver)
    checkout_information_page = CheckoutInformation(logged_in_driver)

    product_page.add_product("sauce-labs-backpack")
    product_page.go_to_checkout()

    checkout_page.checkout()

    checkout_information_page.checkout_overview(fname=None, lname="Leon", zip_code="07008")

    assert checkout_information_page.get_error_message() == "Error: First Name is required"
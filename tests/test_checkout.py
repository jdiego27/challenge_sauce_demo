from pages.product_page import ProductPage
from pages.checkout_information_page import CheckoutInformation
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverview

def test_checkout(logged_in_driver):
    product_page = ProductPage(logged_in_driver)
    checkout_page = CheckoutPage (logged_in_driver)
    checkout_information_page = CheckoutInformation(logged_in_driver)
    checkout_overview_page = CheckoutOverview(logged_in_driver)

    
    product_page.add_product("sauce-labs-backpack")
    product_page.go_to_checkout()

    checkout_page.checkout()

    checkout_information_page.checkout_overview("Juan", "Leon", "07008")

    checkout_overview_page.checkout_final()

    assert checkout_overview_page.get_confirmation_message() == "Thank you for your order!"



    
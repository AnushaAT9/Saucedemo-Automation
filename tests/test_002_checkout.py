from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from faker import Faker
import json

fake = Faker()

def test_checkout_form(driver):
    with open("utils/config.json") as config_file:
        config = json.load(config_file)

    login_page = LoginPage(driver)
    login_page.login(config["username"], config["password"])

    checkout = CheckoutPage(driver)
    checkout.add_product_and_checkout()

    checkout.fill_checkout_form(
        fake.first_name(),
        fake.last_name(),
        fake.postcode()
    )

    assert checkout.verify_checkout_page()
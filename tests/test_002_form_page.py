from pages.form_page import FormPage
from pages.login_page import LoginPage

from faker import Faker
import json

fake = Faker()

def test_checkout_form(driver):
    with open("utils/config.json") as config_file:
        config = json.load(config_file)

    login_page = LoginPage(driver, config)
    login_page.enter_username()
    login_page.enter_password()
    login_page.click_login()

    form_page = FormPage(driver, config)

    form_page.add_to_cart()
    form_page.verify_cart()
    form_page.click_checkout()


    form_page.enter_first_name(fake.first_name())
    form_page.enter_last_name(fake.last_name())
    form_page.enter_postal_code(fake.postcode())

    form_page.click_continue()
    form_page.click_finish()

    success = form_page.verify_success_message()

    assert success.is_displayed()
    assert "Thank you for your order!" in success.text
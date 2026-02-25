from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

        self.add_to_cart_id = 'add-to-cart-sauce-labs-backpack'
        self.cart_class = 'shopping_cart_link'
        self.check_out_id = 'checkout'
        self.first_name_id = 'first-name'
        self.last_name_id = 'last-name'
        self.postal_code_id = 'postal-code'
        self.continue_button_id = 'continue'
        self.finish_button_id = 'finish'
        self.success_message_class = 'complete-header'

    def add_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.add_to_cart_id))
        ).click()

    def verify_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, self.cart_class))
        ).click()

    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.check_out_id))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.first_name_id))
        )

    def enter_first_name(self, first):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.first_name_id))
        ).send_keys(first)

    def enter_last_name(self, last):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.last_name_id))
        ).send_keys(last)

    def enter_postal_code(self, postal):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.postal_code_id))
        ).send_keys(postal)

    def click_continue(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.continue_button_id))
        ).click()

    def click_finish(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.finish_button_id))
        ).click()

    def verify_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.success_message_class))
        )
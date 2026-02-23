from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT = (By.ID, "checkout")

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_and_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART)).click()
        self.driver.find_element(*self.CART).click()
        self.driver.find_element(*self.CHECKOUT).click()

    def fill_checkout_form(self, first, last, postal):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal)
        self.driver.find_element(*self.CONTINUE).click()

    def verify_checkout_page(self):
        return "Checkout" in self.wait.until(
            EC.visibility_of_element_located(self.TITLE)
        ).text
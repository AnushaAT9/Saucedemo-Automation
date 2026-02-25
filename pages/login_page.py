from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

        self.id_username = "user-name"
        self.id_password = "password"
        self.id_login_button = "login-button"

    def enter_username(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.id_username))
        ).send_keys(self.config["username"])

    def enter_password(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.id_password))
        ).send_keys(self.config["password"])

    def click_login(self):
        wait = WebDriverWait(self.driver, 10)
        login_button = wait.until(
            EC.element_to_be_clickable((By.ID, self.id_login_button))
        )
        login_button.click()
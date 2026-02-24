import json
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_valid_login(driver):
    with open("utils/config.json") as config_file:
        config = json.load(config_file)

    login_page = LoginPage(driver, config)
    login_page.enter_username()
    login_page.enter_password()
    login_page.click_login()

    dashboard_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    assert dashboard_element.is_displayed()
    assert "Swag Labs" in driver.title
import json
from pages.login_page import LoginPage

def test_valid_login(driver):
    with open("utils/config.json") as config_file:
        config = json.load(config_file)

    login_page = LoginPage(driver)
    login_page.login(config["username"], config["password"])

    assert login_page.is_logged_in()
    assert "Swag Labs" in driver.title
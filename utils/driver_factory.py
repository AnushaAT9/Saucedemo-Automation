import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    with open("utils/config.json") as config_file:
        config = json.load(config_file)

    chrome_options = Options()

    if config["headless"]:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.maximize_window()
    driver.get(config["base_url"])

    return driver
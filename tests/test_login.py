from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_valid_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        driver.get("https://www.saucedemo.com")
        # Locate username field and enter valid username
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # Similarly locate password field and enter valid password
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # Similarly locate and click the login button
        driver.find_element(By.ID, "login-button").click()

        time.sleep(5)
        assert "inventory.html" in driver.current_url

        print("Login test passed successfully.")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_valid_login()

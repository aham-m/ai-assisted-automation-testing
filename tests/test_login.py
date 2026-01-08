from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_valid_login():
    # Setup Chrome browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        # Open SauceDemo login page
        driver.get("https://www.saucedemo.com")

        # Locate username field and enter valid username
        driver.find_element(By.ID, "user-name").send_keys("standard_user")

        # Locate password field and enter valid password
        driver.find_element(By.ID, "password").send_keys("secret_sauce")

        # Click the login button
        driver.find_element(By.ID, "login-button").click()

        # Wait for page to load
        time.sleep(5)

        # Verify successful login by checking URL
        assert "inventory.html" in driver.current_url

        print("Login test passed successfully.")

    finally:
        # Close the browser
        driver.quit()


# IMPORTANT: Call the test function
if __name__ == "__main__":
    test_valid_login()
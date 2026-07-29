from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com")

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "user-name"))
)

password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()

WebDriverWait(driver, 10).until(
    EC.url_contains("inventory")
)

assert "inventory" in driver.current_url, "Login failed!"

print("✅ Login Test Passed")

time.sleep(5)
driver.quit()
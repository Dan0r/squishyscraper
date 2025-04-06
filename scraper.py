import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# function for WebDriver to check cookie-button-deny
def check_cookie(c):
    try:
        return root.find_element(By.CSS_SELECTOR, "[data-testid='uc-deny-all-button']").is_enabled()
    except Exception:
        return False


## Setup chrome options for WSL2
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
chrome_options.binary_location = f"{homedir}/chrome-linux64/chrome"
webdriver_service = Service(f"{homedir}/chromedriver-linux64/chromedriver")

# Choose Chrome Browser
driver = webdriver.Chrome()

# Open Zalando
url = "https://www.zalando.de"
shoe = "Asics Japan S"

driver.get(url)

# Navigate into Shadow DOM to select cookie-button 
try:
    # Wait for parent to appear
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#usercentrics-root"))
        )
        
    host = driver.find_element(By.CSS_SELECTOR, '#usercentrics-root')
    root = host.shadow_root

    # Wait for the button inside the shadow root to be clickable
    WebDriverWait(driver, 10).until(
        check_cookie
    )
    # Select button and click 
    cookie = root.find_element(By.CSS_SELECTOR, "[data-testid='uc-deny-all-button']")
    cookie.click()
    print("cookie was clicked")
except Exception as e:
    print("cookie not clicked", e)

# Search for Asics Japan S 
searchbox = driver.find_element("id","header-search-input")
searchbox.click()
searchbox.send_keys(shoe)
searchbox.send_keys(Keys.ENTER)

# Search for color


time.sleep(3)
driver.quit()

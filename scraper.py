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
color = "JAPAN S - Trainers - black"
size = 45

driver.get(url)

# Navigate into Shadow DOM to select cookie-button 
try:
    # Wait for parent to appear
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "usercentrics-root"))
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

# Search for color (of course you can just include it in the search term)
    # Search XPath globally and match string
shoe_color = driver.find_element(By.XPATH, f"//h3[text()='{color}']")
try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((shoe_color))
    ).click()
    print("shoe_color clicked")
except Exception as e:
    print("shoe_color not clicked", e)

# Search shoe size, notice if out of stock
try:
    # Select button 
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "picker-trigger"))
    ).click()
    # Search size
    select_size = driver.find_element(By.XPATH, f"//span[text()={size}]")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((select_size))
    ).click()
    # Determine if out of stock
        # Navigate back in the tree and find the parent element
    
    # !!!Figure out why this Works!!!
    time.sleep(2)
    parent_element = driver.find_element(By.XPATH, f"//span[text()='{size}']/ancestor::*[@data-is-selected]")
    print(parent_element.get_attribute("data-is-selected"))
    print("Button clicked")
except Exception as e:
    print("Button not clicked", e)




# Read and save price 

time.sleep(3)
driver.quit()

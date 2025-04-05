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

# set-up for WSL2
## Setup chrome options
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
    time.sleep(3)
    cookie = driver.execute_script('return document.querySelector("#usercentrics-root").shadowRoot.querySelector("[data-testid=\'uc-deny-all-button\']")')
    cookie.click()
    print("cookie was clicked")
except:
    print("cookie not clicked")
# Search for Asics Japan S 
searchbox = driver.find_element("id","header-search-input")
searchbox.click()

searchbox.send_keys(shoe)
searchbox.send_keys(Keys.ENTER)

time.sleep(3)
driver.quit()

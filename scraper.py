import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

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
browser = webdriver.Chrome()
url = "https://www.zalando.de"
browser.get(url)
title = browser.title
print(f"Der Titel der URL '{url}' lautet: '{title}'")

#description = browser.find_element(By.NAME, "description").get_attribute("content")

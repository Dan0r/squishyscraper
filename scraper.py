import os
from dotenv import find_dotenv, load_dotenv
import requests
import time
import smtplib
from email.message import EmailMessage
import ssl



from datetime import datetime
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
# function to convert price into float
def parse_price(price):
    # remove Euro, replace comma with dot, remove blank_space
    price = price.replace("€", "").replace(",",".").strip()
        # convert into float
    return float(price)


## Setup chrome options for WSL2
chrome_options = Options()

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~/programming/squishyscraper")
chrome_options.binary_location = f"{homedir}/chrome-linux64/chrome"
webdriver_service = Service(f"{homedir}/chromedriver-linux64/chromedriver")

# Choose Chrome Browser
driver = webdriver.Chrome()
# Open Zalando
url = "https://www.zalando.de"
shoe = "Asics Japan S"
color = "JAPAN S - Trainers - black"
size = 45
default_price = 79.95

# load up .env
load_dotenv()


# start driver
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
    parent_element = driver.find_element(By.XPATH, f"//span[text()={size}]/ancestor::div[@data-is-selected]")
        # the css-element "data-is-selected" switches from true to false
    if parent_element.get_attribute("data-is-selected") == "true":
        print("shoe is in stock")
    else:
        print("shoe is not in stock")
except Exception as e:
    print("Button not clicked", e)
# Read and save price 
price = driver.find_element(By.CSS_SELECTOR, "[data-testid='pdp-price-container'] p span")
# Convert euro to float
price = parse_price(price.text)
# store price and date of scrape in a dictionary
date = datetime.now().strftime("%d-%m-%Y")
prices = {}
prices = {"price": price,
          "date": date}
# if the price is lower than the default, send me an e-mail with the price and the url
if prices["price"] < default_price:
    current_price = prices["price"]
    # configure e-mail
    sender = os.getenv("email-sender")
    receiver = os.getenv("email-receiver")
    password = os.getenv("app-password")
    current_url = driver.current_url
    subject = "👟 Zalando-Scraper 👟"
    body = f"""\
    <html>
        <body>
            <p>The <strong>{shoe}</strong> costs only <strong>{current_price}€</strong> right now.
            👉<a href="{current_url}">Path</a>
            </p>
        </body>
    </html>
    """

    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = receiver 
    msg['Subject'] = subject 
    msg.add_alternative(body, subtype='html')
    
    # encrypt
    context = ssl.create_default_context()

    # send e-mail via smtp
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, msg.as_string())
    print("email sent")
else:
    print("price is same or higher than default_price")
driver.quit()

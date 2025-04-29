# Scrape a shoe from Zalando


# Installation 
Set up a virutal environment and install the required packages.

```
python -m venv env

source env/bin/activate

pip install -r requirements.txt
```
Install Chromium. Can be run in WSL2. Chromedriver is installed with this [set-up script](https://github.com/rehanhaider/selenium-wsl2-ubuntu) for selenium.
But --headless=new doesn't seem to work with chromedriver-linux64.

Then execute the script. 
```
python scraper.py
```

# How to read
The below code sets the path to the chromedriver. I use the absolute path.
```
homedir = os.path.expanduser("~/programming/squishyscraper")
chrome_options.binary_location = f"{homedir}/chrome-linux64/chrome"
webdriver_service = Service(f"{homedir}/chromedriver-linux64/chromedriver")
```
Because we do not want to give our e-mail-adress, app-password and the sender's email-address
away we store the values of these variables in .env. The following command loads the variables inside .env: 
```
load_dotenv()
```
Using os.getenv we can retreive the values at a later point.
```
    sender = os.getenv("email-sender")
    receiver = os.getenv("email-receiver")
    password = os.getenv("app-password")
```

# How to scrape a shoe 
The default shoe is Asics Black Japan S. All the default values are given at the top.
Of course, you can change the default_price to a value at which you would buy the shoe.
```
url = "https://www.zalando.de"
shoe = "Asics Japan S"
color = "JAPAN S - Trainers - black"
size = 45
default_price = 79.95
```
After that I save the data to an SQLite3 database. Windows Task Scheduler (cuz I'm a Windows noob) to automatically play the script on start-up.
Planning to run this as a cron job on a Raspi 5 though.

# Future plans
I plan to deploy this script on AWS. [EC2](https://medium.com/@angelaniederberger/automated-web-scraping-with-aws-72b7f80c2927) seems to be a good option to run it.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random
import time

# Setup headless Chrome
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Replace with path to your ChromeDriver
driver_path = "/Users/ryanmcmaster/Documents/chromedriver-mac-x64/chromedriver"
service = Service(driver_path)

# Replace with the actual base URL of your site
base_url = "https://mcmaster42.github.io/mcccDigitalDesignPortfolio"
pages = [
    "/",               # Home
    "/contact.html",
    "/extras.html",
    "/portfolio.html",
    "/resume.html"
    
]

def simulate_visit():
    page = random.choice(pages)
    url = base_url + page
    print(f"Visiting: {url}")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    
    # Wait 5-15 seconds like a human
    time.sleep(random.randint(3, 6))
    
    # Optionally: click a link
    links = driver.find_elements("tag name", "a")
    if links:
        random.choice(links).click()
        time.sleep(random.randint(3, 8))
    
    driver.quit()

# Run every 10–30 minutes, N times
for i in range(50):  # Adjust to simulate X number of visits
    simulate_visit()
    delay = random.randint(15, 30)  # wait 15 - 30 secondes
    print(f"Sleeping for {delay / 60:.1f} minutes...\n")
    time.sleep(delay)



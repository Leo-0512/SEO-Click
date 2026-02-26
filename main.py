import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

def seo_bot():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--remote-debugging-port=9222")
    
    # Railway के Chromium का सही रास्ता
    chrome_options.binary_location = "/usr/bin/chromium-browser"

    try:
        # webdriver-manager को Chromium इस्तेमाल करने के लिए मजबूर करना
        service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        print("Bot Started! Navigating to Google... 🚀")
        driver.get("https://www.google.com")
        
        # --- आपका सर्च और क्लिक वाला पुराना लॉजिक यहाँ आएगा ---
        
        print("Success! Website visited.")
        driver.quit()
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    while True:
        seo_bot()
        time.sleep(random.randint(600, 1200))

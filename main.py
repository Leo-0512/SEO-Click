import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def seo_bot():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # Railway के सिस्टम में Chromium यहाँ होता है
    chrome_options.binary_location = "/usr/bin/chromium-browser"

    try:
        # हम सीधा सिस्टम के ड्राइवर का इस्तेमाल करेंगे
        service = Service(executable_path="/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        print("Leo Bot Online! 🚀 Connecting to Google...")
        driver.get("https://www.google.com")
        print(f"Success! Page Title: {driver.title}")
        
        # यहाँ अपना सर्च लॉजिक
        search_box = driver.find_element("name", "q")
        search_box.send_keys("Aman Civil Engineering AutoCAD")
        search_box.submit()
        time.sleep(5)
        
        driver.quit()
        print("Task Finished. Waiting for next cycle... 😴")
    except Exception as e:
        print(f"Final Error: {e}")

if __name__ == "__main__":
    while True:
        seo_bot()
        time.sleep(random.randint(600, 1200))

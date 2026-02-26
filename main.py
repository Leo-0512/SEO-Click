import time
import random
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def seo_bot():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # Railway/Nixpacks में ये ही स्टैंडर्ड लोकेशन होती हैं
    chrome_options.binary_location = "/usr/bin/google-chrome" # या "/usr/bin/chromium"

    try:
        # हम सीधा सिस्टम ड्राइवर को कॉल करेंगे
        # अगर /usr/bin/chromedriver काम न करे तो "chromedriver" लिखें
        service = Service(executable_path="chromedriver") 
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        print("🚀 LEO STEALTH SYSTEM: SEO BOT ONLINE!")
        driver.get("https://www.google.com")
        print(f"✅ Google Connected. Title: {driver.title}")
        
        # सर्च लॉजिक
        search_box = driver.find_element("name", "q")
        search_box.send_keys("Aman Civil Engineering AutoCAD")
        search_box.submit()
        time.sleep(5)
        print("🔍 Search Success! Link finding in progress...")
        
        driver.quit()
    except Exception as e:
        print(f"❌ Leo, even after fix: {e}")

if __name__ == "__main__":
    while True:
        seo_bot()
        # 10-15 मिनट का इंतज़ार
        time.sleep(random.randint(600, 900))

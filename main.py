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
    
    # Railway के सिस्टम में Chromium और Driver यहाँ होते हैं
    chrome_options.binary_location = "/usr/bin/chromium-browser"

    try:
        # यहाँ हम किसी मैनेजर का इंतज़ार नहीं करेंगे, सीधा सिस्टम फाइल उठाएंगे
        # Railway Nixpacks में chromedriver इसी पाथ पर आता है
        service = Service(executable_path="/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        print("Leo Bot: System Connected Successfully! 🚀")
        driver.get("https://www.google.com")
        print(f"Verified: Google is Open. Title: {driver.title}")
        
        # --- आपका कीवर्ड सर्च ---
        search_box = driver.find_element("name", "q")
        search_box.send_keys("Aman Civil Engineering AutoCAD")
        search_box.submit()
        time.sleep(5)
        print("Search Result Loaded! ✅")
        
        driver.quit()
        print("Session Finished. Relaxing... 😴")
    except Exception as e:
        print(f"Leo, final error check: {e}")

if __name__ == "__main__":
    while True:
        seo_bot()
        time.sleep(random.randint(600, 1200))

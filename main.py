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
    
    # Railway/Nixpacks में Chromium का पक्का रास्ता
    chrome_options.binary_location = "/usr/bin/chromium-browser"

    try:
        # यहाँ हम किसी मैनेजर का इंतज़ार नहीं करेंगे, सीधा सिस्टम ड्राइवर उठाएंगे
        service = Service(executable_path="/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        print("Leo Bot Connected Successfully! 🚀")
        driver.get("https://www.google.com")
        print(f"Current Page: {driver.title}")
        
        # --- आपका कीवर्ड सर्च लॉजिक ---
        search_box = driver.find_element("name", "q")
        search_box.send_keys("Aman Civil Engineering AutoCAD") # यहाँ अपना कीवर्ड डालें
        search_box.submit()
        time.sleep(5)
        print("Search complete. Now finding your link...")
        
        driver.quit()
        print("Cycle Finished. Sleeping... 😴")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    while True:
        seo_bot()
        time.sleep(random.randint(600, 1200)) # 10-20 मिनट का गैप

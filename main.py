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
    
    # Railway/Nixpacks में Chromium इसी लोकेशन पर होता है
    chrome_options.binary_location = "/usr/bin/chromium-browser"

    try:
        # यहाँ हम webdriver-manager के बिना सीधा सिस्टम ड्राइवर इस्तेमाल कर रहे हैं
        service = Service(executable_path="/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        print("Bot Started Successfully! 🚀")
        driver.get("https://www.google.com")
        print(f"Page Title: {driver.title}") # यह चेक करने के लिए कि पेज खुला या नहीं
        
        # --- आपका सर्च लॉजिक यहाँ ---
        
        driver.quit()
        print("Session Completed. Sleeping... 😴")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    while True:
        seo_bot()
        # गूगल को शक न हो इसलिए रैंडम ब्रेक
        time.sleep(random.randint(600, 1200))

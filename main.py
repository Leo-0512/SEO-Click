import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def seo_bot():
    # --- ब्राउज़र सेटिंग्स (Railway के लिए) ---
    chrome_options = Options()
    chrome_options.add_argument('--headless') # बिना स्क्रीन के चलेगा
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # असली यूजर जैसा दिखने के लिए User-Agent
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # 1. गूगल पर जाना
        driver.get("https://www.google.com")
        time.sleep(random.randint(3, 5))

        # 2. कीवर्ड सर्च करना (यहाँ अपनी साइट का नाम लिखें)
        search_query = "Aman Civil Engineering AutoCAD" # अपना कीवर्ड यहाँ बदलें
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(random.randint(5, 7))

        # 3. अपनी वेबसाइट का लिंक ढूंढना और क्लिक करना
        # यहाँ 'yourwebsite.com' की जगह अपनी असली साइट का URL डालें
        my_site_link = driver.find_element(By.PARTIAL_LINK_TEXT, "aman-civil") 
        my_site_link.click()
        print("Website found and clicked! ✅")

        # 4. साइट पर रुकना और पेजों पर घूमना
        time.sleep(random.randint(30, 60)) # 1 मिनट तक रुकना
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # स्क्रॉल करना
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    while True:
        seo_bot()
        # गूगल को शक न हो इसलिए 10-20 मिनट का लंबा ब्रेक
        time.sleep(random.randint(600, 1200))

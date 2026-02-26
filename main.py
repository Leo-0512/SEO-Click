import asyncio
import random
import os
from playwright.async_api import async_playwright

async def seo_bot():
    async with async_playwright() as p:
        # Railway पर Playwright ब्राउज़र को अक्सर इस पाथ पर रखता है
        # हम कोड को खुद ढूँढने के लिए कह रहे हैं
        browser_path = "/app/.cache/ms-playwright/chromium-1148/chrome-linux/chrome"
        
        try:
            # अगर पाथ मिल जाता है तो ठीक, वरना डिफ़ॉल्ट ट्राई करेगा
            if os.path.exists(browser_path):
                print("📍 Custom Browser Path Found!")
                browser = await p.chromium.launch(executable_path=browser_path, headless=True)
            else:
                print("📍 Using Default Launch...")
                browser = await p.chromium.launch(headless=True)

            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            )
            page = await context.new_page()

            print("🚀 LEO SYSTEM: CONNECTING...")
            await page.goto("https://www.google.com", wait_until="networkidle")
            print(f"✅ Success! Google Title: {await page.title()}")

            # सर्च लॉजिक
            await page.fill('textarea[name="q"]', "https://officialleo.netlify.app/")
            await page.keyboard.press("Enter")
            await page.wait_for_timeout(5000)
            print("🔍 Search results loaded successfully!")

            await browser.close()
        except Exception as e:
            print(f"❌ Leo, browser issue again: {e}")

async def main():
    while True:
        await seo_bot()
        await asyncio.sleep(random.randint(600, 900))

if __name__ == "__main__":
    asyncio.run(main())

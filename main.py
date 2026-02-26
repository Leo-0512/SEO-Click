import asyncio
import random
from playwright.async_api import async_playwright

async def seo_bot():
    async with async_playwright() as p:
        # ब्राउज़र लॉन्च (Headless mode)
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        try:
            print("🚀 LEO PLAYWRIGHT SYSTEM: ONLINE!")
            await page.goto("https://www.google.com", wait_until="networkidle")
            print(f"✅ Google Loaded: {await page.title()}")

            # कीवर्ड टाइप करना
            await page.fill('textarea[name="q"]', "https://officialleo.netlify.app/")
            await page.keyboard.press("Enter")
            
            # रिजल्ट्स का इंतज़ार
            await page.wait_for_timeout(5000)
            print("🔍 Search Results are visible!")

            # यहाँ आपकी वेबसाइट ढूँढने का लॉजिक आएगा
            
            await browser.close()
            print("😴 Task Done. Sleeping for a while...")
        except Exception as e:
            print(f"❌ Error: {e}")
            await browser.close()

async def main():
    while True:
        await seo_bot()
        await asyncio.sleep(random.randint(600, 900))

if __name__ == "__main__":
    asyncio.run(main())

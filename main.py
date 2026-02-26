import asyncio
import os
from playwright.async_api import async_playwright

async def seo_bot():
    async with async_playwright() as p:
        try:
            # यह कमांड खुद ब्राउज़र को सही जगह से उठा लेगी
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            
            print("🚀 LEO SYSTEM: SEO BOT IS ONLINE!")
            await page.goto("https://www.google.com")
            print(f"✅ Success! Page Title: {await page.title()}")
            
            await browser.close()
        except Exception as e:
            # अगर फिर भी न मिले, तो हम मैन्युअली उसे पाथ देंगे
            print(f"📍 Manual Path searching... Error was: {e}")
            try:
                # Railway का नया स्टैंडर्ड पाथ
                path = "/app/.cache/ms-playwright/chromium-1148/chrome-linux/chrome"
                browser = await p.chromium.launch(executable_path=path, headless=True)
                print("✅ Found using Manual Path!")
                await browser.close()
            except Exception as final_e:
                print(f"❌ Final Error: {final_e}")

if __name__ == "__main__":
    asyncio.run(seo_bot())

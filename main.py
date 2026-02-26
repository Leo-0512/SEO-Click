import asyncio
import os
from playwright.async_api import async_playwright

async def seo_bot():
    async with async_playwright() as p:
        print("🚀 LEO SYSTEM: STARTING SEO BOT...")
        try:
            # यह अपने आप सही फोल्डर से ब्राउज़र उठाएगा
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            
            await page.goto("https://www.google.com")
            print(f"✅ Success! Connected to: {await page.title()}")
            
            await browser.close()
        except Exception as e:
            print(f"📍 Trying Emergency Launch... Error was: {e}")
            # अगर डिफ़ॉल्ट फेल हुआ, तो यह बैकअप पाथ यूज़ करेगा
            try:
                browser = await p.chromium.launch(
                    executable_path="/app/.playwright-browsers/chromium-1148/chrome-linux/chrome",
                    headless=True
                )
                print("✅ Emergency Launch Success!")
                await browser.close()
            except Exception as e2:
                print(f"❌ Final attempt failed: {e2}")

if __name__ == "__main__":
    asyncio.run(seo_bot())

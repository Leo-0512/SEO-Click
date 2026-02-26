import asyncio
import os
import subprocess
from playwright.async_api import async_playwright

async def install_playwright():
    print("🛠️ Leo, browsers missing. Installing now...")
    subprocess.run(["playwright", "install", "chromium"], check=True)
    subprocess.run(["playwright", "install-deps"], check=True)

async def seo_bot():
    async with async_playwright() as p:
        print("🚀 LEO SYSTEM: STARTING SEO BOT...")
        try:
            # हम पहले डिफ़ॉल्ट कोशिश करेंगे
            browser = await p.chromium.launch(headless=True)
        except Exception:
            # अगर फेल हुआ, तो खुद इंस्टॉल करके दोबारा कोशिश करेगा
            await install_playwright()
            browser = await p.chromium.launch(headless=True)
            
        page = await browser.new_page()
        await page.goto("https://www.google.com")
        print(f"✅ BINGO! Connected to: {await page.title()}")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(seo_bot())

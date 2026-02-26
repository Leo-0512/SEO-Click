import asyncio
import random
import subprocess
from playwright.async_api import async_playwright

async def install_playwright():
    print("🛠️ Leo, setting up the sniper tools...")
    subprocess.run(["playwright", "install", "chromium"], check=True)
    subprocess.run(["playwright", "install-deps"], check=True)

async def seo_bot():
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(headless=True)
        except Exception:
            await install_playwright()
            browser = await p.chromium.launch(headless=True)
            
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        try:
            print(f"🚀 LEO SEO SYSTEM: TARGETING officialleo.netlify.app")
            # 1. गूगल पर जाना
            await page.goto("https://www.google.com")
            
            # 2. कीवर्ड सर्च करना (वही कीवर्ड जो आपने दिखाया)
            search_query = "officialleo.netlify.app"
            await page.fill('textarea[name="q"]', search_query)
            await page.keyboard.press("Enter")
            
            # इंतज़ार करें जब तक रिजल्ट्स न आ जाएँ
            await page.wait_for_selector('div#search')
            print(f"🔍 Search results loaded for: {search_query}")

            # 3. पहली लिंक को ढूँढना (Sniper Logic)
            # चूंकि आपकी साइट पहले नंबर पर है, हम सीधे नेटलिंक वाली लिंक पर क्लिक करेंगे
            target_link = page.locator('a[href*="officialleo.netlify.app"]').first
            
            if await target_link.is_visible():
                print("🎯 Target Spotted at Rank #1! Clicking now...")
                await target_link.click()
                await page.wait_for_load_state("networkidle")
                
                # 4. साइट पर रुकना (असली इंसान की तरह बिहेव करना)
                stay_time = random.randint(120, 180) # 2-3 मिनट रुकना बेस्ट है
                print(f"✅ Success! Landed on officialleo.netlify.app. Staying for {stay_time}s.")
                
                # थोड़ा स्क्रॉल करना ताकि गूगल को लगे कि कोई पढ़ रहा है
                await page.mouse.wheel(0, 500)
                await asyncio.sleep(stay_time / 2)
                await page.mouse.wheel(0, 500)
                await asyncio.sleep(stay_time / 2)
                
            else:
                print("⚠️ Link not visible on first spot. Visiting directly as backup...")
                await page.goto("https://officialleo.netlify.app")
                await asyncio.sleep(120)

        except Exception as e:
            print(f"❌ Leo, something went wrong: {e}")
        finally:
            await browser.close()
            print("😴 Cycle Finished. Next run in 15-20 mins.")

async def main():
    while True:
        await seo_bot()
        # हर 15-25 मिनट में एक नया विज़िटर भेजें
        wait_next = random.randint(600, 900)
        await asyncio.sleep(wait_next)

if __name__ == "__main__":
    asyncio.run(main())

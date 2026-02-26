import asyncio
import random
import subprocess
from playwright.async_api import async_playwright

async def install_playwright():
    print("🛠️ Leo, setting up the search tools...")
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
            
            # 2. कीवर्ड सर्च करना
            search_query = "https://officialleo.netlify.app"
            await page.fill('textarea[name="q"]', search_query)
            await page.keyboard.press("Enter")
            await page.wait_for_load_state("networkidle")
            print(f"🔍 Searched for: {search_query}")

            # 3. अपनी वेबसाइट का लिंक ढूँढना और क्लिक करना
            # हम 'officialleo.netlify.app' वाले लिंक को खोज रहे हैं
            website_link = page.locator('a[href*="officialleo.netlify.app"]')
            
            if await website_link.count() > 0:
                print("🎯 Target Spotted! Clicking on your website...")
                await website_link.first.click()
                await page.wait_for_load_state("networkidle")
                
                # 4. साइट पर रुकना (SEO बढ़ाने के लिए 1-2 मिनट रुकना ज़रूरी है)
                stay_time = random.randint(60, 120)
                print(f"✅ Success! Staying on site for {stay_time} seconds to boost SEO.")
                await asyncio.sleep(stay_time)
            else:
                print("⚠️ Link not found on first page. Direct visiting to boost traffic...")
                await page.goto("https://officialleo.netlify.app")
                await asyncio.sleep(60)

        except Exception as e:
            print(f"❌ Error during task: {e}")
        finally:
            await browser.close()
            print("😴 Task complete. Waiting for next cycle...")

async def main():
    while True:
        await seo_bot()
        # हर 15-20 मिनट में एक नया क्लिक
        wait_next = random.randint(900, 1200)
        await asyncio.sleep(wait_next)

if __name__ == "__main__":
    asyncio.run(main())

import asyncio
import random
import subprocess
from playwright.async_api import async_playwright

async def install_playwright():
    print("🛠️ Leo, fixing the system for Google bypass...")
    subprocess.run(["playwright", "install", "chromium"], check=True)
    subprocess.run(["playwright", "install-deps"], check=True)

async def seo_bot():
    async with async_playwright() as p:
        try:
            # Slow_mo बोट की रफ्तार को थोड़ा कम रखेगा ताकि शक न हो
            browser = await p.chromium.launch(headless=True, slow_mo=random.randint(500, 1000))
        except Exception:
            await install_playwright()
            browser = await p.chromium.launch(headless=True, slow_mo=random.randint(500, 1000))
            
        # असली मोबाइल/डेस्कटॉप यूजर जैसा दिखने के लिए सेटिंग्स
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            viewport={'width': 1280, 'height': 720}
        )
        page = await context.new_page()

        try:
            print("🚀 LEO SYSTEM: ATTEMPTING ORGANIC SEARCH...")
            
            # सीधा गूगल की जगह पहले बिंग पर जाकर 'नॉर्मल' व्यवहार दिखाना
            await page.goto("https://www.bing.com")
            await asyncio.sleep(3)
            
            await page.goto("https://www.google.com")
            
            # इंसानी तरीके से एक-एक अक्षर टाइप करना
            search_query = "officialleo.netlify.app"
            await page.type('textarea[name="q"]', search_query, delay=random.randint(150, 300))
            await page.keyboard.press("Enter")
            
            # चेक करना कि कहीं गूगल ने 'Sorry' पेज तो नहीं दिखाया
            await asyncio.sleep(5)
            if "sorry" in page.url or "captcha" in page.url:
                print("🛑 Google blocked IP! Switching to Direct Traffic Strategy...")
                await page.goto("https://officialleo.netlify.app", wait_until="networkidle")
            else:
                # अगर गूगल ने ब्लॉक नहीं किया, तो लिंक ढूँढना
                target_link = page.locator('a[href*="officialleo.netlify.app"]').first
                if await target_link.is_visible():
                    print("🎯 Target Found! Clicking Link...")
                    await target_link.click()
                else:
                    await page.goto("https://officialleo.netlify.app")

            # --- वेबसाइट पर समय बिताना (SEO Boost) ---
            print("✅ Landed on site! Performing human actions...")
            # 2 से 4 मिनट रुकना
            stay_seconds = random.randint(120, 240)
            
            # धीरे-धीरे नीचे स्क्रॉल करना
            for _ in range(5):
                await page.mouse.wheel(0, random.randint(300, 600))
                await asyncio.sleep(stay_seconds / 5)
            
            print(f"💎 Session Complete ({stay_seconds}s). SEO Updated!")

        except Exception as e:
            print(f"❌ Leo, task interrupted: {e}")
        finally:
            await browser.close()
            print("😴 Resting to avoid suspicion...")

async def main():
    while True:
        # अब हम 5 से 10 मिनट के बीच एक विज़िट भेजेंगे
        # यह आधे घंटे में 1 की जगह 1 घंटे में 4-6 विज़िट कर देगा
        await seo_bot()
        wait_next = random.randint(100, 150) 
        print(f"⏳ Next visit in {wait_next // 60} minutes...")
        await asyncio.sleep(wait_next)

if __name__ == "__main__":
    asyncio.run(main())

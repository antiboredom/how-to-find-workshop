from playwright.sync_api import sync_playwright

urls = [
    "https://www.shutterstock.com/",
    "https://www.browserscan.net/bot-detection",
    "https://amazon.com",
    "https://google.com",
    "https://realtor.com",
    "https://trulia.com",
    "https://x.com/Pontifex",
    "https://reddit.com",
]

playwright = sync_playwright().start()

browser = playwright.chromium.launch(
    headless=False,
    args=["--disable-blink-features=AutomationControlled", "--disable-infobars"],
)

page = browser.new_page()

for url in urls:
    page.goto(url)
    page.wait_for_timeout(3000)

browser.close()
playwright.stop()

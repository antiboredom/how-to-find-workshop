from playwright.sync_api import sync_playwright
import requests

##### VARIABLES THAT YOU SHOULD MODIFY #####

# change to True to hide the browser
HEADLESS = False

# the url the browser will open
START_URL = "https://www.shutterstock.com/search/crying-cops"

# the css selector of the text content we want to grab
CONTENT_SELECTOR = ".mui-1l7n00y-thumbnail"

# max number of pages to get
MAX_PAGES = 3

##### FUNCTION TO DOWNLOAD IMAGES (OR OTHER CONTENT) #####


def download(url):
    local_filename = url.split("/")[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)


##### THE ACTUAL SCRIPT #####

# an empty list to store the results
all_results = []

# store the current page
current_page = 1

# create a new instance of playwright and then launch the browser
playwright = sync_playwright().start()

browser = playwright.chromium.launch(
    headless=False,
    args=["--disable-blink-features=AutomationControlled", "--disable-infobars"],
)

# open a new empty page
page = browser.new_page()

# visit out starting URL
page.goto(START_URL)

while current_page <= MAX_PAGES:
    # pause for a moment
    page.wait_for_timeout(5000)

    # find the elements specified by our CONTENT_SELECTOR
    items = page.locator(CONTENT_SELECTOR)

    # if there are no items, break
    if items.count() == 0:
        break

    for item in items.all():
        src = item.get_attribute("src")
        print(src)
        download(src)

    # find the next page button
    next_button = page.get_by_text("Next")

    # if there is no next page button, exit
    if next_button.count() == 0:
        break

    # click the next page button
    next_button.click()

    # increase our current page by one
    current_page += 1

# close the browser
browser.close()

# end the playwright instance
playwright.stop()

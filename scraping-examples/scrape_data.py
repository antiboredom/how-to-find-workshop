import json
from playwright.sync_api import sync_playwright

##### VARIABLES THAT YOU SHOULD MODIFY #####

# change to True to hide the browser
HEADLESS = False

# the url the browser will open
START_URL = "https://old.reddit.com/top/"

# the css selector of the "next page" button
NEXT_SELECTOR = ".next-button"

# a text file to save the results to
OUTPUT_FILE = "scraped_data.json"

# max number of pages to get
MAX_PAGES = 5

##### THE ACTUAL SCRIPT #####

# an empty list to store the results
all_results = []

# store the current page
current_page = 1

# create a new instance of playwright and then launch the browser
playwright = sync_playwright().start()

# we're using firefox because it seems to trigger fewer bot blockers
browser = playwright.firefox.launch(headless=HEADLESS)

# open a new empty page
page = browser.new_page()

# visit out starting URL
page.goto(START_URL)

while current_page <= MAX_PAGES:
    # pause for a moment
    page.wait_for_timeout(2000)

    # find the the elements we're interested in
    items = page.locator(".entry")

    # if there are no items, break
    if items.count() == 0:
        break

    # for each element, extract the url, title, total comments and username
    for item in items.all():
        # note that you can run "locator" on other locators!
        href = item.locator("a.title").get_attribute("href")
        title = item.locator("a.title").inner_text()
        total_comments = item.locator("a.comments").inner_text()
        username = item.locator("a.author").inner_text()

        all_results.append(
            {
                "title": title,
                "url": href,
                "comments": total_comments,
                "username": username,
            }
        )

    # find the next page button
    next_button = page.locator(NEXT_SELECTOR)

    # if there is no next page button, exit
    if next_button.count() == 0:
        break

    # click the next page button
    next_button.click()

    # increase our current page by one
    current_page += 1

# save the file
with open(OUTPUT_FILE, "w") as f:
    json.dump(all_results, f, indent=2)

# close the browser
browser.close()

# end the playwright instance
playwright.stop()

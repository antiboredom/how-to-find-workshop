from playwright.sync_api import sync_playwright

##### VARIABLES THAT YOU SHOULD MODIFY #####

# change to True to hide the browser
HEADLESS = False

# the url the browser will open
START_URL = "https://old.reddit.com/top/"

# the css selector of the text content we want to grab
CONTENT_SELECTOR = "a.title"

# the css selector of the "next page" button
NEXT_SELECTOR = ".next-button"

# a text file to save the results to
OUTPUT_FILE = "scraped_text.txt"

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

    # find the elements specified by our CONTENT_SELECTOR
    items = page.locator(CONTENT_SELECTOR)

    # if there are no items, break
    if items.count() == 0:
        break

    # get the text content of all of our items
    contents = items.all_inner_texts()

    # add each bit of text to the results list
    for text in contents:
        text = text.strip()
        if text:
            all_results.append(text)

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
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for item in all_results:
        f.write(item + "\n")

# close the browser
browser.close()

# end the playwright instance
playwright.stop()

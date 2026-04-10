import csv
from playwright.sync_api import sync_playwright

##### VARIABLES THAT YOU SHOULD MODIFY #####

# change to True to hide the browser
HEADLESS = False

# the url the browser will open
START_URL = "https://www.forbes.com/billionaires/"

# a text file to save the results to
OUTPUT_FILE = "scraped_data.json"

# max number of pages to get
MAX_PAGES = 70

HEADERS = ["rank", "name", "net_worth", "age", "country", "source", "industry"]

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

page.set_default_timeout(60000)

# visit out starting URL
page.goto(START_URL)

while current_page <= MAX_PAGES:
    # pause for a moment
    page.wait_for_timeout(2000)

    # find the the elements we're interested in
    items = page.locator(".ListTable_tableRow__P838D")

    # if there are no items, break
    if items.count() == 0:
        break

    # for each element, extract the url, title, total comments and username
    for item in items.all():
        # note that you can run "locator" on other locators!
        tds = item.locator("td").all()

        if len(tds) != len(HEADERS):
            continue

        all_results.append(
            {
                "rank": tds[0].inner_text(),
                "name": tds[1].inner_text(),
                "net_worth": tds[2].inner_text(),
                "age": tds[3].inner_text(),
                "country": tds[4].inner_text(),
                "source": tds[5].inner_text(),
                "industry": tds[6].inner_text(),
            }
        )

    # find the next page button
    next_button = page.get_by_label("Next")

    # if there is no next page button, exit
    if next_button.count() == 0:
        break

    # click the next page button
    next_button.click()

    # increase our current page by one
    current_page += 1

    # save the file
    with open("forbes_list.csv", "w") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=HEADERS)
        writer.writeheader()
        for row in all_results:
            writer.writerow(row)

# close the browser
browser.close()

# end the playwright instance
playwright.stop()

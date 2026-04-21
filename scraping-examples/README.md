# Examples

Here's a quick walkthrough on how to use the examples in the `scraping-examples` folder.

## Prerequisites

To use the examples you should have a code editor (I suggest [Visual Studio Code](https://code.visualstudio.com/)) and install [uv](https://docs.astral.sh/uv/getting-started/installation/).

To install `uv`, open a terminal and then for Mac paste in:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

or for Windows:

```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

I suggest [downloading this entire git repository](https://github.com/antiboredom/how-to-find-workshop/archive/refs/heads/main.zip) as a folder, then unzipping it, and opening `scraping-examples` in Visual Studio Code.

Then, open Visual Studio Code's built-in terminal, by going to the `Terminal` menu and selecting `New Terminal`.

Finally, type `uv run SCRIPTNAME.py`, replacing "SCRIPTNAME.py" with the file you'd like to run.

## General Notes

I've tried to make these examples as accessible to new coders as possible by putting the important variables at the top of the file, in all caps. This means that for _many_ (but not all) cases, you should be able to just modify the variable values to make the examples work with different websites.

## test_some_websites.py

```
uv run test_some_websites.py
```

This just tests to see if a variety of different websites will load. Some sites use sophisticated blocking mechanisms to prevent web scraping.

The `urls` variable at the top is a list of sites to load.

## scrape_text.py

```
uv run scrape_text.py
```

Download post titles from reddit.

This looks for elements matching a particular css selector and saves the text content of each one to a file. Each line of the file represents the text of a single element. The script will attempt to click a "next" button if available to get multiple pages of results.

Variables:

`START_URL`: the url to visit

`HEADLESS`: determines if the browser runs in "headless" mode, or will be visible to you. It helps with avoiding bot detection if you leave this to `False`, but it makes the script run a little bit slower.

`CONTENT_SELECTOR`: the css selector of the elements we want

`NEXT_SELECTOR`: the css selector of the "next" button

`OUTPUT_FILE`: the filename to save the content to

`MAX_PAGES`: the maximum number of pages to scrape.

## scrape_images.py

```
uv run scrape_images.py
```

Download images of crying cops from Shutterstock.com.

This looks for images matching a particular css selector and saves them to the same folder as the script. The script will attempt to click a "next" button if available to get multiple pages of results. HOWEVER, in this example the next button is located with `page.get_by_text()` which looks for an element with a particular text value.

## scrape_data.py

```
uv run scrape_data.py
```

Download post titles, links, username, and total comments from reddit, and saves them as a .json file.

This is a more complicated example, based off of `scrape_text.py`. Instead of just downloading the text of an element it looks for other data as well, and then saves everything to a .json file.

To make this work with other sites, you'll need to modify lines 52 to 67.

## forbes_browser.py

```
uv run forbes_browser.py
```

Downloads the Forbes billionaire list as a csv file.

This is a more advanced example, but is very similar in structure to `scrape_data.py`.

## forbes_requests.py

```
uv run forbes_requests.py
```

Downloads the Forbes billionaire list as a json file.

This is the most advanced example. It avoids using a browser entirely and instead duplicates an http request to access data more directly. See the second to last section of `005-web-scraping.md` in the notes folder for more on this technique.

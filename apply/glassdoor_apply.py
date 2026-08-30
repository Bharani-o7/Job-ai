from playwright.sync_api import sync_playwright
import time


def apply_glassdoor(job):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(job["apply_url"])
        time.sleep(5)

        try:
            page.locator(
                "button:has-text('Easy Apply')"
            ).click()

            print("Applied on Glassdoor")

        except:
            print("Glassdoor apply failed")

        browser.close()
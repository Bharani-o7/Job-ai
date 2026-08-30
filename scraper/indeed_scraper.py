from playwright.sync_api import sync_playwright
import time


def fetch_indeed_jobs():
    jobs = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(
            "https://www.indeed.com/jobs?q=software+engineer+intern",
            timeout=60000
        )

        time.sleep(5)

        cards = page.locator(
            "[data-jk]"
        ).all()

        for job in cards[:10]:
            try:
                title = job.locator("h2").inner_text()
                company = job.locator(
                    "[data-testid='company-name']"
                ).inner_text()

                link = job.locator("a").first.get_attribute("href")

                if link and link.startswith("/"):
                    link = "https://www.indeed.com" + link

                jobs.append({
                    "source": "indeed",
                    "title": title,
                    "company": company,
                    "apply_url": link
                })

            except:
                continue

        browser.close()

    return jobs
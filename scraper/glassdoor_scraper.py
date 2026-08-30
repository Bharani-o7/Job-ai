from playwright.sync_api import sync_playwright
import time


def fetch_glassdoor_jobs():
    jobs = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(
            "https://www.glassdoor.com/Job/software-engineer-intern-jobs-SRCH_KO0,24.htm",
            timeout=60000
        )

        time.sleep(5)

        cards = page.locator(".react-job-listing").all()

        for job in cards[:10]:
            try:
                title = job.locator("a").first.inner_text()
                company = job.locator(
                    ".EmployerProfile_compactEmployerName"
                ).inner_text()

                link = job.locator("a").first.get_attribute("href")

                if link and link.startswith("/"):
                    link = "https://glassdoor.com" + link

                jobs.append({
                    "source": "glassdoor",
                    "title": title,
                    "company": company,
                    "apply_url": link
                })

            except:
                continue

        browser.close()

    return jobs
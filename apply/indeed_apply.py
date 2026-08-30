from playwright.sync_api import sync_playwright
import time


def fetch_indeed_jobs():
    jobs = []

    with sync_playwright() as p:
        # use persistent browser session like linkedin
        context = p.chromium.launch_persistent_context(
            user_data_dir="indeed_session",
            headless=False
        )

        page = context.new_page()

        print("Opening Indeed jobs...")

        page.goto(
            "https://www.indeed.com/jobs?q=software+engineer+intern",
            timeout=60000
        )

        # wait manually if cloudflare appears
        print("If verification appears, solve it manually.")
        time.sleep(20)

        try:
            job_cards = page.locator(
                '[data-testid="job_seen_beacon"]'
            ).all()

            print(f"Found {len(job_cards)} Indeed jobs")

            for job in job_cards[:10]:
                try:
                    title = job.locator("h2").inner_text()
                    company = job.locator(
                        '[data-testid="company-name"]'
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

                    print(f"Found: {title}")

                except:
                    continue

        except Exception as e:
            print("Indeed scraping failed:", e)

        context.close()

    return jobs
from playwright.sync_api import sync_playwright
import time


def fetch_linkedin_jobs():
    jobs = []

    with sync_playwright() as p:
        # Persist LinkedIn login session
        context = p.chromium.launch_persistent_context(
            user_data_dir="linkedin_session",
            headless=False
        )

        page = context.new_page()

        print("Opening LinkedIn jobs page...")

        page.goto(
            "https://www.linkedin.com/jobs/search/?keywords=software%20engineer%20intern",
            timeout=60000
        )

        time.sleep(5)

        # Close popup if it appears
        try:
            page.locator(
                "button[aria-label='Dismiss']"
            ).click(timeout=3000)
            print("Closed popup")
        except:
            print("No popup found")

        print("Scrolling to load jobs...")

        # Scroll to load more jobs
        for _ in range(3):
            page.mouse.wheel(0, 5000)
            time.sleep(2)

        # Get all job cards
        job_cards = page.locator(".job-card-container").all()

        print(f"Found {len(job_cards)} job cards")

        for i, job in enumerate(job_cards[:10]):
            try:
                print(f"\nProcessing job {i+1}...")

                # TITLE selector (primary + fallback)
                try:
                    title = job.locator(
                        ".job-card-list__title"
                    ).first.text_content(timeout=3000)
                except:
                    title = job.locator(
                        "strong"
                    ).first.text_content(timeout=3000)

                # COMPANY selector (primary + fallback)
                try:
                    company = job.locator(
                        ".job-card-container__company-name"
                    ).first.text_content(timeout=3000)
                except:
                    company = job.locator(
                        ".artdeco-entity-lockup__subtitle"
                    ).first.text_content(timeout=3000)

                # LINK selector
                try:
                    link = job.locator(
                        "a"
                    ).first.get_attribute(
                        "href",
                        timeout=3000
                    )
                except:
                    link = None

                # Convert relative LinkedIn links → full URLs
                if link and link.startswith("/"):
                    link = "https://www.linkedin.com" + link

                # Skip incomplete jobs
                if not title or not company or not link:
                    print(f"Skipping incomplete job {i+1}")
                    continue

                job_data = {
                    "source": "linkedin",
                    "title": title.strip(),
                    "company": company.strip(),
                    "apply_url": link
                }

                jobs.append(job_data)

                print(
                    f"Found job: {title.strip()} at {company.strip()}"
                )

            except Exception as e:
                print(f"Skipping job {i+1}: {e}")
                continue

        print(f"\nFinal jobs collected: {len(jobs)}")

        time.sleep(2)
        context.close()

    return jobs
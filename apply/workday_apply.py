from playwright.sync_api import sync_playwright
import time
import json
import os


def save_applied_job(job):
    file_path = "applied_jobs.json"

    jobs = []

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            jobs = json.load(f)

    jobs.append(job)

    with open(file_path, "w") as f:
        json.dump(jobs, f, indent=4)


def apply_workday(job):
    job_url = job["apply_url"]

    print(f"Opening Workday job: {job_url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto(
            job_url,
            timeout=60000
        )

        time.sleep(5)

        try:
            apply_btn = page.locator(
                "button:has-text('Apply')"
            ).first

            apply_btn.click()

            print("Clicked Workday Apply button")

        except Exception as e:
            print(
                f"Apply button failed: {e}"
            )

        try:
            page.set_input_files(
                "input[type='file']",
                job["resume_path"]
            )

            print("Resume uploaded")

        except Exception as e:
            print(
                f"Resume upload failed: {e}"
            )

        save_applied_job(job)

        print("Workday job saved")

        time.sleep(10)
        browser.close()
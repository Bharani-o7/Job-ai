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


def apply_greenhouse(job):
    job_url = job["apply_url"]

    print(f"Opening Greenhouse job: {job_url}")

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
            # Upload resume
            page.set_input_files(
                "input[type='file']",
                job["resume_path"]
            )

            print("Resume uploaded successfully")

        except Exception as e:
            print(
                f"Resume upload failed: {e}"
            )

        try:
            # Fill basic info
            page.fill(
                "input[name='first_name']",
                "Bharani"
            )

            page.fill(
                "input[name='last_name']",
                "Karlapudi"
            )

            page.fill(
                "input[name='email']",
                "bkarlapu@asu.edu"
            )

            print("Basic details filled")

        except Exception as e:
            print(
                f"Form fill failed: {e}"
            )

        try:
            page.locator(
                "button:has-text('Submit Application')"
            ).click()

            print("Greenhouse application submitted")

            save_applied_job(job)

        except Exception as e:
            print(
                f"Submission failed: {e}"
            )

        time.sleep(10)
        browser.close()
from playwright.sync_api import sync_playwright
import time
import json
import os


def save_applied_job(job):
    file_path = "applied_jobs.json"

    applied_jobs = []

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            applied_jobs = json.load(f)

    applied_jobs.append(job)

    with open(file_path, "w") as f:
        json.dump(applied_jobs, f, indent=4)


def apply_to_job(job):
    job_url = job["apply_url"]

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir="linkedin_session",
            headless=False
        )

        page = context.new_page()

        print("Opening application page...")
        page.goto(job_url, timeout=60000)

        time.sleep(5)

        applied = False

        # -----------------------------
        # EASY APPLY DETECTION
        # -----------------------------
        easy_apply_selectors = [
            "button:has-text('Easy Apply')",
            "span:has-text('Easy Apply')",
            "[aria-label*='Easy Apply']",
            ".jobs-apply-button"
        ]

        for selector in easy_apply_selectors:
            try:
                button = page.locator(selector).first

                if button.is_visible(timeout=3000):
                    print(f"Found Easy Apply using: {selector}")
                    button.click()
                    applied = True
                    break

            except Exception:
                continue

        # -----------------------------
        # NORMAL APPLY
        # -----------------------------
        if not applied:
            normal_selectors = [
                "button:has-text('Apply')",
                "a:has-text('Apply')",
                "[aria-label*='Apply']"
            ]

            for selector in normal_selectors:
                try:
                    button = page.locator(selector).first

                    if button.is_visible(timeout=3000):
                        print(f"Found normal Apply using: {selector}")
                        button.click()
                        applied = True
                        break

                except Exception:
                    continue

        # -----------------------------
        # EXTERNAL APPLY
        # -----------------------------
        if not applied:
            try:
                external_link = page.locator(
                    "a[href*='apply'], a[href*='jobs']"
                ).first

                if external_link.is_visible(timeout=3000):
                    external_link.click()
                    print("Clicked external Apply link")
                    applied = True

            except:
                print("External apply link not found")

        # -----------------------------
        # SAVE JOB
        # -----------------------------
        if applied:
            print("Application process started successfully")
            save_applied_job(job)
            print("Job saved successfully")
        else:
            print("Could not apply")

        time.sleep(8)
        context.close()
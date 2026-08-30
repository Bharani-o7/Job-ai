from scraper.linkedin_scraper import fetch_linkedin_jobs
from scraper.indeed_scraper import fetch_indeed_jobs
from scraper.glassdoor_scraper import fetch_glassdoor_jobs

from scraper.job_description import fetch_job_description

from ats.parser import extract_resume_text
from ats.scorer import calculate_ats_score
from ats.resume_optimizer import optimize_resume
from ats.rewrite_resume import (
    rewrite_resume_suggestions,
    create_tailored_resume
)

from apply.linkedin_apply import apply_to_job
from apply.greenhouse_apply import apply_greenhouse
from apply.workday_apply import apply_workday
from apply.indeed_apply import apply_indeed
from apply.glassdoor_apply import apply_glassdoor

from apply.router import detect_platform


def choose_job_source():
    print("\nChoose job source:")
    print("1. LinkedIn")
    print("2. Indeed")
    print("3. Glassdoor")
    print("4. All platforms")

    choice = input("\nEnter choice: ")

    if choice == "1":
        return "linkedin"

    elif choice == "2":
        return "indeed"

    elif choice == "3":
        return "glassdoor"

    else:
        return "all"


def fetch_jobs_from_selected_source(source):
    if source == "linkedin":
        return fetch_linkedin_jobs()

    elif source == "indeed":
        return fetch_indeed_jobs()

    elif source == "glassdoor":
        return fetch_glassdoor_jobs()

    elif source == "all":
        jobs = []

        print("\nFetching LinkedIn jobs...")
        jobs.extend(fetch_linkedin_jobs())

        print("\nFetching Indeed jobs...")
        jobs.extend(fetch_indeed_jobs())

        print("\nFetching Glassdoor jobs...")
        jobs.extend(fetch_glassdoor_jobs())

        return jobs

    return []


def run_jobforge():
    print("\n==============================")
    print("     JOBFORGE AI STARTING")
    print("==============================\n")

    # -----------------------------------
    # STEP 1: Choose job source
    # -----------------------------------
    selected_source = choose_job_source()

    print(f"\nSelected source: {selected_source}")

    jobs = fetch_jobs_from_selected_source(
        selected_source
    )

    if not jobs:
        print("\nNo jobs found.")
        return

    print(f"\nTotal jobs scraped: {len(jobs)}")

    # -----------------------------------
    # STEP 2: Parse resume
    # -----------------------------------
    print("\nUsing original resume file...")
    resume_path = "resumes/master_resume.pdf"

    resume_text = extract_resume_text(
        resume_path
    )

    best_job = None
    best_score = 0
    best_description = None

    print("\nEvaluating jobs...\n")

    # -----------------------------------
    # STEP 3: Evaluate all jobs
    # -----------------------------------
    for i, job in enumerate(jobs):
        print(
            f"\nJob {i+1}: {job['title']} at {job['company']}"
        )

        try:
            job_description = fetch_job_description(
                job["apply_url"]
            )

            if not job_description:
                print("Could not fetch description")
                continue

            score = calculate_ats_score(
                job_description,
                resume_text,
                job["title"]
            )

            print(f"ATS Score: {score}")

            if score > best_score:
                best_score = score
                best_job = job
                best_description = job_description

        except Exception as e:
            print(
                f"Error evaluating job: {e}"
            )
            continue

    # -----------------------------------
    # STEP 4: Best job selection
    # -----------------------------------
    if not best_job:
        print(
            "\nNo valid job descriptions found."
        )
        return

    print("\n==============================")
    print(" BEST JOB MATCH FOUND ")
    print("==============================\n")

    print(
        f"Title: {best_job['title']}"
    )

    print(
        f"Company: {best_job['company']}"
    )

    print(
        f"Apply Link: {best_job['apply_url']}"
    )

    print(
        f"Best ATS Score: {best_score}"
    )

    best_job["score"] = best_score

    # -----------------------------------
    # STEP 5: Missing keywords
    # -----------------------------------
    missing_keywords = optimize_resume(
        best_description,
        resume_text
    )

    print("\nMissing Keywords:")
    print(missing_keywords)

    # -----------------------------------
    # STEP 6: Resume suggestions
    # -----------------------------------
    suggestions = rewrite_resume_suggestions(
        missing_keywords
    )

    print("\nResume Suggestions:")

    if suggestions:
        for s in suggestions:
            print("-", s)
    else:
        print(
            "Your resume already matches this role well."
        )

    # -----------------------------------
    # STEP 7: Resume generation
    # -----------------------------------
    tailored_resume_path = create_tailored_resume(
        resume_text,
        suggestions
    )

    print(
        f"\nTailored resume created: {tailored_resume_path}"
    )

    best_job["resume_path"] = tailored_resume_path

    # -----------------------------------
    # STEP 8: Auto Apply
    # -----------------------------------
    print("\nStarting auto apply process...\n")

    platform = detect_platform(
        best_job["apply_url"]
    )

    print(
        f"Detected platform: {platform}"
    )

    print(
        f"Applying to: {best_job['title']} at {best_job['company']}"
    )

    try:
        # LinkedIn
        if platform == "linkedin":
            print(
                "\nLaunching LinkedIn apply bot..."
            )
            apply_to_job(best_job)

        # Greenhouse
        elif platform == "greenhouse":
            print(
                "\nLaunching Greenhouse apply bot..."
            )
            apply_greenhouse(best_job)

        # Workday
        elif platform == "workday":
            print(
                "\nLaunching Workday apply bot..."
            )
            apply_workday(best_job)

        # Indeed
        elif platform == "indeed":
            print(
                "\nLaunching Indeed apply bot..."
            )
            apply_indeed(best_job)

        # Glassdoor
        elif platform == "glassdoor":
            print(
                "\nLaunching Glassdoor apply bot..."
            )
            apply_glassdoor(best_job)

        else:
            print(
                "\nUnsupported platform detected."
            )
            print(
                f"URL: {best_job['apply_url']}"
            )

    except Exception as e:
        print(
            f"\nApplication failed: {e}"
        )


if __name__ == "__main__":
    run_jobforge()
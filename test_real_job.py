from scraper.linkedin_scraper import fetch_linkedin_jobs
from scraper.job_description import fetch_job_description
from ats.parser import extract_resume_text
from ats.scorer import calculate_ats_score


jobs = fetch_linkedin_jobs()

selected_job = jobs[0]

print("\nSelected Job:")
print(selected_job["title"])
print(selected_job["company"])

job_description = fetch_job_description(
    selected_job["apply_url"]
)

resume_text = extract_resume_text(
    "resumes/master_resume.pdf"
)

score = calculate_ats_score(
    job_description,
    resume_text
)

print(f"\nATS Match Score: {score}")
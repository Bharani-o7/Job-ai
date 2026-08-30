from scraper.linkedin_scraper import fetch_linkedin_jobs
from scraper.job_description import fetch_job_description
from ats.parser import extract_resume_text
from ats.resume_optimizer import optimize_resume


jobs = fetch_linkedin_jobs()

job = jobs[0]

print(f"Testing: {job['title']} at {job['company']}")

job_desc = fetch_job_description(job["apply_url"])

resume = extract_resume_text(
    "resumes/master_resume.pdf"
)

missing_keywords = optimize_resume(
    job_desc,
    resume
)

print("\nMissing Resume Keywords:")
print(missing_keywords)
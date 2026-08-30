from scraper.linkedin_scraper import fetch_linkedin_jobs

jobs = fetch_linkedin_jobs()

print(f"\nFound {len(jobs)} LinkedIn jobs\n")

for job in jobs:
    print(job)
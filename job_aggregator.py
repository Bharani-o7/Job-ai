from scraper.greenhouse import fetch_greenhouse_jobs
from scraper.linkedin_scraper import fetch_linkedin_jobs

def get_all_jobs():
    greenhouse_jobs = fetch_greenhouse_jobs("stripe")
    linkedin_jobs = fetch_linkedin_jobs()

    all_jobs = greenhouse_jobs + linkedin_jobs

    return all_jobs


if __name__ == "__main__":
    jobs = get_all_jobs()

    print(f"\nTotal jobs found: {len(jobs)}\n")

    for job in jobs[:20]:
        print(job)
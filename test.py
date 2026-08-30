from scraper.greenhouse import fetch_greenhouse_jobs

keywords = [
    "software",
    "engineer",
    "developer",
    "backend",
    "frontend",
    "full stack",
    "machine learning",
    "data"
]

jobs = fetch_greenhouse_jobs("stripe")

filtered_jobs = []

for job in jobs:
    title = job["title"].lower()

    if any(keyword in title for keyword in keywords):
        filtered_jobs.append(job)

print(f"Found {len(filtered_jobs)} relevant jobs\n")

for job in filtered_jobs[:10]:
    print(job)
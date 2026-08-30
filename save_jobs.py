from scraper.greenhouse import fetch_greenhouse_jobs
from database.db import SessionLocal, engine, Base
from database.models import Job

Base.metadata.create_all(bind=engine)

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

db = SessionLocal()

jobs = fetch_greenhouse_jobs("stripe")

new_jobs_count = 0

for job in jobs:
    title = job["title"].lower()

    if not any(keyword in title for keyword in keywords):
        continue

    existing_job = db.query(Job).filter(
        Job.apply_url == job["apply_url"]
    ).first()

    if existing_job:
        continue

    new_job = Job(
        company=job["company"],
        title=job["title"],
        location=job["location"],
        apply_url=job["apply_url"]
    )

    db.add(new_job)
    new_jobs_count += 1

db.commit()
db.close()

print(f"{new_jobs_count} new jobs saved!")
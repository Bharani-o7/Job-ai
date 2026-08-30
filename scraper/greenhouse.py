import requests

def fetch_greenhouse_jobs(company):
    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()
    jobs = []

    for job in data.get("jobs", []):
        jobs.append({
            "company": company,
            "title": job["title"],
            "location": job["location"]["name"],
            "apply_url": job["absolute_url"]
        })

    return jobs
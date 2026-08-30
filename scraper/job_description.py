import requests
from bs4 import BeautifulSoup


def fetch_job_description(url):
    try:
        print(f"Fetching description from: {url}")

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=15
        )

        if response.status_code != 200:
            print("Failed to fetch job page")
            return None

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        # LinkedIn job description container
        description_section = soup.find(
            "div",
            class_="show-more-less-html__markup"
        )

        if description_section:
            return description_section.get_text(
                separator=" ",
                strip=True
            )

        # fallback
        return soup.get_text(
            separator=" ",
            strip=True
        )[:5000]

    except Exception as e:
        print("Error:", e)
        return None
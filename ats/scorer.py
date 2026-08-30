import re


def extract_keywords(text):
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    stop_words = {
        "the", "and", "for", "with", "your",
        "that", "this", "will", "have",
        "from", "into", "our", "you"
    }

    return [
        word for word in words
        if len(word) > 2 and word not in stop_words
    ]


def calculate_ats_score(job_description, resume_text, job_title=""):
    score = 0

    job_keywords = set(extract_keywords(job_description))
    resume_keywords = set(extract_keywords(resume_text))

    matched_keywords = job_keywords.intersection(
        resume_keywords
    )

    keyword_score = min(
        len(matched_keywords) * 2,
        40
    )

    score += keyword_score

    tech_keywords = [
        "python",
        "java",
        "react",
        "aws",
        "docker",
        "sql",
        "machine learning",
        "ai",
        "backend",
        "frontend",
        "flask",
        "javascript"
    ]

    for keyword in tech_keywords:
        if (
            keyword.lower() in job_description.lower()
            and keyword.lower() in resume_text.lower()
        ):
            score += 5

    if job_title:
        title_words = job_title.lower().split()

        for word in title_words:
            if word in resume_text.lower():
                score += 5

    return min(score, 100)
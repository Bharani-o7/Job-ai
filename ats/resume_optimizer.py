from collections import Counter
import re


BAD_WORDS = {
    "jobs", "job", "apply", "sign", "join",
    "linkedin", "click", "show", "week",
    "company", "remote", "full", "time",
    "work", "your", "will", "that",
    "about", "help", "including",
    "opportunities", "members",
    "their", "they", "them", "role",
    "team", "candidate", "position",
    "years", "experience"
}


TECH_KEYWORDS = {
    "python", "java", "javascript", "react",
    "node", "sql", "aws", "docker",
    "kubernetes", "machine", "learning",
    "ai", "ml", "api", "backend",
    "frontend", "cloud", "flask",
    "fastapi", "data", "security",
    "devops", "automation"
}


def extract_keywords(text):
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    filtered = []

    for word in words:
        if (
            len(word) > 3
            and word not in BAD_WORDS
        ):
            filtered.append(word)

    keyword_counts = Counter(filtered)

    # prioritize technical keywords
    prioritized = []

    for word, count in keyword_counts.most_common():
        if word in TECH_KEYWORDS:
            prioritized.append(word)

    return prioritized[:20]


def optimize_resume(job_description, resume_text):
    job_keywords = extract_keywords(job_description)

    resume_words = set(
        re.findall(
            r"\b[a-zA-Z]+\b",
            resume_text.lower()
        )
    )

    missing = []

    for keyword in job_keywords:
        if keyword not in resume_words:
            missing.append(keyword)

    return missing
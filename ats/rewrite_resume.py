def rewrite_resume_suggestions(missing_keywords):
    suggestions = []

    keyword_map = {
        "cloud": "Highlight AWS cloud deployment experience.",
        "backend": "Highlight backend API development work.",
        "frontend": "Highlight React frontend experience.",
        "machine learning": "Highlight ML projects.",
        "ai": "Highlight AI/LLM related projects.",
        "sql": "Highlight database experience."
    }

    for keyword in missing_keywords:
        keyword = keyword.lower()

        if keyword in keyword_map:
            suggestions.append(keyword_map[keyword])

    return suggestions


def create_tailored_resume(original_resume_text, suggestions):
    """
    Keep original resume unchanged.
    Just return original PDF path.
    """

    print("\nUsing original resume for application...")

    if suggestions:
        print("\nATS Optimization Notes:")
        for s in suggestions:
            print("-", s)

    return "resumes/master_resume.pdf"
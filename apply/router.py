def detect_platform(url):
    url = url.lower()

    if "linkedin.com" in url:
        return "linkedin"

    elif "greenhouse.io" in url:
        return "greenhouse"

    elif "myworkdayjobs.com" in url:
        return "workday"

    elif "indeed.com" in url:
        return "indeed"

    elif "glassdoor.com" in url:
        return "glassdoor"

    else:
        return "unknown"
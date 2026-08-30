from parser import extract_resume_text
from scorer import calculate_ats_score

resume_text = extract_resume_text("../resumes/master_resume.pdf")

job_description = """
We are hiring a Software Engineer Intern with experience in Python,
SQL, APIs, cloud platforms, machine learning, and backend systems.
"""

score = calculate_ats_score(job_description, resume_text)

print("ATS Score:", score)
# JobForge AI 🚀

> AI-powered job discovery, ATS optimization, and application automation platform.

JobForge AI is a full-stack job application automation system designed to streamline the repetitive parts of the software engineering job search.

The system discovers job opportunities, extracts job descriptions, evaluates resume compatibility using an ATS scoring engine, identifies missing keywords, generates resume optimization suggestions, routes applications based on the target platform, and tracks application activity.

---

## ✨ Features

### 🔎 Multi-Platform Job Discovery

JobForge AI supports job discovery across multiple platforms:

- LinkedIn
- Greenhouse
- Workday
- Indeed
- Glassdoor

The platform-specific scraping architecture allows each source to have its own scraper while sharing a common job representation.

---

### 📊 ATS Resume Matching

Each discovered job is evaluated against the user's resume.

The ATS pipeline:

1. Extracts resume text from PDF
2. Extracts relevant job-description information
3. Compares resume content with job requirements
4. Calculates an ATS compatibility score
5. Identifies missing keywords
6. Generates optimization suggestions

Example:

Job: Software Engineer - Cloud

ATS Score: 82

Missing Keywords:
- automation
- cloud infrastructure
- backend

🏗️System Architecture
                         JobForge AI
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
    Scrapers               ATS Engine           Application
        │                     │                     │
        │                     │                     │
   ┌────┼────┐          ┌─────┼─────┐        ┌──────┼──────┐
   │    │    │          │     │     │        │      │      │
  LI  Indeed Glassdoor Parser Scorer Optimizer  LI  GH  WD
   │    │    │                                  │      │
   └────┼────┘                                  │      │
        │                                       │      │
        ▼                                       ▼      ▼
    Job Data                              Browser Automation
        │                                       │
        └───────────────────┬───────────────────┘
                            │
                            ▼
                     Application Tracking


==================================================
JOBFORGE AI - REQUIREMENTS.TXT
==================================================

fastapi
uvicorn
playwright
pandas
numpy
scikit-learn
sqlalchemy
pypdf
pdfplumber
fpdf
python-multipart
requests
beautifulsoup4
lxml


==================================================
SETUP & RUN - WINDOWS POWERSHELL
==================================================

1. Open PowerShell and go to the project folder:

cd "C:\Users\bhara\OneDrive\Desktop\jobforge-ai"


2. Create a virtual environment:

python -m venv venv


3. Activate the virtual environment:

.\venv\Scripts\Activate.ps1


If PowerShell blocks activation, run:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Then activate again:

.\venv\Scripts\Activate.ps1


4. Upgrade pip:

python -m pip install --upgrade pip


5. Install all Python dependencies:

pip install -r requirements.txt


6. Install Playwright browsers:

playwright install


7. Make sure your resume is located here:

C:\Users\bhara\OneDrive\Desktop\jobforge-ai\resumes\master_resume.pdf


8. Verify the resume exists:

Get-Item .\resumes\master_resume.pdf


9. Run JobForge AI:

python main.py


==================================================
OPTIONAL - START FASTAPI BACKEND
==================================================

Open another PowerShell window.

Go to the project:

cd "C:\Users\bhara\OneDrive\Desktop\jobforge-ai"

Activate the virtual environment:

.\venv\Scripts\Activate.ps1

Start FastAPI:

uvicorn api.main:app --reload


The backend will be available at:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs


==================================================
OPTIONAL - START REACT FRONTEND
==================================================

Open another PowerShell window.

Go to the frontend:

cd "C:\Users\bhara\OneDrive\Desktop\jobforge-ai\frontend"

Install Node dependencies:

npm install

Start the frontend:

npm run dev


==================================================
NORMAL DAILY USAGE
==================================================

After the project is already installed, you only need:

cd "C:\Users\bhara\OneDrive\Desktop\jobforge-ai"

.\venv\Scripts\Activate.ps1

python main.py


==================================================
IMPORTANT
==================================================

Do NOT commit these files/folders to GitHub:

venv/
linkedin_session/
greenhouse_session/
workday_session/
indeed_session/
glassdoor_session/
resumes/master_resume.pdf
resumes/tailored_resume.pdf
applied_jobs.json
jobs.db
.env

Add them to .gitignore.

Your actual resume should remain:

resumes/master_resume.pdf

When you update your resume, replace that file with the new version using the SAME filename and SAME location.

JobForge AI will then use the updated resume the next time you run:

python main.py


==================================================
TROUBLESHOOTING
==================================================

If Playwright gives a browser error:

playwright install


If a Python package is missing:

pip install -r requirements.txt


If you get an import error:

Make sure you are running from the project root:

cd "C:\Users\bhara\OneDrive\Desktop\jobforge-ai"

Then:

.\venv\Scripts\Activate.ps1

python main.py


If you get:

ModuleNotFoundError

Run:

pip install -r requirements.txt


If you get:

ImportError: cannot import name ...

Check that the function name imported in main.py exactly matches
the function defined inside the corresponding .py file.



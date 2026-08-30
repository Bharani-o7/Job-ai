from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Allow React frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "JobForge AI Backend Running"
    }


@app.get("/applied-jobs")
def get_applied_jobs():
    file_path = "applied_jobs.json"

    # If file doesn't exist
    if not os.path.exists(file_path):
        return {
            "total_applied": 0,
            "jobs": []
        }

    try:
        with open(file_path, "r") as f:
            jobs = json.load(f)

        formatted_jobs = []

        for job in jobs:
            formatted_jobs.append({
                "company": job.get("company", "Unknown"),
                "title": job.get("title", "Unknown"),
                "score": job.get("score", 0),
                "status": job.get("status", "Applied"),
                "url": job.get("url", "")
            })

        return {
            "total_applied": len(formatted_jobs),
            "jobs": formatted_jobs
        }

    except Exception as e:
        return {
            "error": str(e),
            "total_applied": 0,
            "jobs": []
        }


@app.get("/stats")
def get_stats():
    file_path = "applied_jobs.json"

    if not os.path.exists(file_path):
        return {
            "total_jobs": 0,
            "avg_ats_score": 0
        }

    with open(file_path, "r") as f:
        jobs = json.load(f)

    if len(jobs) == 0:
        return {
            "total_jobs": 0,
            "avg_ats_score": 0
        }

    total_score = sum(
        job.get("score", 0)
        for job in jobs
    )

    avg_score = round(
        total_score / len(jobs),
        2
    )

    return {
        "total_jobs": len(jobs),
        "avg_ats_score": avg_score
    }
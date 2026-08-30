from ats.rewrite_resume import rewrite_resume_suggestions

missing = ["cloud", "backend"]

suggestions = rewrite_resume_suggestions(missing)

print("\nResume Bullet Suggestions:\n")

for s in suggestions:
    print("-", s)
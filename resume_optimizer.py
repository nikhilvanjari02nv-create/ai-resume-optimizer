import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


def optimize_resume(resume_text, job_description):
    prompt = f"""You are an expert resume reviewer and ATS specialist.

Compare the RESUME below against the JOB DESCRIPTION and provide:
1. A match score out of 100
2. A list of important keywords from the job description that are MISSING from the resume
3. Three specific, actionable rewrite suggestions to improve the resume's match

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Respond in this exact format:
MATCH SCORE: [number]/100

MISSING KEYWORDS:
- [keyword 1]
- [keyword 2]

REWRITE SUGGESTIONS:
1. [suggestion]
2. [suggestion]
3. [suggestion]
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text


sample_resume = """
John Doe
Customer Service Representative with 2 years experience.
Handled customer calls, resolved complaints, used basic computer skills.
"""

sample_job_description = """
We are looking for an AI Content Reviewer to evaluate AI-generated responses
for quality, accuracy, and tone. Must have strong attention to detail,
experience with data annotation or content moderation, and familiarity
with AI/ML concepts. Remote role.
"""

result = optimize_resume(sample_resume, sample_job_description)
print(result)

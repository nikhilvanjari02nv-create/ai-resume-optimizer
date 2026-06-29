import os
import streamlit as st
from google import genai

st.set_page_config(page_title="AI Resume Optimizer", page_icon="📄")

st.title("📄 AI Resume Optimizer")
st.write("Paste your resume and a job description below. Get an instant ATS match score, missing keywords, and rewrite suggestions powered by AI.")

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


col1, col2 = st.columns(2)

with col1:
    resume_input = st.text_area("Your Resume", height=300, placeholder="Paste your resume text here...")

with col2:
    job_input = st.text_area("Job Description", height=300, placeholder="Paste the job description here...")

if st.button("Optimize My Resume", type="primary"):
    if resume_input.strip() == "" or job_input.strip() == "":
        st.warning("Please paste both your resume and the job description.")
    else:
        with st.spinner("Analyzing your resume against the job description..."):
            result = optimize_resume(resume_input, job_input)
        st.markdown("### Results")
        st.markdown(result)

st.markdown("---")
st.caption("Built by Nikhil • Powered by Google Gemini")

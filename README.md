# 📄 AI Resume Optimizer

> After 50+ job applications and zero interviews, I dug into *why*. Turns out my resume was getting auto-rejected by ATS systems before a human ever saw it — generic keywords, no role-specific tailoring, inconsistent formatting. So I built a tool to fix that, for myself and anyone else stuck in the same loop.

**[Live Demo →](https://ai-resume-optimizer-nikhil.streamlit.app/)**

---

## What it does

Paste in your resume and a job description. The app uses the Gemini API to:

- Score your resume's match against the job description (out of 100)
- Identify important keywords from the job posting that are missing from your resume
- Generate three specific, actionable rewrite suggestions to close the gap

No generic "add more keywords" advice — it tells you exactly which keywords, and exactly how to rewrite each section.

## Why I built this

I was applying to AI Trainer, Content Reviewer, and Virtual Assistant roles and getting silence. After auditing my own process, I found the real problem: ATS auto-rejection from inconsistent answers, location mismatches, and one generic resume spread across incompatible role categories. Once I fixed that manually, I realized this is a problem almost every job seeker has — and most have no visibility into *why* they're being rejected.

This project is both a portfolio piece and a real tool I use for my own applications.

## Tech stack

- **Python** — core logic
- **Google Gemini API** — resume/job description analysis
- **Streamlit** — web interface
- **Git/GitHub** — version control

## How it works

1. User pastes resume text and a target job description
2. App sends both to Gemini with a structured prompt requesting a match score, missing keywords, and rewrite suggestions
3. Results render directly in the browser — no signup, no data stored

## Running it locally

```bash
git clone https://github.com/nikhilvanjari02nv-create/ai-resume-optimizer.git
cd ai-resume-optimizer
pip install -r requirements.txt
```

Set your Gemini API key as an environment variable:

```bash
setx GEMINI_API_KEY "your-key-here"      # Windows
export GEMINI_API_KEY="your-key-here"    # Mac/Linux
```

Then run:

```bash
streamlit run app.py
```

## What's next

- [ ] Support for PDF/DOCX resume uploads (not just paste)
- [ ] Export optimized resume as a downloadable file
- [ ] Multi-job comparison (paste 3 job postings, see which one fits best)

---

Built by [Nikhil Vanjari](https://github.com/nikhilvanjari02nv-create) • [LinkedIn](https://www.linkedin.com/in/nikhil-vanjari-7006a0204)

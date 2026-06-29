import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello and tell me you're ready to optimize resumes for job applications."
)

print(response.text)

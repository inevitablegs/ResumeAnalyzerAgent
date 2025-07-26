import google.generativeai as genai

def analyze_resume(text: str) -> str:
    prompt = f"""
You are a resume expert.

Task:
1. Extract key sections from the resume.
2. Identify any missing or weak sections.
3. Suggest improvements.

Resume:
{text}
    """
    model = genai.GenerativeModel("gemini-2.5-pro")
    return model.generate_content(prompt).text

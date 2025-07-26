import google.generativeai as genai

def improve_resume(text: str) -> str:
    prompt = f"""
Rewrite or improve the following resume content. Focus on clarity, action verbs, formatting, and better impact.

Resume:
{text}
    """
    model = genai.GenerativeModel("gemini-2.5-pro")
    return model.generate_content(prompt).text

import pdfplumber

def extract_text_from_pdf(file_path: str) -> str:
    with pdfplumber.open(file_path) as pdf:
        return "\n".join([page.extract_text() or "" for page in pdf.pages])

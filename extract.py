import PyPDF2
from typing import List

def extract_text_from_pdf(file_path: str) -> str:
    """Extract all text from a PDF file."""
    text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def extract_tables_from_pdf(file_path: str) -> List[dict]:
    """Extract structured data (tables) from PDF."""
    return []

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
import markdown
from weasyprint import HTML
import tempfile
import re

router = APIRouter()

EXCLUDED_ENTITIES = ["ChatFormatter", "Convert"]

def clean_text(text: str) -> str:
    text = re.sub(r'##+\s*', '', text)
    return text

@router.post("/convert/")
async def convert_markdown_to_pdf(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        text = contents.decode("utf-8")
        cleaned_text = clean_text(text)
        html_body = markdown.markdown(cleaned_text)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_pdf:
            output_pdf_path = tmp_pdf.name
            HTML(string=html_body).write_pdf(output_pdf_path)

        return FileResponse(path=output_pdf_path, filename="output.pdf", media_type="application/pdf")

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

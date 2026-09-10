from fastapi import FastAPI, File, Form, UploadFile
import tempfile
import os

from app.ai.ocr.ocr_service import extract_document_number


app = FastAPI(
    title="Voting System OCR Service",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "OCR Service is running successfully!"
    }


@app.post("/ocr/extract")
async def extract_ocr(
    document_type: str = Form(...),
    file: UploadFile = File(...)
):
    # Create temporary file
    suffix = os.path.splitext(file.filename or "")[1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as temp_file:

        temp_file.write(await file.read())
        temp_path = temp_file.name

    try:
        # Run OCR
        result = extract_document_number(
            image_path=temp_path,
            document_type=document_type
        )

        return result

    finally:
        # Remove temporary image
        if os.path.exists(temp_path):
            os.remove(temp_path)